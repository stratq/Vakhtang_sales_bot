#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import types
from telebot import types

bot = telebot.TeleBot('5664614354:AAGn8lPRmOXytJkPXaZwAWYdWLmE9V4m8Ok')
PAYMENTS_TOKEN = '381764678:TEST:44295'
# PAYMENTS_TOKEN = '401643678:TEST:337a0c19-863c-4175-a31f-2cc1b1f88196'
# PAYMENTS_TOKEN = '284685063:TEST:ZGJlZjkwNWU1NThj'


# global ITEM
# import pandas as pd
# raise TypeError(f'Object of type {o.__class__.__name__} '
# TypeError: Object of type int64 is not JSON serializable
# df = pd.read_csv("data.txt", sep=';')
# print(df, '\n')
# print(df.info(), '\n')
# df['ID'] = df['ID'].astype(str)
# df['NAME'] = df['NAME'].astype(str)
# df['PHOTO'] = df['PHOTO'].astype(str)
# df['DESCRIPTION'] = df['DESCRIPTION'].astype(str)
# print(df.info(), '\n')
# print(df['NAME'])
# print(df['NAME'][0])
# print(len(df))
# for i in range(len(df)):
#     if df['IS_CLOTHES'][i]:
#         pad = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text=df['NAME'][i], callback_data=df['ID'][i]))
#         bot.send_photo(message.from_user.id, open(df['PHOTO'][i], 'rb'), reply_markup=pad)
# for i in range(len(df)):
#     if not df['IS_CLOTHES'][i]:
#         pad = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text=df['NAME'][i], callback_data=df['ID'][i]))
#         bot.send_photo(message.from_user.id, open(df['PHOTO'][i], 'rb'), reply_markup=pad)
# mess = f"{df['NAME'][ITEM]}, а какой размер?"
# photo_url=f"{df['PHOTO'][ITEM]}",
# title=df['NAME'][ITEM] + str(df['HAS_SIZE'][ITEM]),
# description=df['DESCRIPTION'][ITEM],
# prices=[types.LabeledPrice(label=df['NAME'][ITEM], amount=df['PRICE'][ITEM]*100)],
# for i in range(len(df)):
#     if df['ID'][i] == call.data:
#         ITEM = i
# if call.data == 'hoodie' or call.data == 'shirt':
#     size(call)
# else:
#     buy(call)
# if df['ID'][ITEM] == 'hoodie' or df['ID'][ITEM] == 'shirt':
#     df.loc['HAS_SIZE', ITEM] = message.text

# elif message.text == "M" or message.text == "L" or message.text == "XL":
#     if ITEM.id == 'hoodie' or ITEM.id == 'shirt':
#         ITEM.has_size = message.text
#         buy(message)
#     else:
#         bot.send_message(message.from_user.id, 'Сначала выбери вещь')
#         menu(message)

#
# def change_availability(message):
#     for good in goods:
#         bot.send_message(527557405, f'{good.name} = {good.availability}')
#     bot.send_message(527557405, 'Для смены отображения в боте наличия того или иного товара нужно выбрать')

# bot.send_message(message.from_user.id,
#                  f"Платёж на сумму {message.successful_payment.total_amount / 100} {message.successful_payment.currency} прошёл успешно!!!",
#                  parse_mode='Markdown')

# bot.send_message(message.from_user.id, '💌', reply_markup=types.ReplyKeyboardRemove())

# global ITEM
# for good in goods:
#     if good.name == call.data:
#         buy(call, good)
        # ITEM = good
# if call.data == 'hoodie' or call.data == 'shirt':
    # size(call)
# else:
#     buy(call, ITEM)

# @bot.message_handler(commands=['deletebot'])
# def stop(message):
#     mess = f'ДЕЛАТЬ ЧТОБЫ ПО ЭТОЙ КОМАНДЕ БОТ УДАЛЯЛСЯ?</b>'
#     bot.send_message(message.from_user.id, mess, parse_mode='html')


# def size(message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     keyboard.add(types.KeyboardButton("M"),
#                  types.KeyboardButton("L"),
#                  types.KeyboardButton("XL"),
#                  types.KeyboardButton("Назад в меню"))
#     mess = f"{ITEM.name}, а какой размер?"
#     bot.send_message(message.from_user.id, mess, reply_markup=keyboard)

