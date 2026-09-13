# Ejercicios C5 — Colisiones

Archivos: `src/map_loader.py` (`load_collisions`, `point_in_polygon`), `src/tilemap.py` (`is_collidable`, `pixel_to_tile`), `src/systems/movement_system.py`.

1. (Fácil) Marcá un tile con `set_collision` y verificá `is_collidable` en True/False/adentro/afuera del mapa.
2. (Fácil) `pixel_to_tile` / `tile_to_pixel` ida y vuelta con 5 puntos (incluido un borde exacto múltiplo de 32).
3. (Fácil) Rect de 1 tile (32×32 alineado) marca exactamente 1 tile. Demostralo.
4. [INTEGRADOR] Muro de 3 tiles: rect de 96×32 → exactamente 3 tiles marcados, verificado con loop. Integrás rect + grilla + chequeo.
5. (Medio) Rect parcial de 21 px: ¿qué tiles toca con la fórmula `(x+w-1)//32`? ¿Y con la vieja `x//32 + w//32`?
6. (Medio) En papel: 3 puntos de polígono → calculá su caja (min/max) a mano.
7. (Medio) `point_in_polygon` con un cuadrado 0..100: centro True, (200,200) False, punto sobre el borde (anotá qué da y por qué).
8. [INTEGRADOR] Polígono en U: la caja marca el hueco, el test exacto no. Demostralo con un test que compare ambos conteos. Integrás bbox + ray casting + grilla.
9. (Difícil) Colisión multi-punto del jugador: chequeá centro + 4 esquinas en vez de solo el centro.
10. (Difícil) Flood fill de alcanzabilidad desde el spawn como función reutilizable (detecta zonas encerradas).
