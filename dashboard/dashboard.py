# -*- coding: utf-8 -*-
import pandas as pd
import plotly.express as px

# Charger les données nettoyées
df = pd.read_csv("../data/processed/offres_remoteok_clean.csv")

# ======================
# Graphique 1 : Répartition des offres par lieu
# ======================
top_lieux = df['lieu'].value_counts().head(10).reset_index()
top_lieux.columns = ['lieu', 'nombre']

fig_lieux = px.bar(
    top_lieux,
    x='lieu',
    y='nombre',
    title="Top 10 des lieux d'offres",
    labels={"lieu": "Lieu", "nombre": "Nombre d'offres"},
    text='nombre'
)
fig_lieux.update_traces(textposition='outside')

# ======================
# Graphique 2 : Répartition des offres par entreprise
# ======================
top_entreprises = df['entreprise'].value_counts().head(10).reset_index()
top_entreprises.columns = ['entreprise', 'nombre']

fig_entreprises = px.pie(
    top_entreprises,
    names='entreprise',
    values='nombre',
    title="Répartition des offres par entreprise"
)

# ======================
# Export en fichiers HTML
# ======================
fig_lieux.write_html("../data/processed/dashboard_lieux.html", auto_open=True)
fig_entreprises.write_html("../data/processed/dashboard_entreprises.html", auto_open=True)

print("✅ Dashboards générés et ouverts dans le navigateur.")
