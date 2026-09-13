# Ejercicios C6 — Cámara

Archivos: `src/camera.py`, `src/settings.py` (`SCREEN_WIDTH/HEIGHT`), uso en `explore_state.py`.

1. (Fácil) Centrar cámara en un punto sin smooth: `target - SCREEN // 2`, con 3 ejemplos numéricos.
2. (Fácil) Clamp manual con `max/min` para mapa grande: 3 casos (cerca del 0, medio, pasado del máximo).
3. (Fácil) Mapa chico: calculá el centrado (da negativo) y explicá por qué igual dibuja bien.
4. [INTEGRADOR] Follow con smooth: mismo recorrido con `smooth` 2.0 vs 8.0, describí la diferencia de feel. Integrás update + dt + clamp.
5. (Medio) `apply` / `reverse_apply` ida y vuelta: mundo → pantalla → mundo con 3 puntos.
6. (Medio) `is_on_screen` con 4 casos: adentro, afuera izquierda, borde exacto, objeto más grande que la pantalla.
7. (Medio) Lookahead: desplazá la cámara unos px hacia la dirección del movimiento.
8. [INTEGRADOR] Screenshake: variable trauma que decae con `dt` + offset aleatorio al renderizar. Integrás cámara + combate + dt.
9. (Difícil) Zoom: investigá `pygame.transform` para escalar la vista y medí el costo en FPS.
10. (Difícil) Cámara en la casa (30×20): calculá con números que queda centrada y sin scrollear.
