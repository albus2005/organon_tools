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
par_province = df.groupby('admin1_label')['person'].sum()
par_province = par_province.sort_values(ascending=False)
print(par_province)

# Question 2 — Causes des déplacements
par_cause = df.groupby('cause_label')['person'].sum()
par_cause = par_cause.sort_values(ascending=False)
print(par_cause)