
from function import func

def zero(a, b, err=0.01, max_inter=100):
    n = 0
    
    if func(a) * func(b) > 0:
        print('Intervalo inválido')
        return None

    while n < max_inter:
        if n == 0:
            new_ant = b
        new = (a+b)/2

        if func(new) == 0 or abs((new - new_ant)/new) < err:
            return new
        elif func(a) * func(new) < 0:
            b = new
        else:
            a = new

        n += 1

    print(f'Excedeu o número de interações máximo. ({max_inter} {n})')
    return None
 


if __name__ == "__main__":

    print(zero(a=1, b=2, err=0.0001))