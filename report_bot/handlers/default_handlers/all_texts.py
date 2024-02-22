from loader import bot
from states.overall import OverallState
from utils.sheets import all_texts_of_author


@bot.message_handler(commands=['all_texts'])
def all_texts(message):
    bot.send_message(message.chat.id, "Введи имя автора (как в таблице) Пример:"
                                      "\n\nПаша")
    bot.set_state(message.chat.id, state=OverallState.all_texts)


@bot.message_handler(state=OverallState.all_texts)
def answer(message):
    all_texts = all_texts_of_author(message.text)
    if all_texts:
        with open(all_texts, 'rb') as file:
            bot.send_document(message.chat.id, file)
    else:
        msg = "Ничего не нашел по нему( Точно имя правильное?"
        bot.send_message(message.chat.id, msg)
    bot.delete_state(message.chat.id)
