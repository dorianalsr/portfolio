import random

def choisir_mot():
    # Liste de mots sur le thème de l'informatique
    mots = ["python", "algorithme", "programme", "variable", "ordinateur", "serveur"]
    return random.choice(mots)

def jouer():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = []
    tentatives = 8
    
    print("--- BIENVENUE DANS LE JEU DU PENDU ---")
    
    while tentatives > 0:
        affichage = ""
        # On construit l'affichage (ex: p _ t _ o n)
        for lettre in mot_a_deviner:
            if lettre in lettres_trouvees:
                affichage += lettre + " "
            else:
                affichage += "_ "
        
        print(f"\nMot : {affichage}")
        print(f"Tentatives restantes : {tentatives}")
        
        # Victoire
        if "_" not in affichage:
            print("Félicitations ! Tu as gagné.")
            break
            
        proposition = input("Propose une lettre : ").lower()
        
        # Logique de vérification
        if len(proposition) != 1 or not proposition.isalpha():
            print("Erreur : Entre une seule lettre.")
            continue

        if proposition in lettres_trouvees:
            print("Tu as déjà proposé cette lettre !")
        elif proposition in mot_a_deviner:
            print("Bien joué !")
            lettres_trouvees.append(proposition)
        else:
            print("Raté...")
            tentatives -= 1
            lettres_trouvees.append(proposition)
            
    if tentatives == 0:
        print(f"\nDommage ! Le mot était : {mot_a_deviner}")

if __name__ == "__main__":
    jouer()