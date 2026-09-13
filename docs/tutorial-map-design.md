# Guía de Diseño del Mapa Tutorial — Porro Adventures

## Contexto narrativo

El jugador aparece en un bosque (confundido). No sabe dónde está. Debe encontrar el camino hacia la ciudad, donde los rebeldes lo encuentran.

---

## Estructura del mapa (Zona Normal - Tutorial)

### Layout recomendado: 40x23 tiles (1280x720 px)

```
FILA 0-2:   BORDE SUPERIOR (bosque denso, intransitable)
FILA 3-5:   ZONA DE APARICIÓN (bosque abierto, camino)
FILA 6-10:  CAMINO PRINCIPAL (path claro hacia la ciudad)
FILA 11-15: ENTRADA A LA CIUDAD (muros, puerta)
FILA 16-20: INTERIOR CIUDAD (edificios, NPCs)
FILA 21-22: BORDE INFERIOR (muro exterior)
```

### Zonas del mapa

| Zona | Tiles | Función | Colisión |
|------|-------|---------|----------|
| **Bosque denso** | Árboles, arbustos | Borde, guía visual | Sí |
| **Camino** | Tierra, piedra | Path principal | No |
| **Hierba alta** | Pasto largo | Encuentros aleatorios | No |
| **Muro exterior** | Piedra | Límite del mapa | Sí |
| **Puerta ciudad** | Arco, entrada | Transición bosque→ciudad | No |
| **Edificios** | Casas, tienda | Interacción, tiendas | Sí |
| **Base rebelde** | Edificio especial | NPCs, misiones | No (interior) |

---

## Diseño paso a paso

### 1. Borde del mapa (tiles 1-2 del tileset)

Crear muro natural de árboles alrededor de todo el mapa:
- Fila 0: árboles densos (no transitable)
- Columna 0: árboles densos
- Columna 39: árboles densos
- Fila 22: árboles densos

**Tile a usar:** Tile 1 (árbol) del tileset Pipoya

### 2. Punto de aparición del jugador

Ubicar al jugador en:
- **x:** 10 (columna 10)
- **y:** 4 (fila 4)
- **Dirección inicial:** abajo (mirando hacia el camino)

Esto deja al jugador en una zona abierta del bosque, visible pero no en el centro.

### 3. Camino principal (path guidance)

Crear un camino claro de tierra que lleve desde la aparición hasta la ciudad:

```
Aparición (10,4)
    ↓
Camino hacia abajo (10,5) → (10,6) → (10,7)
    ↓
Camino hacia la derecha (11,7) → (12,7) → ... → (20,7)
    ↓
Camino hacia abajo (20,8) → (20,9) → (20,10)
    ↓
Entrada a la ciudad (20,11)
```

**Tiles a usar:**
- Camino de tierra: tile 3 (camino)
- Borde del camino: tile 0 (hierba)

### 4. Hierba alta (encuentros aleatorios)

Zonas de hierba alta alrededor del camino:
- Izquierda del camino: columnas 5-9, filas 5-10
- Derecha del camino: columnas 25-30, filas 5-10

**Tile a usar:** tile 2 (hierba alta)

### 5. Entrada a la ciudad

Crear una abertura en el muro sur del bosque:
- Muro de piedra en fila 11
- Puerta abierta en columna 20 (3 tiles de ancho)
- Tiles de puerta: tile 4 (arco/puerta)

### 6. Interior de la ciudad

Después de la puerta (fila 12 en adelante):
- Calles de piedra
- Edificios a los lados
- Base rebelde al fondo

**Tiles a usar:**
- Calle: tile 3 (camino de piedra)
- Edificios: tile 1 (pared)
- Puertas de edificios: tile 4

---

## Flujo del jugador (UX)

```
1. Jugador aparece en (10,4) mirando abajo
2. Ve el camino de tierra debajo
3. Camina hacia abajo
4. El camino dobla a la derecha (guía visual)
5. Sigue el camino hacia la ciudad
6. Entra por la puerta
7. Explora la ciudad
8. Encuentra a los rebeldes
```

### Señales visuales para guiar al jugador

| Señal | Ubicación | Propósito |
|-------|-----------|-----------|
| Camino de tierra | Desde aparición | Guía natural |
| Árboles densos | Bordes | Límite visual |
| Hierba alta | Alrededor del camino | Indica zona de exploración |
| Puerta de ciudad | Final del camino | Objetivo claro |
| NPC visible | Dentro de la ciudad | Incentivo para entrar |

---

## Capas en Tiled

### Capa 1: ground (piso)
- Todo el fondo: hierba (tile 0)
- Caminos: tierra (tile 3)
- Calles ciudad: piedra (tile 3)

### Capa 2: objects (objetos)
- Árboles (tile 1) en bordes
- Arbustos decorativos
- Edificios (tile 1) en ciudad
- Puertas (tile 4)

### Capa 3: collisions (colisiones)
- Object layer con rectángulos
- Muros de árboles
- Paredes de edificios
- Todo lo que no se puede atravesar

### Capa 4: portals (transiciones)
- Portal entrada ciudad: lleva a `ciudad_normal.json`
- Portal bosque: lleva a `overworld_normal.json`
- Spawn points para cada transición

---

## Tiles del tileset Pipoya (referencia rápida)

| ID | Descripción | Uso |
|----|-------------|-----|
| 0 | Hierba base | Fondo general |
| 1 | Árbol/arbusto | Bordes, bosque |
| 2 | Hierba alta | Encuentros aleatorios |
| 3 | Camino de tierra | Paths, calles |
| 4 | Puerta/arco | Entradas |
| 5 | Pared piedra | Edificios, muros |
| 6 | Agua | Ríos, lagos |
| 7 | Arena | Playas, bordes de agua |

---

## Checklist de diseño

- [ ] Borde de árboles alrededor del mapa
- [ ] Punto de aparición visible y accesible
- [ ] Camino claro desde aparición hasta ciudad
- [ ] Hierba alta alrededor del camino
- [ ] Puerta de entrada a la ciudad
- [ ] Calles dentro de la ciudad
- [ ] Edificios básicos (2-3 casas)
- [ ] Base rebelde (edificio especial)
- [ ] Colisiones en muros y edificios
- [ ] Portal de entrada a ciudad
- [ ] Spawn point dentro de ciudad
- [ ] NPCs visibles dentro de ciudad

---

## Errores comunes a evitar

| Error | Problema | Solución |
|-------|----------|----------|
| Mapa muy grande | Jugador se pierde | 40x23 es suficiente |
| Sin señales visuales | Jugador no sabe dónde ir | Camino de tierra claro |
| Colisiones incompletas | Jugador atraviesa muros | Verificar todas las paredes |
| Sin portal | No puede entrar a ciudad | Object layer con portal |
| Spawn en muro | Jugador aparece bloqueado | Verificar spawn point |

---

## Referencias

- `docs/tutorial.md` — Estructura del tutorial
- `docs/mundo.md` — Descripción de la Zona Normal
- `docs/tiled-guide.md` — Cómo usar Tiled
- `docs/estetica.md` — Paleta de colores, estilo visual
