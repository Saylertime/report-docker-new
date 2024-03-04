from telebot.types import Message
from loader import bot
from pg_maker import refresh_db

@bot.message_handler(state=None)
def bot_echo(message: Message) -> None:
    """ Вызывается, когда пользователь без состояния вводит несуществующую команду """

    if message.text == 'ОБНОВИСЬ':
        refresh_db()
        bot.send_message(message.chat.id, 'Обновились')

    else:
        bot.reply_to(
            message, f"Такой команды нет: {message.text}\n"
                     f"Нажмите /start, чтобы посмотреть весь список команд"
        )
