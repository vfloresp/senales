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

    print('Butterbord Wp =' + str(Wp))
    print("N = "+ str(Nb) )
    print("Wn = "+ str(Wnb) )
    Zb,Pb,Kb = signal.buttap(Nb)
    ab,bb = signal.zpk2tf(Zb,Pb,Kb)
    print("H(s) = ")
    strFunTrans = funTrans([ab,bb])
    print(strFunTrans)
    print("\n")
    wb, hb = freqs(ab, bb)
    plt.semilogx(wb, abs(hb))

    print('Chebychev Wp =' + str(Wp))
    print("N = "+ str(Nc) )
    print("Wn = "+ str(Wnc) )
    Zc,Pc,Kc = signal.buttap(Nc)
    ac,bc = signal.zpk2tf(Zc,Pc,Kc)
    print("H(s) = ")
    strFunTrans = funTrans([ac,bc])
    print(strFunTrans)
    print("\n")
    wc, hc = freqs(ac, bc)  
    plt.semilogx(wc, abs(hc))

    print('Eliptica Wp =' + str(Wp))
    print("N = "+ str(Ne) )
    print("Wn = "+ str(Wne) )
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

calcFiltros(2,14,1,2)
calcFiltros(2,14,1,1.5)
calcFiltros(2,14,1,1.3)




plt.show()