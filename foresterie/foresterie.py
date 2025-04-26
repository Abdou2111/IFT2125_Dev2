  
# Nom(s) étudiant(s) / Name(s) of student(s):

import sys

# Espace pour fonctions auxillaires :
# Space for auxilary functions :


# Fonction à compléter / function to complete:
def solve(cost, forest):
    # Conditions d'initialisation:

    # Si la forêt est vide, il n'y a pas d'arbre à couper
    if len(forest) == 0:
        return 0

        # Si le coût d'exploitation est négatif, il n'y a pas de profit
    if cost < 0:
        return -1

    # Si il n'y a qu'un arbre dans la forêt,
    # Il faut comparer le profit de le couper ou de ne pas le couper.
    if len(forest) == 1:
        return max(0, forest[0] - cost)

    # Si il y a deux arbres dans la forêt, on regarde
    # le profit de couper le premier arbre ou le deuxième arbre.
    # et le profit de ne pas couper d'arbre.
    if len(forest) == 2:
        return max(0, forest[0] - cost, forest[1] - cost)

    # Si il y a plus de deux arbres dans la forêt,
    # il faut utiliser l'algorithme de programmation dynamique.
    profit = [0] * len(forest)
    profit[0] = forest[0] - cost
    profit[1] = max(forest[0] - cost, forest[1] - cost)
    # On remplit la liste de profit en utilisant la relation de récurrence.
    for i in range(2, len(forest)):
        profit[i] = max(profit[i - 1], profit[i - 2] + forest[i] - cost)
    # On retourne le profit maximal.
    return profit[-1]


# Ne pas modifier le code ci-dessous :
# Do not modify the code below :

def process_numbers(input_file):
    try:
        # Read integers from the input file
        with open(input_file, "r") as f:
            lines = f.readlines() 
            cost = int(lines[0].strip())  # cout d'exploitation pour couper un arbre
            forest = list(map(int, lines[1].split()))  # valeur de chaque arbre    

        return solve(cost, forest)
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python foresterie.py <input_file>")
        return

    input_file = sys.argv[1]

    print(f"Input File: {input_file}")
    res = process_numbers(input_file)
    print(f"Result: {res}")

if __name__ == "__main__":
    main()