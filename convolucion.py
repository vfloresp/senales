#Tarea programa convoluciones
#Víctor Hugo Flores
#Python 3
import numpy as np
import matplotlib.pyplot as plt

def convolucion(x1,x2,title):
    n1 = len(x1)
    n2 = len(x2)
    if n1>n2:
        n = n1
    else:
        n = n2
    y = np.zeros(n)
    for i in range(n):
        val = 0
        for j in range(n):
            if (i-j)>=0 and (i-j)<len(x2) and (j)<len(x1):
                val = val + x1[j]*x2[i-j]
        y[i] = val
    xAxis = np.linspace(0,n-1,n)
    plt.figure()
    plt.stem(xAxis,y)
    plt.title(title)
    return y

x1 = np.append(np.zeros(50),[np.ones(50),np.zeros(50)])
plt.figure()
plt.stem(np.linspace(0,149,150),x1)
plt.title("Función x1")

x2 = [0.25,0.25,0.25,0.25]
plt.figure()
plt.stem([0,1,2,3],x2)
plt.title("Función x2")

x3 = [0.05,0.25,0.4,0.25,0.05]
plt.figure()
plt.stem([0,1,2,3,4],x3)
plt.title("Función x3")

x4 = [1,0,-1]
plt.figure()
plt.stem([0,1,2],x4)
plt.title("Función x4")


#inciso 1
y1 = convolucion(x1,x2,"Convolución x1 con x2")
print(y1)

#inciso 2
y2 = convolucion(x1,x3,"Convolución x1 con x3")
print(y2)

#inciso 3
y3 = convolucion(x1,x4,"Convolución x1 con x4")
print(y3)

#inciso 4
y4 = convolucion(x3,x4, "Convolución x3 con x4")
y5 = convolucion(x1,y4, "Convolución x1 con resultado x3*x4")
print(y5)

#inciso 5
y6 = convolucion(x1,x1, "Convolución x1 con x1")
print(y6)

plt.show()