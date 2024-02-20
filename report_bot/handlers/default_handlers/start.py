from loader import bot

@bot.message_handler(commands=['start'])
def start_message(message):

    msg = f"Ультимативный бот для сотрудников ГейГуру \n\n" \
          f"/free_authors — Свободные авторы \n\n" \
          f"/free_texts — Свободные брифы \n\n" \
          f"/authors — Все авторы \n\n" \
          f"/new_author — Обновить базу данных \n\n" \
          f"/money — Гонорары за месяц\n\n"

    bot.send_message(message.chat.id, msg)
