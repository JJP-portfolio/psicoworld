import pygame
from src.states.state_machine import State
from src.settings import WHITE, BLACK, RED, SCREEN_WIDTH, SCREEN_HEIGHT

class CharacterCreationState(State):

    def enter(self):
        self.font = pygame.font.Font("assets/fonts/diablo.ttf", 32)
        self.title_font = pygame.font.Font("assets/fonts/diablo.ttf", 48)
        self.selected = 0
        self.classes = [
            {"name": "Guerrero", "alias": "El Anclado", "hp": 120, "attack": 15, "magic": 3, "speed": 5},
            {"name": "Mago", "alias": "El Visionario", "hp": 80, "attack": 5, "magic": 15, "speed": 6},
            {"name": "Arquero", "alias": "El Observador", "hp": 90, "attack": 10, "magic": 8, "speed":10}
        ]

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.classes)
                elif event.key == pygame.K_UP:
                    self.selected = (self.selected -1) % len(self.classes)
                elif event.key == pygame.K_RETURN:
                    self.game.player_class = self.classes[self.selected]
                    self.game.state_machine.change("explore")

    def render(self, screen):
        screen.fill(BLACK)

        title = self.title_font.render("Elegí tu clase", True, RED)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, title_rect)

        for i, cls in enumerate(self.classes):
            color = WHITE if i == self.selected else (100, 100, 100)

            name = self.font.render(f"{cls['name']} ({cls['alias']})", True, color)
            name_rect = name.get_rect(center=(SCREEN_WIDTH // 2, 250 + i * 120))
            screen.blit(name, name_rect)

            if i == self.selected:
                stats = self.font.render(f"HP:{cls['hp']} ATK:{cls['attack']} MAG:{cls['magic']} SPD:{cls['speed']}", True, (150, 150, 150))
                stats_rect = stats.get_rect(center=(SCREEN_WIDTH // 2, 290 + i * 120))
                screen.blit(stats, stats_rect)
