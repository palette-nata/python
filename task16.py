# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math
N = int(input('введите натуральное число N: '))
def primeFactors(n):
    while n % 2 == 0:
        print (2, end=" ")
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            print (i, end =" ")
            n = n / i
    if n > 2:
        print (n, end=" ")

primeFactors(N)