import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import seaborn as sns


# Data_Frame1
UmsatzOnline2020 = {'Monat': ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August",
                              "September", "Oktober", "November", "Dezember"],
                    "Besucher": [259, 364, 312, 290, 400, 350,
                                 200, 350, 280, 320, 470, 520],
                    "BesucherOhneAktion(Online)": [122, 182, 198, 150, 111, 170,
                                                   184, 210, 52, 190, 260, 190],
                    "UmsatzInEuro(Online2020)": [3549.43, 5324.99, 5350.12, 9612.89, 8002.98, 6199.89,
                                                 5987.78, 4649.88, 3544.89, 6987.78, 7254.78, 11323.87]}



# Erstellung des ersten dataframes ohne Index
df0 = pd.DataFrame(UmsatzOnline2020)
print("\u0332".join("      Umsatz online im Jahr 2020 "))
blankIndex = [''] * len(df0)
df0.index = blankIndex
print(df0)
print("\n")
print("\n")

# Der Umsatz für das Jahr 2020
totalWert0 = df0["UmsatzInEuro(Online2020)"].sum()
totalWert0 = round(totalWert0, 2)
print("Der Umsatz für das Jahr 2020 beträgt: " + str(totalWert0) + " Euro")
year2020 = 2020
print("\n")



# Data_Frame2
UmsatzOnline2021 = {'Monat': ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August",
                              "September", "Oktober", "November", "Dezember"],
                    "Besucher": [259, 364, 312, 290, 400, 350,
                                 200, 350, 280, 320, 470, 520],
                    "BesucherOhneAktion(Online)": [122, 182, 198, 150, 101, 170,
                                                   180, 220, 32, 230, 260, 190],
                    "UmsatzInEuro(Online2021)": [4549.43, 5324.99, 4000.12, 4312.89, 5002.98, 5699.89,
                                                 3987.78, 3689.88, 4544.89, 5987.78, 6254.78, 7323.87]}



# Erstellung des zweiten dataframes ohne Index
df1 = pd.DataFrame(UmsatzOnline2021)
print("\u0332".join("      Umsatz online im Jahr 2021 "))
blankIndex = [''] * len(df1)
df1.index = blankIndex
print(df1)
print("\n")
print("\n")


# Der Umsatz für das Jahr 2021
totalWert1 = df1["UmsatzInEuro(Online2021)"].sum()
totalWert1 = round(totalWert1, 2)
print("Der Umsatz für das Jahr 2021 beträgt: " + str(totalWert1) + " Euro")
year2021 = 2021
print("\n")



# Data_Frame3
UmsatzOnline2022 = {'Monat': ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August",
                              "September", "Oktober", "November", "Dezember"],
                    "Besucher": [359, 344, 212, 390, 300, 289,
                                 246, 380, 340, 370, 473, 420],
                    "BesucherOhneAktion(Online)": [162, 152, 238, 180, 131, 150,
                                                   150, 240, 96, 210, 240, 210],
                    "UmsatzInEuro(Online2022)": [6249.23, 8467.99, 7340.12, 7852.89, 9922.98, 8999.89,
                                                 5187.78, 6889.88, 6244.89, 6857.78, 9258.78, 14333.87]}


# Erstellung des dritten dataframes ohne Index
df2 = pd.DataFrame(UmsatzOnline2022)
print("\u0332".join("        Umsatz online im Jahr 2022 "))
blankIndex = [''] * len(df2)
df2.index = blankIndex
print(df2)
print("\n")



# Der Umsatz für das ganze Jahr 2022
totalWert2 = df2["UmsatzInEuro(Online2022)"].sum()
totalWert2 = round(totalWert2, 2)
print("Der Umsatz für das Jahr 2022 beträgt: " + str(totalWert2) + " Euro")
year2022 = 2022
year2023 = 2023
print("\n")






# Verbinden anhand der Monate
merged_df = pd.merge(df0, df1, on='Monat')
merged_df = pd.merge(merged_df, df2, on='Monat')
#merged_df = pd.merge(df0,df1, df2, on='Monat')

# Balkendiagramm erstellen Vergleich 2021 und 2022
plt.figure(figsize=(16, 8))


bar_width = 0.25  # Breite der Balken
bar_positions = range(len(merged_df))


plt.bar(bar_positions, merged_df['UmsatzInEuro(Online2020)'], label='Umsatz 2020', color='red', alpha=0.7, width=bar_width)
plt.bar([pos + bar_width for pos in bar_positions], merged_df['UmsatzInEuro(Online2021)'], label='Umsatz 2021', color='blue', alpha=0.7, width=bar_width)
plt.bar([pos + 2*bar_width for pos in bar_positions], merged_df['UmsatzInEuro(Online2022)'], label='Umsatz 2022', color='grey', alpha=0.7, width=bar_width)



plt.xlabel('Monat')
plt.ylabel('Umsatz in Euro')
plt.legend()
plt.xticks([pos + bar_width for pos in bar_positions], merged_df['Monat'], rotation=45)
plt.tight_layout()
plt.grid()
plt.style.use("Solarize_Light2")



for i, v1, v2, v3 in zip(bar_positions, merged_df['UmsatzInEuro(Online2020)'], merged_df['UmsatzInEuro(Online2021)'], merged_df['UmsatzInEuro(Online2022)']):
    plt.text(i, v1 + 100, str(round(v1, 2)), color='red', fontsize=10, ha='center')
    plt.text(i + bar_width, v2 + 100, str(round(v2, 2)), color='blue', fontsize=10, ha='center')
    plt.text(i + 2*bar_width, v3 + 100, str(round(v3, 2)), color='grey', fontsize=10, ha='center')

