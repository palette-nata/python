# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
number = int(input('Введите целое положительное число: '))
print("{0:b}".format(number))