# Про-то где можно забрать вещь надо написать или выдавать геолокацию например.
# заблочить ли возможность пересылать блок Buy
# Как сделать чтобы некоторые кнопки срабатывали только в определенном месте , reply_to_message_id=message.from_user.id)
# bot.polling(none_stop=True)   # разобраться с аргументами , interval=0, skip_pending=False|True, allowed_updates=[]
# Просто надо не bot.infinity_polling(), а вебхук настроить
# while True:
#     pass
# может выдавать весь асортимент сразу, там не таку уж много
# НУЖНА ФОТКА 640х360 или GIF 320х180 вроде, название и логин бота
# нужны нормальные фотки, количетсво вещей каждого (типа/вида/размера), стоимость
# хз как сделать чтобы те размеры (и модели) которых уже нет - не показывались в кнопках
# разобраться с отключением и нужна ли команда start в меню и help отдельным
# сделать чтобы клава скрывалась и был фокус на покупку
# мб стоит поменять текст ПЛатёж на сумму 300 рублей прошёл успешно, или вообще убрать надпись и оставить только стикер
# 1111 1111 1111 1026 12/22 000
# 2200 0000 0000 0053 12/14 123


class Good:
    def __init__(self, id, name, photo, description, price, is_clothes, availability=True, availability_text='есть'):
        self.id = id
        self.name = name
        self.photo = photo
        self.description = description
        self.price = price
        self.is_clothes = is_clothes
        self.availability = availability
        self.availability_text = availability_text


