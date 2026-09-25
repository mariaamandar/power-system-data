import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

# Oppgave 1
t = np.linspace(0, 24, 400)

A = 800
mu = 13.5
sigma = 4

G = A * np.exp(-(t-mu)**2/(2*sigma**2))

plt.figure(1)
plt.plot(t, G)
plt.title("Gauss-modell")
plt.xlabel("Time")
plt.ylabel("Innstråling")
plt.grid()
#plt.show()
#plt.savefig("ovinger/oving6/gauss_modell.png")

# Oppgave 5
df = pd.read_csv("ovinger/oving6/innstraaling_hjemme.csv", skiprows=8, nrows=8760) # hopper over de første 8 radene i csv-filen, som inneholder metadata
df["time"] = pd.to_datetime(df["time"], format = "%Y%m%d:%H%M", utc=True) # konverterer kolonnen "time" til datetime-format
df = df.set_index("time")
df = df.tz_convert("Europe/Oslo")
print(df.head())

df["G(i)"] = df["Gb(i)"] + df["Gr(i)"] + df["Gd(i)"] # global innstråling 
print(df["G(i)"].head())

innstraaling = df.loc["2023-07-08", "G(i)"]

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(innstraaling.index.hour, innstraaling)
ax.set_title("Global innstråling 8. juli 2023")
ax.set_xlabel("Tid")
ax.set_ylabel(r"Innstråling [W/m$^2$]")
ax.grid(True)

#plt.show()
#plt.savefig("ovinger/oving6/innstraaling_8_juli.png")

# Oppgave 6
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, G, label="Gauss-modell")
ax.plot(innstraaling.index.hour, innstraaling.values, "o-", label="PVGIS-data")
ax.set_title("Gauss-modell og PVGIS-data, 8. juli 2023")
ax.set_xlabel("Tid [timer]")
ax.set_ylabel(r"Innstråling [W/m$^2$]")
ax.legend()
ax.grid(True)

plt.show()
#plt.savefig("ovinger/oving6/Gauss_modell_og_PVGIS_data_endret")
