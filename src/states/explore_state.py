import pygame
import random
from src.states.state_machine import State
from src.settings import BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, ENCOUNTERS_ENABLED
from src.entities.entity import Entity
from src.components.position import Position
from src.components.sprite import Sprite
from src.components.stats import Stats
from src.components.dialogue import Dialogue
from src.components.hitbox import Hitbox
from src.components.hurtbox import Hurtbox
from src.systems import movement_system
from src.systems.movement_system import _touches_wall
from src.tileset import Tileset
from src.tilemap import Tilemap
from src.camera import Camera
from src.settings import ENCOUNTER_STEPS
from src.map_loader import load_tiled_map, get_objects_from_map, load_collisions

class ExploreState(State):

    def enter(self):
        # Si ya existe el jugador, no reconstruimos la escena.
        # Esto permite conservar el estado al volver de una batalla.
        if hasattr(self, 'player'):
            return
        
        # Estas son las fuentes del juego. Por ahora tenemos 1, la del diablo.
        self.font = pygame.font.Font("assets/fonts/diablo.ttf", 48)
        self.dialogue_font = pygame.font.Font(
            "assets/fonts/diablo.ttf",
            28
        )
        
        # Creamos la entidad principal del jugador.
        self.player = Entity()
        
        self.player.add_component(
            Position(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2)
        )
        
        self.player.add_component(
            Sprite(32, 32, (0, 128, 255))
        )

        self.player.add_component(
            Hurtbox(32,32)
        )
        self.player.add_component(
            Hitbox(
                width=48,
                height=32,
                offset_x=32,
                offset_y=0
            )
        )
        
        player_sprite = self.player.get_component(Sprite)
        player_sprite.load_spritesheet(
            "assets/sprites/player/Male/Male 01-1.png",
            32,
            32,
            {
                "idle": {"row": 0, "frames": 3},
             "walk_down": {"row": 0, "frames": 3},
             "walk_left": {"row": 1, "frames": 3},
             "walk_right": {"row": 2,"frames": 3},
             "walk_up": {"row": 3, "frames": 3},
            }
        )

        # Recuperamos la clase elegida en CharacterCreationState.
        player_class = getattr(self.game, 'player_class', None)
        
        if player_class:
            self.player.add_component(
                Stats(
                    hp=player_class['hp'],
                    attack=player_class['attack'],
                    magic=player_class['magic'],
                    speed=player_class['speed']
                )
            )
            
        else:
            self.player.add_component(Stats())
            
        # Tiempo por el cual la hitbox permanece activa.
        self.attack_timer = 0

        # Duracion breve del golpe
        self.attack_duration = 0.15

        # Direccion inicial del jugador
        # Por ahora le ataque apunta hacia la derecha.
        self.attack_direction = "right"
        
        # Variables de control de la escena.
        # Deben crearse antes de llamar a load_map()
        self.entities = [self.player]
        self.step_counter = 0
        self.current_zone = "normal"
        self.frozen = False
        self.casa_intro_done = False
        self.guards_spawned = False
        

        # Estas referencias se completan cuando se carga el mapa.
        self.owner_dialogue = None
        self.guard_dialogue = None
        self.tileset = Tileset("assets/tilesets/pipoya-rpg-tileset/[Base]BaseChip_pipo.png")
        self.load_map("data/maps/overworld_normal.json")


        
    def load_map(self, path):
        self.current_map = path
        self.tilemap = load_tiled_map(self.tileset, path)
        load_collisions(self.tilemap, path)
        objects = get_objects_from_map(path)
        for obj in objects:
            if obj['name'] == 'spawn_player':
                self.player.get_component(Position).x = obj['x']
                self.player.get_component(Position).y = obj['y']

        self.portals = []
        for obj in objects:
            if obj['layer'] == 'Portal':
                self.portals.append(obj)
                if 'target_map' not in obj['properties']:
                    print("AVISO: portal", obj['name'], "sin target_map en", path)
        self.ignore_portals = True
        self.npcs = []
        sheets = {
            'duenio_casa': "assets/sprites/player/Male/Male 02-1.png",
            'hija_duenio': "assets/sprites/player/Female/Female 01-1.png",
            'guardia_1': "assets/sprites/player/Soldier/Soldier 01-1.png",
            'guardia_2': "assets/sprites/player/Soldier/Soldier 01-1.png",
        }
        npc_anims = {"idle": {"row": 0, "frames":3},
                     "walk_down": {"row": 0, "frames": 3},
                     "walk_left": {"row": 1, "frames": 3},
                     "walk_right": {"row": 2, "frames": 3},
                     "walk_up": {"row": 3, "frames": 3}}
        for obj in objects:
            if obj['layer'] == 'NPC' and obj['name']:
                npc = Entity()
                npc.add_component(
                    Position(obj['x'], obj['y'])
                )
                
                npc_sprite = Sprite(
                    32,
                    32,
                    (0, 128, 255)
                )

                npc_sprite.load_spritesheet(
                    sheets.get(
                        obj['name'],
                        "assets/sprites/player/Male/Male 01-1.png"
                    ),
                    32,
                    32,
                    npc_anims
                )
                npc.add_component(npc_sprite)
                
                # Solo el duenio tiene este dialogo.
                
                if obj['name'] == 'duenio_casa':
                    self.owner_dialogue = Dialogue([
                        (
                            "Dueño", "Y vos quien carajo sos?"
                        ),
                        (
                            "Dueño", "Sos uno de esos guardias que vienen a buscarme para ejecutarme?"
                        ),
                        (
                            "Dueño", "Cerrá la puerta. Y no pises el símbolo."
                        ),
                   ])
                    npc.add_component(self.owner_dialogue)
                self.npcs.append(npc)
        map_width = self.tilemap.width * self.tilemap.tile_size
        map_height = self.tilemap.height * self.tilemap.tile_size
        self.camera = Camera(map_width, map_height)
    # Herramienta para cortar escenas, futura escalabilidad para gestionar todas las animaciones ingame.
    
    def update_cutscene(self, dt):
        if self.casa_intro_done or not self.current_map.endswith('casa_duenio.json'):
            return
        duenio = None
        for npc in self.npcs:
            if npc.get_component(Dialogue):
                duenio = npc
                break
        if duenio is None:
            return
        player_pos = self.player.get_component(Position)
        duenio_pos = duenio.get_component(Position)
        dx = player_pos.x - duenio_pos.x
        dy = player_pos.y - duenio_pos.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist < 96:
            dialogue = duenio.get_component(Dialogue)
            if not dialogue.active:
                dialogue.start()
                self.frozen = True
                self.casa_intro_done = True
                duenio_sprite = duenio.get_component(Sprite)
                if abs(dx) > abs(dy):
                    duenio_sprite.direction = "right" if dx > 0 else "left"
                else:
                    duenio_sprite.direction = "down" if dy > 0 else "up"
        
    #Esto hay que reestructurarlo, el space se va luego y hay que redefinir los botones.
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.state_machine.change("battle")
                if event.key == pygame.K_e:
                    self.advance_dialogue()

    def advance_dialogue(self):
        for npc in self.npcs:
            dialogue = npc.get_component(Dialogue)

            # Solo nos interesa el NPC que tiene una conversacion activa.
            if not dialogue or not dialogue.active:
                continue
            # Pasamos a la siguiente linea.
            dialogue.advance()

            # Si todavia quedan lines, terminamos este metodo.
            # El proximo eventkey E continua la conversacion.
            
                # La conversacion todavia no termino.
            if not dialogue.finished():
                break
            # Termino el dialogo del duenio:
            if dialogue is self.owner_dialogue:
                self.frozen = False
                self.spawn_guards()
                break
            # Termino el dialogo de los guardias.
            if dialogue is self.guard_dialogue:
                self.start_battle()
                break

            # Caso general: Termino una conversacion cualquiera:
            self.frozen = False
            break

    def start_battle(self):
        
        # Preparamos los datos del jugador antes de cambiar de estado.
        # battle_state crea su propia entidad visual, pero reutiliza estas estadisticas
        self.game.player_stats = self.player.get_component(Stats)
        
        self.game.state_machine.change("battle")

    def spawn_guards(self):
        # Creamos los guardias dentro de la casa.
        # En esta primera version los hacemos aparecer directamente en la puerta.
        # Despues vemos que onda.
        if getattr(self, "guards_spawned", False):
            return

        self.guards_spawned = True
        self.frozen = True

        guard_animations = {
            "idle": {"row": 0, "frames": 3},
            "walk_down": {"row": 0, "frames": 3},
            "walk_left": {"row": 1, "frames": 3},
            "walk_right": {"row": 2, "frames": 3},
            "walk_up": {"row": 3, "frames": 3},
        }

        guard_positions = [
            (400, 520),
            (464, 520),
        ]
        
        for index, (x, y) in enumerate(guard_positions):
            guard = Entity()
            guard.add_component(Position(x, y))

            guard_sprite = Sprite(32, 32, (0, 182, 255))
            guard_sprite.load_spritesheet(
                "assets/sprites/player/Soldier/Soldier 01-1.png",
                32,
                32,
                guard_animations
            )
            guard.add_component(guard_sprite)

            # Solo uno de los guardias habla.
            # El segundo funciona como presencia visual.

            if index == 0:
                self.guard_dialogue = Dialogue([
                    ("Guardia", "Ahi esta!"),
                    ("Guardia", "Por orden del gobierno, quedas detenido!"),
                    ("Guardia", "No nos obligues a usar la fuerza!"),
                ])

                guard.add_component(self.guard_dialogue)
                self.guard_dialogue.start()

            self.npcs.append(guard)
            
    def update(self, dt):
        # Guarda posicion antes de mover.
        player_pos = self.player.get_component(Position)
        old_x = player_pos.x
        old_y = player_pos.y

        
        # Mover al jugador, desde movement_system. La referencia esta ahi.
        # Agregamos un condicional if para verificar si frozen esta  o no enabled. Para las animaciones.
       
        if not self.frozen:
            movement_system.update(self.entities, dt, self.tilemap)
        self.update_cutscene(dt)
        
        # Verificar si se movio (cambio de posicion).
        if player_pos.x != old_x or player_pos.y != old_y:
            self.step_counter += 1
            max_steps = ENCOUNTER_STEPS.get(self.current_zone, 40)
            if ENCOUNTERS_ENABLED and self.step_counter >= max_steps:
                self.step_counter = 0
                self.game.state_machine.change("battle")
        player_rect = pygame.Rect(player_pos.x, player_pos.y, 32, 32)
        touching = False
        for portal in self.portals:
            portal_rect = pygame.Rect(portal['x'], portal['y'], portal['width'], portal['height'])
            if player_rect.colliderect(portal_rect):
                touching = True
                if not self.ignore_portals:
                    target = portal['properties'].get('target_map')
                    if target:
                        self.load_map("data/maps/" + target)
                    player_pos.x = portal['properties'].get('target_x', player_pos.x)
                    player_pos.y = portal['properties'].get('target_y', player_pos.y)
                    self.ignore_portals = True
                break
        if not touching:
            self.ignore_portals = False
        
    #Actualizar animacion del sprite segun la direccion que se mueve.
    #movement_system ya setea sprite.direction con "up", "down", "left", "right".
                
        sprite = self.player.get_component(Sprite)
        if sprite:
            is_moving = player_pos.x != old_x or player_pos.y != old_y
            if is_moving:
                if sprite.direction == "up":
                    sprite.current_animation = "walk_up"
                elif sprite.direction == "down":
                    sprite.current_animation = "walk_down"
                elif sprite.direction == "left":
                    sprite.current_animation = "walk_left"
                elif sprite.direction == "right":
                    sprite.current_animation = "walk_right"
            else:
                sprite.current_animation = "idle"

            sprite.update_animation(dt)
                    
        # Actualizar camara.
        self.camera.update(player_pos.x, player_pos.y, dt)
        
    def render(self, screen):
        screen.fill(BLACK)

        self.tilemap.render(screen, self.camera.x, self.camera.y)
        
        position = self.player.get_component(Position)
        sprite = self.player.get_component(Sprite)

        if position and sprite:
            screen_x, screen_y = self.camera.apply(position.x, position.y)
            sprite.render(screen, screen_x, screen_y)

        for npc in self.npcs:
            npc_pos = npc.get_component(Position)
            npc_sprite = npc.get_component(Sprite)
            if npc_pos and npc_sprite:
                npc_x, npc_y = self.camera.apply(npc_pos.x, npc_pos.y)
                npc_dialogue = npc.get_component(Dialogue)
                if npc_dialogue:
                    dx, dy = npc_dialogue.shake_offset()
                    npc_x += dx
                    npc_y += dy
                npc_sprite.render(screen, npc_x, npc_y)
        # Aca comenzamos stats, por eso estan pegaos
        
        stats = self.player.get_component(Stats)
        if stats:
            hp_text = self.font.render(f"HP: {stats.hp}/{stats.max_hp}", True, WHITE)
            screen.blit(hp_text, (10,10))

        for npc in self.npcs:
            dialogue = npc.get_component(Dialogue)
            if dialogue and dialogue.active and dialogue.current():
                speaker, text = dialogue.current()
                box = pygame.Rect(40, SCREEN_HEIGHT - 160, SCREEN_WIDTH - 80, 120)
                pygame.draw.rect(screen, (0, 0, 0), box)
                pygame.draw.rect(screen, WHITE, box, 2)
                speaker_text = self.dialogue_font.render(speaker, True, (255, 255, 0))
                screen.blit(speaker_text, (box.x + 20, box.y + 10))
                line_text = self.dialogue_font.render(text, True, WHITE)
                screen.blit(line_text, (box.x + 20, box.y + 60))
                break
