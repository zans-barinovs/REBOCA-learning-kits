import telebot
import bot_settings

bot = telebot.TeleBot(bot_settings.token)


@bot.message_handler(commands=['start'])
def start(message):
    getting_kit_way = telebot.types.InlineKeyboardMarkup(row_width=1)
    getting_kit_way.add(
        telebot.types.InlineKeyboardButton("Show most popular learning kits", callback_data="most_popular_kit"),
        telebot.types.InlineKeyboardButton("Serch learning kit", callback_data="search_kit")
    )
    
    bot.send_message(message.chat.id, 'Hello! \nI\'m RIBOCA assistant bot.')
    bot.send_message(message.chat.id, 'Here is what I can do.', reply_markup=getting_kit_way)   
    
def FunctionName(args):
    

@bot.callback_query_handler(func=lambda data: True)
def buttons_callbacks(data):
    if data.data == 'most_popular_kit':
        bot.send_message(data.message.chat.id, 'Choose one for you')
    elif data.data == "search_kit":
        bot.send_message(data.message.chat.id, 'Enter the topic please')
        
        
    
    

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
