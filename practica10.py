import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import signal
from scipy.signal import freqs

#Función para escribir las funciones de transferencia 
def funTrans(pol):
    strPol = ""
    grado = ["","x", "x^2","x^3", "x^4", "x^5", "x^6","x^7", "x^8"]
    num = pol[0]
    den = pol[1]
    i = 0
    for i in range (0,len(num)):
        strPol = strPol + str(num[i]) + str(grado[i]) + " +"
    strPol = strPol[:-2] + "/"
    i = 0
    for i in range (0,len(den)):
        strPol = strPol + str(den[i]) + str(grado[i]) + " +"
    return strPol[:-2]

#Función que recibe los paremetros de un filtro
# Calcula sus aproxiamciones Butterbord, Chebychev y Eliptica
# Gráfica una comparación de las respuestas de los filtros resultantes
def calcFiltros(A1,A2,Wc,Wp):
    plt.figure()
    Nb, Wnb = signal.buttord(Wp,Wc,A1,A2,True)  
    Nc, Wnc = signal.cheb1ord(Wp,Wc,A1,A2,True)
    Ne, Wne = signal.ellipord(Wp,Wc,A1,A2,True)

    Zb,Pb,Kb = signal.buttap(Nb)
    ab,bb = signal.zpk2tf(Zb,Pb,Kb)
    print("H(s) = ")
    strFunTrans = funTrans([ab,bb])
    print(strFunTrans)
    print("\n")
    wb, hb = freqs(ab, bb)
    plt.semilogx(wb, abs(hb))  

    Zc,Pc,Kc = signal.buttap(Nc)
    ac,bc = signal.zpk2tf(Zc,Pc,Kc)
    print("H(s) = ")
    strFunTrans = funTrans([ac,bc])
    print(strFunTrans)
    print("\n")
    wc, hc = freqs(ac, bc)  
    plt.semilogx(wc, abs(hc))

    Ze,Pe,Ke = signal.buttap(Ne)
    ae,be = signal.zpk2tf(Ze,Pe,Ke)
    print("H(s) = ")
    strFunTrans = funTrans([ae,be])
    print(strFunTrans)
    print("\n")  
    we, he = freqs(ae, be)
    plt.semilogx(we, abs(he))

    plt.xlabel('Frequency')
    plt.ylabel('Amplitude response')
    plt.grid()

#Inciso 1
#Butterbord
#Wp = 2
N, Wn = signal.buttord(2,1,2,14,True)
print('Butterbord Wp = 2')
print("N = "+ str(N) )
print("Wn = "+ str(Wn) )
#Inciso 2
Z,P,K = signal.buttap(N)
a,b = signal.zpk2tf(Z,P,K)
print("H(s) = ")
strFunTrans = funTrans([a,b])
print(strFunTrans)
print("\n")
w, h = freqs(a, b)
plt.semilogx(w, abs(h))
plt.xlabel('Frequency')
plt.ylabel('Amplitude response')
plt.grid()


#Wp = 1.5
[N, Wn] = signal.buttord(1.5,1,2,14,True)
print('Butterbord Wp = 1.5')
print("N = "+ str(N) )
print("Wn = "+ str(Wn) )
#Inciso 2
Z,P,K = signal.buttap(N)
a,b = signal.zpk2tf(Z,P,K)
print("H(s) = ")
strFunTrans = funTrans([a,b])
print(strFunTrans)
print("\n")

#Wp = 1.3
[N, Wn] = signal.buttord(1.3,1,2,14,True)
print('Butterbord Wp = 1.3')
print("N = "+ str(N) )
print("Wn = "+ str(Wn) )
#Inciso 2
Z,P,K = signal.buttap(N)
a,b = signal.zpk2tf(Z,P,K)
print("H(s) = ")
strFunTrans = funTrans([a,b])
print(strFunTrans)
print("\n")


#Chebychev
#Wp = 2
[N, Wn] = signal.cheb1ord(2,1,2,14,True)
print('Chebychev Wp = 2')
print("N = "+ str(N) )
print("Wn = "+ str(Wn) )
#Inciso 2
Z,P,K = signal.buttap(N)
a,b = signal.zpk2tf(Z,P,K)
print("H(s) = ")
strFunTrans = funTrans([a,b])
print(strFunTrans)
print("\n")

#Wp = 1.5
[N, Wn] = signal.cheb1ord(1.5,1,2,14,True)
print('Chebychev Wp = 1.5')
print("N = "+ str(N) )
print("Wn = "+ str(Wn) )
#Inciso 2
Z,P,K = signal.buttap(N)
a,b = signal.zpk2tf(Z,P,K)
print("H(s) = ")
strFunTrans = funTrans([a,b])
print(strFunTrans)
print("\n")

#Wp = 1.3
[N, Wn] = signal.cheb1ord(1.3,1,2,14,True)
print('Chebychev Wp = 1.3')
print("N = "+ str(N) )
print("Wn = "+ str(Wn) )
#Inciso 2
Z,P,K = signal.buttap(N)
a,b = signal.zpk2tf(Z,P,K)
print("H(s) = ")
strFunTrans = funTrans([a,b])
print(strFunTrans)
print("\n")


#Eliptica
#Wp = 2
[N, Wn] = signal.ellipord(2,1,2,14,True)
print('Eliptica Wp = 2')
print("N = "+ str(N) )
print("Wn = "+ str(Wn) )
#Inciso 2
Z,P,K = signal.buttap(N)
a,b = signal.zpk2tf(Z,P,K)
print("H(s) = ")
strFunTrans = funTrans([a,b])
print(strFunTrans)
print("\n")

#Wp = 1.5
[N, Wn] = signal.ellipord(1.5,1,2,14,True)
print('Eliptica Wp = 1.5')
print("N = "+ str(N) )
print("Wn = "+ str(Wn) )
#Inciso 2
Z,P,K = signal.buttap(N)
a,b = signal.zpk2tf(Z,P,K)
print("H(s) = ")
strFunTrans = funTrans([a,b])
print(strFunTrans)
print("\n")

#Wp = 1.3
[N, Wn] = signal.ellipord(1.3,1,2,14,True)
print('Eliptica Wp = 1.3')
print("N = "+ str(N) )
print("Wn = "+ str(Wn) )
#Inciso 2
Z,P,K = signal.buttap(N)
a,b = signal.zpk2tf(Z,P,K)
print("H(s) = ")
strFunTrans = funTrans([a,b])
print(strFunTrans)
print("\n")


plt.show()