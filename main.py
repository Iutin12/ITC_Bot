import telebot
import config
import requests

bot = telebot.TeleBot (config.TOKEN)
@bot.message_handler(content_types=["text"])
def text(message):
    resp = requests.get("https://random.dog/woof.json").json().get('url')
    bot.send_photo(message.chat.id, resp)
bot.polling(none_stop=True)