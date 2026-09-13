# Sprites — Porro Adventures

## Fuente
**PIPOYA FREE RPG Character Sprites 32x32**
- Licencia: Uso comercial/personal, modificar libremente
- Tamaño: 32x32 px
- Animación: 4 direcciones (caminar)
- URL: https://pipoya.itch.io/pipoya-free-rpg-character-sprites-32x32

## Estructura

```
sprites/
├── player/           # Sprites del jugador
│   ├── Male/         # Personajes masculinos (18 variantes)
│   ├── Female/       # Personajes femeninos (25 variantes)
│   └── Soldier/      # Soldados/armados (7 variantes)
├── enemies/          # Enemigos
│   ├── Enemy/        # Enemigos básicos (22 tipos)
│   └── Boss/         # Jefes (1 tipo)
├── npcs/             # NPCs y animales
│   ├── Animal/       # Gatos, perros
│   └── Other/        # Otros personajes
└── items/            # (pendiente)
```

## Naming Convention

Los sprites siguen el patrón:
- `Nombre XX-Y.png` donde:
  - `XX` = número de variante
  - `Y` = dirección (1=abajo, 2=izquierda, 3=derecha, 4=arriba)

## Uso en el Juego

### Jugador
- **Guerrero (El Anclado):** Usar sprites de `Soldier/` como base
- **Mago (El Visionario):** Usar sprites de `Male/` o `Female/` con modifications
- **Arquero (El Observador):** Usar sprites de `Male/` o `Female/` con modifications

### Enemigos
- **Zona Normal:** `Enemy 01-1.png` a `Enemy 10-1.png`
- **Zona Hielo:** `Enemy 11-1.png` a `Enemy 15-*.png` (con animación)
- **Zona Volcánica:** `Enemy 16-*.png` (con animación)
- **Desierto:** `Enemy 18.png` a `Enemy 22.png`
- **Bosses:** `Boss/Boss 01.png`

## Próximos Pasos

1. Modificar sprites con Krita para aesthetic Medieval Futurism
2. Agregar animaciones de ataque (usar Mithrillor Free Demo como referencia)
3. Crear sprites específicos por zona
4. Agregar efectos visuales (psicotrópicos)
