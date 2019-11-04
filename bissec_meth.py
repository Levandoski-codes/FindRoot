
def function(x):
    f = float(x**3 - x - 2)
    return f

def zero(a, b, err=0.01, max_inter=100):
    n = 0
    
    if function(a) * function(b) > 0:
        print('Intervalo errado')
        return None

    while n < max_inter:
        med_ant = med
        med = (a+b)/2

        if function(med) == 0 or abs((med - med_ant)/med) < err:
            return med
        elif function(a) * function(med) < 0:
            b = med
        else:
            a = med

        n += 1

    print(f'Excedeu o número de interações máximo. ({max_inter} {n})')
    return None
 


if __name__ == "__main__":

    print(zero(a=1, b=2, err=0.0001))