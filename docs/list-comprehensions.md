# List Comprehensions — Guía Rápida

## Qué es

Una forma compacta de crear listas en Python. En vez de escribir un `for` largo, lo hacés en una línea.

---

## Sintaxis básica

```python
[expresión for variable in iterable]
```

**Ejemplo simple:**
```python
# Forma tradicional
numeros = []
for x in range(5):
    numeros.append(x * 2)
# → [0, 2, 4, 6, 8]

# Forma compacta
numeros = [x * 2 for x in range(5)]
# → [0, 2, 4, 6, 8]
```

---

## Con condición (filter)

```python
[expresión for variable in iterable if condición]
```

**Ejemplo:**
```python
# Solo números pares
pares = [x for x in range(10) if x % 2 == 0]
# → [0, 2, 4, 6, 8]

# Solo palabras largas
palabras = ["hola", "hi", "mundo", "ok"]
largas = [p for p in palabras if len(p) > 2]
# → ["hola", "mundo"]
```

---

## Con if/else

```python
[expresión_si_verdadero if condición else expresión_si_falso for variable in iterable]
```

**Ejemplo:**
```python
# Etiquetar números
etiquetas = ["par" if x % 2 == 0 else "impar" for x in range(5)]
# → ["par", "impar", "par", "impar", "par"]

# Multiplicar pares, impares quedan en 0
resultado = [x * 2 if x % 2 == 0 else 0 for x in range(6)]
# → [0, 0, 4, 0, 8, 0]
```

---

## Anidadas (nuestro caso)

Cuando necesitás una lista de listas (matriz 2D).

```python
[[expresión for x in range(ancho)] for y in range(alto)]
```

**Ejemplo — Nuestro tilemap:**
```python
# Crear mapa de 5 columnas x 3 filas lleno de ceros
self.map = [[0 for _ in range(5)] for _ in range(3)]
```

**Qué hace paso a paso:**
```python
# Paso 1: la parte interna crea UNA fila
[0 for _ in range(5)]  # → [0, 0, 0, 0, 0]

# Paso 2: la parte externa repite esa fila 3 veces
[[0, 0, 0, 0, 0] for _ in range(3)]
# → [[0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0]]
```

**Resultado visual:**
```
Fila 0:  [0, 0, 0, 0, 0]
Fila 1:  [0, 0, 0, 0, 0]
Fila 2:  [0, 0, 0, 0, 0]
          ↑  ↑  ↑  ↑  ↑
        Col0 Col1 Col2 Col3 Col4
```

**Para acceder:** `mapa[fila][columna]`
```python
mapa[2][3] = 5  # Fila 2, columna 3 → valor 5
```

---

## Anidadas con valores diferentes

```python
# Mapa con valores distintos
mapa = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 4, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
```

---

## Con funciones

```python
# Longitud de cada palabra
palabras = ["hola", "mundo", "python"]
longitudes = [len(p) for p in palabras]
# → [4, 5, 6]

# Convertir a mayúsculas
mayusculas = [p.upper() for p in ["hola", "mundo"]]
# → ["HOLA", "MUNDO"]
```

---

## Forma tradicional vs Comprensión

| Forma tradicional | Comprensión |
|-------------------|-------------|
| ```python | ```python |
| resultado = [] | resultado = [x*2 for x in range(5)] |
| for x in range(5): | |
|     resultado.append(x*2) | |
| ``` | ``` |

**Cuándo usar cada una:**

| Situación | Recomendación |
|-----------|---------------|
| Lógica simple | Comprensión |
| Lógica compleja (múltiples if, cálculos) | Forma tradicional |
| Solo estás aprendiendo | Forma tradicional |
| Ya sabés leer comprensiones | Comprensión |

---

## Errores comunes

### Olvidar los corchetes externos
```python
# Mal — crea un generador, no una lista
(0 for _ in range(5))

# Bien — crea una lista
[0 for _ in range(5)]
```

### Confundir el orden del if/else
```python
# Mal — el if va al final para filtrar
[x for x in range(10) if x > 5 else 0]

# Bien — filtrar al final
[x for x in range(10) if x > 5]

# Bien — if/else va al principio
[x if x > 5 else 0 for x in range(10)]
```

---

## Resumen rápido

```python
# Básica
[expresión for variable in iterable]

# Con filtro
[expresión for variable in iterable if condición]

# Con if/else
[si_verdadero if condición else si_falso for variable in iterable]

# Anidada (matriz 2D)
[[expresión for x in range(ancho)] for y in range(alto)]
```
