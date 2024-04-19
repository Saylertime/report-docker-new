from loader import bot
import handlers
from telebot.custom_filters import StateFilter
from utils.set_bot_commands import set_default_commands
import time
import threading
from utils.tasks import send_notifications

def scheduled_job():
    while True:
        send_notifications()
        time.sleep(60)

if __name__ == "__main__":
    try:
        bot.add_custom_filter(StateFilter(bot))
        set_default_commands(bot)
        thread = threading.Thread(target=scheduled_job)
        thread.start()
        bot.polling()
    except Exception as e:
        time.sleep(3)
        print(e)
