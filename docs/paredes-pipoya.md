# Paredes Pipoya en Tiled — Guía (investigado 2026-09-13)

Fuentes: doc oficial Tiled (Terrain Sets, Automapping), foros Tiled (RPG Maker autotiles ≠ Tiled),
devlog oficial de Pipoya (compatibilidad Tiled 1.5), spec comunitario de autotiles RPG Maker MV/MZ,
inspección directa de `[Base]BaseChip_pipo.png`.

## 1. Concepto clave: en top-down todo se ve de frente

No existen "paredes 3D". La pared NORTE se dibuja de frente; las paredes ESTE/OESTE se dibujan
como **tiras verticales de la misma textura con sombreado lateral** (la franja oscura dice "borde").
Por eso el sheet trae columnas sombreadas: son los costados.

## 2. Set de madera exterior (G497-512)

| Tiles | Rol |
|---|---|
| G497-500 | Tablones con borde superior plano → **pared norte** (fila de arriba) |
| G505-508 | Tablones cuerpo → **pared sur** y rellenos |
| G501-502 / G509-510 | Tablones con banda oscura a la derecha → **paredes este/oeste** (apilados en vertical) |
| G511 | Panel liso → parche/relleno interior |
| G504, G512 | Postigos/puertitas decorativas |

## 3. Set interior papel + zócalo (G513-528) — ideal casa por dentro

| Tiles | Rol |
|---|---|
| G513-518 | Papel rayado → pared interior norte |
| G521-526 | Papel + zócalo oscuro abajo → pared interior sur (o 2ª fila bajo el papel) |
| G519, G527 | Panel liso |
| G528 | **Puerta marrón** (1 tile, para el hueco) |

## 4. Receta casa 30×20 (pared de 1 tile)

1. Piso de madera primero en todo el interior (capa Suelo).
2. Fila superior (y=0): G497-500 repetidos = pared norte.
3. Columna izquierda (x=0) y derecha (x=29): G501/G509 apilados = costados.
4. Fila inferior (y=19): G505-508, dejando hueco de 2 tiles en el centro.
5. Hueco: puerta G528 arriba + tile de piso abajo (se pisa para salir).
6. Esquinas: se tocan solas; si se ve un diente, tapar con G511.
7. Pared divisoria (pisos): misma receta en chico + hueco de escalera con tiles de escalera.
8. Colisiones: un rect por cada tramo de pared (4 exteriores + divisoria); NADA en el hueco.

## 5. Alternativas (cuándo usarlas)

- **Terrain Brush** (doc oficial Tiled "Using Terrains"): para pintar pasto↔tierra rápido. Requiere
  marcar tiles (Corner/Edge/Mixed). NO sirve directo para autotiles RPG Maker A1-A4 (piezas, no tiles).
- **Automapping**: para acantilados/lados verticales automáticos. Overkill para una casa.
- Para la casa: **sello manual** (Stamp Brush). Son ~100 tiles, 15 minutos.

## 6. Incertidumbres honestas

- El rol exacto de cada columna sombreada se infiere del sombreado, no de doc Pipoya (no publican
  mapa de roles). Si un costado se ve raro, probar la columna vecina.
- Pisos de madera: están en el sheet cerca de muebles (zona baja); ubicar por ID al pasar el mouse.
