import matplotlib.pyplot as plt

# Graphique 1 — Déplacés par province
fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(par_province.index, 
        par_province.values,
        color='#1a7a4a')

ax.set_title('Personnes déplacées par province — Est RDC',
             fontsize=14, pad=15)
ax.set_xlabel('Nombre de personnes')

# Ajouter les valeurs sur les barres
for i, v in enumerate(par_province.values):
    ax.text(v, i, f' {v:,}', va='center')

plt.tight_layout()
plt.savefig('graphique1_provinces_deplacepent_population.png', dpi=150)
print("Graphique 1 sauvegardé.")