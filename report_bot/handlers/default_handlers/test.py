from loader import bot
import openai
import os

openai.api_key = os.getenv("CHATGPT_API_KEY")

@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.chat.id, 'Привет! Я ChatGPT. Просто напиши мне, и я постараюсь ответить.')

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_input = message.text

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=user_input,
        max_tokens=1000
    )

    chatgpt_reply = response['choices'][0]['text'].strip()

    bot.send_message(message.chat.id, chatgpt_reply)
