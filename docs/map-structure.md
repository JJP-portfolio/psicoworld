# Estructura de Mapas — Porro Adventures

## Mapas por zona

Cada zona tiene 3 tipos de mapa:

```
ZONA NORMAL (Nivel 1-5) — Tutorial
├── overworld_normal.json    ← Bosque, camino, exploración
├── ciudad_normal.json       ← Megalopolis (hub seguro)
└── bossplace_normal.json    ← [Por definir]

ZONA HIELO (Nivel 5-10)
├── overworld_hielo.json     ← Terreno congelado
├── ciudad_hielo.json        ← Asentamiento subterráneo
└── bossplace_hielo.json     ← Laboratorio (El Conservador)

ZONA VOLCÁNICA (Nivel 10-15)
├── overworld_volcanica.json ← Lava, terreno inestable
├── ciudad_volcanica.json    ← Asentamiento pequeño
└── bossplace_volcanica.json ← Templo volcánico

ZONA DESIERTO (Nivel 15-20)
├── overworld_desierto.json  ← Arena, árido
├── ciudad_desierto.json     ← Asentamiento mínimo
└── bossplace_desierto.json  ← Guarida del antagonista
```

## Conexiones entre mapas

| Mapa origen | Portal | Mapa destino | Spawn |
|-------------|--------|--------------|-------|
| overworld_normal | borde norte | overworld_hielo | (320, 400) |
| overworld_normal | puerta ciudad | ciudad_normal | (160, 400) |
| ciudad_normal | salida bosque | overworld_normal | (320, 100) |
| overworld_hielo | puerta lab | bossplace_hielo | (160, 400) |
| bossplace_hielo | salida | overworld_hielo | (100, 200) |

## Tamaño de mapas

| Tipo | Tamaño tiles | Tamaño pixels | Notas |
|------|-------------|---------------|-------|
| Overworld | 40x23 | 1280x736 | Pantalla completa |
| Ciudad | 30x20 | 960x640 | Más chica, más detallada |
| Bossplace | 20x15 | 640x480 | Dungeon, habitaciones |

## Carpetas

```
data/maps/
├── normal/
│   ├── overworld_normal.json
│   ├── ciudad_normal.json
│   └── bossplace_normal.json
├── hielo/
│   ├── overworld_hielo.json
│   ├── ciudad_hielo.json
│   └── bossplace_hielo.json
├── volcanica/
│   └── ...
├── desierto/
│   └── ...
└── shared/
    └── pipoya-32x32.tsx
```
