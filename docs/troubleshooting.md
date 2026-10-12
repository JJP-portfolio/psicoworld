# Troubleshooting — PsicoWorld

> Incidentes reales de la sesión 2026-09-13 + FAQs de Tiled verificadas en la doc oficial (doc.mapeditor.org) y el foro.

## Incidente 2026-09-13: "se rompió" al limpiar tiles invisibles

**Evidencia recogida (todo sano):**

| Chequeo | Resultado |
|---|---|
| `limpiar_mapa.py` en el proyecto / home / tmp | No existe — el script nunca se creó ni corrió |
| `data/maps/*.bak` | No existe — confirma que el script nunca corrió |
| `overworld_normal.json` | Válido: 60×40, 12 capas, timestamp = último export de Tiled |
| `py_compile` de todo `src/` | OK |
| Smoke headless explore (60 frames update+render) | OK |

**Conclusión:** nada del proyecto está roto.pendiente: el estudiante debe pasar el **texto exacto del error** (traceback o mensaje) para diagnosticar. Sospechas: correr el script desde otro directorio (`FileNotFoundError`), error de tipeo/indentación al escribirlo, o el juego sigue mostrando negro (esperable: las 40 celdas nunca se limpiaron).

## FAQ 1 — Guardar (.tmx) vs Exportar (.json)

- `Ctrl+S` guarda el `.tmx`. El juego lee el `.json` → hay que **Archivo → Exportar como** cada vez.
- Alternativa por línea de comandos (doc oficial): `tiled --export-map mapa.tmx data/maps/mapa.json`. Sirve para automatizar.
- REGLA (incidente 11:17, definitiva 2026-09-13): el `.json` de `data/maps/` es la fuente de verdad.
  Se borró `assets/tmx/mapa_inicio.tmx` (pisaba los fixes al exportar). Abrir y guardar el `.json`
  directo en Tiled. Backup post-fix: `*.fixed`.

## FAQ 2 — Editar el JSON a mano o con script

- Seguro si: el JSON sigue válido + backup previo. Validar con `python -c "import json; json.load(open('...'))"`.
- Tiled re-lee el archivo al abrirlo; no se corrompe por editarlo externamente.
- `layer["data"][y * width + x]` = celda (x, y). Ponerla en 0 = goma de borrar.

## FAQ 3 — Tipos de objeto (doc oficial, formato JSON)

- **Point:** `"point": true`, `width = height = 0`. Sin área: no se puede estirar ni detectar overlap. Usar solo para posiciones (spawn, NPCs).
- **Rectangle:** `width`/`height` en px. Para zonas (colisiones, portales).
- **Polygon:** puntos en `obj["polygon"]`, **relativos** a `x, y`; `width = height = 0`. Nuestro código los lee con bbox + `point_in_polygon`.
- **Polyline:** igual que polygon pero línea abierta (caminos, paredes finas). Nuestro código aún no la soporta.

## FAQ 4 — Tiles negros (agujeros y franjas)

- **Caso A (40 celdas):** tile **transparente del PNG** pintado en una capa superior tapa el suelo → agujero negro. Detectar con conteo de tiles 100 % transparentes usados. Se arregla borrando la celda (goma)… o mejor, ver Caso B.
- **Caso B (raíz real, sesión 2026-09-13):** el cargador viejo guardaba **UN tile por celda** (ganaba la última capa). El tile de árbol **reemplazaba** al pasto en vez de apilarse → sus bordes transparentes mostraban el fondo negro. Se veía negro "todo lo que tenía colisión" porque las colisiones están sobre árboles/cercos/plantas (capas superiores).
- **Fix:** `Tilemap.layers` (una grilla por capa) + render apilado saltando ceros. Verificado: píxeles negros 14321 → 20.

## FAQ 6 — Colisiones "raras" (anotado 2026-09-13, pendiente ajuste)

- Detectado por script: 34 celdas con colisión y arte claro (lum > 110), concentradas arriba-derecha (fila 2 x50-59, fila 3 x43-44/x50-59, zona casa). Se siente como pared invisible: el rect cubre más que el muro visible (techo incluido).
- Otras causas posibles: enganche de esquinas al deslizar (el margen 4 px lo mitiga pero no lo elimina), caja de 32 px vs arte más chico.
- Fix futuro: ajustar rects al muro visible o colisión por tile; re-correr el script de detección para verificar 0 casos.

## FAQ 5 — firstgid y GIDs

- Con un solo tileset con `firstgid = 1`: `índice = gid - 1`.
- Si se agregan tilesets, cada uno trae su `firstgid`; el índice es `gid - firstgid` del rango correspondiente.
- Referencia: doc oficial "Global Tile IDs / Mapping a GID to a Local Tile ID".

## Recuperación

- Si un script rompe el JSON: restaurar desde el `.bak` (`cp archivo.json.bak archivo.json`).
- Si Tiled no abre el mapa: validar JSON (FAQ 2) y revisar que los `.tsx`/PNG referenciados existan en su ruta.
