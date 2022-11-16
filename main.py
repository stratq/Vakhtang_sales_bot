#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import types
from telebot import types

bot = telebot.TeleBot('5664614354:AAGn8lPRmOXytJkPXaZwAWYdWLmE9V4m8Ok')
PAYMENTS_TOKEN = '401643678:TEST:337a0c19-863c-4175-a31f-2cc1b1f88196'
PAYMENTS_TOKEN_kass = '381764678:TEST:44295'
global ITEM
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


class Good:
    def __init__(self, id, name, photo, description, price, has_size, is_clothes):
        self.id = id
        self.name = name
        self.photo = photo
        self.description = description
        self.price = price
        self.has_size = has_size
        self.is_clothes = is_clothes


goods = [Good('hoodie',      'Худи',             'https://downloader.disk.yandex.ru/preview/92734843c16d5b55bb3177e62603852ae6738fe85d4844f5ba3081c731875597/63756dfa/rfxXmPbxn4XpIWyLBCMqqYQEwxCg4I2e0_B2dpixROBfKhpOOVBEII0AcpGlJrApNxYxKX7HHKs5VErryCFbyw%3D%3D?uid=0&filename=%D0%A5%D1%83%D0%B4%D0%B8.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048',          'Описание худака',              3000, True,   True),
         Good('shirt',       'Футболка',         'https://downloader.disk.yandex.ru/preview/6609235c426a91ba2d5695aa45b563079bb16409e1488cdcaaeb1ce9aa558f81/63756dc1/zaG-o_OWA_lKVdmEbCXrN35OkJChHTg5HmV7a3Dy_UwDK780O1zkNTuo9B8S7mADP9pvFY_yTXMmPsC90zMOGA%3D%3D?uid=0&filename=%D0%A4%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048',      'Описание футболки',            2000, True,   True),
         Good('sock',        'Носки',            'https://downloader.disk.yandex.ru/preview/27f31fc675292e51ffaf2fd88a7f761047eab7cac8b6d5474f75acf7c432c9d3/63756d78/vR0yglLIvLHWmU9BOSZcCNOiNFoh7dGQoW_rj8KjDfd8ftRf8h2eumm-KrOAWZY8AOjIF1IZCyXritQtcVO3dQ%3D%3D?uid=0&filename=%D0%9D%D0%BE%D1%81%D0%BA%D0%B8.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048',         'Описание носков',              500, '',     True),
         Good('hat',         'Шапка',            'https://downloader.disk.yandex.ru/preview/e6e9ce3ff1f25c9f782584f5918aa5fad8470d49052a3a7bd403a80e362490b2/63756d1f/CBSeuMWTOpTyAoiiJcIKtGZDamRRtza3VurjjY4Uzv_uapKUTQgFiRBiu77rzc0gJE5q2KnDGGmwewLnQAs1Rg%3D%3D?uid=0&filename=hat.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048',         'Описание шапки',               1000, '',     True),
         Good('notebook',    'Блокнот',          'https://downloader.disk.yandex.ru/preview/06349c3037e03bc5146a1829bd5410a7e5d3c742051e95816f1e3368dd33bd2b/63756d2e/SW7a7zwm6hg0dqYp80uuOD2rt87r17JLMLTG5rRd9CWqSgbQNud5w2HgECYZSLCTfVR7bjZBh8uSSQ3ktoP2eA%3D%3D?uid=0&filename=%D0%91%D0%BB%D0%BE%D0%BA%D0%BD%D0%BE%D1%82.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048',       'Описание блокнота',            300, '',     False),
         Good('doping1',     'Таблетница 1',     'https://downloader.disk.yandex.ru/preview/2c0b0f7ccbea283a79237fd3d37ba7e944578130256f230ccb4f09092ebfd9e6/63756d46/MN2Bk29cAHuWL9RicuyW435OkJChHTg5HmV7a3Dy_UzR055kEF4j7TxbCU6SBGEp5Bmi3GbDKZ7c2Em8lEbasw%3D%3D?uid=0&filename=%D0%94%D0%BE%D0%BF%D0%B8%D0%BD%D0%B31.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048',       'Описание таблетницы 1',        200, '',     False),
         Good('doping2',     'Таблетница 2',     'https://downloader.disk.yandex.ru/preview/87ff5b724b2ba1aea255cc7f9f4246e737d62393a2b09c5f9583b04b5a37f353/63756d5a/QHxQE270CVgBXe0vbECRvdOiNFoh7dGQoW_rj8KjDfdNaQ7S6xu74MvQyzGOreZ1_gsj1g06JklHV9N9ggCoRg%3D%3D?uid=0&filename=%D0%94%D0%BE%D0%BF%D0%B8%D0%BD%D0%B32.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048',       'Описание таблетницы 2',        200, '',     False),
         Good('cup',         'Кружка',           'https://downloader.disk.yandex.ru/preview/1597e121eedeca47ba1542bbfef53f6b348cac42809c663a3cb81d8e18173616/63756d64/54udLxnJw_YfCcz1RLIhYn5OkJChHTg5HmV7a3Dy_UzsTzCQUyHhkrkg9aNXi0EbyDHMNQJihh5i_PCo1YbnkQ%3D%3D?uid=0&filename=%D0%9A%D1%80%D1%83%D0%B6%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048',        'Описание кружки',              400, '',     False),
         Good('thermo_mug',  'Термокружка',      'https://downloader.disk.yandex.ru/preview/d4a083141d16fd4b53c39e5430ae440fe76401016e531d8f1b11e43e9942fd65/63756db2/cl8slIqwhSnrUtW9m_aDY9OiNFoh7dGQoW_rj8KjDfdV00_bUnI_sOu8xzFxBd7TEhpojkn3BjlsRhQNrLfHfw%3D%3D?uid=0&filename=%D0%A2%D0%B5%D1%80%D0%BC%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048',   'Описание термо кружки',        450, '',     False),
         Good('plaid',       'Плед',             'https://downloader.disk.yandex.ru/preview/3578d9655794161a4872394670552264c243aa9ff1cd9f5b581fe309c6cd543f/63756d84/hRwzepJKQBDDh_qjer2VTtPL9EKIhaHyIz0Lq1cpNRTO1SXzOBFZ8RIcpNCty1aT1cpIKPLO2ATd4ieCKITFBw%3D%3D?uid=0&filename=%D0%9F%D0%BB%D0%B5%D0%B4.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048',          'Описание пледа',               1500, '',     False),
         Good('stickers',    'Стикеры',          'https://downloader.disk.yandex.ru/preview/441a92b4ebe3ceeb5b60dadf76e353ecb11985934bc1de906a9a804578253343/63756da2/yJH_ATwgWZXudrsWliezcZ58w0pTF3LtEav6JWhRlHVMycwHnmEmZzGFg4a_yVbDlx-NTeGrOBJ4-9ik10EXzg%3D%3D?uid=0&filename=%D0%A1%D1%82%D0%B8%D0%BA%D0%B5%D1%80%D1%8B.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048',       'Описание стикеров',            100, '',     False),
         Good('ball',        'Новогодний шар',   'https://downloader.disk.yandex.ru/preview/a87f5f404358de66aaf21b966291e998324cf540c663ab9fc560ff4efe71bd48/63756e08/pA5zBOz1fuxOwT6yucvbqdOiNFoh7dGQoW_rj8KjDfezLvaGv6EJjIUzYBPGn6__EegygdvD8bSkwtX8VvvQlw%3D%3D?uid=0&filename=%D0%A8%D0%B0%D1%80.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048',           'Описание новогоднего шара',    250, '',     False),
         Good('shopper1',    'Шопер 1',          'https://downloader.disk.yandex.ru/preview/c377da532829e3a1b6f9dc409200a195b99612d96e133020f6a51e4bcbb3e386/63756e16/b5oOeI0p5ds9Cv3xjkuKYp58w0pTF3LtEav6JWhRlHVMYSty31aWaTppZhPEB3STtwSMjKeQFGuUBId3Z0tJkQ%3D%3D?uid=0&filename=%D0%A8%D0%BE%D0%BF%D0%B5%D1%801.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048',        'Описание шопера 1',            1200, '',     False),
         Good('shopper2',    'Шопер 2',          'https://downloader.disk.yandex.ru/preview/441017d36d1c2e14554ed8a1a314add1fe18925682c6943c424186228123020e/63756e21/nVLtOjqqkW8XXdDZT7YWvtOiNFoh7dGQoW_rj8KjDfe2EedX-ayFSav7CyHg731OUMU5TtTL5als8KuKezOaRw%3D%3D?uid=0&filename=%D0%A8%D0%BE%D0%BF%D0%B5%D1%802.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Описание шопера 1',            1200, '',     False)]


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(types.KeyboardButton("Боже, храни ВТФМ!\u2764\uFE0F❤!"))
    mess = 'Дорогие друзья! Мы рады приветсвовать Вас на ВТФМ 2022!'
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


