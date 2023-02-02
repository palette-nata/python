# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?


import random


def run_play(n = 2021, m = 28):
    print(f"Всего {n} конфет, можно взять от 1 до {m} конфет, кто берёт последние, тот выигрывает.")
    play = True
    level = 1
    opponent = int(input('Выберите вариант игры 1-с человеком, 2-с компьютером: '))
    if opponent == 2:
        level = int(input("Введите сложность уровня 1- лёгкий 10-сложный: "))
    player = 0 # 0-игрок 1, 1-второй игрок, 2-компьютер
    x = m+1
    while play:
        print(f"Число равно {n}")
        num = 0 
        mx = n if n<m else m
        if player<2:
            while num < 1 or num > n or num > m: 
                num = int(input(f"Игрок {player+1} - введите число больше 0 и не больше {mx}: "))
        elif random.randint(1,10)>level: # random
            num = random.randint(1,mx)
            print(f"Компьютер сделал случайный ход выбрав число: {num}")
        else:
            x = n % (m+1)
            num =  x if x>0 else random.randint(1,mx)
            print(f"Компьютер сделал ход выбрав число: {num}")
        
        n -= num
        if n == 0:
            winner = f"игрок {player+1}" if player<2 else "компьютер"
            print(f"Победил {winner}")
            play = False
        else:
            player = abs(player - opponent)

run_play()