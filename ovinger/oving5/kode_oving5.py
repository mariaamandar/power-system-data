import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Oppgave 1
t = np.linspace(0, 23, 200)

L_0 = 1635 # velger denne verdien for L_0, fordi den er rundt den laveste observerte verdien i datasettet
A = [125, 255, 480, 100] 
my = [0, 10.3, 18, 24]
sigma = [1.4, 1.9, 3.5, 2]

L = np.full_like(t, L_0, dtype=float) # lager array med samme størrelse som t, hvor startverdi er L0

for i in range(len(A)):
    L = L + A[i] * np.exp(-(t-my[i])**2/(2*sigma[i]**2))

plt.figure(1)
plt.plot(t, L)
plt.xlabel('Time')
plt.ylabel('Belastning')
plt.title('Modell for belastning over et døgn')
plt.grid()
#plt.show()
#plt.savefig("ovinger/oving5/belastning_modell.png")

# Oppgave 2
df_orginal = pd.read_csv("ovinger/oving5/consumption_per_group_mba_hour.csv", sep=";", decimal=",") # leser inn den store csv filen
df_orginal["STARTTID"] = pd.to_datetime(df_orginal["STARTTID"], utc=True)
df_orginal = df_orginal.set_index("STARTTID")
df_orginal =df_orginal.tz_convert("Europe/Oslo")

januar_data = df_orginal[(df_orginal["FORBRUKSGRUPPE"] == "Husholdning") & (df_orginal.index.year == 2026) & (df_orginal.index.month == 1)] # henter ut alle verdiene for husholdningsgruppen i januar 2026
januar_data.to_csv("ovinger/oving5/januar_2026_husholdning.csv", sep=";", decimal=",") # lagrer verdiene i en ny csv-fil som kan brukes i git

df = pd.read_csv("ovinger/oving5/januar_2026_husholdning.csv", sep=";", decimal=",") # lesr inn den nye csv filen
df["STARTTID"] = pd.to_datetime(df["STARTTID"], utc=True)
df = df.set_index("STARTTID")
df =df.tz_convert("Europe/Oslo")

df_NO2 = df[(df["PRISOMRÅDE"] == "NO2")] # henter ut verdiene kun for prisområde NO2
dogn_profil = df_NO2.loc["2026-01-03", "VOLUM_KWH"] # velger 2. januar for døgnprofilen, og henter ut verdiene for kolonnen VOLUM_KWH
belastning_MW = dogn_profil / 1000 # konverterer fra kWh til MW, 1 800 000/1 time = 1 800 000 KW = 1 800 MW

#print(belastning_MW)

timer_observert = belastning_MW.index.hour
#print(timer_observert) # sjekker at det er timer fra 0 til 23

plt.figure(2)
plt.plot(timer_observert, belastning_MW, marker="o")
plt.title("Forbruksprofil for 3. januar 2026")
plt.xlabel("Time")
plt.ylabel("Elektrisk belastning (MW)")
plt.grid()
plt.legend(["Forbruk"])
#plt.show()
#plt.savefig("ovinger/oving5/forbruksprofil_3_januar_2026.png")

plt.figure(3)
plt.plot(t, L, label="Modell")
plt.plot(timer_observert, belastning_MW, marker="o", label="Observed")
plt.title("Sammenligning av modell og observert forbruksprofil")
plt.xlabel("Time")
plt.ylabel("Elektrisk belastning (MW)")
plt.grid()
plt.legend(["Modell", "Observed"])
#plt.show()
#plt.savefig("ovinger/oving5/sammenligning_modell_observert.png")