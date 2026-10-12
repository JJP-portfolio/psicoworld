import pygame


class Dialogue:

    def __init__(self,lines):
        self.lines = lines
        self.index = 0
        self.active = False
        self.shake_start = None
        
    def start(self):
        self.index = 0
        self.active = True
        self.shake_start = pygame.time.get_ticks()

    def shake_offset(self):
        if self.shake_start is None:
            return(0, 0)
        elapsed = pygame.time.get_ticks() - self.shake_start
        if elapsed > 600:
            return (0,0)
        if (elapsed // 60) % 2 == 0:
            return (3,0)
        return (-3, 0)
        
        
    def current(self):
        if self.active and self.index < len(self.lines):
            return self.lines[self.index]
        return None

    def advance(self):
        self.index += 1
        if self.index >= len(self.lines):
            self.active = False

    def finished(self):
        return not self.active
