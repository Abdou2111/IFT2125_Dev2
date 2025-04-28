import random
import time

# Tri par insertion
# Complexité : O(n^2)
def tri_insertion(arr):
    if len(arr) <= 1:
        return arr

    for i in range(2, len(arr) - 1):
        val = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = val
    return arr


# Tri fusion
# Complexité : O(n log n)
def tri_fusion(arr, seuil):
    if len(arr) <= seuil:
        return tri_insertion(arr)

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    tri_fusion(arr[:mid], seuil)
    tri_fusion(arr[mid:], seuil)
    return fusion(arr, mid)


# Fusion deux tableaux triés
# Complexité : O(n)
def fusion(arr, mid):
    left = arr[:mid]
    right = arr[mid:]
    for i in range(len(left) - 1):
        left[i] = arr[i]
    for j in range(len(right) - 1):
        right[j] = arr[mid + 1 + j]

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr



# Tester différents seuils pour trouver le meilleur
def test_seuil():

    # Générer un tableau de taille aléatoire avec des données aléatoire
    taille_tableau = random.randint(0, 5000)
    donnees = [random.randint(0, taille_tableau) for _ in range(taille_tableau)]

    print(f"Taille du tableau: {taille_tableau}")

    # Initialiser les variables pour stocker le meilleur seuil et le meilleur temps
    meilleur_temps = float('inf')
    meilleur_seuil = 0

    # Tester différents seuils
    for seuil in range(2, 100):
        # Copier le tableau original pour éviter de modifier les données
        copie_tableau = donnees.copy()
        
        # Tester le même seuil 20 fois pour obtenir une moyenne
        for _ in range(10):
            # Mesurer le temps d'exécution pour le seuil actuel
            debut = time.time()
            # Appeler la fonction tri_fusion avec le seuil actuel
            tri_fusion(copie_tableau, seuil)
            fin = time.time()
            duree = fin - debut
            # Afficher le temps d'exécution pour le seuil actuel
            print(f"Seuil {seuil}: {duree:.6f} secondes")

           # Mettre à jour le meilleur seuil et le meilleur temps si nécessaire
            if duree < meilleur_temps:
                meilleur_temps = duree
                meilleur_seuil = seuil
                print(f" Nouveau meilleur seuil: {meilleur_seuil} avec {meilleur_temps:.6f} secondes")
                print("")

    print(f"\nMeilleur seuil: {meilleur_seuil} with time {meilleur_temps:.6f} seconds")



def main():
    for _ in range(5):
        test_seuil()

if __name__ == "__main__":
    main()