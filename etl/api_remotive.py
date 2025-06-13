import requests
import json
import os

API_URL = "https://remotive.io/api/remote-jobs"
params = {"search": "data"}

print("📡 Récupération des offres depuis Remotive.io...")

response = requests.get(API_URL, params=params)

if response.status_code == 200:
    offres = response.json()["jobs"]
    os.makedirs("data/raw", exist_ok=True)

    with open("data/raw/offres_remotive.json", "w", encoding="utf-8") as f:
        json.dump(offres, f, indent=4, ensure_ascii=False)

    print(f"✅ {len(offres)} offres sauvegardées dans data/raw/offres_remotive.json")
else:
    print(f"❌ Erreur HTTP {response.status_code} : {response.text}")
