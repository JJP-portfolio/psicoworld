import pygame
import random
from src.states.state_machine import State
from src.settings import BLACK, WHITE, RED, SCREEN_WIDTH, SCREEN_HEIGHT
from src.entities.entity import Entity
from src.entities.enemy import Enemy
from src.components.position import Position
from src.components.sprite import Sprite
from src.components.stats import Stats
from src.components.health import Health
from src.systems import combat_system

class BattleState(State):

    def enter(self):
        self.font = pygame.font.Font("assets/fonts/diablo.ttf", 32)
        self.player = Entity()
        self.player.add_component(Position(100,SCREEN_HEIGHT // 2))
        self.player.add_component(Sprite(32, 32, (0, 128, 255)))
        self.player.add_component(Stats(hp=100, attack=15, magic=5, speed=8))
        self.player.add_component(Health(100))

        enemy_color = (255, 0, 0)
        self.enemy = Enemy(SCREEN_WIDTH - 150, SCREEN_HEIGHT //2, enemy_color, health = 80, damage = 10)

        self.entities = [self.player, self.enemy]
        self.message = ""
        self.message_timer = 0
        self.game_over = False
        self.turn = "player"

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_RETURN:
                        self.game.state_machine.change("explore")
                    return

                if self.turn != "player":
                    return

                player_stats = self.player.get_component(Stats)
                enemy_health = self.enemy.get_component(Health)

                if event.key == pygame.K_SPACE:
                    damage = player_stats.attack
                    enemy_health.take_damage(damage)
                    self.message = f"Golpeaste por {damage} de daño!"
                    self.message_timer = 2
                    self.turn = "enemy"

                elif event.key == pygame.K_e:
                    damage = player_stats.magic * 2
                    enemy_health.take_damage(damage)
                    self.message = f"Poder mágico por {damage} de daño!"
                    self.message_timer = 2
                    self.turn = "enemy"
                    
                    
    def update(self, dt):
        if self.message_timer > 0:
            self.message_timer -= dt
            if self.message_timer <= 0:
                self.message = ""
        self.player.get_component(Health).update(dt)
        self.enemy.get_component(Health).update(dt)
        
        if self.turn == "enemy" and self.message_timer <= 0:
            #Primero verifico si el enemigo murio.
            if not self.enemy.get_component(Health).is_alive():
                self.message ="Victoria! Ganaste 50 EXP!"
                self.message_timer = 3
                player_stats = self.player.get_component(Stats)
                player_stats.gain_exp(50)
                self.game_over = True
                return
            
            # Si no murio, el enemigo ataca.
            enemy_damage = self.enemy.damage
            player_health = self.player.get_component(Health)
            player_health.take_damage(enemy_damage)
            self.message = f"El enemigo te golpeó por {enemy_damage}!"
            self.message_timer = 2
            self.turn = "player"
            
            if not player_health.is_alive():
                self.message = "Derrota! Presiona Enter para volver."
                self.game_over = True

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

        
