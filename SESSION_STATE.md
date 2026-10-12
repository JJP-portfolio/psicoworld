# Estado de Sesión — Mi JRPG

> **Última actualización:** 2026-09-13
> **Paso actual:** Mapa 60×40 con tileset único, colisiones con polígonos funcionando, encuentros desactivados, pendiente test visual + casa + transiciones

## CHECKPOINT 2026-09-13 — Nuevo punto de partida

Verificado headless: portales ida/vuelta sin rebotes, cinemática dueño (proximidad→diálogo×3→libera),
NPCs con sprites, tembleque, spawn casa 4/4, casa 341 tiles colisión (regla: sin arte = pared),
overworld intacto. Flujo jugable: spawn → puerta → casa → dueño → puerta.
Docs: c1-c8 ejercicios, combate-swarm-atb, troubleshooting, paredes, filtros, explore-state,
animacion-patterns, animacion-arquitectura. Track nuevo: `docs/diseno/` (D1-D8).
Pendiente: Beat 5 (guardias entran → primera batalla), combate tiempo real por fases.

---

## Checklist de implementación

### Fase 1: Entorno y estructura ✅
| Paso | Archivo | Estado |
|------|---------|--------|
| 1 | Entorno (venv + pygame-ce) | ✅ |
| 2 | Estructura de carpetas | ✅ |
| 3 | `src/settings.py` | ✅ |
| 4 | `src/game.py` | ✅ |
| 5 | `main.py` | ✅ |

### Fase 2: State Machine y Menú ✅
| Paso | Archivo | Estado |
|------|---------|--------|
| 6 | `src/states/state_machine.py` | ✅ |
| 7 | `src/states/menu_state.py` | ✅ |
| 8 | `assets/fonts/diablo.ttf` | ✅ |
| 9 | Conectar menú con game.py | ✅ |

### Fase 3: Exploración ✅
| Paso | Archivo | Estado |
|------|---------|--------|
| 10 | `src/states/explore_state.py` | ✅ |
| 11 | Registrar explore_state en game.py | ✅ |
| 12 | Probar menú → exploración | ✅ |

### Fase 4: Entity + Components ✅
| Paso | Archivo | Estado |
|------|---------|--------|
| 13 | `src/entities/entity.py` | ✅ |
| 14 | `src/components/position.py` | ✅ |
| 15 | `src/components/sprite.py` | ✅ (spritesheet + animaciones + flip) |
| 16 | `src/components/stats.py` | ✅ (HP, Attack, Magic, Speed, level up) |
| 17 | `src/systems/movement_system.py` | ✅ (WASD + normalización diagonal + colisiones tilemap) |

### Fase 5: Creación de Personaje ✅
| Paso | Archivo | Estado |
|------|---------|--------|
| 18 | `src/states/character_creation_state.py` | ✅ (selección de clase con stats) |
| 19 | Modificar menu_state.py (ir a creación) | ✅ |
| 20 | Modificar explore_state.py (agregar jugador) | ✅ |
| 21 | Modificar game.py (registrar character_creation) | ✅ |

### Fase 6: Combate ✅
| Paso | Archivo | Estado |
|------|---------|--------|
| 22 | `src/states/battle_state.py` | ✅ (combate por turnos, victoria vuelve a explore) |
| 23 | `src/components/health.py` | ✅ (HP + invencibilidad) |
| 24 | `src/components/hitbox.py` | ✅ (caja de ataque) |
| 25 | `src/components/hurtbox.py` | ✅ (caja de daño) |
| 26 | `src/systems/combat_system.py` | ✅ (detección de colisiones) |
| 27 | `src/entities/enemy.py` | ✅ (enemigo base) |
| 28 | `src/systems/ai_system.py` | ✅ (persigue al jugador) |

### Fase 7: Tilemap System ✅
| Paso | Archivo | Estado |
|------|---------|--------|
| 29 | `src/tileset.py` | ✅ (carga spritesheet, corta tiles) |
| 30 | `src/tilemap.py` | ✅ (matriz 2D, colisiones, render con cámara) |
| 31 | `src/camera.py` | ✅ (smooth follow + clamping) |
| 32 | Modificar `explore_state.py` (usar tilemap) | ✅ |

