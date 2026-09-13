# Ejercicios C3 — Entity + Componentes

Archivos: `src/entities/entity.py`, `enemy.py`, `src/components/` (`position.py`, `stats.py`, `health.py`, `hitbox.py`, `hurtbox.py`, `sprite.py`).

1. (Fácil) Creá una entidad "antorcha" con `Position` + `Sprite` de color y dibujala.
2. (Fácil) Agregá y quitá `Stats` a una entidad en runtime. Verificá con `has_component` antes y después.
3. (Fácil) Componente nuevo `Contador(numero)` con método `sumar(dt)`. Probalo 5 segundos.
4. [INTEGRADOR] Poción: entidad con `Position` + `Sprite` que al tocarla (distancia < 32) cura con `Stats.heal()` y desaparece. Integrás entidad + sistema + stats.
5. (Medio) Enemigo con `damage` según la clase elegida (`game.player_class`).
6. (Medio) Componente `Inventario` (lista) con `agregar(item)` y `usar(item)`.
7. (Medio) Sistema `render_system`: dibuja todas las entidades que tengan `Position` + `Sprite`.
8. [INTEGRADOR] NPC quieto: `Position` + `Sprite` + `Dialogo(texto)`; con `E` cerca muestra el texto 3 s. Integrás entidad + input + UI.
9. (Difícil) `get_component` de algo inexistente devuelve `None`: blindá todos los accesos con el patrón `if x:`.
10. (Difícil) Serializá una entidad a dict (`{tipo: {attrs}}`) y reconstruila desde el dict (base del guardado).
