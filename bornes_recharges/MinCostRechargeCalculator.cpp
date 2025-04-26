#include "MinCostRechargeCalculator.h"
#include <vector>
#include <math.h>
#include <iostream>
#include <algorithm> // for std::max

// Nom(s) étudiant(s) / Name(s) of student(s):

// ce fichier contient les definitions des methodes de la classe MinCostRechargeCalculator
// this file contains the definitions of the methods of the MinCostRechargeCalculator class

using namespace std;

MinCostRechargeCalculator::MinCostRechargeCalculator()
{
}

int MinCostRechargeCalculator::CalculateMinCostRecharge(const vector<int>& RechargeCost) {
   int nombre_de_bornes = RechargeCost.size();
   // Les conditions d'initialisation de l'algorithme

   // Si le nombre de bornes est inférieur à 3, le coût est 0
   if (nombre_de_bornes < 3) return 0;

   // Si le nombre de bornes est égal à 3, le coût est le minimum des trois bornes
   else if (nombre_de_bornes == 3) {
      return min(RechargeCost[0], min(RechargeCost[1], RechargeCost[2]));
   }

   // Si le nombre de bornes est supérieur à 3, on utilise la formule de récurrence
   else {
      // initialiser le tableau cout avec les trois premiers coûts de recharge
      vector<int> cout(nombre_de_bornes, 0);
      cout[0] = RechargeCost[0];
      cout[1] = RechargeCost[1];
      cout[2] = RechargeCost[2];

      // On remplir la lsite des coûts en utilisant la formule de récurrence
      for (int i = 3; i < nombre_de_bornes; ++i)
         cout[i] = RechargeCost[i] + min(cout[i - 1], min(cout[i - 2], cout[i - 3]));
         return min(cout[nombre_de_bornes - 1],
            min(cout[nombre_de_bornes - 2], cout[nombre_de_bornes - 3]));
   }
}
