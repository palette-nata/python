# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предиката.
# ¬ НЕ - логическое отрицание   NOT
# ⋁ ИЛИ - логическое сложение   OR
# ⋀ И - логическое умножение    AND
#
# X Y Z
# 0 0 0     1
# 0 0 1     2
# 0 1 0     3
# 0 1 1     4
# 1 0 0     5
# 1 0 1     6
# 1 1 0     7
# 1 1 1     8
#

def compare(x,y,z):
    return (not(x or y or z)) == ((not x) and (not y) and (not z))

x = False
y = False
z = False
r1 = compare(x,y,z) # 000

x = False
y = False
z = True
r2 = compare(x,y,z) # 001

x = False
y = True
z = False
r3 = compare(x,y,z) # 010

x = False
y = True
z = True
r4 = compare(x,y,z) # 011

x = True
y = False
z = False
r5 = compare(x,y,z) # 100

x = True
y = False
z = True
r6 = compare(x,y,z) # 101

x = True
y = True
z = False
r7 = compare(x,y,z) # 110

x = True
y = True
z = True
r8 = compare(x,y,z) # 111


print(f"проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предиката завершена с результатом: {r1 and r2 and r3 and r4 and r5 and r6 and r7 and r8}")
