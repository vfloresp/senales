#Víctor Hugo Flores Pineda 155990
#Rebeca Baños
#Python 3
import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal as sg

N, Wn = sg.buttord(1, 2, 2, 14, True)
print(N)
print(Wn)

N, Wn = sg.buttord(1, 1.5, 2, 14, True)
print(N)
print(Wn)

N, Wn = sg.buttord(1, 1.3, 2, 14, True)
print(N)
print(Wn)

z,p,k = sg.buttap(N)