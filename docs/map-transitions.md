# Sistema de Transiciones — Porro Adventures

## Cómo funciona

Cuando el jugador toca un portal:
1. Guardar stats del jugador (HP, nivel, inventario)
2. Fade a negro (0.5 seg)
3. Cargar nuevo mapa desde Tiled
4. Posicionar al jugador en target_x, target_y
5. Fade desde negro (0.5 seg)

## Formato de portal en Tiled

Object Layer "portals" con rectángulos:

```json
{
  "name": "portal_ciudad",
  "type": "portal",
  "x": 320, "y": 0,
  "width": 64, "height": 32,
  "properties": [
    {"name": "target_map", "type": "string", "value": "ciudad_normal.json"},
    {"name": "target_x", "type": "int", "value": 160},
    {"name": "target_y", "type": "int", "value": 400}
  ]
}
```

## Transiciones estilo FF1

FF1 (NES) usaba:
- Mapa mundo (overworld) = pantalla grande
- Mapa ciudad = pantalla separada
- Al tocar tile de ciudad → fade a negro → cargar ciudad
- Al tocar salida → fade a negro → volver al overworld

## Método moderno (nuestro approach)

1. Cada mapa es un archivo JSON/TMX separado
2. Portales son objetos en Tiled con properties
3. El juego detecta colisión con portal
4. Carga nuevo mapa y reposiciona jugador
5. Fade in/out para la transición

## Archivos a crear

- `src/transition.py` — Efecto fade in/out
- `src/map_loader.py` — Carga mapas desde Tiled
- Modificar `explore_state.py` — Usar loader + transiciones