goods = [Good('hoodie', 'Худи oversize', 'https://downloader.disk.yandex.ru/preview/e8ffd5e66f6e48e6b68d87e3a1424ace5c0813e4c6f813c36d90b5ab97c79835/637e228f/rfxXmPbxn4XpIWyLBCMqqYQEwxCg4I2e0_B2dpixROBfKhpOOVBEII0AcpGlJrApNxYxKX7HHKs5VErryCFbyw%3D%3D?uid=0&filename=%D0%A5%D1%83%D0%B4%D0%B8.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание худака', 300, True),
         Good('shirt', 'Футболка oversize', 'https://downloader.disk.yandex.ru/preview/7e63314552b363b88a7dbe49d49167b03d27d88ea517116fcda8275ca1e59a48/637e2275/zaG-o_OWA_lKVdmEbCXrN35OkJChHTg5HmV7a3Dy_UwDK780O1zkNTuo9B8S7mADP9pvFY_yTXMmPsC90zMOGA%3D%3D?uid=0&filename=%D0%A4%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание футболки', 200, True),
         Good('shirt', 'Футболка oversize long', 'https://downloader.disk.yandex.ru/preview/7e63314552b363b88a7dbe49d49167b03d27d88ea517116fcda8275ca1e59a48/637e2275/zaG-o_OWA_lKVdmEbCXrN35OkJChHTg5HmV7a3Dy_UwDK780O1zkNTuo9B8S7mADP9pvFY_yTXMmPsC90zMOGA%3D%3D?uid=0&filename=%D0%A4%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание футболки', 200, True),
         Good('sock', 'Носки one size', 'https://downloader.disk.yandex.ru/preview/1983eb668beafad9126bbd7912503f465eac88cbc36b5ee19401e5fb7cc10cbd/637e21f9/vR0yglLIvLHWmU9BOSZcCNOiNFoh7dGQoW_rj8KjDfd8ftRf8h2eumm-KrOAWZY8AOjIF1IZCyXritQtcVO3dQ%3D%3D?uid=0&filename=%D0%9D%D0%BE%D1%81%D0%BA%D0%B8.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание носков', 500, True),
         Good('hat', 'Шапка', 'https://downloader.disk.yandex.ru/preview/f92f71efeff9ed905b72808040add379e2c94aed58ff535cc569a069e63b1ec3/637e2131/CBSeuMWTOpTyAoiiJcIKtGZDamRRtza3VurjjY4Uzv_uapKUTQgFiRBiu77rzc0gJE5q2KnDGGmwewLnQAs1Rg%3D%3D?uid=0&filename=hat.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание шапки', 800, True),
         Good('notebook', 'Блокнот', 'https://downloader.disk.yandex.ru/preview/565269cac7e19e9a350189f0324879d4122da050ffe1cfde65cc3ccc13ad7ff2/637e2192/SW7a7zwm6hg0dqYp80uuOD2rt87r17JLMLTG5rRd9CWqSgbQNud5w2HgECYZSLCTfVR7bjZBh8uSSQ3ktoP2eA%3D%3D?uid=0&filename=%D0%91%D0%BB%D0%BE%D0%BA%D0%BD%D0%BE%D1%82.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание блокнота', 300, False),
         Good('doping1', 'Таблетница 1', 'https://downloader.disk.yandex.ru/preview/01e03ed032957cdc504edd507fdbaa933cbb007eacfff8fa1d95f7e9faace11d/637e21aa/MN2Bk29cAHuWL9RicuyW435OkJChHTg5HmV7a3Dy_UzR055kEF4j7TxbCU6SBGEp5Bmi3GbDKZ7c2Em8lEbasw%3D%3D?uid=0&filename=%D0%94%D0%BE%D0%BF%D0%B8%D0%BD%D0%B31.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание таблетницы 1', 200, False),
         Good('doping2', 'Таблетница 2', 'https://downloader.disk.yandex.ru/preview/4b887b7e9d6afdc67ef1314838f81075c409c226fc1bfd1276b63a3ee719c517/637e21be/QHxQE270CVgBXe0vbECRvdOiNFoh7dGQoW_rj8KjDfdNaQ7S6xu74MvQyzGOreZ1_gsj1g06JklHV9N9ggCoRg%3D%3D?uid=0&filename=%D0%94%D0%BE%D0%BF%D0%B8%D0%BD%D0%B32.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание таблетницы 2', 200, False),
         Good('cup', 'Кружка', 'https://downloader.disk.yandex.ru/preview/5759990749c9dfaf3adfa8c2426e056ee5d8770cbbfb6f2ae0528fb41ae20ae3/637e21d7/54udLxnJw_YfCcz1RLIhYn5OkJChHTg5HmV7a3Dy_UzsTzCQUyHhkrkg9aNXi0EbyDHMNQJihh5i_PCo1YbnkQ%3D%3D?uid=0&filename=%D0%9A%D1%80%D1%83%D0%B6%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048', 'Описание кружки', 400, False),
         Good('therm_mug', 'Термокружка', 'https://downloader.disk.yandex.ru/preview/48521d21551cd76981de819c835d92a46feb3b18caf63720d216635c7d99374d/637e2235/cl8slIqwhSnrUtW9m_aDY9OiNFoh7dGQoW_rj8KjDfdV00_bUnI_sOu8xzFxBd7TEhpojkn3BjlsRhQNrLfHfw%3D%3D?uid=0&filename=%D0%A2%D0%B5%D1%80%D0%BC%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048', 'Описание термокружки', 450, False),
         Good('plaid', 'Плед', 'https://downloader.disk.yandex.ru/preview/f37921d4b99cd2df6bdb09855fb702da553fead34774281d394d0b2592419937/637e220b/hRwzepJKQBDDh_qjer2VTtPL9EKIhaHyIz0Lq1cpNRTO1SXzOBFZ8RIcpNCty1aT1cpIKPLO2ATd4ieCKITFBw%3D%3D?uid=0&filename=%D0%9F%D0%BB%D0%B5%D0%B4.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание пледа', 500, False),
         Good('stickers', 'Стикеры', 'https://downloader.disk.yandex.ru/preview/59443195dd28e81fb0015e5c5e88376be86eebb99b9894960d6579695ba11a78/637e221b/yJH_ATwgWZXudrsWliezcZ58w0pTF3LtEav6JWhRlHVMycwHnmEmZzGFg4a_yVbDlx-NTeGrOBJ4-9ik10EXzg%3D%3D?uid=0&filename=%D0%A1%D1%82%D0%B8%D0%BA%D0%B5%D1%80%D1%8B.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание стикеров', 100, False),
         Good('ball', 'Новогодний шар', 'https://downloader.disk.yandex.ru/preview/f6448ab4e5cbd04aeb1315b8d6ca15601baed2000487af770f7ed3ba52e89546/637e22a2/pA5zBOz1fuxOwT6yucvbqdOiNFoh7dGQoW_rj8KjDfezLvaGv6EJjIUzYBPGn6__EegygdvD8bSkwtX8VvvQlw%3D%3D?uid=0&filename=%D0%A8%D0%B0%D1%80.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание новогоднего шара',    250,    False),
         Good('shopper1', 'Шопер 1', 'https://downloader.disk.yandex.ru/preview/c7f9695f25f3831b9de6c73ec6071e377cfcdc1e38606ea997c678f0f0160945/637e22ba/b5oOeI0p5ds9Cv3xjkuKYp58w0pTF3LtEav6JWhRlHVMYSty31aWaTppZhPEB3STtwSMjKeQFGuUBId3Z0tJkQ%3D%3D?uid=0&filename=%D0%A8%D0%BE%D0%BF%D0%B5%D1%801.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание шопера 1', 999, False),
         Good('shopper2', 'Шопер 2', 'https://downloader.disk.yandex.ru/preview/0f73f7bc69d1f246eac745ce000bfeac5e1d102f26554c0472e84da573a7abf2/637e22cd/nVLtOjqqkW8XXdDZT7YWvtOiNFoh7dGQoW_rj8KjDfe2EedX-ayFSav7CyHg731OUMU5TtTL5als8KuKezOaRw%3D%3D?uid=0&filename=%D0%A8%D0%BE%D0%BF%D0%B5%D1%802.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание шопера 2', 500, False)]


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(types.KeyboardButton("Боже, храни ВТФМ!\u2764\uFE0F❤❤!"))
    mess = 'Дорогие друзья! Мы рады приветсвовать Вас на ВТФМ 2022!'
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


