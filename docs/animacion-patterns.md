# Patrones de animación en pygame (investigado 2026-09-13)

Fuentes: doc oficial pygame-ce (`transform`, `examples`, `aliens.py`), Real Python Primer,
Stack Overflow (alien warp), GitHub `01one/pygameExamples` y `kadraman/pygame-delta-time`.

## 1. Los 3 relojes posibles (elegir uno por animación)

| Patrón | Cómo avanza | Ejemplo | Pro / contra |
|---|---|---|---|
| Por frame | `frame += 1` por update | `01one` ej. 49 | Simple. MAL si el FPS varía (a 30 FPS todo va a mitad de velocidad) |
| Por contador fijo | `frame += 1` cada N ticks + `clock.tick(60)` | `aliens.py` (`animcycle`, `life`) | Determinista. Bien si el juego corre a FPS fijo |
| Por tiempo (dt o ms) | acumulador `+= dt`, cambia al superar umbral | SO alien warp (timestamps ms), **nuestro `Sprite`** (`frame_timer += frame_speed*dt*60`) | Independiente del FPS. El correcto para nosotros |

## 2. Casos revisados (qué copiar, qué no)

- **`01one` ej. 49**: BIEN `pygame.sprite.Group` + `draw`. MAL: sin `dt`, sin `.convert()`,
  frames numerados `1.png..10.png` (frágil), sin estados (una sola animación).
- **`aliens.py` (oficial)**: BIEN imágenes como atributos de CLASE (se cargan una vez, no por
  instancia), `clock.tick` fijo, `Explosion` con `life` (animación con fin → patrón para ataques).
  MAL para nosotros: lógica atada a FPS fijo.
- **SO alien warp**: BIEN estado dentro de `update()` (`warp_at_time`), selección de frame por
  tiempo (`ms // 200`), retorno a imagen base al terminar. Es el patrón a imitar para
  startup → active → recovery.
- **Real Python Primer**: referencia de estructura (loop, `Group`, `USEREVENT` para spawns por timer —
  útil para nuestro `wave_system` futuro).

## 3. Nuestro `Sprite` vs lo investigado

BIEN: acumulador dt, reset al cambiar de animación (`_prev_animation`), corte con chequeo de
bordes (filas incompletas no rompen), fallback a rectángulo de color sin imagen.
A MEJORAR (para el combate):
1. `frame_speed = 0.15` mágico → constante nombrada por animación (`fps: 6` en el config).
2. Sin evento de fin: los ataques necesitan "avisar cuando terminan" (como `Explosion.life`).
   Agregar `finished` o callback `on_end`.
3. Sin ping-pong ni frame de hold (útil para idle: 2 frames ida y vuelta).
4. `flip_x` eliminado correctamente: el arte ya trae ambas direcciones (ver C7).

## 4. Buenas prácticas aplicadas (checklist)

- Cargar imágenes UNA vez al inicio, nunca en el loop. ✅ (tileset/spritesheet en `enter`)
- `.convert()` / `.convert_alpha()` siempre. ✅
- Lógica con `dt`, render separado de update. ✅
- `get_rect`/`colliderect` para choques, no matemática a mano. ✅ (portales, combate)
- Grupos para dibujar colecciones (`Group.draw`). ⏳ pendiente (dibujamos a mano en `render`)
- Timestamps/duración en segundos, no en frames. ✅ (`Health`, `message_timer`)
