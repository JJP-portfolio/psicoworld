# Ejercicios D4 — Progresión y economía

Base: `Stats` (hp/attack/magic/speed/level/exp), tabla psicotrópicos por zona (`DESIGN.md`), upgrades de oleadas (doc combate).

1. (Fácil) Leé `stats.py`: ¿qué sube por nivel y cuánto? ¿Cuántos EXP pide el nivel 3?
2. (Fácil) Listá las 4 monedas/recursos del juego (EXP, HP, PE futuro, psicotrópicos).
3. (Fácil) Cada psicotrópico de la tabla: ¿consumible, equipable o reliquia? ¿Por qué esa categoría?
4. [INTEGRADOR] Flujo de una mejora completa (matar → EXP → nivel → stat) con números reales del código. Integrás sistema + datos.
5. (Medio) Balance: ¿cuántos golpes aguanta el Guerrero vs el Mago contra daño 10? ¿Es justo?
6. (Medio) Diseñá el costo PE de invocar 1/2/3 monstruos + regen/s (que no spamee ni nunca alcance).
7. (Medio) Tabla de upgrades entre oleadas (3 opciones × 3 niveles) con costos.
8. [INTEGRADOR] Economía del tutorial: qué gana el jugador en Beats 1-5 y qué gasta. Sin recompensa en algún beat → rediseñarlo. Integrás guion + números.
9. (Difícil) Curva EXP 1-20: fórmula que no se dispare (compará lineal vs `level*100` actual).
10. (Difícil) Decidí y documentá: ¿el combate da EXP, drops, o ambos? ¿Por qué? (pilares mandan.)
