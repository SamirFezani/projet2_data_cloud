import json
import os

JSON_PATH = "data/raw/offres_remotive.json"
OUTPUT_PATH = "data/processed/offres_cleaned.json"

def charger_offres_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    if not os.path.exists(JSON_PATH):
        print(f"❌ Fichier introuvable : {JSON_PATH}")
    else:
        offres = charger_offres_json(JSON_PATH)
        print(f"✅ {len(offres)} offres extraites depuis JSON local.")

        os.makedirs("data/processed", exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f_out:
            json.dump(offres, f_out, indent=4, ensure_ascii=False)
        print(f"💾 Offres sauvegardées dans : {OUTPUT_PATH}")
