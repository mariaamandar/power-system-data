import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd

# Oppgave 1
t = np.linspace(0, 24, 400)

A = 800
mu = 13
sigma = 3

G = A * np.exp(-(t-mu)**2/(2*sigma**2))

plt.plot(t, G)
plt.title("Gauss-modell")
plt.xlabel("Time")
plt.ylabel("Innstråling")
plt.grid()
plt.show()
#plt.savefig("ovinger/oving6/gauss_modell.png")

# Oppgave 5
df = pd.read_csv("ovinger/oving6/innstraling_monaco.csv")

print(df.head())
