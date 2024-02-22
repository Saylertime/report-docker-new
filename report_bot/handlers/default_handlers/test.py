# import requests
# from loader import bot
# import os

# openai.api_key = os.getenv("CHATGPT_API_KEY")
#
# @bot.message_handler(commands=['test'])
# def test(message):
#     bot.send_message(message.chat.id, 'Привет! Я ChatGPT. Просто напиши мне, и я постараюсь ответить.')
#
# @bot.message_handler(func=lambda message: True)
# def handle_text(message):
#     user_input = message.text
#
#     proxy = {
#        "http": "http://your_proxy_address",
#        "https": "https://your_proxy_address",
#     }
#
#     response = requests.post(
#        "https://api.openai.com/v1/engines/gpt-3.5-turbo/completions",
#        headers={"Authorization": f"Bearer {os.getenv('CHATGPT_API_KEY')}"},
#        json={"prompt": user_input, "max_tokens": 1000},
#        proxies=proxy
#     )
#
#     chatgpt_reply = response.json()['choices'][0]['text'].strip()
#
#     bot.send_message(message.chat.id, chatgpt_reply)
