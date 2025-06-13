import os
import requests
import json
from datetime import datetime

# Vos identifiants d'application Pôle Emploi
CLIENT_ID = "PAR_projet2datacloud_fd28af025714373e87bbc015608bbad09fbb3e2a16051f6f1bd8ed952bae9d58"
CLIENT_SECRET = "b1f39825834f808b00f055d22b328ca434603fb089e1fe7733720aa4a1cc21a5"

# Répertoire de sauvegarde
OUTPUT_DIR = "data/raw"

# Assurez-vous que le dossier existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_access_token():
    url = "https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=/partenaire"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "api_offresdemploiv2 o2dsoffre"
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code in [200, 206]:
        return response.json().get("resultats", [])
    else:
        raise Exception(f"Erreur récupération des offres : {response.status_code} - {response.text}")


def get_job_offers(token, mot_cle="data", departement="75", max_results=20):
    url = "https://api.pole-emploi.io/partenaire/offresdemploi/v2/offres/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "motsCles": "data",
        "range": "0-9"
    }


    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["resultats"]
    else:
        raise Exception(f"Erreur récupération des offres : {response.status_code} - {response.text}")

def save_offers_to_file(offers):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(OUTPUT_DIR, f"offres_{now}.json")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(offers, f, ensure_ascii=False, indent=2)

    print(f"✅ Offres sauvegardées dans : {filename}")

if __name__ == "__main__":
    try:
        print("🔐 Obtention du token...")
        token = get_access_token()

        print("📥 Récupération des offres...")
        offers = get_job_offers(token)

        print("💾 Sauvegarde des offres...")
        save_offers_to_file(offers)

        print("✅ Tout est terminé avec succès.")
    except Exception as e:
        print(f"❌ Erreur : {e}")
