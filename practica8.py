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
h1 = control.TransferFunction(num,den)
[zeros,poles,gain] = signal.tf2zpk(num,den)
print("h1")
print("zeros")
print(zeros)
print("polos ")
print(poles)
print("\n")
control.pzmap(h1, Plot=True, grid=False, title='H1')
[t,y] = signal.impulse( ([1,-3],[1,4,4]) )
plt.plot(t, y)
[t,y] = signal.step( ([1,-3],[1,4,4]) )
plt.plot(t, y)

#B
num = [1]
den = [1,4,4]
h2 = control.TransferFunction(num, den)
[zeros,poles,gain] = signal.tf2zpk(num,den)
print("h2")
print("zeros")
print(zeros)
print("polos ")
print(poles)
print("\n")
control.pzmap(h2, Plot=True, grid=False, title='H2')
[t,y] = signal.impulse( ([1],[1,4,4]) )
plt.plot(t, y)
[t,y] = signal.step( ([1],[1,4,4]) )
plt.plot(t, y)


#C
num = [1]
den = [1,20,100]
h3 = control.TransferFunction(num, den)
[zeros,poles,gain] = signal.tf2zpk(num,den)
print("h3")
print("zeros")
print(zeros)
print("polos ")
print(poles)
print("\n")
control.pzmap(h3, Plot=True, grid=False, title='H3')
[t,y] = signal.impulse( ([1],[1,20,100]) )
plt.plot(t, y)
[t,y] = signal.step( ([1],[1,20,100]) )
plt.plot(t, y)


#D
num = [4]
den = [1,0,1]
h4 = control.TransferFunction(num, den)
[zeros,poles,gain] = signal.tf2zpk(num,den)
print("h4")
print("zeros")
print(zeros)
print("polos ")
print(poles)
print("\n")
control.pzmap(h4, Plot=True, grid=False, title='H4')
[t,y] = signal.impulse( ([4],[1,0,1]) )
plt.plot(t, y)
[t,y] = signal.step( ([4],[1,0,1]) )
plt.plot(t, y)


#E
num = [2,2]
den = [1,1,-7,-15]
h5 = control.TransferFunction(num, den)
[zeros,poles,gain] = signal.tf2zpk(num,den)
print("h5")
print("zeros")
print(zeros)
print("polos ")
print(poles)
print("\n")
control.pzmap(h5, Plot=True, grid=False, title='H5')
[t,y] = signal.impulse( ([2,2],[1,1,-7,-15]) )
plt.plot(t, y)
[t,y] = signal.step( ([2,2],[1,1,-7,-15]) )
plt.plot(t, y)


#F
num = [3,12]
den = [1,-2,5]
h6 = control.TransferFunction(num, den)
[zeros,poles,gain] = signal.tf2zpk(num,den)
print("h6")
print("zeros")
print(zeros)
print("polos ")
print(poles)
print("\n")
control.pzmap(h6, Plot=True, grid=False, title='H6')
[t,y] = signal.impulse( ([3,12],[1,-2,5]) )
plt.plot(t, y)
[t,y] = signal.step( ([3,12],[1,-2,5]) )
plt.plot(t, y)

plt.show()