import pandas as pd

df = pd.read_excel('donnees/rdc_mouvement_de_population_deplace_stock_mars_2026.xlsx', 
                    sheet_name='Data')

# Garder nos colonnes
cols = ['person', 'household', 'admin1_label', 
        'admin2_label', 'movement_date', 
        'cause_label', 'population_label']
df = df[cols]

# Nettoyage
df = df.drop_duplicates()
df = df[df['person'] > 0]
est_rdc = ['Nord-kivu', 'Sud-kivu', 'Ituri', 
           'Tanganyika', 'Maniema']
df = df[df['admin1_label'].isin(est_rdc)]

# Question 1 — Déplacés par province
print("Regroupement par provinces")
par_province = df.groupby('admin1_label')['person'].sum()
par_province = par_province.sort_values(ascending=False)
print(par_province)

# Question 2 — Causes des déplacements
print("Regroupement par causes ")
par_cause = df.groupby('cause_label')['person'].sum()
par_cause = par_cause.sort_values(ascending=False)
print(par_cause)

print("Evolution mensuelle des déplacements dans l'Est de la RDC ")
print("Nombre de mois :", len(par_mois))
print("Premier mois :", par_mois.index[0])
print("Dernier mois :", par_mois.index[-1])
# Question 3 — Evolution dans le temps
df['mois'] = df['movement_date'].dt.to_period('M')
par_mois = df.groupby('mois')['person'].sum()
print(par_mois)