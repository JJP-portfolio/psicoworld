# Workflow de Sprites con Krita y Tablet

## Visión General

Guía para crear y modificar sprites usando Krita (gratuito) y una tableta gráfica. Ideal para el proyecto Porro Adventures.

---

## Configuración de Krita para Pixel Art

### 1. Crear documento

| Parámetro | Valor | Notas |
|-----------|-------|-------|
| **Tamaño** | 32x32 px (sprites base) | Para personajes: 32x48 |
| **Resolución** | 72 DPI | Pixel art no necesita alta resolución |
| **Color** | RGB 8-bit | Suficiente para pixel art |
| **Fondo** | Transparente | Para sprites con transparencia |

### 2. Configurar pinceles

**Pincel recomendado para pixel art:**
- **Pixel Brush** (pincel de pixel)
- Tamaño: 1px
- Sin suavizado (smoothing = 0)
- Sin anti-aliasing

**Atajos de teclado útiles:**
| Atajo | Función |
|-------|---------|
| `B` | Cambiar a modo pincel |
| `E` | Modo borrador |
| `Shift + Arrastrar` | Cambiar tamaño de pincel |
| `Ctrl + Click` | Seleccionar color |
| `I` / `O` | Aumentar/disminuir opacidad |
| `Tab` | Modo solo canvas |
| `M` | Espejo horizontal |
| `X` | Alternar color frente/fondo |

### 3. Configurar herramientas

**Herramienta de relleno (Bucket):**
- Threshold: 1
- Anti-aliasing: OFF
- Feather: 0px

**Herramienta de selección:**
- Anti-aliasing: OFF
- Feather: 0px

---

## Workflow de Creación de Sprites

### Paso 1: Sketch/Concepto

1. Crear capa nueva "Sketch"
2. Dibujar forma básica del personaje
3. Usar colores simples para definir masas
4. No preocuparse por detalles aún

### Paso 2: Line Art

1. Crear capa nueva "Lineart"
2. Dibujar líneas limpias sobre el sketch
3. Usar pincel de 1px
4. Mantener consistencia en grosor

### Paso 3: Color Base (Flat Color)

1. Crear capa nueva "Color" debajo de "Lineart"
2. Rellenar áreas con color base
3. Usar herramienta de relleno
4. Mantener paleta de colores limitada

### Paso 4: Sombreado

1. Crear capa nueva "Shading" (clipping mask sobre "Color")
2. Agregar sombras con color más oscuro
3. Agregar luces con color más claro
4. Usar pinceles de 1-2px

### Paso 5: Detalles

1. Crear capa nueva "Details"
2. Agregar detalles finos (ojos, ropa, etc.)
3. Refinar bordes
4. Agregar texturas si es necesario

### Paso 6: Exportar

1. Ocultar capas de sketch
2. Exportar como PNG con transparencia
3. Mantener tamaño original (32x32 o 32x48)

---

## Spritesheet con Krita

### Opción 1: Usar plugin Spritesheet Generator

**Instalación:**
1. Descargar plugin de GitHub
2. Copiar a carpeta de plugins de Krita
3. Activar en Configuración → Complementos de Python
4. Acceder desde Herramientas → Scripts

**Uso:**
1. Crear animación frame por frame en capas
2. Abrir plugin
3. Configurar layout (filas/columnas)
4. Configurar tamaño de sprite
5. Exportar spritesheet

### Opción 2: Método manual

1. Crear documento del tamaño del spritesheet
2. Copiar cada frame desde su documento
3. Pegar en posición correcta
4. Exportar como PNG

---

## Animación con Krita

### Configuración

1. Ir a Window → Dockers → Animation
2. Configurar framerate (8-12 FPS para pixel art)
3. Usar onion skinning para ver frames anteriores

### Proceso

1. Dibujar frame 1
2. Crear frame 2
3. Dibujar movimiento (usar onion skin como guía)
4. Repetir para cada frame
5. Previsualizar con botón de play
6. Exportar como spritesheet

### Frames típicos por acción

