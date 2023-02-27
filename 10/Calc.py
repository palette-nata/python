# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
import os
import sys
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder,ContextTypes, CommandHandler, MessageHandler, ConversationHandler,filters


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


# Логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

CHOICE, RATIONAL_ONE, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO = range(7)



class Calculator:

    def calculate(self, n1,n2, operation):
        match operation:
            case '+':
                return n1 + n2
            case '-':
                return n1 - n2
            case '*':
                return n1*n2
            case '/':
                if n2 !=0:
                    return n1/n2


calc = Calculator()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mess = f'Привет, {update.effective_user.first_name}, это - калькулятор. Выберите пожалуйста команду.\n' 'Команда /cancel, чтобы прекратить разговор.\n\n1 - рациональные числа; \n2 - комплесные числа; \n3 - Выйти из калькулятора \n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=mess)
    return CHOICE

async def choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    mess = ''
    match user_choice:
        case '1':
            mess = 'Введите число. \n Первое рациональное число - это: '
            await context.bot.send_message(chat_id=update.effective_chat.id, text=mess)
            return RATIONAL_ONE

        case '2':
            mess = 'Введите Re и Im первого числа через ПРОБЕЛ: '
            await context.bot.send_message(chat_id=update.effective_chat.id, text=mess)
            return COMPLEX_ONE
        case '3':
            mess = 'Выход '
            await context.bot.send_message(chat_id=update.effective_chat.id, text=mess)
            return ConversationHandler.END

async def rational_one(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mess = 'Введите второе число'
    data = 'rational_one'

    if await get_num(update, context, data, mess):
        return RATIONAL_TWO


async def rational_two(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mess = 'Выберите действие: \n\n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n'
    data = 'rational_two'

    if await get_num(update, context, data, mess):
        return OPERATIONS_RATIONAL

async def get_num(update, context, data, mess):
    logger.info("%s ввел число: %s", update.message.from_user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        context.user_data[data] = float(get_rational)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mess)
        return True
    return False

async def operatons_rational(update, context):
    logger.info("%s выбрал операцию : %s", update.message.from_user.first_name, update.message.text)

    num1 = context.user_data.get('rational_one')
    num2 = context.user_data.get('rational_two')
    result = calc.calculate(num1, num2, update.message.text)
    logger.info("результат : %s",  result)
    if result != None:
        mess = f'Результат: {num1} {update.message.text} {num2} = {result}'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mess)
        return ConversationHandler.END

async def complex_one(update, context):
    mess = ' Введите Re и Im второго числа через ПРОБЕЛ:'
    data = 'complex_one'

    if await get_complex(update,context, data, mess):
        return COMPLEX_TWO



async def complex_two(update, context):
    mess = 'Выберите действие: \n\n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n'
    data = 'complex_two'

    if await get_complex(update,context, data, mess):
        return OPERATIONS_COMPLEX


async def get_complex(update, context, data, mess):
    logger.info("%s ввел число: %s", update.message.from_user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace(' ', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex_num = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data[data] = complex_num
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mess)
        return True
    return False


async def operatons_complex(update, context):
    logger.info("%s выбрал операцию : %s", update.message.from_user.first_name, update.message.text)

    num1 = context.user_data.get('complex_one')
    num2 = context.user_data.get('complex_two')
    result = calc.calculate(num1, num2, update.message.text)
    if result != None:
        await update.message.reply_text(f'Результат: {num1} {update.message.text} {num2} = {result}')
        return ConversationHandler.END


def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text('Спасибо, до свидания!')
    return ConversationHandler.END


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Калькулятор /start")


if __name__ == '__main__':
    updater = ApplicationBuilder().token(getToken()).build()

    conversation_handler = ConversationHandler(

        entry_points=[CommandHandler('start', start)],

        states={
            CHOICE: [MessageHandler(filters.TEXT, choice)],
            RATIONAL_ONE: [MessageHandler(filters.TEXT, rational_one)],
            RATIONAL_TWO: [MessageHandler(filters.TEXT, rational_two)],
            OPERATIONS_RATIONAL: [MessageHandler(filters.TEXT, operatons_rational)],
            OPERATIONS_COMPLEX: [MessageHandler(filters.TEXT, operatons_complex)],
            COMPLEX_ONE: [MessageHandler(filters.TEXT, complex_one)],
            COMPLEX_TWO: [MessageHandler(filters.TEXT, complex_two)],
        },

        fallbacks=[CommandHandler('cancel', cancel)],
    )

    updater.add_handler(conversation_handler)
    updater.add_handler(CommandHandler('help', help_command))
    print('server start')
    updater.run_polling()
