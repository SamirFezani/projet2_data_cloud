import json
import os

with open("data/raw/offres_remotive.json", encoding="utf-8") as f:
    offres = json.load(f)

# Nettoyage simple
for o in offres:
    o["titre"] = o["titre"].strip().capitalize()

# Sauvegarde nettoyée
os.makedirs("data/processed", exist_ok=True)
with open("data/processed/offres_cleaned.json", "w", encoding="utf-8") as f:
    json.dump(offres, f, indent=2, ensure_ascii=False)

print(f"✅ {len(offres)} offres nettoyées sauvegardées.")
