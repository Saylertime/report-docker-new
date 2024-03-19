from telebot.types import Message
from loader import bot
from pg_maker import refresh_db, delete_author, new_table

@bot.message_handler(state=None)
def bot_echo(message: Message) -> None:
    """ Вызывается, когда пользователь без состояния вводит несуществующую команду """

    if message.text == 'ОБНОВИСЬ':
        refresh_db()
        bot.send_message(message.chat.id, 'Обновились')

    elif message.text == 'НАПОМИНАЛКА':
        new_table()
        bot.send_message(message.chat.id, 'Создана')

    elif "УДАЛИТЬ" in message.text:
        try:
            name = message.text.split(" ")[1]
            result = delete_author(name)
            if result:
                bot.send_message(message.chat.id, f"Мы будем скучать по тебе, {name} ;(")
            else:
                bot.send_message(message.chat.id, f"Такого нет. Может, мы его выперли уже давно?")
        except:
            bot.send_message(message.chat.id, f"Такого нет. Может, мы его выперли уже давно?")

    else:
        bot.reply_to(
            message, f"Такой команды нет: {message.text}\n"
                     f"Нажмите /start, чтобы посмотреть весь список команд"
        )
