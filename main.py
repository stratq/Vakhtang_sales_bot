#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import types
from telebot import types


bot = telebot.TeleBot('5664614354:AAGn8lPRmOXytJkPXaZwAWYdWLmE9V4m8Ok')
CHANNEL_NAME = '@Python_sales_bot'
PAYMENTS_TOKEN = '381764678:TEST:44295'
MODEL = ''
SIZE = ''


# import socks
# import urllib3
# from urllib3.contrib.socks import SOCKSProxyManager
#
# proxy = SOCKSProxyManager('socks5h://10.2.45.34:8080/')
# proxy.request('GET', 'http://api.telegram.org)/')
#
# proxy = urllib3.ProxyManager('http://10.2.45.34:8080/')
# r1 = proxy.request('GET', 'http://api.telegram.org/')
# r2 = proxy.request('GET', 'http://httpbin.org/')
# len(proxy.pools)
#
# proxy = socks.socksocket()
# proxy.set_proxy(socks.SOCKS5, "socks.example.com") # uses default port 1080
# proxy.set_proxy(socks.HTTP, "10.2.45.34", 8080)
# proxy.connect(("10.2.45.34", 8080))
#
#
# f = open('data/fun.txt', 'r', encoding='UTF-8')
# jokes = f.read().split('\n')
# f.close()
#
# message.text.strip().lower() обрезка от лишних пробелов и приведение к нижнему регистру


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Саламалекум, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, \n<i>НУЖНА ФОТКА 640х360</i> вроде. Про-то где можно забрать вещь надо написать или выдавать геолокацию например. Надо проверить как бот будет общаться в <u>группе</u>.'
    bot.send_message(message.from_user.id, mess, parse_mode='html')
    menu(message)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Я умею общаться только с помощью меню и кнопок")


@bot.message_handler(commands=['deletebot'])
def stop(message):
    mess = f'Дотвидания, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, или просто - петук!'
    bot.send_message(message.from_user.id, mess, parse_mode='html')
    bot.stop_bot()                                                                          # разобраться с отключением и нужна ли команда start в меню и help отдельным


@bot.message_handler(commands=['shop'])
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    keyboard.add(types.KeyboardButton("Одежда"),
                 types.KeyboardButton("Лекции"),
                 types.KeyboardButton("Аксессуары"))
    mess = "Наш магазин предоставляет выбор одежды, что бы вы хотели купить?"
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


def clothes(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton("Худи"),
                 types.KeyboardButton("Футболки"),
                 types.KeyboardButton("Назад в меню"))
    mess = "Что интересует, худи или футболки?"
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


def lectures(message):
    bot.send_message(message.from_user.id, "Ждём блок-схему по лекциям")                            #блок схемы?


def accessories(message):
    bot.send_message(message.from_user.id, "Ждём блок-схему по аксессуарам")