### Fase 8: Tiled Map Editor Integration ✅ (parcial)
| Paso | Archivo | Estado |
|------|---------|--------|
| 33 | `src/map_loader.py` | ✅ (load_tiled_map, get_objects_from_map, load_collisions + `point_in_polygon` para polígonos) |
| 34 | Cargar mapa desde Tiled JSON | ✅ (overworld_normal.json, 60×40, tileset único Pipoyafull firstgid=1) |
| 35 | Spawn point desde Object Layer | ✅ (objeto "spawn_player" en capa "Spawn") |
| 36 | Colisiones desde Object Layer | ✅ (rectángulos + polígonos con test punto-en-polígono exacto) |
| 37 | Expandir mapa en Tiled (60×40 tiles) | ✅ (1920×1280 px, cámara scrollea) |
| 38 | Pintar tiles reales en Tiled | ✅ (suelo, decoración, plantas, casa, árboles) |
| 39 | Definir rectángulos de colisión en Tiled | ✅ (50 rects + 7 polígonos; 7 rects de área cero por revisar) |
| 40 | NPCs en Tiled (capa NPC) | ⏳ Parcial — `guardia_1`, `guardia_2` nombrados y alcanzables; falta `duenio_casa` (va en casa_duenio.json) |
| 41 | Estirar `portal_casa` hacia el camino | ✅ (era punto, convertido a rect 32×64 sobre puerta + camino; overlap verificado) |

### Pendiente: Sistema de encuentros aleatorios
- Contador de pasos en `explore_state.py` ✅ (ya funciona)
- Diferente frecuencia por zona (Normal: 40, Hielo: 30, Volcánica: 20, Desierto: 15) ✅ (ENCOUNTER_STEPS en settings.py)
- Transición a `battle_state.py` al superar umbral ✅
- Guardar stats del jugador entre batallas — pendiente

### Pendiente: Conversión a tiempo real
Ver `docs/combate-tiempo-real.md` para plan de implementación.

### Pendiente: Fondos de combate por zona
Ver `docs/battle-backgrounds.md` para plan de implementación.

## Errores corregidos en sesiones anteriores

| Archivo | Error | Corrección |
|---------|-------|------------|
| `menu_state.py:2` | Import incorrecto de State | Corregido a `from src.states.state_machine import State` |
| `state_machine.py` | Faltaba método `render` | Agregado |
| `explore_state.py:9` | Doble asignación de `pygame.font` | Corregido |
| `battle_state.py` | Múltiples bugs (muerte, HP, orden) | Reestructurado completo |
| `battle_state.py:37` | Victoria volvía a "menu" | Corregido a "explore" |
| `sprite.py` | Animación no reseteaba frames al cambiar | Agregado `_prev_animation` tracking |
| `map_loader.py:43` | Syntax error: `]` extra en línea h = int(...) | ✅ Corregido sesión 2026-09-13 |
| `map_loader.py:44-47` | Variables `end_ty` y `tx` no definidas | ✅ Corregido — loop anidado + fórmula `(x+w-1)//tile` |
| `map_loader.py` (polígonos) | Objetos polígono ignorados (w=0/h=0 → rango vacío) | ✅ Corregido — `point_in_polygon` (ray casting) + marcado exacto por centro de tile |
| `camera.py` clamping | `max(0, min(x, map_w - screen_w))` daba 0 con mapa chico | ✅ Corregido — scrolleo con clamping si mapa > pantalla, centrado si no |
| `explore_state.py` enter() | Al volver de batalla se reconstruía todo → spawn | ✅ Corregido — guarda `if hasattr(self, 'player'): return` |
| `explore_state.py` animación | Al chocar mostraba idle (=mirar abajo) | ✅ Corregido — animación por teclas (`trying_to_move`), pasos por posición real |
| Encuentros aleatorios | Interrumpían test de exploración sin sprites de combate | ✅ Desactivados — flag `ENCOUNTERS_ENABLED = False` en settings.py (SPACE manual sigue) |

---

## Bugs conocidos (pendientes de sesión nueva)

