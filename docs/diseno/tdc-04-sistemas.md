# TDC-04 Juegos como Sistemas — Resumen fiel + ejercicios (parcial)

Fuente: `~/unahur/TallerDeDiseñoConceptual/markdown/04-JuegosComoSistemas.md`.

## Resumen

- **Definiciones (4 autores):** Parlett (formal: fines = disputa por objetivo + medios = reglas/equipo), Abt (2+ jugadores deciden en contexto limitado), Huizinga (libre, fuera de lo ordinario, absorbe, sin interés material), Crawford (sistema cerrado formal + conflicto + resultado cuantificable + espacio seguro), Zimmerman/Salen (conflicto artificial + reglas + resultado cuantificable).
- **Sistema =** objetos con atributos + relaciones internas + entorno delimitado.
- **Meaningful play:** discernible (se percibe causa→efecto) + integrado (afecta el estado general). Sin eso no hay juego significativo.
- **Feedback loops:** positivo/refuerzo (minar→mejor pico→minar más, Minecraft) y negativo/regulador (correr→hambre→comer).
- **Tabla sistema:** objetos (jugador, NPCs, tiles), atributos (HP, ATK, posición), relaciones (combate, diálogo), entorno (3 escenas), reglas (turnos, colisiones), resultados (victoria, EXP).

## Ejercicios (→ respuesta esperada)

1. Definí juego según Crawford (4 elementos). → Sistema cerrado + conflicto + resultado cuantificable + espacio seguro.
2. Crawford vs Huizinga: ¿en qué se diferencian? → Resultado cuantificable vs actividad libre sin beneficio.
3. Componentes de un sistema (6) con ejemplo PsicoWorld c/u. → La tabla de arriba.
4. [INTEGRADOR] PsicoWorld como sistema completo (tabla llena con datos reales del código). → Objetos=Entity etc.
5. Meaningful play: ¿nuestro portal puerta→casa es discernible? ¿integrado? → Sí/sí (se ve el cambio + cambia mapa/pos).
6. ¿Y presionar E lejos de un NPC (hoy)? → No hay feedback → NO meaningful. Fix D6.
7. Loop positivo y uno negativo de PsicoWorld (inventar con EXP/hambre). → Ej: ganar→nivel→matar más rápido; PE gasta→espera regen.
8. [INTEGRADOR] Beat 5 como sistema: objetos, atributos, relaciones, reglas y resultado + dónde vive en código. → Diseño→implementación.
9. Parlett: fines y medios de nuestra primera batalla. → Fin: sobrevivir/entrar; medios: clicks + PE + i-frames.
10. Zimmerman/Salen en 1 línea + por qué nuestro diálogo SÍ es juego (decisión con resultado: frozen, flags, batalla).
