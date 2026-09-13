import pygame
import os

class Sprite:

    def __init__(self, width=32, height=32, color=None, image_path=None):
        self.width = width
        self.height = height
        self.color = color or (0, 128, 255)
        self.image = None
        self.animations = {}
        self.current_animation = "idle"
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_speed = 0.15
        self.direction = "down"
        self.flip_x = False
        self._prev_animation = "idle"
        
    def load_image(self, path):
        if os.path.exists(path):
            self.image = pygame.image.load(path).convert_alpha()

    def load_spritesheet(self, path, frame_width, frame_height, animations_config):
        if not os.path.exists(path):
            return

        sheet = pygame.image.load(path).convert_alpha()
        sheet_width = sheet.get_width()
        sheet_height = sheet.get_height()

        for anim_name, config in animations_config.items():
            frames = []
            row = config.get("row", 0)
            num_frames = config.get("frames", 1)
            for i in range(num_frames):
                x = i * frame_width
                y = row * frame_height
                if x + frame_width <= sheet_width and y + frame_height <= sheet_height:
                    frame = sheet.subsurface(pygame.Rect(x, y, frame_width, frame_height))
                    frames.append(frame)
            if frames:
                self.animations[anim_name] = frames

    def get_current_frame(self):
        if self.animations and self.current_animation in self.animations:
            frames = self.animations[self.current_animation]
            if frames:
                return frames[self.current_frame]
        if self.image:
            return self.image
        return None

    def update_animation(self, dt):
        if not self.animations or self.current_animation not in self.animations:
            return
        # Resetear frame cuando cambia la animacion (implementacion)
        if self.current_animation != self._prev_animation:
            self.current_frame = 0
            self.frame_timer = 0
            self._prev_animation = self.current_animation
        frames = self.animations[self.current_animation]
        if not frames:
            return
        self.frame_timer += self.frame_speed * dt * 60
        if self.frame_timer >= 1:
            self.frame_timer = 0
            self.current_frame += 1
            if self.current_frame >= len(frames):
                self.current_frame = 0

    def render(self, surface, x, y):
        frame = self.get_current_frame()
        if frame:
            if self.flip_x:
                frame = pygame.transform.flip(frame, True, False)
            surface.blit(frame, (x, y))
        else:
            rect = pygame.Rect(x, y, self.width, self.height)
            pygame.draw.rect(surface, self.color, rect)
            