def start2(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(types.KeyboardButton("Привет БОТ!"))
    mess = 'Мы стремимся идти в ногу со временем и сделали для вас Супер бота для мерча!'
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


def start3(message):
    bot.send_message(message.from_user.id, 'Легкий FAQ!\n\n'
                                           'Как это работает?\n\n'
                                           '- Выбирай мерч для себя и друзей\n\n'
                                           '- Оплачивай прямо здесь\n\n'
                                           '- Волонтер принесет и торжественно вручит покупку!\n\n'
                                           '- Только самовывоз и только во время проведения ВТФМ 8-12 декабря😎', reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton("ДА!"), types.KeyboardButton("НЕТ!"))
    mess = 'Познакомимся с Ассортиментом ВТФМ 2022?'
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Я умею общаться только с помощью меню и кнопок")


@bot.message_handler(commands=['shop'])
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton("Одежда"), types.KeyboardButton("Сувенирка ВФТМ"))
    mess = "Одежда или сувениры?"
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


def myFunc(e):
    return e.availability


def clothes(message):
    i = 0
    goods.sort(key=myFunc)
    pad = types.InlineKeyboardMarkup()
    for good in goods:
        if good.is_clothes and good.availability:
            pad = pad.add(types.InlineKeyboardButton(text=good.name, callback_data=good.name))
            if i == range(len(goods)) or goods[i+1].id != good.id:
                bot.send_photo(message.from_user.id, good.photo, reply_markup=pad)
                pad = types.InlineKeyboardMarkup()
        i += 1


def accessories(message):
    for good in goods:
        if not good.is_clothes and good.availability:
            pad = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text=good.name, callback_data=good.name))
            bot.send_photo(message.from_user.id, good.photo, reply_markup=pad)


def search_good(name):
    for good in goods:
        if good.name == name:
            return good


def buy(message, good):
    bot.send_invoice(message.from_user.id,
                     title=good.name,
                     description=good.description,
                     photo_url=good.photo,
                     provider_token=PAYMENTS_TOKEN,
                     currency="rub",
                     prices=[types.LabeledPrice(label=good.name, amount=good.price*100)],
                     need_name=True,
                     need_phone_number=True,
                     invoice_payload=good.name)


@bot.pre_checkout_query_handler(lambda query: True)
def checkout(checkout_q):
    mess = "Извините, кто-то только что купил последний такой товар, пока вы заполняли платежные реквизиты."
    bot.answer_pre_checkout_query(checkout_q.id, ok=search_good(checkout_q.invoice_payload).availability, error_message=mess)


