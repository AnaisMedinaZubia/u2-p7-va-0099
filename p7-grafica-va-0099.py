# Anais Medina NC 0099 fecha 28 de octubre 2026
import numpy as pd
import matplotlib.pyplot as plt


no_listas = [1,2,3,16,40]
califa_ml = [20,30,80,67,100]
califa_va = [70,90,60,90,100]

plt.plot(no_listas, califa_ml, label='califa ML')
plt.plot(no_listas, califa_va, label='califa VA')

plt.title("Calificaciones materias 0099")
plt.xlabel("numero de lista")
plt.ylabel("Calificacion")
plt.legend()
plt.show()

print("Anais Medina NC 0099")