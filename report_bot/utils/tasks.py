from loader import bot
from pg_maker import find_for_tasks

def send_notifications():
    notification = find_for_tasks()

    if notification:
        for instance in find_for_tasks():
            user_id = instance[0]
            text = instance[2]
            bot.send_message(user_id, text, parse_mode='HTML')

        # user_ids = [n[0] for n in find_for_tasks()]
        # user_texts = [n[2] for n in find_for_tasks()]
        # text = "<b>НАПОМИНАНИЕ:</b> "
        # for t in user_texts:
        #     text += f"{t}\n\n"
        #
        # for id in user_ids:
        #     bot.send_message(id, text, parse_mode='HTML')
