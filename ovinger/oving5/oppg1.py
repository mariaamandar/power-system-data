import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 23, 200)

L_0 = 12000
A = [15000, 30000]
my = [8, 16]
sigma = [3, 1]

L = np.full_like(t, L_0, dtype=float) # lager array med samme størrelse som t, hvor startverdi er L0

for i in range(len(A)):
    L = L + A[i] * np.exp(-(t-my[i])**2/(2*sigma[i]**2))


plt.plot(t, L)
plt.xlabel('Time')
plt.ylabel('Belastning')
plt.title('Modell for belastning over et døgn')
plt.grid()
#plt.show()
plt.savefig("ovinger/oving5/belastning_eks_6.png")
