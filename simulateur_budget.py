def calculer_epargne():
    print("\n--- CALCULATEUR D'ÉPARGNE ---")
    mensualite = float(input("Combien pouvez-vous mettre de côté par mois (€) ? : "))
    taux = float(input("Taux d'intérêt annuel (en %) : ")) / 100
    annees = int(input("Durée du placement (années) : "))
    
    # Formule des intérêts composés
    capital_final = mensualite * 12 * annees * (1 + taux)
    print(f"\nEstimation : Après {annees} ans, vous aurez environ {round(capital_final, 2)}€.")

def calculer_credit():
    print("\n--- SIMULATEUR DE CRÉDIT ---")
    montant = float(input("Montant de l'emprunt (€) : "))
    taux_annuel = float(input("Taux d'intérêt annuel (en %) : ")) / 100
    duree_mois = int(input("Durée du crédit (en mois) : "))
    
    # Formule de mensualité de crédit classique
    taux_mensuel = taux_annuel / 12
    mensualite = (montant * taux_mensuel) / (1 - (1 + taux_mensuel)**-duree_mois)
    
    total_du = mensualite * duree_mois
    cout_credit = total_du - montant
    
    print(f"\nMensualité : {round(mensualite, 2)}€ / mois")
    print(f"Coût total du crédit (intérêts) : {round(cout_credit, 2)}€")

def main():
    print("=== OUTIL DE GESTION FINANCIÈRE BAGA ===")
    print("1. Calculer une épargne")
    print("2. Simuler un crédit")
    choix = input("Votre choix (1 ou 2) : ")
    
    if choix == "1":
        calculer_epargne()
    elif choix == "2":
        calculer_credit()
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()