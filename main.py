# -*- coding: utf-8 -*-

# importation des fonctions nécessaires dans le modules
from random import randint
from modules.fonctions import attempt

solution = randint(1, 100)
print(solution) # pour tester le fonctoinnement
attempt(solution)