plt.show()


# Daten für 2023
monate_2023 = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober",
               "November", "Dezember"]

# Erstellung eines DataFrame für 2023 mit den Monaten
df_2023 = pd.DataFrame({"Monat": monate_2023})


# Initialisierung einer leeren Liste für die Umsatzvorhersagen
umsatz_vorhersagen = []


# Schleife durch die Monate in 2023
for monat in monate_2023:
    # Daten für den aktuellen Monat aus den letzten beiden Jahren holen
    daten_2020 = df0[df0["Monat"] == monat]
    daten_2021 = df1[df1["Monat"] == monat]
    daten_2022 = df2[df2["Monat"] == monat]

    # Gesamtumsatz für den aktuellen Monat aus den letzten beiden Jahren berechnen
    gesamtumsatz_2020 = daten_2020["UmsatzInEuro(Online2020)"].values[0]
    gesamtumsatz_2021 = daten_2021["UmsatzInEuro(Online2021)"].values[0]
    gesamtumsatz_2022 = daten_2022["UmsatzInEuro(Online2022)"].values[0]


    # Lineare Regression vorbereiten
    x = np.array([year2020, year2021, year2022]).reshape(-1, 1)
    y = np.array([gesamtumsatz_2020, gesamtumsatz_2021, gesamtumsatz_2022])
    regressor = LinearRegression()

    # Lineare Regression anpassen
    regressor.fit(x, y)

    # Umsatz für 2023 vorhersagen
    umsatz_2023 = regressor.predict([[2023]])[0]

    # Umsatzvorhersage zur Liste hinzufügen
    umsatz_vorhersagen.append(umsatz_2023)



# Umsatzvorhersagen in den DataFrame für 2023 einfügen
df_2023["UmsatzInEuro(Online2023)"] = umsatz_vorhersagen





# Balkendiagramm für die Umsatzvorhersagen 2023 erstellen
plt.figure(figsize=(12, 6))
plt.bar(df_2023['Monat'], df_2023['UmsatzInEuro(Online2023)'], label='Umsatz 2023 (Forecast)', color='green', alpha=0.7)
plt.xlabel('Monat')
plt.ylabel('Umsatz in Euro')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()
plt.style.use("Solarize_Light2")

for i, v in enumerate(umsatz_vorhersagen):
    plt.text(i - 0.1, v + 100, str(round(v, 2)), fontsize=10)
plt.show()

print("\n")
print("\u0332".join("      Forecast für das Jahr 2023 "))
blankIndex = [''] * len(df_2023)
df_2023.index = blankIndex
print(df_2023)

print("\n")




# Der Forecast für das Jahr 2023
totalWert3 = df_2023["UmsatzInEuro(Online2023)"].sum()
totalWert3 = round(totalWert3, 2)
print("Der voraussichtliche Umsatz für das Jahr 2023 beträgt: " + str(totalWert3) + " Euro")




# Daten für das Balkendiagramm
jahre = [year2020, year2021, year2022, year2023]
umsatzwerte = [totalWert0, totalWert1, totalWert2, totalWert3]




# Farben für die Balken
farben = ['skyblue', 'lightcoral', 'green', 'black']




# Erstellen des Balkendiagramms
plt.figure(figsize=(8, 6))
plt.bar(jahre, umsatzwerte, color=farben)
plt.xlabel('Jahr')
plt.ylabel('Umsatz in Euro')
plt.xticks(jahre)
plt.title('Jahresumsätze 2021, 2022 und Umsatzvorhersage für 2023')
plt.grid()
plt.style.use("Solarize_Light2")

for i, v in enumerate(umsatzwerte):
    plt.text(jahre[i] - 0.1, v + 100, str(round(v, 2)), color=farben[i], fontsize=10)

plt.show()




#Verwendung von Seaborn
labels= [2020,2021,2022,str(2023)+"(Forecast)"]
value=[totalWert0,totalWert1,totalWert2,totalWert3]
ax=sns.barplot(y=value,x=labels, color='r',hue=labels, palette='bright', saturation=0.9, edgecolor='r',linewidth=5, legend=False)
for i, v in enumerate(value):
    ax.text(i, v + 50, str(v), ha='center', va='bottom', fontsize=12, color='black')
plt.plot(range(len(labels) - 1), value[:-1], marker='o', linestyle='-', markersize=8, color='blue', label='Verlauf')
plt.plot(range(len(labels) ), value[:], marker='o', linestyle='-', markersize=8, color='blue', label='Verlauf')
plt.xlabel("Jahr")
plt.ylabel("Umsatz in Euro")
plt.title("Darstellung der Jahre")
plt.grid()
sns.set_style("darkgrid")
sns.set_palette("pastel")
plt.style.use("Solarize_Light2")



# Anzeigen des Plots

plt.show()

# DataFrame in eine CSV-Datei schreiben
temp_csv_file = 'Umsatzdaten.csv'
df_2023.round(2).to_csv(temp_csv_file, index=False)

# Verbindung zur MySQL-Datenbank erstellen
engine = create_engine('mysql+mysqlconnector://root:Deusen123!hallo@localhost/RT')

# CSV-Datei in die MySQL-Datenbank schreiben
with engine.connect() as connection:
    myd = pd.read_csv(temp_csv_file)
    myd.to_sql(name='umsatzvorhersage', con=connection, if_exists='replace', index=False)
