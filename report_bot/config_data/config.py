import os
import openai
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
openai.api_key = os.getenv("CHATGPT_API_KEY")

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("authors", "Все авторы"),
    ("free_authors", "Свободные авторы"),
    ("free_texts", "Свободные брифы"),
    ("new_author", "Обновить базу данных"),
    ("money", "Гонорары за месяц"),
    ("test", "test"),
    ("stats_month", "Статистика по текстам за месяц"),
    ("history", "Инфа по отдельному автору"),
    ("all_texts", "Тексты автора за всё время"),
)
