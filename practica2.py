#Víctor Hugo Flores Pineda 155990
#Python 3
import matplotlib.pyplot as plt
import numpy as np

#Ejercicio 1 función exponencial
def exponencial(t):
    """Esta función recibe un arreglo de valores t y grafica
    exp(0.3*t)*sin(2*pi*t) para todos sus valores """
    fexp = np.exp(0.3*t)*np.sin(2*np.pi*t)
    plt.plot(t,fexp)
    plt.title('Función exponencial compleja')

t = np.linspace(-5,5,300)
exponencial(t)

#Ejercicio 2    
plt.figure(2,figsize=(8,6))
x2 = np.linspace(0,30,31)

f1 = 1
y1 = np.cos(x2*f1)
plt.subplot(331)
plt.stem(x2,y1)
plt.ylim(-1.5,1.5)
plt.title('x(n) = cos(n)')

f2 = x2/8
y2 = np.cos(np.pi*f2)
plt.subplot(332)
plt.stem(x2,y2)
plt.ylim(-1.5,1.5)
plt.title('x(n) = cos(pi*n/8)')

f3 = x2/4
y3 = np.cos(np.pi*f3)
plt.subplot(333)
plt.stem(x2,y3)
plt.ylim(-1.5,1.5)
plt.title('x(n) = cos(pi*n/4)')

f4 = x2/2
y4 = np.cos(np.pi*f4)
plt.subplot(334)
plt.stem(x2,y4)
plt.ylim(-1.5,1.5)
plt.title('x(n) = cos(pi*n)')

f5 = x2
y5 = np.cos(np.pi*f5)
plt.subplot(335)
plt.stem(x2,y5)
plt.ylim(-1.5,1.5)
plt.title('x(n) = cos(n)')

f6 = x2/2
y6 = np.cos(3*np.pi*f6)
plt.subplot(336)
plt.stem(x2,y6)
plt.ylim(-1.5,1.5)
plt.title('x(n) = cos(3*pi*n/2)')

f7 = x2/4
y7 = np.cos(7*np.pi*f7)
plt.subplot(337)
plt.stem(x2,y7)
plt.ylim(-1.5,1.5)
plt.title('x(n) = cos(7*pi*n/4)')

f8 = x2/8
y8 = np.cos(15*np.pi*f8)
plt.subplot(338)
plt.stem(x2,y8)
plt.ylim(-1.5,1.5)
plt.title('x(n) = cos(15*pi*n/8)')

f9 = x2
y9 = np.cos(2*np.pi*f9)
plt.subplot(339)
plt.stem(x2,y9)
plt.ylim(-1.5,1.5)
plt.title('x(n) = cos(2*pi*n)')

plt.subplots_adjust(hspace=0.5)

plt.show()