| Archivo | Bug | Descripción |
|---------|-----|-------------|
| `map_loader.py:43` | Syntax error | `h = int(obj.get('height', 32))]` — corchete extra |
| `map_loader.py:46-47` | Variables indefinidas | `end_ty` y `tx` no existen, debería calcularse el rango de tiles |
| `camera.py:25-26` | Clamping bloquea cámara | ✅ Resuelto — ver tabla de arriba |
| `explore_state.py:27-31` | Animación idle = walk_down | ✅ Parcial — idle sigue en fila 0; al chocar ahora mantiene dirección por `trying_to_move` |
| Mapa 40×23 | Demasiado chico | ✅ Resuelto — ahora 60×40, un solo tileset (Pipoyafull) |
| Tiled: 2 tilesets mezclados | GIDs de Pipoyafull fuera de rango del otro tileset | ✅ Resuelto — eliminado `pipoya-32x32`, re-pintado con Pipoyafull |
| `portal_casa` | Era punto (sin área, imposible de detectar/estirar) | ✅ Resuelto — rect 32×64; jugador lo solapa 16px al acercarse por (54,6) |
| `get_objects_from_map` | No lee custom properties (target_map/target_x/...) | ⏳ Extender cuando se programe el sistema de portales |

---

## Decisiones de diseño

| Decisión | Elección | Razón |
|----------|----------|-------|
| Perspectiva | Top-down | Más simple, ideal para aprender |
| Combate | Tiempo real (WASD + mouse) | Más intenso |
| Ataques | Click izq (melee) + Click der (rango) | Escalable |
| Encuentros | Contador de pasos por zona | Simple, escalable a Earthbound |
| Arquitectura | Entity + Components (composición) | Flexible, escalable |
| Editor de código | Emacs | Preferencia del estudiante |
| Editor de mapas | Tiled Map Editor | Estándar de la industria, exporta JSON |
| Tileset | Pipoya RPG 32x32 ([Base]BaseChip_pipo.png) | Libre,organizado en `assets/tilesets/pipoya-rpg-tileset/` |
| Fuente | diablo.ttf | Estilo gótico/medieval, soporta español |
| **Género visual** | **Medieval Futurism** | **Dune, Phantasy Star, mezcla tech/medieval** |
| **Tono** | **Hilarante y divertido** | **Humor absurdo/psicodélico** |
| **Narrativa** | **Viaje psicotrópico** | **Mundo pseudo-medieval alterado por drogas** |
| **Conflicto** | **Detener segundo reinicio** | **Alguien repite el experimento que reinició el planeta** |
| **Estructura** | **4 zonas (continente)** | **2 bloqueadas por puzzles, progresión lineal** |
| **Cámara** | **Zelda ALTTP/Pokémon** | **Smooth follow + transiciones entre mapas** |

---

## Conceptos aprendidos

### Entity-Component (composición)
```
Entity = caja vacía que guarda piezas
Position = pieza que dice dónde está
Sprite = pieza que dice cómo se ve
Stats = pieza que dice qué tan fuerte es
```

### Components vs Systems
```
Component = guarda datos    (Position, Sprite, Stats)
System = ejecuta lógica     (movement_system, combat_system)
```

### Delta Time (dt)
```python
position.x += dx * speed * dt  # Siempre igual, sin importar los FPS
```

### Normalización diagonal
```python
dx=1, dy=1 → dx/=√2, dy/=√2 → velocidad = 1 (misma que cardinal)
```

### Tiled → Pygame (carga de mapas)
```python
# Tiled exporta JSON con:
# - tilelayers: array de GIDs por celda
# - objectgroups: objetos libres (spawns, portales, colisiones)
# map_loader.py convierte GIDs a índices de tileset y rectángulos a grid de colisiones
```

---

## Documentación del proyecto

