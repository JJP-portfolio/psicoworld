# Ejercicios C2 — State Machine

Archivos: `src/states/state_machine.py`, `menu_state.py`, `character_creation_state.py`, `explore_state.py`, `battle_state.py`, `src/game.py`.

1. (Fácil) Registrá un estado `"pausa"` vacío y entrá con `P` desde explore. Volvé con `P`.
2. (Fácil) Logueá cada `change()`: imprimí `"saliendo de X → entrando a Y"`.
3. (Fácil) Explicá con tus palabras: ¿por qué `enter()` se ejecuta más veces que `__init__`? ¿Dónde se crean los estados?
4. [INTEGRADOR] Estado `"game_over"`: al morir en battle muestra texto y con RETURN vuelve a `"menu"`. Integrás estados + eventos + render.
5. (Medio) Pasá datos por `game` (como `player_class`): contá muertes en `game.muertes` y mostralas en el menú.
6. (Medio) Implementá `exit()` en explore que guarde la posición en `game.last_pos`.
7. (Medio) Al volver de battle, posicioná al jugador en `game.last_pos` (alternativa al `hasattr` actual). Compará ambas.
8. [INTEGRADOR] Pila push/pop: pausa encima de explore sin reconstruir nada al volver. Integrás lifetime + input + render.
9. (Difícil) `change()` seguro: nombre inexistente → mensaje y seguir en el estado actual, sin romper.
10. (Difícil) Transición con fade de 0.5 s a negro entre estados (base de `src/transition.py`).
