import json
import shutil

RUTA = "data/maps/overworld_normal.json"

# celdas a borrar: (capa, x, y)

BORRAR = [
    ("Plantas Layer 1", 23, 0), ("Plantas Layer 1", 24, 0),
    ("Plantas Layer 1", 25, 0), ("Plantas Layer 1", 26, 0),
    ("Plantas Layer 1", 27, 0), ("Plantas Layer 1", 28, 0),
    ("Plantas Layer 1", 29, 0), ("Plantas Layer 1", 30, 0),
    ("Plantas Layer 1", 31, 0),
]

with open(RUTA) as f:
    data = json.load(f)

width = data["width"]
for layer in data["layers"]:
    if layer["type"] != "tilelayer":
        continue
    for (capa, x, y) in BORRAR:
        if layer["name"] == capa:
            layer["data"][y * width + x] = 0

shutil.copy(RUTA, RUTA + ".bak")
with open(RUTA, "w") as f:
    json.dump(data,f)

print("listo, backup en", RUTA + ".bak")
