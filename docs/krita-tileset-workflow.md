# Workflow Krita para Tilesets — Porro Adventures

## Pipeline completo

```
Krita (diseñar tiles 32x32)
    ↓
Exportar como spritesheet PNG
    ↓
Tiled (cargar tileset, diseñar mapas)
    ↓
Exportar como JSON/TMX
    ↓
Pygame carga con pytmx
```

## Configuración de Krita para pixel art

| Setting | Valor |
|---------|-------|
| Tamaño canvas | 32x32 px por tile |
| Resolución | 72 DPI |
| Fondo | Transparente |
| Pincel | Pixel Brush, 1px, sin smoothing |
| Relleno | Threshold: 1, sin anti-aliasing |

## Atajos útiles

| Atajo | Función |
|-------|---------|
| B | Pincel |
| E | Borrador |
| Ctrl+Click | Seleccionar color |
| Tab | Solo canvas |
| M | Espejo horizontal |

## Crear tileset en Krita

1. Crear documento 256x544 (8 cols x 17 filas de 32x32)
2. Crear grilla guía (View → Show Grid → 32x32)
3. Dibujar cada tile en su posición
4. Exportar como PNG

## Plugin SZK Pixel Art Suite

- Pixel perfect brush (evita pixels dobles)
- Exportación escalada
- Instalar desde: https://krita-artists.org/t/szk-pixel-art-suite/114390

## Templates GDQuest

- https://github.com/GDQuest/krita-tileset-templates
- Incluye PSD (Krita), TMX (Tiled), TSX
- Estilo Zelda top-down

## Paleta por zona

### Zona Normal
| Elemento | Color | Hex |
|----------|-------|-----|
| Piel | (220, 180, 140) | #DCB48C |
| Pelo | (80, 50, 30) | #50321E |
| Ropa hierba | (60, 120, 40) | #3C7828 |

### Zona Hielo
| Elemento | Color | Hex |
|----------|-------|-----|
| Piel helada | (180, 220, 255) | #B4DCFF |
| Cristal | (200, 230, 255) | #C8E6FF |
| Escarcha | (240, 248, 255) | #F0F8FF |

### Zona Volcánica
| Elemento | Color | Hex |
|----------|-------|-----|
| Lava | (255, 80, 0) | #FF5000 |
| Roca caliente | (180, 60, 20) | #B43C14 |
| Fuego | (255, 200, 0) | #FFC800 |

### Zona Desierto
| Elemento | Color | Hex |
|----------|-------|-----|
| Arena | (220, 200, 160) | #DCC8A0 |
| Piedra seca | (180, 160, 120) | #B4A078 |
| Cielo | (100, 130, 160) | #6482A0 |
