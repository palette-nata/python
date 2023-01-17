# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randrange

k = int(input('Введите натуральную степень k: '))
str = ""

for i in range (k):
    koef = randrange(0,100)
    if koef != 0:
        str = str + f" {koef}*x^{k-i} + "

str=str+f"{randrange(0,100)}"
str.replace("^1 "," ")
with open('TaskPython04.txt', 'w') as data:
        data.write(str)
print(str)