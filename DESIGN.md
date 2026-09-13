# Diseño del Juego — Decisiones

## Género Visual: Medieval Futurism

**Definición:**
> "Futuros tecnológicos, frecuentemente en otros planetas, pero con fuertes resonancias de sistemas feudales medievales como cuerpos gobernantes."

**Referentes:**
- Dune (Frank Herbert, 1965)
- Phantasy Star (SEGA, 1987)
- Warhammer 40K
- Star Wars (estética de mundos como Tatooine)

**Por qué funciona para nuestro juego:**
- Permite mezclar tecnología y pseudo-medievalismo
- Justifica la existencia de "psicotrópicos" como fuente de poder/magia
- Crea una atmósfera única y reconocible
- Es visualmente interesante y permite variedad de zonas

---

## Premisa

Una persona en una fiesta se "pasa de viaje" con psicotrópicos y entra en coma. Todo el juego es su alucinación: un mundo pseudo-medieval creado por su mente. Cuando termina el juego, despierta en un hospital.

---

## Narrativa

### Historia base
- Una persona en una fiesta consume psicotrópicos y entra en coma
- Su mente crea un mundo pseudo-medieval (Medieval Futurism)
- El mundo tiene un gobierno mundial controlado por un antagonista
- Los rebeldes se oponen al gobierno
- El jugador debe detener el segundo reinicio

### Conflicto principal
- Entender qué pasó en el primer reinicio
- Encontrar cómo detener el segundo
- Resolver antes de que sea demasiado tarde

### Estructura de 4 actos
1. **Descubrimiento** - Llegada, tutorial, aprender reglas
2. **Exploración** - Zona de Hielo, laboratorio, Criokinesis
3. **Revelación** - Zona Volcánica, entender la amenaza
4. **Confrontación** - Desierto, derrotar al antagonista

---

## Psicotrópicos

### Concepto
- Psicotrópicos reales (MDMA, LSD, Psilocybe, Peyote)
- Presentaciones modificadas
- Receptores humanos modificados con IA
- Dan superpoderes en el mundo del viaje

### Por zona

| Zona | Psicotrópico | Consumo | Poder | Tipo |
|------|--------------|---------|-------|------|
| Normal | Psilocybe | Oral (hongos) | Conexión con naturaleza | Temporal |
| Hielo | MDMA | Poción/bebida | Criokinesis | Permanente |
| Volcánica | LSD | Parche equipable | Alteración visual | Equipable |
| Desierto | Peyote | Masticar cactus | Visión clara | Permanente |

### Sistema de consumo
- **Consumibles:** Temporales (pociones, hongos)
- **Equipables:** Activos al equipar (parches)
- **Reliquias:** Permanentes (peyote)

---

## Estructura del Mundo

### Continente seudo-África

```
                    [ZONA DE HIELO]
                         |
                         |
    [ZONA NORMAL]-------[CENTRO]-------[ZONA VOLCÁNICA]
       (Bosques)                         |
         |                               |
    [CIUDAD CENTRAL]              [DESIERTO]
    (Megalopolis)                 (Jefe Final)
```

### Zonas

| # | Zona | Tipo | Nivel | Boss |
|---|------|------|-------|------|
| 1 | **Normal** | Bosques, megalopolis | 1-5 | [Por definir] |
| 2 | **Hielo** | Criogenia, gravedad | 5-10 | El Conservador |
| 3 | **Volcánica** | Calor extremo | 10-15 | [Por definir] |
| 4 | **Desierto** | Árido, final | 15-20 | Jefe Final |

### Conexiones

| Desde | Hacia | Requisito |
|-------|-------|-----------|
| Normal | Hielo | Tutorial + Psilocybe |
| Hielo | Volcánica | Criokinesis |
| Volcánica | Desierto | Poder de la zona |
| Cualquier zona | Normal | Retorno a megalopolis |

---

## Encuentros Aleatorios

### Sistema actual: Contador de pasos
- Cada vez que el jugador se mueve, se incrementa un contador
- Cuando el contador supera un umbral → encuentro random
- El umbral se ajusta por zona

### Implementación futura: Barra estilo Earthbound
- Barra visible que se llena
- El jugador VE cuándo viene el próximo combate
- Agrega tensión visual y decisión estratégica

### Frecuencia por zona

| Zona | Frecuencia | Razón |
|------|------------|-------|
| Normal | Baja (cada ~40 pasos) | Zona segura |
| Hielo | Media (cada ~30 pasos) | Gravedad dificulta |
| Volcánica | Alta (cada ~20 pasos) | Zona peligrosa |
| Desierto | Muy alta (cada ~15 pasos) | Zona final |

---

## Combate

### Mecánicas
- **Tiempo real** (WASD + mouse)
- **Click izquierdo:** Ataque melee
- **Click derecho:** Ataque rango / poder
- **Shift:** Esquivar / dash
- **Tecla E:** Interactuar
- **I:** Inventario

### Progresión
- El jugador sube de nivel al derrotar enemigos
- Los psicotrópicos dan poderes permanentes
- El training mejora stats
- Cada zona tiene un boss que da un poder

---

## Referentes visuales

| Tipo | Ejemplos | Elementos a tomar |
|------|----------|-------------------|
| Juegos | Phantasy Star, Diablo, Hyper Light Drifter | Mezcla tech/medieval, paleta oscura |
| Películas | Dune (2021), Altered States | Arquitectura masiva, efectos psicodélicos |
| Arte | HR Giger, Moebius | Biomecánico, paisajes alienígenas |

---

## Tilemap

### Decisión: Sistema manual (sin herramientas externas)

**Por qué:**
- Entendemos cómo funciona por dentro
- Sin dependencias externas
- Compatible con nuestro tileset Pipoya 32x32
- Control total sobre el comportamiento
- Ideal para aprender fundamentos

**Arquitectura:**
- `src/tileset.py` — Carga spritesheet, corta tiles individuales
- `src/tilemap.py` — Guarda mapa como lista de listas, renderiza
- `src/camera.py` — Sigue al jugador, maneja scrolling

**Tileset:** PIPOYA FREE RPG World Tileset 32x32
- Mismo autor que los sprites de personajes
- Tiles: pasto, camino, bosque, desierto, agua, montaña
- Licencia: Uso comercial/personal

**Alternativas documentadas:**
- Tiled Map Editor + pytmx (para mapas grandes)
- tilemap-editor PyPI (editor en Pygame)

**Ver:** `docs/tilemap-system.md` para detalles completos

---

## Documentación adicional

Ver carpeta `docs/` para detalles completos:
- `docs/narrativa.md` - Historia, gobierno mundial, rebeldes, lore completo
- `docs/mundo.md` - Geografía pseudo-África, 4 zonas, enemigos
- `docs/estetica.md` - Paleta de colores, UI/UX, efectos visuales, sprites
- `docs/poderes.md` - Sistema de psicotrópicos, mecánicas de consumo, training
- `docs/zona-hielo.md` - Detalle completo de la zona de hielo
- `docs/tutorial.md` - Estructura del tutorial en Zona Normal
- `docs/tilemap-system.md` - Sistema de tilemap: Tileset, Tilemap, Camera, colisiones
- `docs/combate-tiempo-real.md` - Plan para convertir combate por turnos a tiempo real
