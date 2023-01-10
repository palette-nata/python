# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


lst = [1.1, 1.2, 3.1, 5, 10.01]

print(f'Элементы входного списка: {lst}')
index =0
min = max = lst[0] - round(lst[0])

for el in lst:
    tmp = lst[index] - round(lst[index])
    if min  > tmp:
        min = tmp
    if max < tmp:
        max = tmp
    index+=1

print(f'max-min: {max-min}')