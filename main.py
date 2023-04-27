import requests

# Demander la plaque d'immatriculation du véhicule à l'utilisateur
plaque = input("Entrez la plaque d'immatriculation du véhicule (ex: AB-123-CD) : ")

# Construire l'URL de l'API avec la plaque d'immatriculation fournie
url = f"https://api.gouv.fr/api-immatriculation/v1/vehicules?plaque={plaque}"

# Envoyer une requête GET à l'API et récupérer la réponse au format JSON
response = requests.get(url)
data = response.json()

# Vérifier si la requête a réussi (code 200)
if response.status_code == 200:
    # Afficher les caractéristiques du véhicule
    print(f"Marque : {data['marque']}")
    print(f"Modèle : {data['modele']}")
    print(f"Année de fabrication : {data['annee']}")
    print(f"Type de carburant : {data['energie']}")
    print(f"Poids : {data['poids']}")
    print(f"Puissance fiscale : {data['puissance_admin']} CV")
else:
    print("Impossible de récupérer les caractéristiques du véhicule.")
