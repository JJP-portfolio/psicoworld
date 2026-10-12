# TDC-02 Curva de Dificultad — Resumen fiel + ejercicios (parcial)

Fuente: `~/unahur/TallerDeDiseñoConceptual/markdown/02-CurvaDeDificultad.md`.

## Resumen

- **Dificultad =** demandas del sistema (cognitivas/motrices) VS habilidades/recursos del jugador.
- **4 desafíos:** Mecánico (ejecución: Mario saltar), Cognitivo (pensar: Portal), Estratégico (planificar turnos: Fire Emblem), Percepción (leer pantalla: Bullet Hell).
- **Analizar un desafío (4 preguntas):** ¿qué pide? (precisión/lectura/planificación/admin/reacción/memoria) ¿qué info da? (visuales/sonido/ritmo/espacio/UI) ¿qué pasa si falla? (vida/tiempo/recursos/reinicio) ¿cómo cambia al aprender? (menos tiempo, más amenazas, combos, menos ayudas, más castigo).
- **Público:** no hay dificultad absoluta (Dark Souls ≠ Animal Crossing). Preguntas: ¿para quién? ¿experiencia? ¿nicho o amplio?
- **Sierra:** al introducir mecánica nueva, la dificultad BAJA para aprender y vuelve a subir. Etapas: presentación → práctica segura → exigencia aislada → combinación → dominio.
- **Justa vs injusta:** justa = enseñable + anticipa + castigo consistente + se aprende del fallo. Injusta = lo contrario.
- **Artificial** (stats: más vida/daño) vs **diseñada** (mecánicas que obligan a aprender).
- **Ajustes invisibles:** coyote time, hitboxes generosas, primer disparo falla (Bioshock), rubber banding, última vida resistente.
- **Feedback AV:** sonido daño, animaciones impacto, color UI, screenshake, partículas.

## Ejercicios (→ respuesta esperada)

1. Definí dificultad en 1 línea. → Demandas del sistema vs habilidades del jugador.
2. Clasificá: esquivar por timing / leer patrón de boss / administrar PE / ver venir el golpe. → Mecánico, cognitivo, estratégico, percepción.
3. Dibujá la sierra y marcá dónde está nuestra casa (tutorial). → Caída = dueño/diálogo (mecánica nueva), subida = guardias.
4. [INTEGRADOR] Analizá la primera batalla (Beat 5) con las 4 preguntas del apunte. → Detectar si es justa.
5. Etapas 1-5 aplicadas a "entrar a la casa". → Presentación puerta → práctica sin castigo → ... → dominio salir.
6. Justa o injusta: guardia que golpea sin telegraph. → Injusta (no anticipa). Fix: telegraph 0.5 s.
7. Artificial vs diseñada: duplicar HP del guardia vs agregar 2º guardia flanqueando. → Artificial vs diseñada.
8. [INTEGRADOR] 3 ajustes invisibles para PsicoWorld (ej: hitbox jugador chica, primer golpe guardia falla, i-frames). → Implementables.
9. Público: ¿Dark Souls o Animal Crossing? Definí el nuestro en 2 líneas. → Manda en toda la curva.
10. Feedback de nuestro golpe melee (lista de 3: sonido, flash, shake) y dónde va en código.
