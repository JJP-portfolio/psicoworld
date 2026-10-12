import pygame
import random
import os
from src.states.state_machine import State
from src.settings import BLACK, WHITE, RED, SCREEN_WIDTH, SCREEN_HEIGHT
from src.entities.entity import Entity
from src.entities.enemy import Enemy
from src.components.position import Position
from src.components.sprite import Sprite
from src.components.stats import Stats
from src.components.health import Health
from src.components.hitbox import Hitbox
from src.components.hurtbox import Hurtbox
from src.systems import combat_system

class BattleState(State):

    def enter(self):
        self.font = pygame.font.Font("assets/fonts/diablo.ttf", 32)
        self.player = Entity()
        self.player.add_component(Position(100,SCREEN_HEIGHT // 2))

        # Creamos el sprite del jugador
        player_sprite = Sprite(
            32,
            32,
            (0, 128, 255)
        )
        self.player.add_component(player_sprite)

        # Agregamos la carga especifica, esto va a mostrar
        # el sprite del jugador y sus respectivas animaciones.
        player_sprite.load_spritesheet(
            "assets/sprites/player/Male/Male 01-1.png",
            32,
            32,
            {
                "idle": {"row": 0, "frames": 3},
                "walk_down": {"row": 0, "frames": 3},
                "walk_left": {"row": 1, "frames": 3},
                "walk_right": {"row": 2, "frames": 3},
                "walk_up": {"row": 3, "frames": 3},
            }
        )

        # Zona donde el jugador puede recibir daño.
        self.player.add_component(
            Hurtbox(32,32)
        )

        # Color de respaldo
        enemy_color = (255, 0, 0)
        # Acá creamos el enemigo
        self.enemy = Enemy(
            SCREEN_WIDTH - 150,
            SCREEN_HEIGHT  // 2,
            enemy_color,
            health=80,
            damage=10
        )

        # Encapsulamos el sprite en una variable para reutilizarlo.
        enemy_sprite = self.enemy.get_component(Sprite)
        enemy_path = "assets/sprites/enemies/Enemy/Enemy 01-1.png"
        enemy_sprite.load_spritesheet(
            enemy_path,
            32,
            32,
            {
                "idle": {"row": 0, "frames": 3},
                "walk_down": {"row": 0, "frames": 3},
                "walk_left": {"row": 1, "frames": 3},
                "walk_right": {"row": 2, "frames": 3},
                "walk_up": {"row": 3, "frames": 3},
            }
        )
        
        # Zona que produce daño cuando el jugador ataca.
        # Por ahora está ubicada a la derecha del jugador.
        self.player.add_component(
            Hitbox(
                width=48,
                height=32,
                offset_x=32,
                offset_y=0
            )
        )
        
        # Si venimos desde ExploreState, reutilizamos las estadisticas
        # de la clase que eligio el jugador.
        player_stats = getattr(self.game, "player_stats", None)

        # Este caso permite que la batalla siga funcionando
        # aunque se entre directamente sin pasar por exploracion.
        if player_stats is None:
            player_stats = Stats(
                hp=100,
                attack=15,
                magic=5,
                speed=8
            )
        
        self.player.add_component(player_stats)
        
        # Health es el componente usado por BattleState
        # para controlar la vida durante el combate.
        self.player.add_component(Health(player_stats.max_hp))
        
        # Formula vieja, la guardamos para referencia.
        # self.player.add_component(Stats(hp=100, attack=15, magic=5, speed=8))
        # self.player.add_component(Health(100))

        self.player_direction = "right"
        
        self.entities = [self.player, self.enemy]
        self.message = ""
        self.message_timer = 0
        self.game_over = False
        # Temporizador de ataque cuerpo a cuerpo
        # Si es mayor que cero, hay un ataque activo.
        self.attack_timer = 0

        # Duracion del golpe en segundos.
        self.attack_duration = 0.15

        # Temporizador del ataque enemigo.
        self.enemy_attack_timer = 0

        # Tiempo minimo entre ataques enemigos
        self.enemy_attack_cooldown = 1.0

        # Duracion de la hitbox enemiga.
        self.enemy_attack_duration = 0.15

        
    def handle_events(self, events):
        # Para recorrer cada evento dentro de eventoS
        # Tenemos una logica de manejar la informacion:
        # Hay un tipo de evento, que es KEYDOWN, pertenece a pygame.
        # Si, game_over, vuelve a exploracion y termina.
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_RETURN:
                        self.game.state_machine.change("explore")
                    return
        # Acá empieza el combate en tiempo real
        # Primero agarramos los stats del jugador y la vida del enemigo:
                player_stats = self.player.get_component(Stats)
                enemy_health = self.enemy.get_component(Health)

        # Ataque fisico provisional con teclado.
        # Más adelante SPACE puede convertirse en otra habilidad.
                if event.key == pygame.K_SPACE:
                    damage = player_stats.attack
                    enemy_health.take_damage(damage)
                    self.message = f"Golpeaste por {damage} de daño!"
                    self.message_timer = 1

        # Poder mágico provisional.
        # Ya no cambia el turno porque el combate es en tiempo real.
                elif event.key == pygame.K_e:
                    damage = player_stats.magic * 2
                    enemy_health.take_damage(damage)
                    self.message = f"Poder mágico por {damage} de daño!"
                                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.start_melee_attack()

    def start_melee_attack(self):
        # Inicia un ataque cuerpo a cuerpo
        # El click no aplica daño directamente.
        # Solo activa temporalmente la hitbox
        # La detección del golpe ocurre en update()
        if self.game_over:
            return

        # Si el ataque anterior todavia está activo,
        # ignoramos este nuevo click.
        if self.attack_timer > 0:
            return

        hitbox = self.player.get_component(Hitbox)

        if hitbox is None:
            return

        self.attack_timer = self.attack_duration
        hitbox.active = True

        self.message = "Ataque cuerpo a cuerpo"
        self.message_timer = 1

    def update_melee_attack(self, dt):
        # Mantiene activa la hitbox durante el tiempo del golpe
        # y revisa las colisiones.
        hitbox = self.player.get_component(Hitbox)
        
        if hitbox is None:
            return

        # Si no hay otro ataque activo, no hacemos nada.
        if self.attack_timer <= 0:
            hitbox.active = False
            return
        

        self.attack_timer -= dt
        
        # Cuando termina la duracion del ataque,
        # desactivamos la hitbox:
        if self.attack_timer <= 0:
            self.attack_timer = 0
            hitbox.active = False
            

    def update_enemy_attack(self, dt):
        """
        Hace que el enemigo ataque cuando está cerca del jugador.

        Por ahora no hay inteligencia artificial compleja:
        solamente comprueba distancia y activa su Hitbox.
        """
        enemy_hitbox = self.enemy.get_component(Hitbox)

        if enemy_hitbox is None:
            return

        # Reducimos el cooldown con el paso del tiempo.
        if self.enemy_attack_timer > 0:
            self.enemy_attack_timer -= dt

        # Si todavia está esperando, no puede atacar.
        if self.enemy_attack_timer > 0:
            enemy_hitbox.active = False
            return

        player_position = self.player.get_component(Position)
        enemy_position = self.enemy.get_component(Position)

        distance_x = player_position.x - enemy_position.x
        distance_y = player_position.y - enemy_position.y

        # Distancia aproximada entre el jugador y el enemigo.
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        # El enemigo solo atace si el jugador está cerca.
        if distance <= 55:
            enemy_hitbox.active = True
            self.enemy_attack_timer = self.enemy_attack_cooldown
        else:
            enemy_hitbox.active = False
            
            
    def update(self, dt):
        # Actualizamos el mov del jugador.
        self.update_player_movement(dt)
        
        # Actualizamos el ataque del jugador.
        self.update_melee_attack(dt)

        # El enemigo decide si debe atacar.
        self.update_enemy_attack(dt)

        # Revisa las hitboxes activas del jugador y del enemigo.
        combat_system.check_collisions(self.entities)

        # Actualizamos la duracion de los mensajes
        if self.message_timer > 0:
            self.message_timer -= dt
            
            if self.message_timer <= 0:
                self.message = ""

        # Se actualiza la invulnerabilidad temporal de ambos personajes.
        self.player.get_component(Health).update(dt)
        self.enemy.get_component(Health).update(dt)

        # La victoria debe revisarse después de cualquier tipo de ataque:
        # SPACE, E, o click izquierdo.
        player_health = self.player.get_component(Health)
        enemy_health = self.enemy.get_component(Health)
        
        #Primero verifico si el enemigo murio.
        if not enemy_health.is_alive() and not self.game_over:
            self.message ="Victoria! Ganaste 50 EXP!"
            self.message_timer = 3
                
            player_stats = self.player.get_component(Stats)
            player_stats.gain_exp(50)
                
            self.game_over = True
            return

        if not player_health.is_alive() and not self.game_over:
            self.message = "Derrota! Presiona Enter para volver."
            self.game_over = True
                
    def update_player_movement(self, dt):
        # Consulta el teclado en cada frame y mueve al jugador mientras
        # una tecla permanezca apretada
        keys = pygame.key.get_pressed()

        player_position = self.player.get_component(Position)
        player_stats = self.player.get_component(Stats)

        direction_x = 0
        direction_y = 0

        if keys[pygame.K_w]:
            direction_y -= 1

        if keys[pygame.K_s]:
            direction_y += 1

        if keys[pygame.K_a]:
            direction_x -= 1

        if keys[pygame.K_d]:
            direction_x += 1

        # Si no se esta presionando ninguna dirección,
        # no movemos al jugador
        if direction_x == 0 and direction_y == 0:
            return

        # Por ahora usamos una velocidad simple.
        # Mas adelante se puede normalizar el movimiento diagonal
        speed = player_stats.speed * 40

        player_position.x += direction_x * speed * dt
        player_position.y += direction_y * speed * dt
        
    def render(self, screen):
        screen.fill(BLACK)

        position = self.player.get_component(Position)
        sprite = self.player.get_component(Sprite)
        if position and sprite:
            sprite.render(screen, position.x, position.y)

        position = self.enemy.get_component(Position)
        sprite = self.enemy.get_component(Sprite)
        if position and sprite:
            sprite.render(screen, position.x, position.y)

        player_health = self.player.get_component(Health)
        enemy_health = self.enemy.get_component(Health)
        enemy_hp_text = self.font.render(f"Enemigo: {enemy_health.health}/{enemy_health.max_health}", True, RED)
        screen.blit(enemy_hp_text, (10, 50))
         
        
        hp_text = self.font.render(f"Jugador: {player_health.health}/{player_health.max_health}", True, WHITE)
        screen.blit(hp_text, (SCREEN_WIDTH - 300, 10))

        if self.message:
            msg = self.font.render(self.message, True, WHITE)
            msg_rect = msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
            screen.blit(msg, msg_rect)

        if not self.game_over:
            controls = self.font.render("SPACE: Golpear | E: Poder Mágico", True, (100,100,100))
            controls_rect = controls.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
            screen.blit(controls, controls_rect)

        
