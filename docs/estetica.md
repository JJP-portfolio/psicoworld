# Estética Visual — Porro Adventures

## Género Visual: Medieval Futurism

**Definición (Science Fiction Encyclopedia):**
> "Futuros tecnológicos, frecuentemente en otros planetas, pero con fuertes resonancias de sistemas feudales medievales como cuerpos gobernantes."

**Referentes clave:**
- Dune (Frank Herbert, 1965)
- Phantasy Star (SEGA, 1987)
- Warhammer 40K
- Star Wars (estética de mundos como Tatooine)

---

## Referentes Visuales

### Juegos

| Juego | Estilo | Elementos a tomar |
|-------|--------|-------------------|
| Phantasy Star | Sci-fi medieval | Mezcla de magia y tecnología, mundos pseudomedievales |
| Diablo | Dark fantasy | Paleta oscura, atmósfera opresiva |
| Hyper Light Drifter | Pixel art psicodélico | Colores neón, mundo misterioso |
| CrossCode | Sci-fi JRPG | Mundo pseudo-medieval con tecnología |

### Películas/Series

| Título | Elementos a tomar |
|--------|-------------------|
| Dune (2021) | Arquitectura masiva, paleta de colores terrosos |
| Altered States | Efectos psicodélicos, viajes alterados de conciencia |
| Fear and Loathing in Las Vegas | Visualización de psicotrópicos, caos visual |

### Arte

| Artista/Estilo | Elementos a tomar |
|----------------|-------------------|
| HR Giger | Biomecánico, orgánico mezclado con tecnología |
| Moebius | Paisajes alienígenas, colores psicodélicos |
| Syd Mead | Futurismo, tecnología integrada en paisajes |

---

## Paleta de Colores

### Mundo "Real" (Medieval Futurism)

| Elemento | Color RGB | Hex | Uso |
|----------|-----------|-----|-----|
| Piedra | (80, 70, 60) | #504638 | Edificios, suelo |
| Metal | (120, 110, 100) | #786E64 | Tecnología, armas |
| Tierra | (100, 80, 50) | #645032 | Suelo, caminos |
| Hierba | (60, 100, 40) | #3C6428 | Vegetación |
| Agua | (40, 80, 120) | #285078 | Ríos, lagos |
| Cielo | (100, 130, 160) | #6482A0 | Fondo |

### Mundo Psicotrópico (alterado)

| Elemento | Color RGB | Hex | Uso |
|----------|-----------|-----|-----|
| Neón verde | (0, 255, 128) | #00FF80 | Efectos psicotrópicos |
| Neón rosa | (255, 0, 128) | #FF0080 | Alteraciones de realidad |
| Neón azul | (0, 128, 255) | #0080FF | Magia/tecnología |
| Morado | (128, 0, 255) | #8000FF | Zonas alteradas |
| Negro profundo | (10, 5, 15) | #0A050F | Fondos del submundo |

---

## UI/UX

### Tipos de Interfaz (según tu curso)

| Tipo | Ejemplo en nuestro juego |
|------|--------------------------|
| **No diegética** | Barra de vida, minimapa, menú de pausa |
| **Diegética** | [Por definir: inventario como mochila, etc.] |
| **Espacial** | [Por definir] |
| **Meta** | Oscurecimiento de pantalla al recibir daño, efecto psicotrópico |

### Elementos UI

| Elemento | Estilo | Posición |
|----------|--------|----------|
| Barra de HP | Medieval-tech | Esquina superior izquierda |
| Barra de MP/Mana | Medieval-tech | Debajo de HP |
| Minimapa | Medieval-tech | Esquina superior derecha |
| Inventario | Medieval-tech | Centro (se abre con tecla) |
| Diálogos | Caja de texto inferior | Parte inferior |

---

## Efectos Visuales

### Efectos psicotrópicos

| Efecto | Cuándo se usa |
|--------|---------------|
| Screen shake suave | Al recibir daño fuerte |
| Colores saturados | Al usar habilidad especial |
| Distorsión leve | Al estar en zona alterada |
| Flash neón | Al entrar/salir del submundo |
| Partículas | Al recoger items, subir de nivel |

### Animaciones del jugador

| Acción | Frames | Velocidad |
|--------|--------|-----------|
| Idle | 2-4 | Lento |
| Caminar | 4-8 | Medio |
| Ataque melee | 2-4 | Rápido |
| Ataque rango | 2-4 | Rápido |
| Recibir daño | 2 | Rápido |
| Morir | 4-8 | Lento |

---

## Sprites

### Personajes (rectángulos iniciales, sprites futuros)

| Personaje | Tamaño base | Color inicial |
|-----------|-------------|---------------|
| Jugador | 32x48 | (0, 128, 255) |
| Enemigo básico | 32x48 | (255, 0, 0) |
| NPC | 32x48 | (0, 255, 0) |
| Boss | 64x64 | (255, 128, 0) |

###Tiles

| Tile | Tamaño | Notas |
|------|--------|-------|
| Piso | 32x32 | Base |
| Pared | 32x32 | Colisiona |
| Puerta | 32x32 | Interactuable |
| Objeto recogible | 16x16 o 32x32 | Animación de brillo |
