# Ejercicios D7 — Sistemas y decisiones

Base: portales condicionales, flags (`frozen`, `ignore_portals`, `casa_intro_done`), Beat 5, guardias en 2 mapas.

1. (Fácil) Listá todos los flags del juego y qué significan (5 hasta ahora).
2. (Fácil) ¿Qué pasa si `casa_intro_done` no existiera? (re-trigger infinito: explicar el bug.)
3. (Fácil) Portal condicional: escribí en palabras la condición "guardias dejan pasar".
4. [INTEGRADOR] Máquina de estados de la quest casa (afuera → adentro → diálogo → batalla → camino libre) con qué flag la mueve. Integrás guion + código.
5. (Medio) Diseñá el flag `guardias_bloqueando` (True/False): ¿quién lo cambia y cuándo?
6. (Medio) Guardias en 2 mapas: ¿misma entidad o 2? Pros/contras (identidad vs simplicidad).
7. (Medio) Símbolo examinable: objeto + tecla E + texto (reutilizar `Dialogue` sin NPC).
8. [INTEGRADOR] Beat 5 completo en papel: trigger fin-diálogo → guardias entran (spawn + caminan) → `change("battle")` → al volver, camino libre. Archivos y funciones por paso. Integrás todo el juego.
9. (Difícil) Guardado: ¿qué estado mínimo hay que persistir para cerrar y seguir? (mapa, pos, flags, stats: formato dict.)
10. (Difícil) Decisión documentada: ¿batalla separada (`battle_state`) o en el mapa (doc PE)? Escribí el ADR (contexto, opciones, decisión).
