#unprigramme qui diagnostique les probleme dansun dataset.

import pandas as pd

df = pd.read_excel('rdc_mouvement_de_population_deplace_stock_mars_2026.xlsx', 
                    sheet_name='Data')

cols = ['person', 'household', 'admin1_label', 
        'admin2_label', 'movement_date', 
        'cause_label', 'population_label']
df = df[cols]

print("VALEURS MANQUANTES")
print(df.isnull().sum())

print("\nDOUBLONS")
print(df.duplicated().sum())

print("\nVALEURS ABERRANTES")
print("Personnes à zéro :", (df['person'] <= 0).sum())

print("\nCAUSES UNIQUES")
print(df['cause_label'].unique())

print("\nPROVINCES")
print(df['admin1_label'].unique())