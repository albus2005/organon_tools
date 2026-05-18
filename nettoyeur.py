import pandas as pd

df = pd.read_excel('donnees/rdc_mouvement_de_population_deplace_stock_mars_2026.xlsx', 
                    sheet_name='Data')

# Garder nos colonnes
cols = ['person', 'household', 'admin1_label', 
        'admin2_label', 'movement_date', 
        'cause_label', 'population_label']
df = df[cols]

print("Avant nettoyage :", len(df), "lignes")

# Supprimer les doublons
df = df.drop_duplicates()
print("Après suppression doublons :", len(df), "lignes")

# Supprimer les zéros aberrants
df = df[df['person'] > 0]
print("Après suppression zéros :", len(df), "lignes")

# Filtrer l'Est RDC uniquement
est_rdc = ['Nord-kivu', 'Sud-kivu', 'Ituri', 
           'Tanganyika', 'Maniema']
df = df[df['admin1_label'].isin(est_rdc)]
print("Après filtre Est RDC :", len(df), "lignes")

print("\nDonnées propres prêtes.")