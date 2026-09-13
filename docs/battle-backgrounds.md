# Fondos de Combate por Zona — Feature

## Concepto

El fondo del combate refleja la zona donde se encuentra el jugador. Inspirado en:
- **Final Fantasy 1-6** — Fondo según bioma (bosque, cueva, desierto)
- **Phantasy Star 4** — Escenarios detallados por zona
- **Chrono Trigger** — Fondos únicos por ubicación

## Referentes

| Juego | Cómo lo hace |
|-------|--------------|
| FF1-FF6 | Fondo estático de 256x240 px, 16 colores por zona |
| Phantasy Star 4 | Fondos detallados con elementos del entorno |
| Chrono Trigger | Fondos animados con efectos de partículas |
| Earthbound | Fondos surrealistas que cambian con la música |

## Implementación

### Flujo de datos

```
explore_state.py
    ↓
zone = "normal" | "hielo" | "volcanica" | "desierto"
    ↓
battle_state.py
    ↓
battle_background = backgrounds[zone]
    ↓
screen.blit(battle_background, (0, 0))
```

### Estructura de archivos

```
assets/backgrounds/
├── normal/
│   ├── forest.png      ← Bosque nebuloso
│   ├── meadow.png      ← Pradera con psilocybe
│   └── city.png        ← Megalopolis
├── hielo/
│   ├── frozen_lab.png  ← Laboratorio congelado
│   ├── ice_cave.png    ← Cueva de hielo
│   └── crystals.png    ← Cristales de MDMA
├── volcanica/
│   ├── lava_field.png  ← Campo de lava
│   ├── volcano.png     ← Volcán activo
│   └── acid_trail.png  ← Sendero de LSD
└── desierto/
    ├── sand_dunes.png  ← Dunas de arena
    ├── cactus.png      ← Cactus con peyote
    └── mirage.png      ← Espejismo
```

### Tamaño de fondos

| Tipo | Resolución | Uso |
|------|------------|-----|
| **Full** | 1280x720 | Fondo completo del combate |
| **Layer** | 1280x360 | Capa superior (cielo/techo) |
| **Tile** | 32x32 | Tiles individuales para componer |

### Opción 1: Fondos pre-renderizados (recomendada)

Descargar o crear fondos completos para cada zona.

**Ventajas:**
- Simple de implementar
- Calidad visual alta
- No requiere lógica compleja

**Desventajas:**
- Ocupan más memoria
- Menos flexible

### Opción 2: Fondos compuestos con tiles

Usar tiles existentes para componer el fondo.

**Ejemplo:**
```python
def compose_battle_background(zone, tileset):
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    if zone == "normal":
        # Fondo de bosque
        for y in range(0, SCREEN_HEIGHT, 32):
            for x in range(0, SCREEN_WIDTH, 32):
                tile = random.choice([
                    tileset.tiles[1],  # Pasto
                    tileset.tiles[2],  # Pasto con flores
                    tileset.tiles[3],  # Arbusto
                ])
                background.blit(tile, (x, y))

    elif zone == "hielo":
        # Fondo de hielo
        for y in range(0, SCREEN_HEIGHT, 32):
            for x in range(0, SCREEN_WIDTH, 32):
                tile = random.choice([
                    tileset.tiles[10],  # Hielo
                    tileset.tiles[11],  # Hielo con grietas
                    tileset.tiles[12],  # Cristal
                ])
                background.blit(tile, (x, y))

    return background
```

**Ventajas:**
- Reutiliza tiles existentes
- Ahorra memoria
- Flexible

**Desventajas:**
- Menos detallado
- Requiere lógica de composición

### Opción 3: Híbrida

Tiles de fondo + elementos pre-renderizados encima.

```python
def render_battle_background(screen, zone, tileset):
    # 1. Dibujar tiles de fondo
    draw_background_tiles(screen, zone, tileset)

    # 2. Agregar elementos decorativos
    draw_decorations(screen, zone)

    # 3. Agregar efectos de partículas
    draw_particles(screen, zone)
```

## Efectos por zona

### Zona Normal (Psilocybe)

| Elemento | Descripción | Efecto |
|----------|-------------|--------|
| Niebla | Capa semitransparente | Parallax lento |
| Hongos | Psilocybe creciendo | Animación de crecimiento |
| Hojas | Caen del cielo | Partículas |
| Luciérnagas | Puntos de luz | Parpadeo |

### Zona Hielo (MDMA)

| Elemento | Descripción | Efecto |
|----------|-------------|--------|
| Cristales | MDMA congelada | Brillo intermitente |
| Nieve | Caída constante | Partículas |
| Escarcha | Bordes de pantalla | Overlay |
| Aurora | Cielo cambiante | Gradiente animado |

### Zona Volcánica (LSD)

| Elemento | Descripción | Efecto |
|----------|-------------|--------|
| Lava | Ríos de color | Animación de flujo |
| Humo | Columnas ascendentes | Partículas |
| Colores | Alteración visual | Shader/overlay |
| Visiones | Elementos distorsionados | Ondulación |

### Zona Desierto (Peyote)

| Elemento | Descripción | Efecto |
|----------|-------------|--------|
| Espejismo | Ondulación del aire | Ondulación |
| Cactus | Peyote creciendo | Estático |
| Arena | Viento moviendo | Partículas |
| Sol | Luz intensa | Bloom/brillo |

## Integración con battle_state.py

### Modificaciones necesarias

```python
class BattleState(State):

    def enter(self, zone="normal"):
        self.zone = zone
        self.background = self.load_background(zone)
        # ... resto de la inicialización

    def load_background(self, zone):
        """Carga el fondo según la zona"""
        backgrounds = {
            "normal": "assets/backgrounds/normal/forest.png",
            "hielo": "assets/backgrounds/hielo/frozen_lab.png",
            "volcanica": "assets/backgrounds/volcanica/lava_field.png",
            "desierto": "assets/backgrounds/desierto/sand_dunes.png",
        }
        return pygame.image.load(backgrounds[zone])

    def render(self, screen):
        # 1. Dibujar fondo
        screen.blit(self.background, (0, 0))

        # 2. Dibujar entidades
        # ...existing code...

        # 3. Dibujar UI
        # ...existing code...
```

### Pasar zona desde explore_state

```python
# En explore_state.py
def handle_events(self, events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Pasar zona actual al battle state
                self.game.state_machine.change("battle", zone=self.zone)
```

## Assets necesarios

### Opción A: Descargar

Buscar en:
- **itch.io** — "RPG battle background free"
- **OpenGameArt.org** — "battle background"
- **Kenney.nl** — Assets gratuitos de alta calidad

### Opción B: Crear con Krita

Usar el workflow documentado en `docs/krita-workflow.md`:
- Paleta por zona
- Tamaño: 1280x720
- Formato: PNG con transparencia

### Opción C: Componer con tiles

Usar los tiles de Pipoya para crear fondos proceduralmente.

## Pendiente

- [ ] Definir estilo visual de fondos
- [ ] Decidir tamaño de resolución
- [ ] Crear/buscar assets para cada zona
- [ ] Implementar carga de fondos en battle_state
- [ ] Agregar efectos de partículas
- [ ] Probar integración explore → battle
