import telebot

from telebot import types

bot = telebot.TeleBot('5368971136:AAF3APAZRiQtB_RiH4JaIFTGAR-DkS9NJcA')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'<b>Привет, {message.from_user.first_name} именно тут ты сможешь найти ТЕ САМЫЕ СТИКЕРЫ из тг!</b>                     '
                                       'Чтобы начать нажми - /stikers', parse_mode='html')
@bot.message_handler(commands=['stikers'])
def stikers(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('котики', url='https://t.me/addstickers/kotikikiktiitiit' ))
    markup.add(types.InlineKeyboardButton('собачки', url='https://t.me/addstickers/sobakiwolfgang'))
    markup.add(types.InlineKeyboardButton('животные', url='https://t.me/addstickers/Sukrumotion'))
    markup.add(types.InlineKeyboardButton('only котики', url='https://t.me/addstickers/kittiesbynorufx_by_fStikBot'))
    markup.add(types.InlineKeyboardButton('1000-7', url='https://t.me/addstickers/GracesForEveryDay_by_fStikBot'))
    markup.add(types.InlineKeyboardButton('только для students', url='https://t.me/addstickers/Teachers_Sirius_2022'))
    bot.send_message(message.chat.id, "выбери категорию:" , reply_markup=markup)

    
bot.polling(none_stop=True)
print('Bot online')