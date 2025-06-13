import json
import plotly.express as px

with open("data/processed/offres_cleaned.json", encoding="utf-8") as f:
    offres = json.load(f)

df = pd.DataFrame(offres)

fig = px.bar(df['lieu'].value_counts().head(10).reset_index(),
             x='index', y='lieu',
             labels={'index': 'Lieu', 'lieu': "Nombre d'offres"},
             title="Top lieux d'offres")
fig.show()
