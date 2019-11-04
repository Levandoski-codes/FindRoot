import numpy as np
from function import func

def zero(a, b, err=0.01, max_inter=100):
    
    n = 0
    if func(a) * func(b) > 0:
        print('Intervalo inválido')
        return None

    while n < max_inter:
        

        if func(a) == 0:
            return a

        elif func(b) == 0:
            return b

        if n == 0:
            new_ant = b
        new = (((func(a) * (a - b)) / (func(b) - func(a))) + a)
        
        if func(new) == 0 or abs((new - new_ant)/new) < err:
            return new
        elif func(a) * func(new) < 0:
            b = new
        else:
            a = new

        n += 1

if __name__ == "__main__":
    
     print(zero(a=1, b=2, err=0.0001))