# 🚀 Projet 2 — Collecte et Stockage de Données sur le Cloud

## 🌟 Objectif

Mettre en place une infrastructure **ETL complète** permettant de :

* Extraire des offres d'emploi via **scraping HTML** et **API (Remotive.io ou Pôle Emploi)**.
* Transformer et nettoyer les données collectées.
* Stocker les données localement et dans le **cloud (AWS S3 ou RDS)**.
* Visualiser les résultats via un **dashboard interactif (Plotly/Dash)**.

---

## 🧱 Pipeline ETL

### 📅 Extraction (`etl/`)

* `extract.py` : Scraping d’un site (ex: Weworkremotely, RemoteOK, ou HTML local).
* `api_remotive.py` : Récupération d’offres via API Remotive.io.
* `api_pe.py` *(optionnel)* : Requête à l’API Pôle Emploi.

### 🔄 Transformation (`transform.py`)

* Nettoyage des intitulés, entreprises et lieux.
* Formatage JSON pour stockage.

### 📂 Chargement (`load.py`)

* Lecture/écriture locale des fichiers `.json` dans `data/processed/`.
* Optionnel : Upload vers **Amazon S3**.

---

## 📊 Visualisation (`dashboard/`)

Dashboard interactif avec \[Plotly Dash] affichant :

* Histogramme des lieux les plus fréquents.
* Répartition des offres par entreprise.
* Nuage de mots des titres de poste.

---

## ☁️ Cloud (Facultatif)

### ✅ AWS S3

* Stockage des fichiers JSON transformés.
* Accès configuré avec `boto3` et `aws configure`.

### ✅ AWS RDS (PostgreSQL)

* *(Optionnel)* Connexion possible via `psycopg2` pour charger les offres dans une base de données PostgreSQL sur RDS.

---

## 📁 Arborescence du projet

```
projet2_data_cloud/
├── data/
│   ├── raw/
│   └── processed/
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── api_remotive.py
│   └── api_pe.py
├── dashboard/
│   └── dashboard.py
├── notebooks/
│   └── exploration.ipynb
├── infra/
│   ├── s3_config.md
│   ├── rds_config.md
│   └── iam_roles.md
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/SamirFezani/projet2_data_cloud.git
   cd projet2_data_cloud
   ```

2. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Exécution

1. **Extraction** :

   ```bash
   python etl/extract.py
   ```

2. **Transformation** :

   ```bash
   python etl/transform.py
   ```

3. **Chargement (option AWS)** :

   ```bash
   python etl/load.py
   ```

4. **Dashboard** :

   ```bash
   python dashboard/dashboard.py
   ```

---

## 📌 Remarques

* Les fichiers `.html` pour le scraping peuvent être stockés dans `data/raw/`.
* La clé AWS est à configurer via `aws configure`.
* L’accès à l’API PE nécessite une inscription sur [https://emploi-store.dev](https://emploi-store.dev).

---

## 🙌 Auteurs

* **Samir Fezani**
* Projet réalisé dans le cadre du **parcours Data Analyst chez OpenClassrooms**.