def hoodie(message):
    hoodie_red = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Худи красное", callback_data='hoodie_red'))  # написать цикл который будет автоматизировать это дерьмо
    hoodie_green = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Худи зеленое", callback_data='hoodie_green'))  # брать из бд name и url и подставлять в цикл
    hoodie_blue = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Худи синее", callback_data='hoodie_blue'))
    bot.send_photo(message.from_user.id, 'https://cdn.lmbd.ru/f9544273-7f6e-4a3a-be00-7de234aea05a/', reply_markup=hoodie_red)
    bot.send_photo(message.from_user.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSluo1fj_JwKYRv6isrE1CgMH0PX5ev7Bsl5Q&usqp=CAU', reply_markup=hoodie_green)
    bot.send_photo(message.from_user.id, 'https://img.championat.com/s/735x490/news/big/z/c/istoriya-priznaniya-hudi_163482210596339940.jpg', reply_markup=hoodie_blue)


def shirts(message):
    shirts_yellow = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Футболка желтая", callback_data='shirts_yellow'))
    shirts_turquoise = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Футболка бирюзовая", callback_data='shirts_turquoise'))
    shirts_purple = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Футболка фиолетовая", callback_data='shirts_purple'))
    bot.send_photo(message.from_user.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTk1AgahQq7a0XFI77brN4NSoUJKcKoe46bg&usqp=CAU', reply_markup=shirts_yellow)
    bot.send_photo(message.from_user.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6AYpVPadneV562f5gaMiKixcj9oGtrGxwDg&usqp=CAU', reply_markup=shirts_turquoise)
    bot.send_photo(message.from_user.id, 'https://stockmann.ru/istk/6ZmjWDRX83ltP025pjAzpV2UIyu11H3P0cM0CGk-44A/rs:fit:344:516:0/g:ce/bG9jYWw6Ly8vdXBsb2FkL2libG9jay80MjQvNTEwMjA4N18xLkpQRw.jpg', reply_markup=shirts_purple)

# import glob, os, random
# files = []
# for ext in ["png", "jpg", "jpeg"]:
#   [files.append(file) for file in glob.glob(f"*.{ext}")]
#
# random_file = files[random.randint(0, len(files)-1)]                                                            # Доделать красивый вывод
#
#
# Отправить можно так:
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#   if call.data == 'men':
#     with open(random_file, 'rb') as f:
#       bot.send_media_group(call.message.chat.id, [InputMediaPhoto(f)])

def size(message):                                                                    # хз как сделать чтобы те размеры которых уже нет не показывались в кнопках
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    keyboard.add(types.KeyboardButton("S"),
                 types.KeyboardButton("M"),
                 types.KeyboardButton("L"),
                 types.KeyboardButton("Назад к одежде"))
    mess = "{MODEL}, а какой размер?"                                                           # Как правильно передавать модель для отображения!?
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


@bot.message_handler(commands=['buy'])                                                      # РАЗОБРАТЬСЯ С ОПЛАТОЙ И ПЛАТЕЖКОЙ Один вблок в который передавать size model
def buy(message: types.Message):
    PRICE = types.LabeledPrice(label="СЮДА ДЕНЬГИ СУКААААААА", amount=3000*100)
    bot.send_invoice(message.from_user.id,
                     title=f"{MODEL} {SIZE}",
                     description="На самом деле ты можешь получить только пизды, ну я про купон на куни",
                     photo_url='http://pm1.narvii.com/7092/d6f96da5a0210aafb9f06c77ec4845b4bed315bar1-720-1042v2_uhq.jpg',
                     photo_width=200,
                     photo_height=150,
                     photo_size=300,
                     provider_token=PAYMENTS_TOKEN,
                     currency="rub",
                     prices=[PRICE],
                     is_flexible=False,
                     need_phone_number=True,
                     invoice_payload="test-invoice-payload")

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
    # bot.send_message(message.from_user.id, text="\nInputInvoiceMessageContent\n", reply_markup=types.InlineKeyboardMarkup().add(mess), parse_mode='html')


    # keyboard2 = types.InlineKeyboardMarkup()
    # clothes2 = types.InlineKeyboardButton(text="Одежда2", callback_data='clothes')
    # lectures2 = types.InlineKeyboardButton(text="Лекции2", callback_data='lectures')
    # accessories2 = types.InlineKeyboardButton(text="Акссесуары2", callback_data='accessories')
    # keyboard2.add(clothes2, lectures2, accessories2)
    # mess2 = 'Бот ли ты:\nТы написал: ' + message.text + ' - сказал ревизор'
    # bot.send_message(message.from_user.id, text=mess2, reply_markup=keyboard2)


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
#     bot.send_message(message.from_user.id, f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошёл успешно!!!")


@bot.callback_query_handler(func=lambda call: True)                                                  # разобраться с lambda как это работает
def callback_worker(call):
    global MODEL
    MODEL = call
    size(call)


@bot.message_handler(content_types=['text', 'voice', 'photo', 'video', 'audio', 'document', 'sticker'])
def get_text_messages(message):
    global SIZE
    if message.voice:
        bot.send_message(message.from_user.id, 'Я в метро, наушников нет, напиши плиз сообщение')
    elif message.photo:
        bot.send_message(message.from_user.id, 'Классная фотка')
    elif message.video:
        bot.send_message(message.from_user.id, 'Видео как видео, мне больше другого типа нравятся')
    elif message.audio:
        bot.send_message(message.from_user.id, 'Потом послушаю')
    elif message.document:
        bot.send_message(message.from_user.id, 'Ну и что в нем? Сценарий к 2023?')
    elif message.sticker:
        bot.send_message(message.from_user.id, 'Мне впадлу искать для тебя стикер')
    elif message.text == "Назад в меню":
        menu(message)
    elif message.text == "Одежда" or message.text == "Назад к одежде":
        clothes(message)
    elif message.text == "Лекции":
        lectures(message)
    elif message.text == "Аксессуары":
        accessories(message)
    elif message.text == "Худи":
        hoodie(message)
    elif message.text == "Футболки":
        shirts(message)
    elif message.text == "S" or message.text == "L" or message.text == "M":
        SIZE = message
        buy(message)
    else:
        bot.send_message(message.from_user.id, "Это что-то на иврите? Я не понимаю. Напиши /help.")


bot.polling(none_stop=True)                                                    # разобраться с аргументами , interval=0, skip_pending=False, allowed_updates=[]
# bot.infinity_polling()                                                        # Просто надо не bot.infinity_polling(), а вебхук настроить


def print_hi(name):
    print(f'БОТ {name}')


if __name__ == '__main__':
    print_hi('ЗАПУЩЕН!')
