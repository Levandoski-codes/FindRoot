import numpy as np
import matplotlib.pyplot as plt
from time import sleep
# from fals_meth import zero


EPS0 = 1
WP = 68557
GAMA = 364

epsAu = lambda w: 1 - (WP**2)/(w**2 + GAMA*w*1j)

EPS21 = 2
EPS22 = 2

EPSI = 11.7

WP1 = 179.8
WT1 = 1108
GM1 = 15
s1 = lambda w: (WP1**2)/(WT1**2 - w**2 - GM1*w*1j)

WP2 = 219.7
WT2 = 1104
GM2 = 12.6
s2 = lambda w: (WP2**2)/(WT2**2 - w**2 - GM2*w*1j)

WP3 = 203.4
WT3 = 1098
GM3 = 12.76
s3 = lambda w: (WP3**2)/(WT3**2 - w**2 - GM3*w*1j)

WP4 = 330.8
WT4 = 1092
GM4 = 19.6
s4 = lambda w: (WP4**2)/(WT4**2 - w**2 - GM4*w*1j)

WP5 = 392.4
WT5 = 1086
GM5 = 19
s5 = lambda w: (WP5**2)/(WT5**2 - w**2 - GM5*w*1j)

espio2 = lambda w: EPS21 * (1 + s1(w) + s2(w) + s3(w) + s4(w) + s5(w))


D = 0.1*10**-5
kez = lambda q, w: (espio2(w)*w**2 - (q*10**5)**2)**0.5
kaz = lambda q, w: (1 * w**2 - (q*10**5)**2)**0.5
kauz = lambda q, w: (epsAu(w)*w**2 - (q*10**5)**2)**0.5

f4 = lambda q, w: -kauz(q,w)*D - np.arctan(1j*kauz(q,w)/epsAu(w)*kaz(q,w)) - np.arctan(1j*epsAu(w)*kaz(q,w)/1*kauz(q,w))


def zero(func, a, b, w=0, err=0.01, max_inter=100):
	# Recebe uma funcão como paramentro e os pontos a e b iniciais
    print(func(a, w).real, func(b, w).real)
    if func(a, w).real * func(b, w).real > 0:
        print('Intervalo inválido')
        return None
    n=0
    while n < max_inter:
        
        if func(a, w).real == 0:
            return a

        elif func(b, w).real == 0:
            return b

        if n == 0:
            new_ant = b
        else:
            new_ant = new
        new = (((func(a, w) * (a - b)) / 
            (func(b, w) - func(a, w))) + a)
       
        
        if func(new, w).real == 0 or func(new, w).real < err:
            print(new, w)
            print('Zeroooooo ->',func(new, w).real)
            return new
        elif func(a, w).real * func(new, w).real < 0:
            b = new
        else:
            a = new
        print(func(a, w).real)
        print(func(b, w).real)
        print(func(new, w).real)

        n += 1
    print(f'N: {n}')
    return None

W_domain = np.linspace(-1000, 1700, 100)

fx = lambda q, w: q*w + 2*w**2 - q**3

zeros = []

for w in W_domain:
# Calcula os zeros e joga na lista
	# print(f4(0, w).real)
    result = zero(f4, 700, 1000, w=float(w), err=0.1)
    zeros.append(result)

plt.scatter(W_domain, zeros)
plt.xlabel('x')
plt.ylabel('y')
# plt.show()
# print(zeros)
