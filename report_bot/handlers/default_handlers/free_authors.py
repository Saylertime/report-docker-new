from loader import bot
from utils.sheets import who_is_free

@bot.message_handler(commands=['free_authors'])
def free_authors(message):
    free_authors = who_is_free()
    if free_authors:
        msg = 'Сейчас свободны: \n\n'
        for author in free_authors:
            msg += f"{author[1]} — {author[0]}\n"
        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id, 'Все такие занятые, я прям не могу(((')



