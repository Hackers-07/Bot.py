import telebot

# Replace 'YOUR_API_TOKEN' with your actual Telegram Bot API token
API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Forex Signals Bot!")

@bot.message_handler(commands=['signal'])
def send_signal(message):
    # Provide the latest forex signal here
    forex_signal = "EUR/USD Buy Signal: Take Profit at 1.2000"
    bot.send_message(message.chat.id, forex_signal)

if __name__ == '__main__':
    bot.polling()