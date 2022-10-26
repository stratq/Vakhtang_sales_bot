import telebot
import types
from telebot import types

import socks
import urllib3
from urllib3.contrib.socks import SOCKSProxyManager

# proxy = SOCKSProxyManager('socks5h://10.2.45.34:8080/')
# proxy.request('GET', 'http://api.telegram.org)/')

# proxy = urllib3.ProxyManager('http://10.2.45.34:8080/')
# r1 = proxy.request('GET', 'http://api.telegram.org/')
# r2 = proxy.request('GET', 'http://httpbin.org/')
# len(proxy.pools)

# proxy = socks.socksocket()
# proxy.set_proxy(socks.SOCKS5, "socks.example.com") # uses default port 1080
# proxy.set_proxy(socks.HTTP, "10.2.45.34", 8080)
# proxy.connect(("10.2.45.34", 8080))

bot = telebot.TeleBot('5664614354:AAGn8lPRmOXytJkPXaZwAWYdWLmE9V4m8Ok')
CHANNEL_NAME = '@Python_sales_bot'
PAYMENTS_TOKEN = '381764678:TEST:44295'  # Завести платежку

# f = open('data/fun.txt', 'r', encoding='UTF-8')
# jokes = f.read().split('\n')
# f.close()

# message.text.strip().lower() обрезка от лишних пробелов и приведение к нижнему регистру

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Саламалекум, <b>{message.from_user.first_name}</b> <u>{message.from_user.last_name}</u>, туту вступление \n<b>НУЖНА ФОТКА 640х360</b> вроде. \nЗ.Ы. Саня когда в доту заебал?'
    bot.send_message(message.from_user.id, mess, parse_mode='html')
    shop_main_menu(message)


