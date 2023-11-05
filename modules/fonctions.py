# -*- coding: utf-8 -*-

def attempt(solution: int): # l'argument permet de récupérer la solution à trouver, de type int
    msgs = ["Félicitations ! Vous avez trouvé le nombre.", "Plus grand !", "Plus petit !", "Perdu ! Vous avez atteint le nombre maximal d'essais."] # messages qui seront affichés en fonction du nombre entré
    found = False #définition de la variable qui détermine si l'utilisateur a trouvé le bon nombre
    max_attempts = 10 #définition du nombre d'essais maximal
    attempts = 0 # nombre d'essais effectués
    while not found and attempts < max_attempts: #la boucle tourne tant que le bon nombre n'a pas été trouvé
        print("Entrer un nombre :") # l'input est séparé de la question affichée afin d'avoir l'entrée du joueur avec un retour à la ligne
        guess = int(input(""))
        result = check(guess, solution) # compare la réponse avec le nombre choisi
        print(msgs[result]) # affiche un message en fonction du résultat de la fonction check()
        found = not result # on considère que le joueur a trouvé le résultat si la fonction check() a retourné 0 (si le nombre trouvé est égal à la solution)
        attempts += 1
    if not found:
        print(msgs[3])

    
def check(guess: int, ans: int) -> int: #arguments et valeur retournée de type int
    if guess == ans: # comparaison des deux nombres
        return 0 #nombre trouvé
    elif guess < ans:
        return 1 #nombre trop petit
    else:
        return 2 #nombre trop grand
    