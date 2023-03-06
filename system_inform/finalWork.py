# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# производная - 12*x**4·np.sin(x)·np.cos(np.cos(x)) - 48*x**3*np.sin(np.cos(x)) - 54*x*2 + 10*x + 10
# Определить корни+
# Найти интервалы, на которых функция возрастает+
# Найти интервалы, на которых функция убывает+
# Построить график +
# Вычислить вершину +
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

#функция имеет бесконечное множество корней - но мы можем найти корни на нужном нам промежутке

import numpy as np
import matplotlib.pyplot as plt

limit1 = -10
limit2 = 10
step = 0.001

a, b, c, d, e = -12, -18, 5, 10, -30 

x = np.arange(limit1, limit2, step)

def func(x) -> tuple:
       return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e

roots1 = []

# приравнять к нулю сложно тк числа получаются float поэтому 
# мы смотрим где функция меняет знак и ищем приблизительное значение
def take_roots(a, b, c, d, e):
    roots1 = []
    go_up_down = False
    for x_range in x:
        if go_up_down:
            if func(x_range) >= 0:
                root = np.round(x_range)
                roots1.append(root)
                go_up_down = False
  
        else:
            if func(x_range) <= 0:
                root = np.round(x_range)
                roots1.append(root)
                go_up_down = True

    return roots1
   
roots1 = take_roots(a, b, c, d, e)

zero1 = []

roots1[0] = -7.7
print(roots1)

def roots_list():
    zero =[]
    for i in range(len(roots1)):
        zero.append(0)
    return zero
zero1 = roots_list()
print(zero1)

extremums1 = []
extremums2 = []

#производная - пока что только для нашей функции. Экстремумы там, где производная равна нулю.

def derivative(x) -> tuple:
    return 12*x**4*np.sin(x)*np.cos(np.cos(x)) - 48*x**3*np.sin(np.cos(x)) - 54*x*2 + 10*x + 10

def extremum():
    extremums = []
    extr = 0
    go_up_down = False
    for x_range in x:
        if go_up_down:
            if derivative(x_range) >= 0:
                extr = np.round(x_range)
                extremums.append(extr)
                go_up_down = False  
        else:
            if derivative(x_range) <= 0:
                extr = np.round(x_range)
                extremums.append(extr)
                go_up_down = True

    return extremums
   
extremums1 = extremum()
print(extremums1)

#создаем список значений у экстремумов
def x_y_extremum(a, b, c, d, e):
    for i in extremums1:
        temp = np.round(func(i))
        extremums2.append(temp)
    return extremums2
extremums2 = x_y_extremum(a, b, c, d, e)
print(extremums2)

x_down_list = []
x_up_list = []
x_neg_list = []
for i in range(0, len(extremums1)-1, 2):
    x_down = np.arange(extremums1[i], extremums1[i+1], step)
    x_down_list.append(x_down)
for i in range(1, len(extremums1), 2):
    x_up = np.arange(extremums1[i], extremums1[i+1], step)
    x_up_list.append(x_up)
for i in range(0,len(roots1)-1, 2):
    x_neg = np.arange(roots1[i], roots1[i+1], step)
    x_neg_list.append(x_neg)

print(x_neg_list)


# plt.rcParams['lines.linestyle'] = '--'
# plt.plot(x_down, func(x_down), 'b')
# plt.plot(x_down1, func(x_down1), 'b')
# plt.plot(x_down2, func(x_down2), 'b')
# plt.plot(x_down3, func(x_down3), 'b')
# plt.rcParams['lines.linestyle'] = '-.'
# plt.plot(x_up, func(x_up), 'r')
# plt.plot(x_up1, func(x_up1), 'r')
# plt.plot(x_up2, func(x_up2), 'r')
# plt.plot(x_up3, func(x_up3), 'r')
# label1 = "Возрастание"
# label2 = "Убывание"
# label3 = "Меньше нуля"

plt.rcParams['lines.linestyle'] = '--'

for i in range(0, len(x_down_list)):
    plt.plot(x_down_list[i], func(x_down_list[i]), 'b')
           
plt.rcParams['lines.linestyle'] = '-.'
for i in range(0, len(x_up_list)):

    plt.plot(x_up_list[i], func(x_up_list[i]), 'r')
    
plt.rcParams['lines.linestyle'] = '--'
for i in range(0, len(x_neg_list)):
    plt.plot(x_neg_list[i], func(x_neg_list[i]), 'c')

plt.plot(roots1, zero1, 'yo', label ="Корни")
plt.plot(extremums1, extremums2, 'gx', label ="Экстремумы")
plt.legend()
plt.grid()
plt.show()