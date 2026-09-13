# Combate en Tiempo Real — Investigación y Diseño (Swarm + ATB + Minijuego)

> Fecha: 2026-09-13. Reemplaza en alcance a `combate-tiempo-real.md` para el diseño; ese archivo queda como plan viejo de referencia.

## 1. Referencias investigadas

### Swarm (Riot, evento temporal LoL 2024)
- PvE cooperativo estilo **bullet-heaven** (Vampire Survivors): oleadas + jefes + mejoras.
- **WASD para moverse**, ataques básicos **automáticos**, habilidades potentes con **cooldown en botones**.
- Partidas cortas (~15 min), 4 mapas, dificultades desbloqueables, upgrades permanentes entre runs.
- Lección para nosotros: mover con WASD + poco botones + oleadas con timer + upgrades = loop adictivo y barato de implementar.

### Minijuegos de cola (Dota 2)
- Valve ofrece **minijuegos jugables mientras esperás partida** (ej. *Nest of Thrones*): arenas compactas, reglas mínimas, sesión corta, win/lose claro.
- Lección: nuestro combate = **arena autocontenida** (una casa o claro), entra-salí rápido, sin pantallas de setup.

### ATB / Parasite Eve (Square, 1998)
- Tiempo real **pausable**, en el **mismo mapa** (sin pantalla de batalla separada).
- Cada actor tiene **barra ATB** que carga según **speed**; llena → puede actuar.
- Acciones fuertes = más "penalty" (tardan más en recargar). Haste/Slow modifican la carga.
- **PE (energía)**: se regenera con el tiempo, se gasta en poderes.
- Modos Active (el tiempo no para ni en menús) vs Wait (pausa al elegir).
- Lección: nuestro `Stats.speed` ya existe → cada enemigo/jugador carga su barra a distinto ritmo. Los psicotrópicos ("tratamiento") calzan perfecto como PE.

## 2. Diseño propuesto: "Arena ATB en el mapa"

Sin pantalla separada (como PE): al pisar zona de combate (o al tocar enemigo), aparecen enemigos en la misma arena.

- **Movimiento:** WASD + normalización (ya existe).
- **Melee:** click izq, arco frontal, startup→active→recovery (frame data ya documentada en skill).
- **Rango/poder:** click der, gasta PE, PE regenera con el tiempo.
- **ATB por actor:** `atb += speed * dt`; al llegar a 100 el enemigo "puede" atacar (con telegraph previo). El jugador ataca libre (sus clicks son la acción), pero sus poderes usan cooldown + PE.
- **Invocaciones (3 monstruos):** aliados con la `ai_system` actual (chase al enemigo más cercano + attack). Cuestan PE invocarlos, duran X s o hasta morir.
- **Timer de encuentro:** oleadas con cuenta atrás estilo Swarm (ej. sobrevive 60 s → jefe). Entre oleadas: upgrade a elegir (daño/velocidad/PE máx).
- **Sin plataforma:** todo top-down 2D, hitbox vs hurtbox (ya existe), knockback + i-frames (ya existen).

## 3. UI/UX del combate (para aplicar conceptos de la uni)

| Elemento | Tipo UI | Implementación |
|---|---|---|
| Barra HP jugador | No-diegética | HUD arriba-izq (ej. C8-2) |
| Barra ATB enemiga | Espacial | Sobre cada enemigo, carga con speed |
| Barra PE + cooldowns | No-diegética | HUD abajo, radial o barras (ej. C8-5) |
| Damage numbers | Espacial/meta | Flotan y se borran (ej. C8-4) |
| Telegraph rojo | Espacial | Área de ataque 0.5 s antes (ej. C8-7) |
| Hit-stop + shake | Meta | 60 ms congelado + shake (ej. C8-10) |
| Mensaje de oleada | No-diegética | "¡Oleada 3!" centro pantalla |

## 4. Curva de dificultad

- Rampa por oleada: `n_enemigos`, `hp`, `daño` crecen suave (tabla, ej. C8-9). Sin saltos: flow channel.
- Dificultad justa: todo daño enemigo tiene telegraph; i-frames tras golpe.
- Por zona: reutilizar `ENCOUNTER_STEPS` como agresividad (desierto > volcánica > hielo > normal).
- Onboarding: primera arena (casa del dueño) con 1 enemigo lento + tutorial de clicks.

## 5. Roadmap de implementación (el estudiante escribe el código)

1. **Fase A — base:** enemigos spawnean en el mapa (sin pantalla separada), melee con click izq usando `Hitbox.active` + `combat_system.check_collisions`.
2. **Fase B — ATB:** componente `ATB(progreso, umbral)`; enemigos atacan solo con ATB llena + telegraph.
3. **Fase C — PE y poderes:** componente `PE(actual, max, regen)`; click der gasta PE.
4. **Fase D — invocaciones:** 3 aliados con IA chase/attack, costo PE, duración.
5. **Fase E — oleadas + timer:** spawner por tiempo, upgrades entre oleadas, jefe final.
6. **Fase F — game feel:** hit-stop, shake, damage numbers, sonidos.

## 6. Archivos a crear/modificar

- Nuevo `src/components/atb.py`, `src/components/pe.py`, `src/components/summon.py`
- Nuevo `src/systems/wave_system.py` (spawner + timer), `src/systems/ability_system.py`
- Modificar `battle_state.py` (o eliminarlo: el combate pasa a `explore_state.py`) — decisión pendiente
- Modificar `enemy.py` (ATB + telegraph), `ai_system.py` (modo summon)
- UI en `explore_state.render` (barras ATB/PE, oleada)