@bot.message_handler(commands=['shop'])
def shop_main_menu(message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    clothes1 = types.KeyboardButton("Одежда1")
    lectures1 = types.KeyboardButton("Лекции1")
    accessories1 = types.KeyboardButton("Акссесуары1")
    keyboard1.add(clothes1, lectures1, accessories1)
    mess1 = f"<i><u><b>Я знаю три твоих ID</b></u></i>\nmessage.id: {message.id}\nmessage.from_user.id {message.from_user.id}\nmessage.chat.id {message.chat.id}\nПо какому айди отправлять сообщения обратно? \n{message.from_user.is_bot}\nНадо сверить айди с саней"
    bot.send_message(message.chat.id, text=mess1, reply_markup=keyboard1, parse_mode='html')

    keyboard2 = types.InlineKeyboardMarkup()
    clothes2 = types.InlineKeyboardButton(text="Одежда2", callback_data='clothes')
    lectures2 = types.InlineKeyboardButton(text="Лекции2", callback_data='lectures')
    accessories2 = types.InlineKeyboardButton(text="Акссесуары2", callback_data='accessories')
    keyboard2.add(clothes2, lectures2, accessories2)
    mess2 = 'Бот ли ты:\nТы написал: ' + message.text + ' - сказал ревизор'
    bot.send_message(message.chat.id, text=mess2, reply_markup=keyboard2)


def clothes(message):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    hoodie = types.KeyboardButton("Худи")
    t_shirts = types.KeyboardButton("Футболки")
    keyboard1.add(hoodie, t_shirts)
    mess1 = "Что интересует, худи или футболки?"
    bot.send_message(message.chat.id, text=mess1, reply_markup=keyboard1, parse_mode='html')


def hoodie(message):
    keyboard2 = types.InlineKeyboardMarkup()
    model1 = types.InlineKeyboardButton(text="Худи красное", callback_data='h_red')
    model2 = types.InlineKeyboardButton(text="Худи зеленое", callback_data='h_green')
    model3 = types.InlineKeyboardButton(text="Худи синее", callback_data='h_blue')
    keyboard2.add(model1, model2, model3)
    mess2 = "Какая модель"
    bot.send_message(message.chat.id, text=mess2, reply_markup=keyboard2, parse_mode='html')


@bot.message_handler(commands=['buy'])                                                         # РАЗОБРАТЬСЯ С ПОКУПКОЙ
def buy(message: types.Message):
    PRICE = types.LabeledPrice(label="СЮДА ДЕНЬГИ СУКААААААА", amount=500*100)
    # mess = types.InputInvoiceMessageContent(title="Купон на куни",
    #                                         description="что тут не понятного, зачем тут описание",
    #                                         photo_url='',
    #                                         photo_width=300,
    #                                         photo_height=150,
    #                                         photo_size=300,
    #                                         provider_token=PAYMENTS_TOKEN,
    #                                         currency="rub",
    #                                         prices=[PRICE],
    #                                         is_flexible=False,
    #                                         need_phone_number=True,
    #                                         payload="test-invoice-payload")
    #
    # bot.send_message(message.chat.id, text="\nInputInvoiceMessageContent\n", reply_markup=types.InlineKeyboardMarkup().add(mess), parse_mode='html')

    bot.send_invoice(message.chat.id,
                     title="Купон на куни",
                     description="что тут не понятного, зачем тут описание",
                     photo_url='https://klike.net/uploads/posts/2020-09/1601279291_17.jpg',
                     photo_width=300,
                     photo_height=150,
                     photo_size=300,
                     provider_token=PAYMENTS_TOKEN,
                     currency="rub",
                     prices=[PRICE],
                     is_flexible=False,
                     need_phone_number=True,
                     invoice_payload="test-invoice-payload")


# @bot.pre_checkout_query_handler(lambda query: True)
# def checkout(checkout_q: types.PreCheckoutQuery):
#     bot.answer_pre_checkout_query(checkout_q.id, ok=True)
#
# @bot.message_handler(content_types=ContentType.SUCCESSFUL_PAYMAENT)
# def successful_payment(message: types.Message):
#     print("SUCCESSFUL_PAYMAENT:")
#     payment_info = message.successful_payment.to_python()
#     for k, v in payment_info.items():
#         print(f"{k} = {v}")
#
#     bot.send_message(message.chat.id, f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошёл успешно!!!")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'жуй два')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'нет нет')
    elif call.data == "clothes":
        bot.send_message(call.message.chat.id, 'сработал clothes')
        # bot.next_step_backend(clothes)
    elif call.data == "Одежда1":
        bot.send_message(call.message.chat.id, 'сработал Одежда1')
        # bot.next_step_backend(clothes)
    elif call.data == "Худи":
        bot.next_step_backend(hoodie)
    elif call.data == "h_red":
        bot.send_message(call.message.chat.id, 'размер красного худака')
    elif call.data == "h_green":
        bot.send_message(call.message.chat.id, 'размер зеленого худака')
    elif call.data == "h_blue":
        bot.send_message(call.message.chat.id, 'размер синего худака')


# @bot.message_handler(content_types=['text', 'document', 'audio'])
# def get_text_messages(message):
#     if message.text == "Кнопки":
#         keyboard = types.InlineKeyboardMarkup()
#         key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
#         keyboard.add(key_yes)
#         key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
#         keyboard.add(key_no)
#         question = "ты нажал кнопки"
#         bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#     elif message.text == "Привет":
#         bot.send_message(message.chat.id, "Привет, чем я могу тебе помочь?    chat.id")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Я пока нихуя не умею     from_user.id")
    bot.send_message(message.chat.id, "Я пока нихуя не умею     chat.id")


@bot.message_handler(commands=['deletebot'])
def stop(message):
    mess = f'дотвидания, <b>{message.from_user.first_name}</b> <u>{message.from_user.last_name}</u>, или просто петук!'
    bot.send_message(message.from_user.id, mess, parse_mode='html')
    bot.stop_bot()


bot.polling(none_stop=True)  # разобраться с аргументами , interval=0, skip_pending=False, allowed_updates=[]
# bot.infinity_polling()

# def print_hi(name):
#     print(f'Hi, {name}')
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')
