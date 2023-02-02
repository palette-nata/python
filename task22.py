# Создайте программу для игры в ""Крестики-нолики"".

endGame = False
win = ({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7})
board = {1,2,3,4,5,6,7,8,9}

playerX = set()
playerO = set() 
player = playerX

def Game():
    endGame = False
    draw()
    while  endGame == False:
        player = play()
        endGame = check_win()
        draw()
       
def check_win():
    for i in win:
        if i.issubset(playerO):
            print("Победа О")
            return True
        elif i.issubset(playerX):
            print("Победа X")
            return True
        elif not board:
            print("Ничья - победила дружба!")
            return True
    return False

def draw(): 
    for i in range(1,10):
        symb=str(i)
        if i in playerX:
            symb="X"
        elif i in playerO:
            symb="O"
        print(symb) if i in {3,6,9} else print( symb + " ", end="")

def play():
    global player
    number = 0
    while number not in  board:
        number = int(input("Ваш ход: "))
    player.add(number)
    board.remove(number)
    if player == playerX:
        player = playerO
    else:
        player = playerX
 
Game()