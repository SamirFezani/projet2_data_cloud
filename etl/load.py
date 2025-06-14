# etl/load.py
import boto3
import json
import os

BUCKET_NAME = "samir-data-cloud"
OBJECT_KEY = "offres_cleaned.json"
LOCAL_FILE = "data/processed/offres_cleaned_from_s3.json"

def download_file_from_s3(bucket, key, local_path):
    s3 = boto3.client("s3")
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    s3.download_file(bucket, key, local_path)
    print(f"✅ Fichier téléchargé depuis S3 → {local_path}")

def lire_donnees(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    print(f"📊 {len(data)} offres chargées depuis {path}")
    return data

if __name__ == "__main__":
    download_file_from_s3(BUCKET_NAME, OBJECT_KEY, LOCAL_FILE)
    offres = lire_donnees(LOCAL_FILE)