def start2(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(types.KeyboardButton("Привет БОТ!"))
    mess = 'Мы стремимся идти в ногу со временем и сделали для вас Супер бота для мерча!'
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


def start3(message):
    bot.send_message(message.from_user.id, 'Легкий FAQ!\n\nКак это работает?\n\n- Выбирай мерч для себя и друзей\n\n- Оплачивай прямо здесь\n\n- Волонтер принесет и торжественно вручит покупку!')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton("ДА!"), types.KeyboardButton("НЕТ!"))
    mess = 'Познакомимся с Ассортиментом ВТФМ 2022?'
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Я умею общаться только с помощью меню и кнопок")


@bot.message_handler(commands=['deletebot'])
def stop(message):
    mess = f'Дотвидания, <b>{message.from_user.first_name} {message.from_user.last_name}</b>, или просто - петук!'
    bot.send_message(message.from_user.id, mess, parse_mode='html')
    bot.stop_bot()


@bot.message_handler(commands=['shop'])
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton("Одежда"), types.KeyboardButton("Сувенирка ВФТМ"))
    mess = "Одежда или сувениры?"
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


def clothes(message):
    for good in goods:
        if good.is_clothes:
            pad = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text=good.name, callback_data=good.id))
            bot.send_photo(message.from_user.id, good.photo, reply_markup=pad)


