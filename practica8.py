#Víctor Hugo Flores Pineda 155990
#Rebeca Baños
#Python 3
import numpy as np 
import matplotlib.pyplot as plt
import control
from scipy.fftpack import fft, ifft
from scipy import signal

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
print(y)

#Encontrar la fucnion de transferencia
#Usar signal.tf2zpk para encontrar polos y zeros de cada función
#A
num = [1,-3]
den = [1,4,4]
h1 = signal.TransferFunction(num, den)
[zeros,poles,gain] = signal.tf2zpk(num,den)
print(zeros)
print(poles)
print(gain)

#B
num = [1]
den = [1,4,4]
h2 = signal.TransferFunction(num, den)
[zeros,poles,gain] = signal.tf2zpk(num,den)

#C
num = [1]
den = [1,20,100]
h3 = signal.TransferFunction(num, den)
[zeros,poles,gain] = signal.tf2zpk(num,den)

#D
num = [4]
den = [1,0,1]
h2 = signal.TransferFunction(num, den)
[zeros,poles,gain] = signal.tf2zpk(num,den)

#E
num = [2,2]
den = [1,1,-7,-15]
h2 = signal.TransferFunction(num, den)
[zeros,poles,gain] = signal.tf2zpk(num,den)

#F
num = [3,12]
den = [1,-2,5]
h2 = signal.TransferFunction(num, den)
[zeros,poles,gain] = signal.tf2zpk(num,den)