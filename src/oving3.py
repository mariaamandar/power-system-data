import pandas as pd
import matplotlib.pyplot as plt

# oppgave 1
df = pd.read_csv("load/forbruk_2025.csv", parse_dates=["Time"]) # Leser inn filen
df.head() # gir de første 5 radene i filen
print(df.head()) # printer for å sjekke

df["Time"] = pd.to_datetime(df["Time"],dayfirst=True,utc=True) # gjøre det om til datetime med UTC 
df = df.set_index("Time") # sette "Time" som index
df = df.tz_convert("Europe/Oslo")

# beregne månedlig gjennomsnitt, oppgave 2
gjennomsnitt = df["Actual Load"].resample('ME').mean() # regner for load, resampler for hver måned, og mean() finner gjennomsnittet
print(gjennomsnitt) # printer for å sjekke

gjennomsnitt.to_csv("results/manedlig_last_2025.csv") # lagrer filen som csv

gjennomsnitt.plot(y="gjennomsnitt", figsize=(10, 5))
plt.title("Månedlig gjennomsnittlig last for 2025")
plt.xlabel("Tid")
plt.ylabel("Gjennomsnittlig last")
plt.grid(True)
plt.legend(["Gjennomsnittlig last"])

plt.savefig("results/manedlig_last_2025.png")

hoyest_last = df["Actual Load"].resample('ME').max()
print(hoyest_last)

lavest_last = df["Actual Load"].resample('ME').min()
print(lavest_last)

standardavvik = df["Actual Load"].resample('ME').std()
print(standardavvik)

statistikk = pd.concat([hoyest_last, lavest_last, standardavvik], axis=1, keys=["Hoyeste last", "Laveste last", "Standardavvik"]) # axis=1 for å få de bortover og ikke nedover
statistikk.to_csv("results/manedlig_last_statistikk_2025.csv")