| Archivo | Contenido | Estado |
|---------|-----------|--------|
| `SESSION_STATE.md` | Estado del proyecto (este archivo) | ✅ Actualizado |
| `DESIGN.md` | Género visual, narrativa, estructura del mundo | ✅ |
| `docs/narrativa.md` | Premisa, gobierno mundial, rebeldes, lore | ✅ |
| `docs/mundo.md` | Mapa pseudo-África, 4 zonas, conexiones | ✅ |
| `docs/poderes.md` | Sistema de psicotrópicos, mecánicas | ✅ |
| `docs/zona-hielo.md` | Detalle zona de hielo (3 capas, boss) | ✅ |
| `docs/tutorial.md` | Estructura del tutorial en Zona Normal | ✅ |
| `docs/tilemap-system.md` | Sistema de tilemap (tiles, cámara, colisiones) | ⚠️ Desactualizado — ver abajo |
| `docs/tiled-guide.md` | Guía de uso de Tiled Map Editor | ✅ |
| `docs/tutorial-map-design.md` | Diseño del mapa tutorial | ✅ |
| `docs/map-structure.md` | Estructura de carpetas de mapas por zona | ✅ |
| `docs/map-transitions.md` | Sistema de transiciones entre mapas | ✅ |
| `docs/krita-tileset-workflow.md` | Workflow de sprites con Krita | ✅ |
| `docs/combate-tiempo-real.md` | Plan de conversión a tiempo real | ✅ |
| `docs/battle-backgrounds.md` | Fondos de combate por zona | ✅ |
| `docs/krita-workflow.md` | Workflow de sprites con Krita + tablet | ✅ |
| `docs/list-comprehensions.md` | Guía de list comprehensions Python | ✅ |
| `docs/troubleshooting.md` | Incidentes + FAQs de Tiled (save vs export, JSON externo, objetos, tiles negros, firstgid) | ✅ |
| `docs/paredes-pipoya.md` | Anatomía de muros (GIDs por rol), receta casa, Terrain/Automapping | ✅ |
| `docs/graficos-filtros.md` | Filtros SNES (scanlines, smoothscale, scale2x, xBRZ) + snippet | ✅ |
| `docs/explore-state.md` | Explicación de explore_state + hooks de cinemática + trampas | ✅ |
| `docs/animacion-patterns.md` | 3 relojes, 4 casos GitHub/SO revisados, checklist buenas prácticas | ✅ |
| `docs/animacion-arquitectura.md` | 3 capas (Sprite/cinemática-comandos/eventos), sin dependencias | ✅ |
| `docs/diseno/d1-pilares.md` … `d8-playtesting.md` | Track Diseño Conceptual: 10 ej/módulo, 4º y 8º integradores | ✅ |

---

## Sprites descargados

**PIPOYA FREE RPG Character Sprites 32x32** (64 personajes)
- `assets/sprites/player/` — Male (18), Female (25), Soldier (7)
- `assets/sprites/enemies/` — Enemy (22), Boss (1)
- `assets/sprites/npcs/` — Animal, Other
- Licencia: Uso comercial/personal, modificar libremente

**Tileset:**
- `assets/tilesets/pipoya-rpg-tileset/[Base]BaseChip_pipo.png` — Tileset principal
- `assets/tsx/pipoya-32x32.tsx` — Archivo TSX original (no se usa, cargamos PNG directo)

---

## Próximos pasos (orden sugerido)

1. **Test visual** — movimiento libre, árboles frenan, sprite mira arriba al chocar, cámara scrollea
3. **Crear `casa_duenio.json`** — 30×20, dos pisos + escalera, NPCs `duenio_casa` y `hija`, símbolo en el piso
4. **Extender `get_objects_from_map`** — leer custom properties (target_map/target_x/target_y)
5. **Sistema de transiciones entre mapas** — portales en Tiled → cambio de escena (ver `docs/map-transitions.md`); escalera = portal al mismo mapa
6. **Fix animación idle** — separar de walk_down cuando haya sprites (distinta fila o behavior)
7. **Actualizar `docs/tilemap-system.md`** — reflejar integración con Tiled
8. **Reactivar encuentros** — `ENCOUNTERS_ENABLED = True` cuando el combate tenga sprites
9. **Fondos de combate por zona** — ver `docs/battle-backgrounds.md`
10. **Conversión de combate a tiempo real** — ver `docs/combate-tiempo-real.md`

---

## Cómo continuar

```bash
cd ~/Documentos/Proyectos/mi_jrpg
source venv/bin/activate
python main.py
```

## Convención de guía (pedido del estudiante 2026-09-13)

Toda indicación de código debe traer: **archivo + línea + código anterior a reemplazar**. Sin eso, no se escribe nada.

# Archivos clave:
# SESSION_STATE.md — Estado actual (este archivo)
# src/map_loader.py — Carga de mapas desde Tiled (tiene bugs)
# src/camera.py — Cámara con smooth follow
# src/states/explore_state.py — Escena principal de exploración
# data/maps/overworld_normal.json — Mapa actual (exportado desde Tiled)
# docs/ — Toda la documentación

# Bug conocido: map_loader.py línea 43 tiene syntax error (]) 
# Bug conocido: camera.py clamping no funciona para mapas > pantalla
```
