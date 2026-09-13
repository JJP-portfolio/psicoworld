# Sistema de Tilemap — Porro Adventures

> **Última actualización:** 2026-09-11
> **Estado:** Integración con Tiled Map Editor funcionando (con bugs pendientes)

---

## Estado actual

El sistema carga mapas desde **Tiled Map Editor** (exportados como JSON). Ya funciona:
- Carga de tile layers desde JSON
- Spawn point desde Object Layer
- Colisiones desde Object Layer (con bug pendiente)
- Cámara con smooth follow

**Pendiente:** Mapa muy chico (40×23 = pantalla), necesita expandirse en Tiled.

---

## Arquitectura

```
Tiled Map Editor → exporta JSON → map_loader.py → Tilemap + Camera → explore_state.py
```

### Archivos involucrados

| Archivo | Responsabilidad |
|---------|-----------------|
| `src/tileset.py` | Carga PNG spritesheet, corta tiles individuales |
| `src/tilemap.py` | Matriz 2D + grid de colisiones + render con cámara |
| `src/camera.py` | Smooth follow + clamping a bordes del mapa |
| `src/map_loader.py` | Lee JSON de Tiled, construye Tilemap + colisiones + objetos |
| `src/states/explore_state.py` | Orquesta todo: carga mapa, posiciona jugador, actualiza cámara |

---

## Cómo funciona la carga desde Tiled

### 1. Tiled exporta JSON

```json
{
  "width": 40,
  "height": 23,
  "layers": [
    { "type": "tilelayer", "name": "Capa de patrones 1", "data": [...] },
    { "type": "tilelayer", "name": "Capa de patrones 2", "data": [...] },
    { "type": "objectgroup", "name": "Spawn", "objects": [...] },
    { "type": "objectgroup", "name": "Colisiones", "objects": [...] }
  ]
}
```

### 2. `map_loader.py` procesa el JSON

```python
# load_tiled_map() — convierte tilelayers a matriz Tilemap
def load_tiled_map(tileset, json_path):
    # Lee cada tilelayer, convierte GID a índice de tileset
    # GID de Tiled empieza en 1, nuestro tileset en 0 → tile_index = gid - 1

# load_collisions() — convierte rectángulos de Tiled a grid de colisiones
def load_collisions(tilemap, json_path):
    # Lee Object Layer "Colisiones"
    # Cada rectángulo → convierte a coordenadas de tile → marca True en grid

# get_objects_from_map() — lee objetos libres (spawns, portales)
def get_objects_from_map(json_path):
    # Retorna lista de dicts: {name, x, y, width, height}
```

### 3. `explore_state.py` usa todo junto

```python
def enter(self):
    self.tileset = Tileset("assets/tilesets/pipoya-rpg-tileset/[Base]BaseChip_pipo.png")
    self.tilemap = load_tiled_map(self.tileset, "data/maps/overworld_normal.json")
    load_collisions(self.tilemap, "data/maps/overworld_normal.json")
    objects = get_objects_from_map("data/maps/overworld_normal.json")
    for obj in objects:
        if obj['name'] == 'spawn_player':
            self.player.get_component(Position).x = obj['x']
            self.player.get_component(Position).y = obj['y']
```

---

## Estructura de carpetas de mapas

```
data/maps/
├── overworld_normal.json      ← Mapa actual (exportado desde Tiled)
├── normal/                    ← Zona Normal (futuros mapas)
├── hielo/                     ← Zona Hielo
├── volcanica/                 ← Zona Volcánica
├── desierto/                  ← Zona Desierto
└── shared/
    └── pipoya-32x32.tsx       ← Tileset compartido

assets/tilesets/pipoya-rpg-tileset/
├── [Base]BaseChip_pipo.png    ← Tileset principal (cargado por tileset.py)
├── [A]StructerChip_pipo.png   ← Edificios
├── [B]WallChip_pipo.png       ← Paredes
└── ... (10 archivos PNG organizados por categoría)
```

