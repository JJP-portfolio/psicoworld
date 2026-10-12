# PsicoWorld

JRPG top-down con combate en tiempo real (WASD + mouse), hecho con pygame-ce.

## Requisitos

- Python 3.10+
- pygame-ce

## Instalación

```bash
cd ~/Documentos/Proyectos/mi_jrpg
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar

```bash
source venv/bin/activate
python main.py
```

## Estructura

```
mi_jrpg/
├── main.py                 ← Punto de entrada
├── requirements.txt        ← Dependencias
├── DESIGN.md               ← Decisiones de diseño
├── SESSION_STATE.md        ← Estado actual de la sesión
├── src/                    ← Código del juego
│   ├── game.py             ← Loop principal
│   ├── settings.py         ← Constantes
│   ├── states/             ← Escenas (menú, exploración, combate)
│   ├── components/         ← Datos reutilizables
│   ├── systems/            ← Lógica del juego
│   ├── entities/           ← Fábricas de personajes
│   └── utils/              ← Helpers
├── assets/                 ← Imágenes, sonidos, fuentes
└── data/                   ← Mapas, datos de enemigos
```

## Controles

| Tecla | Acción |
|-------|--------|
| W/A/S/D | Movimiento |
| Click izquierdo | Ataque cuerpo a collide |
| Click derecho | Ataque a distancia |
| ESPACIO | Dash (futuro) |

## Licencia

Proyecto de aprendizaje — Taller de Diseño Conceptual y Taller de Programación UNAHUR.