def accessories(message):
    for good in goods:
        if not good.is_clothes:
            pad = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text=good.name, callback_data=good.id))
            bot.send_photo(message.from_user.id, good.photo, reply_markup=pad)


def size(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    keyboard.add(types.KeyboardButton("M"),
                 types.KeyboardButton("L"),
                 types.KeyboardButton("XL"),
                 types.KeyboardButton("Назад в меню"))
    mess = f"{ITEM.name}, а какой размер?"
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)


def buy(message: types.Message):
    bot.send_message(message.from_user.id, '💌', reply_markup=types.ReplyKeyboardRemove())       # сделать чтобы клава скрывалась и был фокус на покупку
    bot.send_invoice(message.from_user.id,
                     title=f'{ITEM.name} {ITEM.has_size}',
                     description=f'{ITEM.description}',
                     photo_url=ITEM.photo,
                     provider_token=PAYMENTS_TOKEN,
                     currency="rub",
                     prices=[types.LabeledPrice(label=f"{ITEM.name}", amount=ITEM.price*100)],
                     need_phone_number=True,
                     send_phone_number_to_provider=True,
                     invoice_payload="test-invoice-payload")


@bot.pre_checkout_query_handler(lambda query: True)
def checkout(checkout_q):
    mess = "Идёт pre_checkout_query_handler, типо проверака чего-то...error_message"
    bot.answer_pre_checkout_query(checkout_q.id, ok=False, error_message=mess)

