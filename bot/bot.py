import telebot
import bot_settings

bot = telebot.TeleBot(bot_settings.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! \n I\'m RIBOCA assistant bot.')
    bot.send_message(message.chat.id, 'Here is what I can do.')


bot.infinity_polling()
# import telebot
# import bot_settings
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# bot = telebot.TeleBot(config.TOKEN)

# def gen_markup():#generates Inline keyboard ansewrs
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(InlineKeyboardButton("Robots", callback_data="cb_Robots"),
#                                InlineKeyboardButton("Sculptures", callback_data="cb_Sculptures"))
#     return markup

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, """
#     Hello I am your RIBOCA assistant
#     Pick the topic which you interested in""", reply_markup=gen_markup())
# #welcome message and Inline keyboard init

# bot.infinity_polling()#bot init