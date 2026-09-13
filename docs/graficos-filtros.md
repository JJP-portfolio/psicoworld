# Filtros gráficos estilo SNES (investigado 2026-09-13)

## Qué viste en realidad (dos cosas distintas)

1. **Filtros de emulador** (ZSNES/Snes9x/RetroArch): 2xSaI, SuperEagle, hqx, xBRZ. Redondean los
   bordes de los píxeles al ampliar. Eso es "píxeles redondeados" — estética de emulador de PC,
   no del hardware original.
2. **CRT real**: la tele de tubo difuminaba (bilineal analógico) + scanlines. Eso es "suave" SNES auténtico.

## Qué ofrece pygame-ce (verificado en docs)

| Función | Efecto | Costo |
|---|---|---|
| `transform.scale` | Nearest (píxel duro, auténtico) | Gratis |
| `transform.smoothscale` | Bilineal suave (borroso, no redondea). Acelerado MMX/SSE2 | Barato |
| `transform.scale2x` | Algoritmo Scale2X: duplica suavizando bordes. Lo más parecido a "redondeado" built-in | Medio |
| xBRZ real | Solo vía paquete externo `xbrz.py` (PyPI, binding C++. OJO licencia AGPLv3/GPLv3) | Caro/invasivo |

## Recomendación para PsicoWorld

- **Hoy:** píxel duro 1:1 (como está). Es lo auténtico y es gratis.
- **Experimento 1 (10 líneas):** overlay de scanlines pre-renderizado + `blit` por frame. Da el vibe CRT/SNES inmediato.
- **Experimento 2:** `scale2x` a un sprite al cargarlo y comparar lado a lado.
- **NO recomendado ahora:** xBRZ en assets (duplica el tile a 64 px → hay que cambiar TODA la matemática de grilla: `tile_size`, colisiones, cámara, Tiled). Deferir a post-vertical-slice.

## Snippet scanlines (probar en `game.py` tras crear screen)

```python
self.scanlines = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
for y in range(0, SCREEN_HEIGHT, 4):
    pygame.draw.line(self.scanlines, (0, 0, 0, 60), (0, y), (SCREEN_WIDTH, y))
# en run(), antes de flip:
# self.screen.blit(self.scanlines, (0, 0))
```
