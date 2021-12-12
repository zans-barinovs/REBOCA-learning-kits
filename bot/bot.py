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


def most_popular_kit(data):
    file = open("..\data\learning_kits\most_popular_learning_kits.txt")
    file_lines = file.readlines()

    most_popular_kits = telebot.types.InlineKeyboardMarkup()
    for i in range(len(file_lines)):
        one_kit = str(file_lines[i])
        most_popular_kits.add(telebot.types.InlineKeyboardButton(
            one_kit, callback_data=str("kitname" + one_kit)))

    bot.send_message(data.message.chat.id,
                     'Choose one for you',
                     reply_markup=most_popular_kits)

    file.close()


def show_kit(data, kit_name):
    bot.send_message(data.message.chat.id, 'Pleace wait for video. Sending '+str(kit_name)+' kit video:')
    
    files_location = '..\data\learning_kits\\'+kit_name+'\\'
    
    video_file = open(files_location+'main_topic.mp4', 'rb')
    bot.send_video(chat_id=data.message.chat.id, data=video_file, supports_streaming=True)
    
    warm_up_file = open(files_location+'warm_up.txt')
    warm_up_file_lines = warm_up_file.readlines()
    for i in range(len(warm_up_file_lines)):
        a=1
    

    for i in warm_up_file_lines:
        print(i)
    print(7)


@bot.callback_query_handler(func=lambda data: True)
def buttons_callbacks(data):
    if data.data == 'most_popular_kit':
        most_popular_kit(data)
    elif data.data == "search_kit":
        bot.send_message(data.message.chat.id, 'Enter the topic please')
    elif data.data[:7] == "kitname":
        print("in kitname:"+data.data[7:len(data.data)-1])
        show_kit(data, data.data[7:len(data.data)-1])


bot.infinity_polling()
