
# Nom(s) étudiant(s) / Name(s) of student(s):
# Abdelghafour Rahmouni 20246224
# Marc Olivier Jean Paul 20241763

import sys
import time


# Espace pour fonctions auxillaires :
# Space for auxilary functions :

def tri_insertion(arr):
    """
    Fonction auxiliaire pour trier un tableau avec le tri par insertion.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def fusion(left, right):
    """
    Fonction auxiliaire pour fusionner deux tableaux triés.
    """
    resultat = []
    i = j = 0
    # fusion the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultat.append(left[i])
            i += 1
        else:
            resultat.append(right[j])
            j += 1
    resultat.extend(left[i:])
    resultat.extend(right[j:])
    return resultat

def tri_fusion(arr):
    """
    Fonction auxiliaire pour trier un tableau avec le tri fusion.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = tri_fusion(arr[:mid])
    right = tri_fusion(arr[mid:])
    return fusion(left, right)


def seuil_optimal(array):
    """
    Fonction auxiliaire pour déterminer le seuil optimal pour le tri hybride
    à partir du array donné.
    """
    seuil_opt = 0
    meilleur_temps = float('inf')

    for seuil in range(len(array)):
        copie = array.copy()
        debut = time.perf_counter()
        tri_hybride(copie, seuil)
        temps_ecoule = time.perf_counter() - debut

        if temps_ecoule < meilleur_temps:
            meilleur_temps = temps_ecoule
            seuil_opt = seuil

    return seuil_opt


def tri_hybride(arr, seuil):
    if len(arr) <= seuil:
        return tri_insertion(arr)
    else:
        return tri_fusion(arr)

# Fonction à compléter / function to complete:
def solve(array) :
    # Chercher le seuil optimal pour le tri hybride
    seuil = seuil_optimal(array)
    return tri_hybride(array, seuil)


# Ne pas modifier le code ci-dessous :
# Do not modify the code below :

def process_numbers(input_file):
    try:
        # Read integers from the input file
        with open(input_file, "r") as f:
            lines = f.readlines() 
            array = list(map(int, lines[0].split()))  # valeur de chaque noeud  

        return solve(array)
    
    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python tri_hybride.py <input_file>")
        return

    input_file = sys.argv[1]

    print(f"Input File: {input_file}")
    res = process_numbers(input_file)
    print(f"resultat: {res}")

if __name__ == "__main__":
    main()