@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message):
    bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAEGFbVje2QQ_w5QhFFMUowHORFG4vI-pQAC1B0AAqdekUu4h9vEFWLtyisE')
    bot.send_message('-882047975', f'\tИмя в телеграм:\n<b>{message.from_user.first_name, message.from_user.last_name, message.from_user.username}</b>\n'
                                   f'\tИмя при оплате:<b><font color=green>\n{message.successful_payment.order_info.name}</font></b>\n'
                                   f'\tОплатил:\n<b>{message.successful_payment.invoice_payload}</b>\n'
                                   f'\tСтоимостью:\n<b>{message.successful_payment.total_amount/100} RUB</b>\n'
                                   f'\tНомер телефона:\n<b>{message.successful_payment.order_info.phone_number}</b>', reply_markup=types.ReplyKeyboardRemove(), parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    buy(call, search_good(call.data))


@bot.message_handler(chat_types=['group'])
def get_text_messages(message):
    if message.chat.id == -882047975 and message.text == '/наличие товаров':
        bot.send_message('-882047975', "Через это меню можно будет менять наличие любого товара.", reply_markup=types.ReplyKeyboardRemove())
        for good in goods:
            bot.send_message('-882047975', f'{good.name} = {good.availability_text}')
        bot.send_message('-882047975', 'Для смены отображения в боте наличия того или иного товара нужно:\n'
                                       'Переслать один из товаров выше в этот же чат с надписью "+" или "-".\n'
                                       '\t"+" есть в наличии\n'
                                       '\t"-" нет в наличии.')
    elif message.chat.id == -882047975 and (message.text == '-' or message.text == '+') and message.reply_to_message:
        for good in goods:
            if message.reply_to_message.text == f'{good.name} = {good.availability_text}' and good.availability:
                good.availability = False
                good.availability_text = 'нет в наличии'
                bot.send_message('-882047975', f'{good.name} = {good.availability_text}', reply_to_message_id=message.id)
            elif message.reply_to_message.text == f'{good.name} = {good.availability_text}' and not good.availability:
                good.availability = True
                good.availability_text = 'есть'
                bot.send_message('-882047975', f'{good.name} = {good.availability_text}', reply_to_message_id=message.id)
    else:
        bot.send_message(message.chat.id, "Я вам тут не мешаю?", reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(content_types=['text', 'voice', 'photo', 'video', 'audio', 'document', 'sticker'])
def get_text_messages(message):
    # if message.chat.id == -882047975 and message.text == '/наличие товаров':
    #     bot.send_message('-882047975', "Через это меню можно будет менять наличие любого товара.", reply_markup=types.ReplyKeyboardRemove())
    #     for good in goods:
    #         bot.send_message('-882047975', f'{good.name} = {good.availability_text}')
    #     bot.send_message('-882047975', 'Для смены отображения в боте наличия того или иного товара нужно:\n'
    #                                    'Переслать один из товаров выше в этот же чат с надписью "+" или "-".\n'
    #                                    '\t"+" есть в наличии\n'
    #                                    '\t"-" нет в наличии.')
    # elif message.chat.id == -882047975 and (message.text == '-' or message.text == '+') and message.reply_to_message:
    #     for good in goods:
    #         if message.reply_to_message.text == f'{good.name} = {good.availability_text}' and good.availability:
    #             good.availability = False
    #             good.availability_text = 'нет в наличии'
    #             bot.send_message('-882047975', f'{good.name} = {good.availability_text}', reply_to_message_id=message.id)
    #         elif message.reply_to_message.text == f'{good.name} = {good.availability_text}' and not good.availability:
    #             good.availability = True
    #             good.availability_text = 'есть'
    #             bot.send_message('-882047975', f'{good.name} = {good.availability_text}', reply_to_message_id=message.id)
    if message.voice:
        bot.send_message(message.from_user.id, 'Я в метро, наушников нет...')
    elif message.photo:
        bot.send_message(message.from_user.id, 'Классная фотка!')
    elif message.video:
        bot.send_message(message.from_user.id, 'Видео как видео, мне больше другого типа нравятся')
    elif message.audio:
        bot.send_message(message.from_user.id, 'Потом послушаю')
    elif message.document:
        bot.send_message(message.from_user.id, 'Ну и что в нем? Сценарий к 2023?')
    elif message.sticker:
        bot.send_message(message.from_user.id, 'Я тоже мог бы отправить тебе стикер, НО не буду')
    elif message.text == "Боже, храни ВТФМ!\u2764\uFE0F❤❤!":
        start2(message)
    elif message.text == "Привет БОТ!":
        start3(message)
    elif message.text == "ДА!" or message.text == "Ну давайте!":
        menu(message)
    elif message.text == "Одежда":
        clothes(message)
    elif message.text == "Сувенирка ВФТМ":
        accessories(message)
    elif message.text == "НЕТ!":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(types.KeyboardButton("Ну давайте!"), types.KeyboardButton("НЕТ!"))
        mess = 'Коллега, этот бот умеет только продавать... Познакомимся с Ассортиментом ВТФМ 2022?'
        bot.send_message(message.from_user.id, mess, reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Это что-то на иврите? Я не понимаю. Напиши /help.")


bot.infinity_polling()


def print_hi(name):
    print(f'БОТ {name}')


if __name__ == '__main__':
    print_hi('ПРЕКРАТИЛ РАБОТУ!')
    bot.send_message('-882047975', "БОТ ПРЕКРАТИЛ РАБОТУ!!!")
