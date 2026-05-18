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
plt.savefig('graphique/graphique1_provinces_deplacepent_population.png', dpi=150)
print("Graphique 1 sauvegardé.")
# Graphique 2 — Causes des déplacements
fig, ax = plt.subplots(figsize=(10, 6))

causes_courtes = [
    'Attaques armées',
    'Catastrophe naturelle',
    'Conflits fonciers',
    'Epidémie'
]

ax.bar(causes_courtes,
       par_cause.values,
       color='#1a7a4a')

ax.set_title('Causes des déplacements — Est RDC',
             fontsize=14, pad=15)
ax.set_ylabel('Nombre de personnes')

for i, v in enumerate(par_cause.values):
    ax.text(i, v, f' {v:,}', 
            ha='center', va='bottom')

plt.tight_layout()
plt.savefig('graphique/graphique2_causes.png', dpi=150)
print("Graphique 2 sauvegardé.")

# Graphique 3 — Evolution mensuelle 2020-2026
par_mois_recent = par_mois['2020-01':]

fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(par_mois_recent.index.astype(str),
        par_mois_recent.values,
        color='#1a7a4a',
        linewidth=2)

ax.fill_between(par_mois_recent.index.astype(str),
                par_mois_recent.values,
                alpha=0.2,
                color='#2ecc71')

ax.set_title('Evolution des déplacements — Est RDC (2020-2026)',
             fontsize=14, pad=15)
ax.set_ylabel('Nombre de personnes')
ax.set_xlabel('Mois')

# Afficher 1 label sur 6 pour lisibilité
ticks = range(0, len(par_mois_recent), 6)
ax.set_xticks(list(ticks))
ax.set_xticklabels(
    [par_mois_recent.index.astype(str)[i] for i in ticks],
    rotation=45)

plt.tight_layout()
plt.savefig('graphique/graphique3_evolution.png', dpi=150)
print("Graphique 3 sauvegardé.")