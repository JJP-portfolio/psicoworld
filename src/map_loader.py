import json
import os
from src.tilemap import Tilemap
from src.tileset import Tileset

def load_tiled_map(tileset, json_path):
    if not os.path.exists(json_path):
        return None

    with open(json_path, 'r') as f:
        data = json.load(f)

    width = data['width']
    height = data['height']
    tilemap = Tilemap(tileset, width, height)
    layers= {}
    for layer in data['layers']:
        if layer['type'] == 'tilelayer':
            grid = [[0 for _ in range(width)] for _ in range(height)]
            for y in range(height):
                for x in range(width):
                    gid = layer['data'][y * width + x]
                    if gid > 0:
                        tile_index = gid - 1
                        if tile_index < len(tileset.tiles):
                            grid[y][x] = tile_index
            layers[layer['name']] = grid

    tilemap.layers = layers
    return tilemap

def point_in_polygon(px, py, pts):
    inside = False
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        if ((y1 > py) != (y2 > py)) and (px < (x2 - x1) * (py - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside

def load_collisions(tilemap, json_path):
    if not os.path.exists(json_path):
        return

    with open(json_path, 'r') as f:
        data = json.load(f)

    for layer in data['layers']:
        if layer['type'] == 'objectgroup' and layer.get('name') == 'Colisiones':
            for obj in layer['objects']:
                if 'polygon' in obj:
                    pts = []
                    for p in obj['polygon']:
                        pts.append((obj['x'] + p['x'], obj['y'] + p['y']))
                    xs = []
                    xy = []
                    for pt in pts:
                        xs.append(pt[0])
                        xy.append(pt[1])
                    x0 = int(min(xs))
                    y0 = int(min(xy))
                    x1 = int(max(xs))
                    y1 = int(max(xy))
                    start_tx = x0 // tilemap.tile_size
                    start_ty = y0 // tilemap.tile_size
                    end_tx = x1 // tilemap.tile_size
                    end_ty = y1 // tilemap.tile_size
                    for ty in range(start_ty, end_ty + 1):
                        for tx in range(start_tx, end_tx + 1):
                            cx = tx * tilemap.tile_size + tilemap.tile_size // 2
                            cy = ty * tilemap.tile_size + tilemap.tile_size //2
                            if point_in_polygon(cx, cy, pts):
                                tilemap.set_collision(tx, ty, True)
                else:
                    x0 = int(obj['x'])
                    y0 = int(obj['y'])
                    x1 = x0 + int(obj.get('width', 32)) - 1
                    y1 = y0 + int(obj.get('height', 32)) - 1
                    start_tx = x0 // tilemap.tile_size
                    start_ty = y0 // tilemap.tile_size
                    end_tx = x1 // tilemap.tile_size
                    end_ty = y1 // tilemap.tile_size
                    for ty in range(start_ty, end_ty + 1):
                        for tx in range(start_tx, end_tx + 1):
                            tilemap.set_collision(tx, ty, True)
                        
def get_objects_from_map(json_path):
    if not os.path.exists(json_path):
        return[]

    with open(json_path, 'r') as f:
        data = json.load(f)

    objects = []
    for layer in data['layers']:
        if layer['type'] == 'objectgroup':
            for obj in layer['objects']:
                objects.append({
                    'name': obj.get('name', ''),
                    'x': obj.get('x', 0),
                    'y': obj.get('y', 0),
                    'width': obj.get('width', 0),
                    'height': obj.get('height', 0),
                })

    return objects