---

## Clases core

### Tileset (`src/tileset.py`)
Carga un spritesheet PNG y lo corta en tiles individuales de 32×32.

### Tilemap (`src/tilemap.py`)
- `map[][]` — matriz de índices de tile (qué tile va en cada celda)
- `collisions[][]` — matriz booleana (True = colisionable)
- `render(screen, camera_x, camera_y)` — dibuja solo tiles visibles
- `pixel_to_tile(px, py)` — convierte píxeles a coordenadas de tile
- `is_collidable(x, y)` — verifica colisión en coordenadas de tile

### Camera (`src/camera.py`)
- `update(target_x, target_y, dt)` — sigue al jugador con interpolación suave
- `apply(x, y)` — convierte coordenada del mundo a coordenada de pantalla
- `map_width`, `map_height` — tamaño del mapa en píxeles (para clamping)

---

## Colisiones

### Cómo se definen en Tiled
1. Crear Object Layer llamado "Colisiones"
2. Dibujar rectángulos sobre las áreas colisionables (árboles, muros, agua)
3. Guardar y exportar JSON

### Cómo se cargan en el código
`load_collisions()` convierte cada rectángulo del JSON a un rango de tiles en el grid:
```
Rectángulo en píxeles (x=64, y=0, w=32, h=128)
→ Tile起点: (64//32, 0//32) = (2, 0)
→ Tile终点: ((64+32)//32, (0+128)//32) = (3, 4)
→ Marca tiles (2,0) hasta (3,4) como colisionables
```

### Cómo se verifican en el movimiento
```python
# movement_system.py
new_x = position.x + dx * speed * dt
tile_x, tile_y = tilemap.pixel_to_tile(new_x + sprite.width//2, new_y + sprite.height//2)
if not tilemap.is_collidable(tile_x, tile_y):
    position.x = new_x  # Solo mover si no hay colisión
```

---

## Cámara — Zelda ALTTP / Pokémon style

La cámara sigue al jugador con interpolación suave y se detiene en los bordes del mapa.

```python
# Suavizado: se acerca al target un % cada frame
self.x += (target_cam_x - self.x) * self.smooth * dt

# Clamping: no salir del mapa
self.x = max(0, min(self.x, self.map_width - SCREEN_WIDTH))
self.y = max(0, min(self.y, self.map_height - SCREEN_HEIGHT))
```

**Bug conocido:** Cuando el mapa es igual o más chico que la pantalla, `map_width - SCREEN_WIDTH` ≤ 0, entonces `max(0, min(x, ≤0))` siempre da 0. Solución: hacer el mapa más grande que la pantalla.

---

## Optimización

### Renderizado solo de tiles visibles
```python
start_x = int(camera_x // self.tile_size)
start_y = int(camera_y // self.tile_size)
end_x = start_x + (SCREEN_WIDTH // self.tile_size) + 2
end_y = start_y + (SCREEN_HEIGHT // self.tile_size) + 2
# Solo dibujar tiles en ese rango
```

---

## Pendiente

- [x] Crear `src/tileset.py`
- [x] Crear `src/tilemap.py`
- [x] Crear `src/camera.py`
- [x] Crear `src/map_loader.py`
- [x] Cargar mapa desde Tiled JSON
- [x] Spawn point desde Object Layer
- [ ] Corregir bug en `map_loader.py:43-47` (syntax error + variables indefinidas)
- [ ] Expandir mapa en Tiled a ~60×40 tiles
- [ ] Pintar tiles reales (piso, caminos, edificios)
- [ ] Agregar rectángulos de colisión en Tiled
- [ ] Corregir camera.py clamping para mapas > pantalla
- [ ] Fix animación idle vs walk_down (misma fila)
- [ ] Sistema de portales/transiciones entre mapas
- [ ] Fondos de combate por zona
