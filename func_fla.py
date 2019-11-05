import numpy as np
import matplotlib.pyplot as plt
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


def zero(func, a, b, w=1000, err=0.01, max_inter=100):

    n=0    
    if func(a, w) * func(b, w) > 0:
        print('Intervalo inválido')
        return None

    while n < max_inter:
        
        if func(a, w) == 0:
            return a

        elif func(b, w) == 0:
            return b

        if n == 0:
            new_ant = b
        new = (((func(a, w) * (a - b)) / (func(b, w) - func(a, w))) + a)
        
        if func(new, w) == 0 or abs((new - new_ant)/new) < err:
            return new
        elif func(a, w) * func(new, w) < 0:
            b = new
        else:
            a = new

        n += 1
    return None


W_domain = np.linspace(0, 4, 1000)

fx = lambda q, w: q*w + 2*w**2 - q*3

zeros = []
for x in W_domain:
    zeros.append(zero(fx, -500, 500, w=x, err=0.01))

plt.scatter(W_domain, zeros)
plt.show()
# print(zeros)