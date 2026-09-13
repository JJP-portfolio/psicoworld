# Ejercicios C4 — Tiled: JSON, GIDs, Capas, Tileset

Archivos: `src/map_loader.py` (`load_tiled_map`, `get_objects_from_map`), `src/tileset.py`, `src/tilemap.py`, `data/maps/overworld_normal.json`.

1. (Fácil) Imprimí `width`, `height` y cantidad de capas del JSON.
2. (Fácil) Listá nombre y tipo (`tilelayer`/`objectgroup`) de cada capa.
3. (Fácil) Función `gid_a_local(gid, firstgid) = gid - firstgid`. Probala con 3 casos.
4. [INTEGRADOR] Mini-cargador: dibujá el mapa en una Surface con solo loops + `blit`, sin usar `Tilemap`. Integrás JSON + GID + tileset.
5. (Medio) Histograma: contá cuántos tiles de cada GID hay por capa.
6. (Medio) Detectá GIDs fuera de rango del tileset e informá capa + coordenada.
7. (Medio) Soportá 2 tilesets: elegí el tileset según el rango del GID (por `firstgid`).
8. [INTEGRADOR] Validador de mapa: chequea firstgid, GIDs válidos, que exista `spawn_player` y que cada portal tenga target. Reporta errores. Integrás todo C4.
9. (Difícil) Culling: dada una cámara, calculá tiles visibles (como `tilemap.render`) y compará dibujados vs totales.
10. (Difícil) Exportá las colisiones a un PNG (rojo = colisión) como mapa de debug.