| Acción | Frames | Notas |
|--------|--------|-------|
| Idle | 2-4 | Movimiento sutil |
| Walk | 4-8 | 4 direcciones |
| Attack | 2-4 | Rápido |
| Hurt | 2 | Expresión de dolor |
| Death | 4-8 | Colapso |

---

## Paleta de Colores por Zona

### Zona Normal

| Elemento | Color | Hex |
|----------|-------|-----|
| Piel | (220, 180, 140) | #DCB48C |
| Pelo | (80, 50, 30) | #50321E |
| Ropa hierba | (60, 120, 40) | #3C7828 |
| Ropa piedra | (120, 100, 80) | #786450 |

### Zona de Hielo

| Elemento | Color | Hex |
|----------|-------|-----|
| Piel helada | (180, 220, 255) | #B4DCFF |
| Cristal | (200, 230, 255) | #C8E6FF |
| Metal helado | (120, 140, 160) | #788CA0 |
| Escarcha | (240, 248, 255) | #F0F8FF |

### Zona Volcánica

| Elemento | Color | Hex |
|----------|-------|-----|
| Lava | (255, 80, 0) | #FF5000 |
| Roca caliente | (180, 60, 20) | #B43C14 |
| Ceniza | (80, 70, 60) | #504638 |
| Fuego | (255, 200, 0) | #FFC800 |

### Desierto

| Elemento | Color | Hex |
|----------|-------|-----|
| Arena | (220, 200, 160) | #DCC8A0 |
| Piedra seca | (180, 160, 120) | #B4A078 |
| Cielo | (100, 130, 160) | #6482A0 |
| Sol | (255, 220, 100) | #FFDC64 |

---

## Recursos Útiles

### Tutoriales

| Recurso | Tipo | Descripción |
|---------|------|-------------|
| [Krita Manual - Pixel Art](https://docs.krita.org) | Documentación | Guía oficial de pixel art en Krita |
| [Aaron Rutten - Pixel Art with Krita](https://aaronrutten.com/pixel-art-with-krita) | Curso video | Curso completo de pixel art |
| [David Revoy - Krita Workflow](https://www.davidrevoy.com) | Video tutorial | Workflow digital painting |
| [SZK Pixel Art Suite](https://krita-artists.org/t/szk-pixel-art-suite/114390) | Plugin | Editor de pixel art dentro de Krita |

### Plugins

| Plugin | Función | Descarga |
|--------|---------|----------|
| SZK Pixel Art Suite | Editor pixel art | Krita Artists |
| Spritesheet Generator | Exportar spritesheets | GitHub |

### Assets de referencia

| Fuente | Tipo | Licencia |
|--------|------|----------|
| [OpenGameArt](https://opengameart.org) | Sprites gratuitos | Varias |
| [itch.io](https://itch.io/game-assets) | Sprites y tilesets | Varias |
| [CraftPix](https://craftpix.net) | Sprites premium | Premium/Free |

---

## Tips para el Proyecto

### Tamaños de sprites

| Elemento | Tamaño | Notas |
|----------|--------|-------|
| Jugador | 32x48 | 4 direcciones |
| Enemigos básicos | 32x32 | 4 direcciones |
| Enemigos grandes | 64x64 | Bosses |
| NPCs | 32x48 | 4 direcciones |
| Items | 16x16 | Recolectables |
| Tiles | 32x32 | Mapa |

### Organización de archivos

```
assets/
├── sprites/
│   ├── player/
│   │   ├── idle.png
│   │   ├── walk.png
│   │   ├── attack.png
│   │   └── hurt.png
│   ├── enemies/
│   │   ├── crystal_living.png
│   │   ├── ice_golem.png
│   │   └── ...
│   ├── npcs/
│   │   ├── rebel_leader.png
│   │   └── ...
│   └── items/
│       ├── psilocybe.png
│       ├── mdsa.png
│       └── ...
├── tilesets/
│   ├── normal/
│   ├── ice/
│   ├── volcanic/
│   └── desert/
└── ui/
    ├── health_bar.png
    ├── inventory.png
    └── ...
```

### Naming convention

- `nombre_accion_direccion.png`
- Ejemplo: `player_walk_right.png`, `enemy_idle.png`
- Spritesheets: `nombre_spritesheet.png`
