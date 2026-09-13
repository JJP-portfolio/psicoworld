import random
from src.components.position import Position

def update(enemies, player_entity, dt):
    player_position = player_entity.get_component(Position)
    if not player_position:
        return

    for enemy in enemies:
        position = enemy.get_component(Position)
        if not position:
            continue

        dx = player_position.x - position.x
        dy = player_position.y - position.y
        distance = (dx**2 + dy**2) ** 0.5

        if distance < 200:
            if distance > 0:
                dx /= distance
                dy /= distance
            speed = 50
            position.x += dx * speed * dt
            position.y += dy * speed * dt
