import telebot
from telebot.types import Message
import bot_settings

bot = telebot.TeleBot(bot_settings.token)
waiting_for_users_answer = False
user_whant_to_craete_hisown = False
user_answer = ""


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


@bot.message_handler(commands=['show_kit'])
def show_kit(message, kit_name):
    global waiting_for_users_answer
    global user_whant_to_craete_hisown

    bot.send_message(message.message.chat.id, 'Pleace wait. Sending ' +
                     str(kit_name)+' learning kit video...')

    files_location = '..\data\learning_kits\\'+kit_name+'\\'

    video_file = open(files_location+'main_topic.mp4', 'rb')
    bot.send_video(chat_id=message.message.chat.id,
                   data=video_file, supports_streaming=True, timeout=None)

    warm_up_file = open(files_location+'warm_up.txt')
    warm_up_file_lines = warm_up_file.readlines()

    counter = 0
    for i in warm_up_file_lines:
        if i[:2] == "Q:":
            question = bot.send_message(
                message.message.chat.id, "*"+i[2:len(i)-1]+"*", parse_mode='Markdown')
            waiting_for_users_answer = True
            bot.register_next_step_handler(
                message=question, callback=extract_message)

            while waiting_for_users_answer:
                pass

            warm_up_file_lines = warm_up_file_lines[0:counter+1] + [
                user_answer] + warm_up_file_lines[counter+1:len(warm_up_file_lines)-1]
            bot.send_message(message.message.chat.id, '*You answered: *' +
                             user_answer + '.\n*Here is what other users answered:*', parse_mode='Markdown')
        else:
            bot.send_message(message.message.chat.id, i[2:len(i)-1])
        counter += 1

    artwork_file = open(files_location+'artwork.jpg', 'rb')
    bot.send_photo(message.message.chat.id, artwork_file)

    text_file = open(files_location+'text.txt')
    text_file_lines = text_file.readlines()
    bot.send_message(message.message.chat.id, '*Some information:*\n' +
                     str(text_file_lines)[2:len(str(text_file_lines))-2], parse_mode='Markdown')

    yes_no = telebot.types.InlineKeyboardMarkup(row_width=2)
    yes_no.add(
        telebot.types.InlineKeyboardButton(
            "yes", callback_data="yes"),
        telebot.types.InlineKeyboardButton(
            "no", callback_data="no")
    )
    
    bot.send_message(message.message.chat.id, 'Do you want to create yours?',
                     reply_markup=yes_no)
    waiting_for_users_answer = True
    while waiting_for_users_answer:
        pass
    
    if user_whant_to_craete_hisown:
        a_file = open(files_location+'quick_activity.txt')
        a_file_lines = a_file.readlines()
        bot.send_message(message.message.chat.id, '*Quick Activity:*\n' +
                         str(a_file_lines)[2:len(str(a_file_lines))-2], parse_mode='Markdown')
    else:
        bot.send_message(message.message.chat.id, 'I am sed, but ok.')

    b_file = open(files_location+'discussion_ideas.txt')
    b_file_lines = b_file.readlines()
    bot.send_message(message.message.chat.id, '*Discuss it in your groups:*\n' +
                     str(b_file_lines)[2:len(str(b_file_lines))-2], parse_mode='Markdown')
    
        


def extract_message(message):
    global user_answer
    global waiting_for_users_answer
    user_answer = message.text
    waiting_for_users_answer = False


@bot.callback_query_handler(func=lambda message: True)
def buttons_callbacks(message):
    global user_answer
    global waiting_for_users_answer
    global user_whant_to_craete_hisown
    print(1)
    if message.data == 'most_popular_kit':
        print('most_popular_kit')
        most_popular_kit(message)
    elif message.data == "search_kit":
        print()
        bot.send_message(message.message.chat.id, 'Enter the topic please')
    elif message.data == "no":
        waiting_for_users_answer = False
    elif message.data == "yes":
        waiting_for_users_answer = False
        user_whant_to_craete_hisown = True
    elif message.data[:7] == "kitname":
        print("in kitname:"+message.data[7:len(message.data)-1])
        show_kit(message, message.data[7:len(message.data)-1])
    elif waiting_for_users_answer == True and message.data != "" and message.data != None:
        print(45678)
        user_answer = message.data()
        waiting_for_users_answer = False
    elif message.data == 'sam':
        print("sana")


bot.infinity_polling()
