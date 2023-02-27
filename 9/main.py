# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP 
# добавлен бот, вместо справочника 9.2.2
import os
import sys

from telegram import Update
from telegram.ext import ApplicationBuilder,ContextTypes,  CommandHandler, MessageHandler, filters

import game

mygame:game.XOGame

def getToken():
    token_file = "token.txt"
    token = ''
    if os.path.isfile(token_file):
        f = open(token_file, "r")
        token = f.read()
        f.close()
        return token
    else:
        print("Отсутствует файл токена 'token.txt'")
    sys.exit()


async def newGame(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global mygame
    mygame = game.XOGame()
    mygame.start_new_game()
    mess = mygame.draw() + "\nВаш ход"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

async def go(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if mygame.endGame:
        mess = "Игра окончена"
        await help_command(update, context)
    else:
        number = mygame.get_number(update.message.text)
        if  number == None:
            mess = "Введите число из оставшихся"
        else:
            mess = mygame.Game(number)
            if not mess:
                mess = "Ваш ход"
                mess = mygame.draw() + '\n' + mess
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mess)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Вы играете за X, для начала игры введите /new_game")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Я бот для игры в крестики-нолики! /help")

if __name__ == '__main__':
    updater = ApplicationBuilder().token(getToken()).build()


    updater.add_handler(CommandHandler('start', start))
    updater.add_handler(CommandHandler('new_game', newGame))
    updater.add_handler(CommandHandler('help', help_command))

    go_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), go)
    updater.add_handler(go_handler)
    print('server start')
    updater.run_polling()
