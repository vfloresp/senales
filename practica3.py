#Víctor Hugo Flores Pineda
#Práctica 3
#python 3
import numpy as np
import matplotlib.pyplot as plt 

#Ejercicio 1
x = [0,2,4,-1]
h = [1,1,1,1]
y = np.convolve(x,h)
plt.stem(np.linspace(0,6,7),y)


#Ejercicio 2 propiedad conmutativa
plt.figure()
n = np.linspace(0,20,21)
x = np.cos((np.pi/10)*n)
plt.subplot(221)
plt.stem(n,x)
h = np.random.rand(1,11)
plt.subplot(222)
plt.stem(np.linspace(0,10,11),h[0])
y1 = np.convolve(x,h[0])

plt.subplot(223)
plt.stem(np.linspace(0,30,31),y1)

y2 = np.convolve(h[0],x)
plt.subplot(224)
plt.stem(np.linspace(0,30,31),y2)

#Ejercicio 3 propiedad distributiva
plt.figure()
h1 = h[0]
h2 = -1*np.random.rand(1,11)[0]
x2 = np.linspace(0,10,11)

plt.subplot(331)
plt.stem(n,x)
plt.subplot(332)
plt.stem(x2,h1)
plt.subplot(333)
plt.stem(x2,h2)

h12 = h1 + h2
plt.subplot(334)
plt.stem(x2,h12)

x3 = np.linspace(0,30,31)
y1 = np.convolve(x,h1)
plt.subplot(335)
plt.stem(x3,y1)

y2 = np.convolve(x,h2)
plt.subplot(336)
plt.stem(x3,y2)

y3 = np.convolve(x,h1+h2)
plt.subplot(337)
plt.stem(x3,y3)

y4 = np.convolve(x,h1)+np.convolve(x,h2)
plt.subplot(338)
plt.stem(x3,y4)

#Ejercicio 4 propiedad asociativa
plt.figure()
plt.subplot(331)
plt.stem(n,x)
plt.subplot(332)
plt.stem(x2,h1)
plt.subplot(333)
plt.stem(x2,h2)

y1 = np.convolve(x,h1)
plt.subplot(334)
plt.stem(x3,y1)

y2 = np.convolve(h2,h1)
x3 = np.linspace(0,20,21)
plt.subplot(335)
plt.stem(x3,y2)

x4 = np.linspace(0,40,41)

y3 = np.convolve(y1,h2)
plt.subplot(337)
plt.stem(x4,y3)

y4 = np.convolve(x,y2)
plt.subplot(338)
plt.stem(x4,y4)



plt.show()

