import telebot
import bot_settings

bot = telebot.TeleBot(bot_settings.token)


@bot.message_handler(commands=['start'])
def start(message):
    getting_kit_way = telebot.types.InlineKeyboardMarkup(row_width=1)
    getting_kit_way.add(
        telebot.types.InlineKeyboardButton(
            "Show most popular learning kits", callback_data="most_popular_kit"),
        telebot.types.InlineKeyboardButton(
            "Serch learning kit", callback_data="search_kit")
    )

    bot.send_message(message.chat.id, 'Hello! \nI\'m RIBOCA assistant bot.')
    bot.send_message(message.chat.id, 'Here is what I can do.',
                     reply_markup=getting_kit_way)


def get_line_count(file): #SOMEHOW DOESNT FUCKING WORK
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1

    return line_count


def most_popular_kit(data):
    file = open("..\data\learning_kits\most_popular_learning_kits.txt")
    
    file_lines = file.readlines()

    most_popular_kits = telebot.types.InlineKeyboardMarkup()
    print(get_line_count(file))
    for i in range(2): #NEED TO CHAINGE
        one_kit = str(file_lines[i])
        print(one_kit)
        tmp = telebot.types.InlineKeyboardButton(
            one_kit, callback_data=str("kitname" + one_kit))
        print("1")
        most_popular_kits.add(tmp)
        print("1")

    print("2")
    bot.send_message(data.message.chat.id, 'Choose one for you',
                     reply_markup=most_popular_kits)
    print("3")

    file.close()


@bot.callback_query_handler(func=lambda data: True)
def buttons_callbacks(data):
    if data.data == 'most_popular_kit':
        most_popular_kit(data)
    elif data.data == "search_kit":
        bot.send_message(data.message.chat.id, 'Enter the topic please')


bot.infinity_polling()
