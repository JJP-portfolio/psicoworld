import pygame
from src.components.position import Position
from src.components.sprite import Sprite

def _touches_wall(tilemap, px, py, w, h):
    margin = 4
    points = [
        (px + margin, py + margin),
        (px + w - margin, py + margin),
        (px + margin, py + h - margin),
        (px + w - margin, py + h - margin),
        (px + w // 2, py + h // 2),
    ]
    for qx, qy in points:
        tx, ty = tilemap.pixel_to_tile(qx, qy)
        if tilemap.is_collidable(tx, ty):
            return True
    return False
        

def update(entities, dt, tilemap):
    keys = pygame.key.get_pressed()
    speed = 200
    
    for entity in entities:
        position = entity.get_component(Position)
        sprite = entity.get_component(Sprite)

        if position and sprite:
            dx = 0
            dy = 0

            if keys[pygame.K_w]:
                dy -= 1
                sprite.direction = "up"
            if keys[pygame.K_s]:
                dy += 1
                sprite.direction = "down"
            if keys[pygame.K_a]:
                dx -= 1
                sprite.direction = "left"
            if keys[pygame.K_d]:
                dx += 1
                sprite.direction = "right"

            if dx != 0 or dy != 0:
                length = (dx**2 + dy**2) ** 0.5
                dx /= length
                dy /= length

            # Verificamos y adivinamos el proximo movimiento del pj, asi podemos recrear los tiles de manera mas eficiente. Ponele.
            new_x = position.x + dx * speed * dt
            if not _touches_wall(tilemap, new_x, position.y, sprite.width, sprite.height):
                position.x = new_x
            new_y = position.y + dy * speed * dt
            if not _touches_wall(tilemap, position.x, new_y, sprite.width, sprite.height):
                position.y = new_y
                
