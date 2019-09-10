#Víctor Hugo Flores Pineda 155990
#Python 3

import numpy as np 
import matplotlib.pyplot as plt

t = np.linspace(0,2)
x = np.cos(2*np.pi*t)
y = np.cos(2*np.pi*t)

plt.subplot(521) 
plt.plot(t,x,'r')
plt.plot(t,y,'b')
plt.subplot(522) 
plt.plot(x,y)

y2 = np.cos((2*np.pi*t)+(np.pi/4))

plt.subplot(523) 
plt.plot(t,x,'r')
plt.plot(t,y2,'b')
plt.subplot(524) 
plt.plot(y2,x)

y3 = np.cos((2*np.pi*t)+(np.pi/2))
plt.subplot(525) 
plt.plot(t,x,'r')
plt.plot(t,y3,'b')
plt.subplot(526) 
plt.plot(y3,x)

y4 = np.cos((2*np.pi*t)+(3*np.pi/4))
plt.subplot(527) 
plt.plot(t,x,'r')
plt.plot(t,y4,'b')
plt.subplot(528) 
plt.plot(y4,x)

y5 = np.cos((2*np.pi*t)+np.pi)
plt.subplot(529) 
plt.plot(t,x,'r')
plt.plot(t,y5,'b')
plt.subplot(5,2,10) 
plt.plot(y5,x)


#Diferente frecuencia
t = np.linspace(0,2,200)
x = np.cos(2*np.pi*t)
y6 = np.cos(2*np.pi*t*2)

plt.figure()
plt.subplot(331)
plt.plot(t,x,'b')
plt.plot(t,y6,'r')

plt.subplot(332)
plt.plot(x,y6)

plt.subplot(333)
y7 = np.cos((2*np.pi*t*2)+np.pi/2)
plt.plot(x,y7)

y8 = np.cos(2*np.pi*t*3)
plt.subplot(334)
plt.plot(t,x,'b')
plt.plot(t,y8,'r')

plt.subplot(335)
plt.plot(x,y8)

plt.subplot(336)
y9 = np.cos((2*np.pi*t*3)+np.pi/2)
plt.plot(x,y9)

y10 = np.cos(2*np.pi*t*4)
plt.subplot(337)
plt.plot(t,x,'b')
plt.plot(t,y6,'r')

plt.subplot(338)
plt.plot(x,y10)

plt.subplot(339)
y11 = np.cos((2*np.pi*t*4)+np.pi/2)
plt.plot(x,y11)

plt.show()



