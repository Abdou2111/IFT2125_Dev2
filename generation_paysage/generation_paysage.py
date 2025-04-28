# Abdelghafour Rahmouni 20246224
# Marc Olivier Jean Paul 20241763


from solid import *
from solid.utils import *
import numpy as np
import random

# CONSTANTS
MAX_HEIGHT = 40
GRID_SIZE = 80
STEP = 2  # plus petit = terrain plus détaillé
GREEN = (0, 1, 0.212)
YELLOW = (1, 1, 0.3)
SEA_BLUE = (0.282, 0.282, 1)
BUSH_GREEN = (0, 0.5, 0)
TREE_BROWN = (0.396, 0.263, 0.129)
TREE_GREEN = (0, 0.6, 0)

# Génération de base: une grille de hauteurs aléatoires lissées

def generate_heightmap(center, max_height, radius):
    size = GRID_SIZE // STEP
    cx, cy = center
    cx = int(cx / STEP)
    cy = int(cy / STEP)
    radius = int(radius / STEP)

    if cx - radius < 0 or cx + radius >= size or cy - radius < 0 or cy + radius >= size:
        return np.zeros((size, size))

    raw_map = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            dx = (i - cx)
            dy = (j - cy)
            d = np.sqrt(dx**2 + dy**2)
            raw_map[i, j] = max(0, 1 - (d / radius)**2)

    for _ in range(50):
        rx, ry = random.randint(0, size - 1), random.randint(0, size - 1)
        pradius = random.randint(3, 6)
        intensity = random.uniform(0.1, 0.5)
        for i in range(max(0, rx - pradius), min(size, rx + pradius)):
            for j in range(max(0, ry - pradius), min(size, ry + pradius)):
                dist = np.sqrt((i - rx)**2 + (j - ry)**2)
                if dist < pradius:
                    raw_map[i, j] += intensity * (1 - dist / pradius)

    smoothed = np.copy(raw_map)
    for _ in range(4):
        for i in range(1, size - 1):
            for j in range(1, size - 1):
                smoothed[i, j] = np.mean(raw_map[i - 1:i + 2, j - 1:j + 2])
        raw_map = np.copy(smoothed)

    return smoothed * max_height

def generate_island_terrain(center, max_height, radius):
    terrain = []
    heightmap = generate_heightmap(center, max_height, radius)
    size = GRID_SIZE // STEP

    for i in range(size):
        for j in range(size):
            h = heightmap[i][j]
            x = i * STEP
            y = j * STEP
            if h > 1:
                col = YELLOW if h < (max_height * 0.25) else GREEN
                block = color(col)(
                    translate([x, y, 1])(cube([STEP, STEP, h], center=False))
                )
                terrain.append(block)
                if h > (max_height * 0.3) and h < (max_height * 0.8):
                    if random.random() < 0.2:  # Densité élevée pour forêt
                        trunk = color(TREE_BROWN)(
                            translate([x + STEP / 2, y + STEP / 2, h + 1])(cylinder(r=0.4, h=3.5))
                        )
                        leaves = color(TREE_GREEN)(
                            translate([x + STEP / 2, y + STEP / 2, h + 4.6])(sphere(r=2.0))
                        )
                        terrain.extend([trunk, leaves])
    return union()(*terrain)

def generate_sea():
    return color(SEA_BLUE)(cube([GRID_SIZE, GRID_SIZE, 2]))

def add_text():
    initials = translate((50, 40, 0))(
        rotate((180, 0, 90))(
            color(GREEN)(
                text("A.R", size=10, font="Arial", valign="center", halign="center")
            )
        )
    )
    noms = translate((30, 40, 0))(
        rotate((180, 0, 90))(
            color(GREEN)(
                text("M.O.J.P", size=10, font="Arial", valign="center", halign="center")
            )
        )
    )
    sigle = translate((10, 40, 0))(
        rotate((180, 0, 90))(
            color(GREEN)(
                text("IFT 2125", size=10, font="Arial", valign="center", halign="center")
            )
        )
    )
    return initials + noms + sigle

# Assemblage final
scene = union()(
    generate_island_terrain(center=(30, 50), max_height=10, radius=20),
    difference()(
        generate_sea(),
        add_text()
    )
)

scad_code = scad_render(scene)
with open("model.scad", "w") as f:
    f.write(scad_code)
