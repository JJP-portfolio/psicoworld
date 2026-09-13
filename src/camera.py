import pygame

from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Camera:

    def __init__(self, map_width, map_height):
        self.x = 0.0
        self.y = 0.0
        self.map_width = map_width
        self.map_height = map_height
        self.smooth = 5.0

    def update(self, target_x, target_y, dt=None):
        target_cam_x = target_x - SCREEN_WIDTH // 2
        target_cam_y = target_y - SCREEN_HEIGHT // 2

        if dt:
            self.x += (target_cam_x - self.x) * self.smooth * dt
            self.y += (target_cam_y - self.y) * self.smooth * dt
        else:
            self.x = target_cam_x
            self.y = target_cam_y

        if self.map_width > SCREEN_WIDTH:
            self.x = max(0, min(self.x, self.map_width - SCREEN_WIDTH))
        else:
            self.x = (self.map_width - SCREEN_WIDTH) // 2
            

        if self.map_height > SCREEN_HEIGHT:
            self.y = max(0, min(self.y, self.map_height - SCREEN_HEIGHT))
        else: self.y = (self.map_height - SCREEN_HEIGHT) // 2
            
    def apply(self, x, y):
        return x - self.x, y - self.y

    def apply_rect(self, rect):
        return pygame.Rect(rect.x - self.x, rect.y - self.y, rect.width, rect.height)

    def reverse_apply(self, screen_x, screen_y):
        return screen_x + self.x, screen_y + self.y

    def is_on_screen(self, x, y, width=32, height=32):
        return (x + width > self.x and x < self.x + SCREEN_WIDTH and
                y + height > self.y and y < self.y + SCREEN_HEIGHT)
        
    
