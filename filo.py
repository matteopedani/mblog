
import math

#Dati
P = 350 # kW
f = 11 # s
h = 10 # m

#Costanti
mu_0 = 4*math.pi*10**-7 # Permeabilità magnetica

#Calcolo
A = P/(mu_0*f*h) # Area del generatore

#Dimensione del filo
d = math.sqrt(4*A/math.pi) # Diametro del filo

#Numero di spire
N = math.sqrt(A/(2*math.pi*d))

#Numero di avvolgimenti
n = math.pi*d*N

#Risultati
print("Dimensione del filo:", round(d,4), "m")
print("Numero di spire:", round(N,4))
print("Numero di avvolgimenti:", round(n,4))
