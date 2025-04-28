# Abdelghafour Rahmouni 20246224
# Marc Olivier Jean Paul 20241763

from solid import *
from solid.utils import *
import numpy as np
import random

# === CONSTANTES DE CONFIGURATION ===
MAX_HEIGHT = 40        # Hauteur maximale du terrain
GRID_SIZE = 80         # Taille de la grille (x et y)
STEP = 2               # Distance entre deux points du terrain
# Définition des couleurs
GREEN = (0, 1, 0.212)
YELLOW = (1, 1, 0.3)
SEA_BLUE = (0.282, 0.282, 1)
BUSH_GREEN = (0, 0.5, 0)
TREE_BROWN = (0.396, 0.263, 0.129)
TREE_GREEN = (0, 0.6, 0)

# === GÉNÉRATION DE LA CARTE DES HAUTEURS (terrain) ===
def generate_heightmap(center, max_height, radius):
    size = GRID_SIZE // STEP
    cx, cy = center
    cx = int(cx / STEP)
    cy = int(cy / STEP)
    radius = int(radius / STEP)

    # Si l'île sort du cadre, on renvoie une carte vide
    if cx - radius < 0 or cx + radius >= size or cy - radius < 0 or cy + radius >= size:
        return np.zeros((size, size))

    # Initialisation d'une carte plate
    raw_map = np.zeros((size, size))

    # Génération d'une base circulaire
    for i in range(size):
        for j in range(size):
            dx = (i - cx)
            dy = (j - cy)
            d = np.sqrt(dx**2 + dy**2)
            raw_map[i, j] = max(0, 1 - (d / radius)**2)

    # Ajout de bosses aléatoires pour rendre la surface plus naturelle
    for _ in range(50):
        rx, ry = random.randint(0, size - 1), random.randint(0, size - 1)
        pradius = random.randint(3, 6)
        intensity = random.uniform(0.1, 0.5)
        for i in range(max(0, rx - pradius), min(size, rx + pradius)):
            for j in range(max(0, ry - pradius), min(size, ry + pradius)):
                dist = np.sqrt((i - rx)**2 + (j - ry)**2)
                if dist < pradius:
                    raw_map[i, j] += intensity * (1 - dist / pradius)

    # Application de 10 passes de lissage (filtre moyenneur 3x3)
    smoothed = np.copy(raw_map)
    for _ in range(10):
        for i in range(1, size - 1):
            for j in range(1, size - 1):
                smoothed[i, j] = np.mean(raw_map[i - 1:i + 2, j - 1:j + 2])
        raw_map = np.copy(smoothed)

    # Mise à l'échelle de la hauteur finale
    return smoothed * max_height

# === CONSTRUCTION DU TERRAIN À PARTIR DE LA HAUTEUR ===
def generate_island_terrain(center, max_height, radius):
    terrain = []
    heightmap = generate_heightmap(center, max_height, radius)
    size = GRID_SIZE // STEP

    for i in range(size):
        for j in range(size):
            h = heightmap[i][j]
            x = i * STEP
            y = j * STEP

            if h > 1:  # On ignore les zones presque plates (sous l'eau)
                # Couleur différente pour la plage (basse altitude)
                col = YELLOW if h < (max_height * 0.17) else GREEN
                block = color(col)(
                    translate([x, y, 1])(cube([STEP, STEP, h], center=False))
                )
                terrain.append(block)

                # Ajout d'arbres pour les hauteurs intermédiaires (forêts)
                if h > (max_height * 0.3) and h < (max_height * 0.8):
                    if random.random() < 0.2:  # 20% de chance de planter un arbre
                        trunk = color(TREE_BROWN)(
                            translate([x + STEP / 2, y + STEP / 2, h + 1])(cylinder(r=0.4, h=3.5))
                        )
                        leaves = color(TREE_GREEN)(
                            translate([x + STEP / 2, y + STEP / 2, h + 4.6])(sphere(r=2.0))
                        )
                        terrain.extend([trunk, leaves])

    return union()(*terrain)  # Union de tous les éléments du terrain

# === GÉNÉRATION DE LA MER ===
def generate_sea():
    return color(SEA_BLUE)(cube([GRID_SIZE, GRID_SIZE, 2]))  # Mer = grande plaque plate bleue

# === AJOUT DE TEXTE PERSONNALISÉ SUR LA SCÈNE ===
def add_text():
    # Initiales
    initials = translate((50, 40, 0))(
        rotate((180, 0, 90))(
            color(GREEN)(
                text("A.R", size=10, font="Arial", valign="center", halign="center")
            )
        )
    )
    # Noms
    noms = translate((30, 40, 0))(
        rotate((180, 0, 90))(
            color(GREEN)(
                text("M.O.J.P", size=10, font="Arial", valign="center", halign="center")
            )
        )
    )
    # Sigle du cours
    sigle = translate((10, 40, 0))(
        rotate((180, 0, 90))(
            color(GREEN)(
                text("IFT 2125", size=10, font="Arial", valign="center", halign="center")
            )
        )
    )
    return initials + noms + sigle  # Assemblage des trois textes

# === ASSEMBLAGE FINAL DE LA SCÈNE ===
scene = union()(
    generate_island_terrain(center=(30, 50), max_height=10, radius=20),  # Génère le terrain
    difference()(
        generate_sea(),   # Génère la mer
        add_text()        # "Découpe" le texte dans la mer
    )
)

# === EXPORTATION DU MODÈLE EN FICHIER SCAD ===
scad_code = scad_render(scene)
with open("model.scad", "w") as f:
    f.write(scad_code)  # Sauvegarde du code SCAD
