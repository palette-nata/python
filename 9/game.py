# Создайте программу для игры в ""Крестики-нолики"".
import random

class XOGame:
    win = ({1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7})

    def start_new_game(self):
        self.playerX = {11}
        self.playerO = {10}#set()
        self.player = self.playerX
        self.board = {1,2,3,4,5,6,7,8,9}
        self.endGame = None
        self.draw()


    def Game(self, number):
        self.play(self.get_number(number))
        self.endGame = self.endgame_message()
        return self.endGame

    def endgame_message(self):
        message = ''
        for i in self.win:
            if i.issubset(self.playerX):
                message = self.draw() + "\nИгра окончена. Вы победили!"
            elif i.issubset(self.playerO):
                message = self.draw() + "\nИгра окончена. Бот победил"
            elif not self.board:
                message = self.draw() + "\nИгра окончена. Ничья - победила дружба!"
        return message

    def draw(self):
        message = ''
        for i in range(1,10):
            symb=str(i)
            if i in self.playerX:
                symb="X"
            elif i in self.playerO:
                symb="O"
            message += symb + '\n' if i in {3,6,9} else symb + " "
        return message

    def play(self, number:int):
        self.player.add(number)
        self.board.remove(number)
        if self.player == self.playerX:
            self.player = self.playerO
            num = random.choice(list(self.board))
            self.play(num)
        else:
            self.player = self.playerX

    def get_number(self, number):
        if self.endGame == True:
            return
        if not str(number).isnumeric() or int(number) not in self.board:
            return None
        return int(number)