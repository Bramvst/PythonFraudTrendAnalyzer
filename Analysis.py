#Observatie1: Fraudetransacties hebben gemiddeld hogere bedragen ( 122 vs 88) 
#Oberservatie2: De maximale bedragen van fraude liggen veel lager dan niet fraude wat kan betekenen dat hoe hoger de bedragen, te meer kans dat de transactie legitiem is (2125 vs 25691) 
#Observatie3: De meeste frauduleuze transacties vallen onder de €105 (Q3)

print("Fraud Analyzer project is running! 🚀")

#Pandas importeren om een dataframe te kunnen maken
import pandas as pd

#Dataframe variabele maken en het bestand inlezen
df = pd.read_csv("Data/creditcard.csv")

#Print de 5 bovenste rijen
print(df.head())
#Print de informatie over de hele dataset
print(df.info())
#Print de basis statistieken van de dataset
print(df.describe())

#Bepalen hoeveel transacties fraude (class = 1) zijn
aantal_frauduleuze_transacties = df["Class"].value_counts()
#(aantal_frauduleuze_transacties)
Aantal_fraude = aantal_frauduleuze_transacties[1]
Aantal_Niet_Fraude = aantal_frauduleuze_transacties[0]
Percentage_Fraude = Aantal_fraude / (Aantal_fraude + Aantal_Niet_Fraude)
print(f" De dataset is {round(Percentage_Fraude*100,2)}% fraud cases --> zwaar ongebalanceerd!")

fraud_df = df[df["Class"]==1]
normal_df = df[df["Class"]==0]

print(fraud_df.describe())
print(normal_df.describe())

