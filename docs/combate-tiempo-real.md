# Combate en Tiempo Real — Plan de Implementación

## Estado Actual

El `battle_state.py` actual es **por turnos** (temporal). Esto es un placeholder.

## Objetivo

Combate en **tiempo real** con:
- Movimiento WASD
- Ataque melee (click izquierdo)
- Ataque mágico (click derecho)
- Esquiva (Shift)
- Enemigos con IA que persiguen

## Arquitectura Actual vs Objetivo

### Actual (por turnos)
```
BattleState
├── turn = "player" | "enemy"
├── handle_events() → espera input
└── update() → ejecuta turno
```

### Objetivo (tiempo real)
```
BattleState
├── movement_system.update() → WASD
├── ai_system.update() → enemigos persiguen
├── combat_system.check_collisions() → daño por contacto
└── render() → dibuja todo cada frame
```

## Pasos para Convertir a Tiempo Real

### Paso 1: Mover todo a `update()`

```python
def update(self, dt):
    movement_system.update(self.entities, dt)
    ai_system.update(self.enemies, self.player, dt)
    combat_system.check_collisions(self.entities)
    
    for entity in self.entities:
        health = entity.get_component(Health)
        if health:
            health.update(dt)
```

### Paso 2: Agregar Hitbox al jugador

```python
# En enter():
from src.components.hitbox import Hitbox

self.player.add_component(Hitbox(32, 32))
```

### Paso 3: Detectar clicks del mouse

```python
def handle_events(self, events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Click izquierdo
                self.attack_melee()
            elif event.button == 3:  # Click derecho
                self.attack_magic()
```

### Paso 4: Métodos de ataque

```python
def attack_melee(self):
    player_hitbox = self.player.get_component(Hitbox)
    player_hitbox.active = True
    combat_system.check_collisions(self.entities)
    player_hitbox.active = False

def attack_magic(self):
    # Crear proyectil que se mueve hacia el mouse
    pass
```

### Paso 5: Enemigos con Hitbox

```python
# En Enemy.__init__():
self.add_component(Hitbox(32, 32))
```

### Paso 6: Daño por contacto

```python
# En combat_system.py:
# Si un enemigo toca al jugador → daño automático
```

## Referencias

### Pygame - Movimiento
```python
# Game loop básico
dt = clock.tick(FPS) / 1000
keys = pygame.key.get_pressed()
if keys[pygame.K_w]:
    player_pos.y -= speed * dt
```

### Pygame - Colisiones
```python
# Verificar si dos rectángulos se tocan
if rect1.colliderect(rect2):
    # Hay colisión
```

### Pygame - Mouse
```python
# Obtener posición del mouse
mouse_pos = pygame.mouse.get_pos()

# Verificar click
if event.type == pygame.MOUSEBUTTONDOWN:
    if event.button == 1:  # Izquierdo
        pass
```

## Extras para Tiempo Real

### Cooldown de ataques

```python
class AttackCooldown:
    def __init__(self, cooldown=0.5):
        self.cooldown = cooldown
        self.timer = 0
        self.can_attack = True
    
    def update(self, dt):
        if not self.can_attack:
            self.timer += dt
            if self.timer >= self.cooldown:
                self.can_attack = True
                self.timer = 0
    
    def use(self):
        if self.can_attack:
            self.can_attack = False
            self.timer = 0
            return True
        return False
```

### Knockback (retroceso al recibir daño)

```python
def apply_knockback(target, source, force=100):
    pos = target.get_component(Position)
    src_pos = source.get_component(Position)
    
    dx = pos.x - src_pos.x
    dy = pos.y - src_pos.y
    length = (dx**2 + dy**2) ** 0.5
    
    if length > 0:
        dx /= length
        dy /= length
    
    pos.x += dx * force
    pos.y += dy * force
```

### Barra de vida con imagen

```python
def draw_health_bar(surface, x, y, health, max_health):
    bar_width = 100
    bar_height = 10
    fill = (health / max_health) * bar_width
    
    pygame.draw.rect(surface, (100, 0, 0), (x, y, bar_width, bar_height))
    pygame.draw.rect(surface, (0, 200, 0), (x, y, fill, bar_height))
```

## Notas

- El sistema actual de components (Position, Sprite, Stats, Health, Hitbox, Hurtbox) ya soporta tiempo real
- Solo hay que cambiar cómo se usa en `battle_state.py`
- `movement_system.py` ya mueve entidades con WASD
- `ai_system.py` ya mueve enemigos hacia el jugador
- `combat_system.py` ya verifica colisiones

## Pendiente

- [ ] Cooldown de ataques
- [ ] Ataque mágico (proyectil)
- [ ] Esquiva (dash)
- [ ] Knockback
- [ ] Barra de vida con imagen
- [ ] Efectos visuales de daño
