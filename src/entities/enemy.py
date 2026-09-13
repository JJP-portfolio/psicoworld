from src.entities.entity import Entity
from src.components.position import Position
from src.components.sprite import Sprite
from src.components.health import Health
from src.components.hitbox import Hitbox
from src.components.hurtbox import Hurtbox

class Enemy(Entity):

    def __init__(self, x=0, y=0, color=(255, 0, 0), health=50, damage=10):
        super().__init__()
        self.add_component(Position(x,y))
        self.add_component(Sprite(32, 32, color))
        self.add_component(Health(health))
        self.add_component(Hitbox(32, 32))
        self.add_component(Hurtbox(32, 32))
        self.damage = damage

        
