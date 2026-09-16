import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ovinger/oving4/load_data.csv")
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"],format="%d.%m.%Y %H:%M:%S %z", utc=True) # %z representerer tidssoneforskyvningen
df = df.set_index("Time(Local)")
df =df.tz_convert("Europe/Oslo")

df["Production"] = df["Production"].str.replace(",", ".").astype(float)
df["Consumption"] = df["Consumption"].str.replace(",", ".").astype(float)

print(df.head())

print(df.index[0])

#print(df.loc["2026-01-01 03:00"])

lastprofil = df.loc["2026-03-01", "Consumption"]
#print(lastprofil)

lastprofil.plot()
plt.title("Consumption profile for March 1, 2026")
plt.xlabel("Time")
plt.ylabel("Consumption")
plt.grid()
plt.legend(["Consumption"])
#plt.show()
plt.savefig("ovinger/oving4/consumption_profile_march_2026.png")

df["Netto"] = (df["Production"]- df["Consumption"])

maks_prod = df["Production"].max()
min_prod = df["Production"].min()
gjennomsnitt_prod = df["Production"].mean()
print("Maks produksjon:", maks_prod)
print("Min produksjon:", min_prod)
print("Gjennomsnitt produksjon:", gjennomsnitt_prod)