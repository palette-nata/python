# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

from random import randint

def multiplyList(myList):
    result = 1
    for x in myList:
        result *= x
    return result

def mixinList(myList):
    for i in range(100):
        a = randint(0,len(myList)-1)
        b = randint(0,len(myList)-1)
        tmp = myList[a]
        myList[a] = myList[b]
        myList[b] = tmp
    
n = int(input('Введите число: ')) 

lst = [randint(-n, n) for i in range(n)]
print(f'Элементы списка: {lst}')

mixinList(lst)


data = [ lst[int(line.strip())] for line in open('PythonWork/file.txt','r')]

print(f'Элементы списка после перемешивания: {lst}')
print(f'Перемножаемые элементы : {data}\nПроизведение элементов на указанных позициях: {multiplyList(data)}')