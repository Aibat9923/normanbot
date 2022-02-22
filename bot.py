import config

import telebot

from telebot import types

bot = telebot.TeleBot(config.TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.InlineKeyboardMarkup(row_width=1)
	itembtn1 = types.InlineKeyboardButton('Игровой', callback_data=1)
	itembtn2 = types.InlineKeyboardButton('Ультрабук', callback_data=2)
	itembtn3 = types.InlineKeyboardButton('Офисный (бюджетный)', callback_data=3)
	itembtn4 = types.InlineKeyboardButton('Нетбук', callback_data=4)
	itembtn5 = types.InlineKeyboardButton('Сенсорный трансформер', callback_data=5)
	itembtn6 = types.InlineKeyboardButton('Свои настройки', callback_data=6)

	markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
	bot.send_message(message.chat.id, "Howdy, how are you doing?")
	bot.send_message(message.chat.id, "Какой тип ноутбука вы хотите купить?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
	if int(call.data) == 1:
		bot.send_message(call.message.chat.id, 'Вы выбрали игровой')
	else:
		bot.send_message(call.message.chat.id, 'Data: {}'.format(str(call.data)))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	markup = types.ReplyKeyboardMarkup(row_width=1)
	itembtn1 = types.KeyboardButton('a')
	itembtn2 = types.KeyboardButton('v')
	itembtn3 = types.KeyboardButton('d')
	markup.add(itembtn1, itembtn2, itembtn3)
	bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)




# run long- polling
if __name__ == "__main__":
	bot.infinity_polling()

	