@bot.message_handler(content_types=['SUCCESSFUL_PAYMENT'])
def successful_payment(message):
    print("SUCCESSFUL_PAYMENT получается всё хорошо прошло:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")
    bot.send_sticker(chat_id=message.chat_id, sticker='https://api.telegram.org/bot<token>/sendSticker?chat_id=<id>&sticker=CAADAgADOQADfyesDlKEqOOd72VKAg')  # https://api.telegram.org/bot<token>/sendSticker?chat_id=<id>&sticker=CAADAgADOQADfyesDlKEqOOd72VKAg
    bot.send_message(message.from_user.id, f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошёл успешно!!!", parse_mode='Markdown')  # parse_mode='html'


# prices = [LabeledPrice(label='Working Time Machine', amount=5750), LabeledPrice('Gift wrapping', 500)]
# shipping_options = [
#     ShippingOption(id='instant', title='WorldWide Teleporter').add_price(LabeledPrice('Teleporter', 1000)),
#     ShippingOption(id='pickup', title='Local pickup').add_price(LabeledPrice('Pickup', 300))]
# @bot.shipping_query_handler(func=lambda query: True)
# def shipping(shipping_query):
#     print(shipping_query)
#     bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
#                               error_message='Oh, seems like our Dog couriers are having a lunch right now. Try again later!')
# #
# @bot.pre_checkout_query_handler(func=lambda query: True)
# def checkout(pre_checkout_query):
#     bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
#                                   error_message="Aliens tried to steal your card's CVV, but we successfully protected your credentials,"
#                                                 " try to pay again in a few minutes, we need a small rest.")
#
# @bot.message_handler(content_types=['successful_payment'])
# def got_payment(message):
#     bot.send_message(message.chat.id,
#                      'Hoooooray! Thanks for payment! We will proceed your order for `{} {}` as fast as possible! '
#                      'Stay in touch.\n\nUse /buy again to get a Time Machine for your friend!'.format(
#                          message.successful_payment.total_amount / 100, message.successful_payment.currency),
#                      parse_mode='Markdown')
#
#
# @bot.pre_checkout_query_handler(lambda query: True)                                                       # проверка при оплате
# def checkout(checkout_q: types.PreCheckoutQuery):
#     mess = "Aliens tried to steal your card's CVV, but we successfully protected your credentials"
#     bot.answer_pre_checkout_query(checkout_q.id, ok=True, error_message=mess)
#
# @bot.message_handler(content_types=ContentType.SUCCESSFUL_PAYMAENT)                                    # уведомление после успешной оплаты
# def successful_payment(message: types.Message):
#     print("SUCCESSFUL_PAYMAENT:")
#     payment_info = message.successful_payment.to_python()
#     for k, v in payment_info.items():
#         print(f"{k} = {v}")
#     bot.send_message(message.from_user.id, f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошёл успешно!!!")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global ITEM
    for good in goods:
        if good.id == call.data:
            ITEM = good
    if call.data == 'hoodie' or call.data == 'shirt':
        size(call)
    else:
        buy(call)


@bot.message_handler(content_types=['text', 'voice', 'photo', 'video', 'audio', 'document', 'sticker'])
def get_text_messages(message):
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
    elif message.text == "Боже, храни ВТФМ!\u2764\uFE0F❤!":
        start2(message)
    elif message.text == "Привет БОТ!":
        start3(message)
    elif message.text == "Назад в меню" or message.text == "ДА!" or message.text == "Ну давайте!":
        menu(message)
    elif message.text == "Одежда":
        clothes(message)
    elif message.text == "Сувенирка ВФТМ":
        accessories(message)
    elif message.text == "M" or message.text == "L" or message.text == "XL":
        if ITEM.id == 'hoodie' or ITEM.id == 'shirt':
            ITEM.has_size = message.text
            buy(message)
        else:
            bot.send_message(message.from_user.id, 'Сначала выбери вещь')
            menu(message)
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
    print_hi('СЛОМАЛСЯ!')
