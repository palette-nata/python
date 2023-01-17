#Вычислить число пи c заданной точностью d
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
def calc_pi(eps):
    s=0
    d=1
    a=4/d
    sgn=1
    while a>eps:
        a=4/d
        s=s+sgn*a
        sgn=-sgn
        d=d+2
    return s

i = int(input('Введите число знаков числа пи: '))
print(f'pi= {round(calc_pi(0.1**i), i+1)}'[:-1])
