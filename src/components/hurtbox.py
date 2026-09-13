import pygame

class Hurtbox:

    def __init__(self, width=32, height=32, offset_x=0, offset_y=0):
        self.width = width
        self.height = height
        self.offset_x = offset_x
        self.offset_y = offset_y

    def get_rect(self, position):
        return pygame.Rect(
            position.x + self.offset_x,
            position.y + self.offset_y,
            self.width,
            self.height
        )
