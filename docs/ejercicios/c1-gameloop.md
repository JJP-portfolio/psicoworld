# Ejercicios C1 — Game Loop, Eventos y Delta Time

Archivos: `main.py`, `src/game.py`. Concepto: el loop init → eventos → update(dt) → render → flip.

1. (Fácil) Imprimí los FPS reales una vez por segundo con `clock.get_fps()`.
2. (Fácil) Cambiá `FPS` a 30, mové al jugador y describí qué cambia. ¿Por qué `dt` mantiene la velocidad igual?
3. (Fácil) Agregá un contador que cierre el juego solo después de 10 segundos.
4. [INTEGRADOR] Pausa con `P`: el update se congela (`dt = 0` efectivo) pero el render sigue. Integrás eventos + update + render.
5. (Medio) Mové un cuadrado a 200 px/s con `* dt`. Medí distancia recorrida en 5 s a 30 y 60 FPS: tiene que dar igual.
6. (Medio) Explicá con un ejemplo cada uno: ¿`KEYDOWN` o `get_pressed()` para disparar un poder? ¿Y para caminar?
7. (Medio) Tecla `C` que cambia el color de fondo, pero una sola vez por pulsación (pista: eventos, no estado).
8. [INTEGRADOR] Avance por frames: en pausa, `N` avanza la lógica exactamente un frame con `dt` fijo. Integrás pausa + update + input.
9. (Difícil) Mostrá `dt` en ms en pantalla. Contá los "picos" (frames de más de 33 ms) en 1 minuto.
10. (Difícil) Fixed timestep: acumulador que corre el update en pasos fijos de 1/60 aunque el render vaya a otra tasa.
