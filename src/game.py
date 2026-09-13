import pygame
import sys
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE, BLACK
from src.states.state_machine import StateMachine
from src.states.menu_state import MenuState
from src.states.explore_state import ExploreState
from src.states.character_creation_state import CharacterCreationState
from src.states.battle_state import BattleState

class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.state_machine = StateMachine()
        self.state_machine.register("menu", MenuState(self))
        self.state_machine.change("menu")
        self.state_machine.register("character_creation", CharacterCreationState(self))
        self.state_machine.register("explore", ExploreState(self))
        self.state_machine.register("battle", BattleState(self))
        
    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.state_machine.handle_events([event])

            self.screen.fill(BLACK)
            self.state_machine.update(dt)
            self.state_machine.render(self.screen)

            pygame.display.flip()

        pygame.quit()
        sys.exit()
    
