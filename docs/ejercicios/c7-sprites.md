# Ejercicios C7 — Sprites y Animación

Archivos: `src/components/sprite.py`, `src/systems/movement_system.py`, animación en `explore_state.py`, sheet `Male 01-1.png` (96×128 = 3 cols × 4 filas: 0 abajo, 1 derecha, 2 izquierda, 3 arriba).

1. (Fácil) Cargá el PNG e imprimí sus dimensiones. ¿Cuántas filas/columnas de 32×32 entran?
2. (Fácil) Cortá la fila 0 en frames y mostralos numerados en pantalla.
3. (Fácil) Se piden 4 frames pero hay 3: ¿qué hace el chequeo de bordes en `load_spritesheet`? Cambiá el config a 3.
4. [INTEGRADOR] Diagnóstico de filas: tira etiquetada por fila (como hicimos con row1/row2) para ver qué mira cada una antes de mapearla. Integrás sheet + frames + render.
5. (Medio) `flip_x`: explicá qué rompe si el arte ya trae ambas direcciones. Sacalo del código.
6. (Medio) En `update_animation`: ¿por qué `frame_timer` usa `* dt * 60`? ¿Qué pasa si sacás el `* 60`?
7. (Medio) `_prev_animation`: ¿qué se vería mal si no reseteara el frame al cambiar de animación?
8. [INTEGRADOR] Animación por intención (teclas) + idle que conserve la última dirección. Integrás input + dirección + animación.
9. (Difícil) Hit-flash: al recibir daño, teñir el sprite de blanco 0.1 s.
10. (Difícil) Sombra elíptica bajo el sprite (feedback de posición y profundidad).
