from src.components.position import Position
from src.components.hitbox import Hitbox
from src.components.hurtbox import Hurtbox
from src.components.health import Health
from src.components.stats import Stats

def check_collisions(entities):
    hitboxes = []
    hurtboxes = []

    for entity in entities:
        position = entity.get_component(Position)
        hitbox = entity.get_component(Hitbox)
        hurtbox = entity.get_component(Hurtbox)

        if position and hitbox and hitbox.active:
            hitboxes.append((entity, position, hitbox))
        if position and hurtbox:
            hurtboxes.append((entity, position, hurtbox))

    for attacker, atk_pos, atk_hitbox in hitboxes:
        atk_rect = atk_hitbox.get_rect(atk_pos)
        for defender, def_pos, def_hurtbox in hurtboxes:
            if attacker is defender:
                continue
            def_rect = def_hurtbox.get_rect(def_pos)
            if atk_rect.colliderect(def_rect):
                health = defender.get_component(Health)
                if health:
                    stats = attacker.get_component(Stats)
                    damage = stats.attack if stats else 10
                    health.take_damage(damage)
                    
