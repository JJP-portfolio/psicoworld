# Guía Tiled Map Editor — Porro Adventures

## Qué es Tiled

Tiled es un editor de mapas 2D gratuito (https://www.mapeditor.org). Es el estándar de la industria para juegos top-down y side-scrollers.

## Conceptos clave

| Concepto | Qué es |
|----------|--------|
| **Tileset** | Tu spritesheet PNG cargado como paleta de tiles |
| **Tile Layer** | Capa de tiles dibujados (piso, paredes, árboles) |
| **Object Layer** | Capa de objetos libres (spawns, portales, NPCs) |
| **Properties** | Datos custom en tiles/objetos (ej: "collidable: true") |

## Instalación

1. Descargar de https://www.mapeditor.org
2. Instalar (gratis, cross-platform)
3. Abrir Tiled

## Crear un mapa

1. File → New → New Map
2. Configurar:
   - Orientation: **Orthogonal**
   - Tile size: **32 x 32**
   - Map size: **40 x 23** (para que ocupe pantalla 1280x720)
3. Guardar en `data/maps/`

## Cargar tileset

1. File → New → New Tileset
2. Browse → seleccionar `pipo-map001.png`
3. Tile size: 32 x 32
4. Margin: 0, Spacing: 0
5. Guardar como `.tsx` en `assets/tilesets/`

## Pintar tiles

1. Seleccionar tile de la paleta izquierda
2. Click izquierdo para pintar en el mapa
3. Click derecho para borrar
4. Shift+click para pintar línea

## Capas (Layers)

Crear capas para organizar:
- **ground** — piso (pasto, camino, agua)
- **objects** — árboles, rocas, edificios
- **collisions** — invisible, marca colisiones
- **portals** — objetos de transición entre mapas

## Colisiones en Tiled

### Opción 1: Propiedades en tiles
1. En el tileset, click derecho en un tile → Properties
2. Agregar property: `collidable` = `true`
3. En el juego, leer esta property

### Opción 2: Object layer
1. Crear Object Layer "collisions"
2. Dibujar rectángulos sobre paredes/obstáculos
3. En el juego, verificar si el jugador colisiona con estos rectángulos

## Portales (transiciones entre mapas)

1. Crear Object Layer "portals"
2. Dibujar rectángulo en la entrada/salida del mapa
3. Click derecho → Properties
4. Agregar:
   - `target_map` = "ciudad_normal.json"
   - `target_x` = 160
   - `target_y` = 400

## Exportar

- File → Export As → JSON
- Guardar en `data/maps/`

## Formato JSON de Tiled

```json
{
  "width": 40,
  "height": 23,
  "tilewidth": 32,
  "tileheight": 32,
  "layers": [
    {
      "name": "ground",
      "type": "tilelayer",
      "data": [1, 2, 3, ...]
    },
    {
      "name": "portals",
      "type": "objectgroup",
      "objects": [
        {
          "name": "portal_ciudad",
          "type": "portal",
          "x": 320, "y": 0,
          "properties": [
            {"name": "target_map", "type": "string", "value": "ciudad.json"}
          ]
        }
      ]
    }
  ],
  "tilesets": [
    {
      "firstgid": 1,
      "source": "pipoya-32x32.tsx"
    }
  ]
}
```

## Cargar en pygame con pytmx

```python
pip install pytmx
```

```python
import pytmx
from pytmx.util_pygame import load_pygame

tmx_data = load_pygame("mapa.tmx")

# Renderizar tiles
for layer in tmx_data.visible_layers:
    if isinstance(layer, pytmx.TiledTileLayer):
        for x, y, gid in layer:
            tile = tmx_data.get_tile_image_by_gid(gid)
            if tile:
                screen.blit(tile, (x * 32, y * 32))

# Leer objects
for obj in tmx_data.get_layer_by_name("portals"):
    if obj.type == "portal":
        target = obj.properties["target_map"]
```
