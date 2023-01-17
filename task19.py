#Даны два файла, 
# в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import collections

def add_value(key, value):
    val = dict.get(key)
    if val != None:
            dict[key] = value + val
    else:
        dict[key]=value

def add_elements(lst):
    for el in lst:
        if "x" in el:
            q = el.split("*x")
            if "^" in q[1]:
                add_value(int(q[1].replace("^","")),int(q[0]))
            else:
                add_value(1,int(q[0]))
        else:
            add_value(0,int(el)) 

def print_prepare(koeff,degree):
    if degree == 0:
        return f"{koeff}"
    elif degree == 1:
        return f"{koeff}*x"
    else:
        return f"{koeff}*x^{degree}"


#str1 = "23*x^4 + 12*x^3 + 4*x + 3"
#str2 = "3*x^3+6*x^2+5*x+12"

with open('file1.txt') as f:
    str1 = f.readline()    

with open('file2.txt') as f:
    str2 = f.readline()    

str1n=str1.replace(" ","")
str2n=str2.replace(" ","")

dict = collections.OrderedDict()
sum_last_number_x0 = 0

lst1 = str1n.split("+")
lst2 = str2n.split("+")

add_elements(lst1)
add_elements(lst2)

od = collections.OrderedDict(sorted(dict.items()))
result = ""
for k, v in od.items(): result = print_prepare(v, k) + "+" + result
print (result[:-1])

