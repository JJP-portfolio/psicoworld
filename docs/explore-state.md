# `explore_state.py` explicado (para trabajar la cinemática)

Archivo: `src/states/explore_state.py` (~154 líneas). Es la escena "caminar por el mapa".

## Ciclo de vida

1. `game.py` crea UNA vez `ExploreState(self)` y lo registra como `"explore"`.
2. Cada `change("explore")` llama a `enter()`. Como el objeto ya existe, la guarda
   `if hasattr(self, 'player'): return` evita reconstruir (así se conserva la posición al volver de batalla).
3. Por frame: `handle_events` → `update(dt)` → `render(screen)`.

## Qué hace cada parte

- **`enter()`**: crea jugador (Entity + Position + Sprite + Stats según `game.player_class`),
  tileset, y llama a `load_map("data/maps/overworld_normal.json")`. Solo corre completo la 1ª vez.
- **`load_map(path)`**: recarga tilemap + colisiones + reposiciona al jugador en `spawn_player`
  + reconstruye `self.portals` (objetos capa `Portal`) + cámara nueva + `ignore_portals = True`.
  Es lo que permite viajar entre mapas sin recrear al jugador (los Stats se conservan).
- **`update(dt)`** en orden: (1) mueve jugador (`movement_system`, ejes separados con slide);
  (2) contador de pasos → batalla si `ENCOUNTERS_ENABLED`; (3) portales: si el rect 32×32 del
  jugador toca un portal Y `ignore_portals` es False → `load_map(target)` + reposicionar +
  `ignore_portals = True`. Si no toca ninguno → `ignore_portals = False`;
  (4) animación por `sprite.direction` (intención, no posición); (5) cámara follow.
- **`render(screen)`**: fondo negro → tilemap con cámara → jugador con `camera.apply` → texto HP.
- **`handle_events`**: `SPACE` fuerza batalla (útil para testear; los encuentros están off).

## Dónde engancha la cinemática (dueño → diálogo → guardias)

1. **Congelar input:** flag `self.frozen`. En `update`, si `frozen`: no correr `movement_system`
   (pero sí animación/cámara/render). Se prende al empezar la cinemática, se apaga al terminar el diálogo.
2. **NPCs:** lista `self.npcs` SEPARADA de `self.entities` (si van a `entities`,
   `movement_system` los mueve con las teclas del jugador). Renderizarlos en `render` con la cámara.
3. **Dueño se acerca:** target = punto frente a la puerta/spawn. Cada frame mover al dueño hacia
   el target a 120 px/s (reutilizar idea de `_touches_wall` para no atravesar muebles, o camino
   recto si está despejado). Al llegar (dist < 8): `dialogue.start()`.
4. **Diálogo:** caja abajo (UI), `E` avanza (`dialogue.advance()`), al `finished()`: `frozen = False`.
5. **Beat 5:** al cerrar el diálogo del dueño, spawnear `guardia_1/2` en `portal_salida` caminando
   adentro → al acercarse (< 48 px) → `change("battle")` guionado.

## Trampas conocidas de este archivo

- `enter()` no corre 2ª vez: todo estado nuevo de mapa va en `load_map`, no en `enter`.
- `ignore_portals` evita el rebote puerta↔mapa (el spawn de la casa está dentro del rect de salida).
- `movement_system.update(self.entities, ...)` mueve TODO lo de esa lista: nunca meter NPCs ahí.
- La animación usa `direction` (teclas), no posición: empujar una pared muestra walk, quieto muestra idle.
