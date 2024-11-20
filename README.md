Ce projet petit utilise un arbre de décision pour prédire si un joueur de football a une "valeur marchande élevée" (supérieure à 50 millions) la monnaie utilisée est le livre Sterling, en fonction de ses statistiques comme l'âge, les buts, les matchs joués et les passes décisives.
players.csv : Fichier CSV contenant les données des joueurs.
Players_DecisionTri.py : Script principal qui :
-Charge les données,
-Effectue le nettoyage et la préparation des données en supprimant les records ou il y a des valeurs manquantes mais aussi certains noms de colonnes peuvent contenir des espaces en début ou en fin, ce qui pose problème lors de leur utilisation. Cette étape supprime ces espaces pour éviter les erreurs.
-Entraîne un modèle de classification d'arbre de décision,
-Affiche l'arbre de décision avec biblio matplotlib
