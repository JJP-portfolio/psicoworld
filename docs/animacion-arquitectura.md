# Arquitectura de animación (decisión 2026-09-13)

Investigado: `pytweening` (PyPI, Al Sweigart), cutscenes como clases (`scartwright91/pygame-tutorials`),
Animator desacoplado (respuesta DMGregory, gamedev.SE), animación data-driven (XML por entidad),
eventos por frame / frame data (startup→active→recovery), `SpriteSheetAnim` (loop vs one-shot).

## Decisión: 3 capas, sin dependencias nuevas

1. **Sprite (datos + reloj):** YA EXISTE. Frames + acumulador dt + reset + bounds-check.
   Mejoras pendientes (ver `animacion-patterns.md`): fps por animación, modo loop/once, flag `finished`.
2. **Cinemáticas (lista de comandos):** en vez de clases de cutscene o `pytweening`,
   la cinemática es DATOS: `[('move', npc, x, y, speed), ('dialogue', dlg), ('battle',)]`
   + un mini-intérprete en `update` que ejecuta un comando por vez. Misma idea que los
   command-lists de motores ECS, a nuestra escala. `pytweening` no se instala todavía:
   el easing que necesitamos (`ease_out_quad`) son 3 líneas; dependencia cuando haya 3+ usos.
3. **Eventos por frame (combate):** el `Hitbox.active` actual evoluciona a rangos
   `[startup, startup+active]` + `finished` para recovery→idle (patrón `aliens.Explosion.life`).

## Reglas de la casa

- Gameplay manda DATOS al visual, nunca al revés (patrón Animator: `SetBool`-style).
- Todo tiempo en segundos con `dt`; nada por frames contados (ver `animacion-patterns.md`).
- Un `frozen` global congela input en cinemáticas/diálogo; animación y cámara siguen.
- NPCs SIEMPRE en `self.npcs`, jamás en `self.entities` (el input es global por lista).
