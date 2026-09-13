# Ejercicios C8 — UI/UX, HUD y Curva de Dificultad

Archivos: renders de `menu_state.py`, `battle_state.py`, `explore_state.py` (texto HP). Conceptos uni: UI no-diegética / diegética / espacial / meta; curva de dificultad y flow.

1. (Fácil) El HP ya se muestra: cambiá su color según % (verde > 60 %, amarillo > 30 %, rojo abajo).
2. (Fácil) Barra de HP no-diegética: fondo + relleno proporcional + borde.
3. (Fácil) Barra ATB que carga con `speed` (base del combate nuevo): `progreso += speed * dt`.
4. [INTEGRADOR] Damage numbers flotantes: texto que sube, se achica y se borra en 1 s. Integrás combate + UI + dt.
5. (Medio) Cooldown visible para el click derecho (barra o número que baja).
6. (Medio) Mensaje contextual 2 s ("¡Bloqueado!") al chocar con los guardias.
7. (Medio) Telegraph: área en rojo 0.5 s antes de que el enemigo golpee (dificultad justa).
8. [INTEGRADOR] Menú de pausa con Continuar/Salir. Integrás estados + UI + input.
9. (Difícil) Curva: tabla oleada → (n enemigos, hp, daño) con rampa suave, sin saltos (flow channel).
10. (Difícil) Hit-stop + shake al golpear: congelar 60 ms + shake chico (game feel / UI meta).
