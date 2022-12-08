#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import types
from telebot import types

bot = telebot.TeleBot('5810807628:AAFbLp5CQpn-YANuVytQbUqPBplKW8semqw')
SBERBANK_TEST_TOKEN = '401643678:TEST:102d50ef-3365-4973-8857-5527eed10b93'
SBERBANK_LIVE_TOKEN = '410182388:LIVE:2dbe1ced-9f4f-431c-8936-d6ad603518dc'
UKASSA_TEST_TOKEN = '381764678:TEST:46304'
PAYMENTS_TOKEN = SBERBANK_LIVE_TOKEN
GROUP_CHAT_ID = -1001485436799


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


goods = [Good('hoodie', 'Худи oversize', 'https://downloader.disk.yandex.ru/preview/b0107dab45b96698fc71ef3e733c03184274f9921311e6abb4106d395d3361b9/6391a7d0/wMwcbZRjal0nVHZy81uINs3S99oXXjK-fpMRcXBvxLKMMKIxOgJ37QzrxiJl02AUR0968Obopc2JZeF0jhn0bQ%3D%3D?uid=0&filename=1Q8A5267.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1879x939', 'Худи черный оверсайз “Мы справимся”', 4500, True),
         Good('shirt', 'Футболка oversize', 'https://downloader.disk.yandex.ru/preview/68856387281b0bf41aded0e736e249342a995db1453255235c8149e5b5f6858a/6391a7d0/qCrrybicoRyrML92Cz1zdc3S99oXXjK-fpMRcXBvxLK3hp9DuRPSYCMpLchl6gr5fV33lOqpS8ou8Cik6sTcnw%3D%3D?uid=0&filename=1Q8A5270.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1879x939', 'Футболка черная оверсайз “Продюсер”', 2500, True),
         Good('shirt', 'Футболка oversize long', 'https://downloader.disk.yandex.ru/preview/68856387281b0bf41aded0e736e249342a995db1453255235c8149e5b5f6858a/6391a7d0/qCrrybicoRyrML92Cz1zdc3S99oXXjK-fpMRcXBvxLK3hp9DuRPSYCMpLchl6gr5fV33lOqpS8ou8Cik6sTcnw%3D%3D?uid=0&filename=1Q8A5270.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1879x939', 'Футболка черная оверсайз - лонг “Продюсер”', 2500, True),
         Good('sock', 'Носки one size', 'https://downloader.disk.yandex.ru/preview/bfee83b30c30803d4f8cb044a24289b94171fa224298e6decd5b411c9bef280b/6391ac16/vR0yglLIvLHWmU9BOSZcCNOiNFoh7dGQoW_rj8KjDfd8ftRf8h2eumm-KrOAWZY8AOjIF1IZCyXritQtcVO3dQ%3D%3D?uid=0&filename=%D0%9D%D0%BE%D1%81%D0%BA%D0%B8.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Носки черные универсального размера с надписью “Тренируй душу - ходи в театр”', 600, True),
         Good('hat', 'Шапка', 'https://downloader.disk.yandex.ru/preview/96fdf0e017c9a818f7d45edb6231779afcf846b7f592a867624fd3a83624d549/6391a7d0/yCX36zxRIXniYP6YxoS4ls3S99oXXjK-fpMRcXBvxLKg75IvbppXh62wyWX1hjIPidy0QWkbLmV0X-ky8u6qWQ%3D%3D?uid=0&filename=1Q8A5292.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1879x939', 'Шапка черная с вышивкой “Продюсер”', 1500, True),
         Good('doping', 'Таблетница', 'https://downloader.disk.yandex.ru/preview/a1efccff5c346e13670174a9799365ca9b819b81150a556481ff8a528256328a/6391a7d0/aPyg8TtVb8OoJ-mjr3Odlc3S99oXXjK-fpMRcXBvxLIPxcJ6gzFY1-edvHHFhhQ9r7QbkNTODzOWCp0CU91RiA%3D%3D?uid=0&filename=1Q8A5280.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=571x430&crop=1', 'Драже аскорбиновой кислоты в металлической коробке “Для тех, кто уже не вывозит”', 350, False),
         Good('therm_mug', 'Термокружка', 'https://downloader.disk.yandex.ru/preview/fccec5e5818c1cc7487cffe7d1b58affe31af028b3d5f2a7a8b1cde19e45123f/6391a7d0/rtcXnbjXlsgbO09CTdHDys3S99oXXjK-fpMRcXBvxLJAPI1nLhEKnlJNQlGmcKlw_HYcODNWoV_cP46CSjdM0g%3D%3D?uid=0&filename=1Q8A5278.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=284x430&crop=1', 'Термостакан софт-тач с гравировкой “У меня антракт”', 2000, False),
         Good('plaid', 'Плед', 'https://downloader.disk.yandex.ru/preview/94c261d2a1284626c9da461741405d814ac079d7693d419e69e417928716ecf6/6391a7d0/0_0kwqBkC-2_aRc9DSrS3s3S99oXXjK-fpMRcXBvxLJRKeGEotWy5eEReKLrLlA7kQTbmc6yp3sG9cBWm2UMoA%3D%3D?uid=0&filename=1Q8A5288.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=427x538&crop=1', 'Плед флисовый с вышивкой на бирке “Теплый прием”', 1500, False),
         Good('ball', 'Новогодний шар', 'https://downloader.disk.yandex.ru/preview/c4ac578a7566a953186cb06e448c1a8e1f8198957da94b421dcec62ac4133bc9/6391a7d0/qrGVlQOA7m1jYbNeIrsXiByOnfBjvtaiFhbxTLyHxrBuMpWPsx6k37lee4WwTsPQo68jKvyIGDhYRP_A6CFnTA%3D%3D?uid=0&filename=1Q8A5284.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=857x646&crop=1', 'Елочный шар “С любовью, ВФТМ”', 500, False),
         Good('shopper', 'Шоппер', 'https://downloader.disk.yandex.ru/preview/c7aaecfb646482476ba4b6116d86668cfdbb6ebc516bedae3f50c5abcfe9cafd/6391abb9/Ow5RB96JE_ntl2rz6SEMZs3S99oXXjK-fpMRcXBvxLKpzpGzp5O02GI8Qen-PTUanpdc3FAcMaNvw5tK_7HNeg%3D%3D?uid=0&filename=1Q8A5272.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=1920x942', 'Шоппер из чёрной саржи с принтом “Реквизит”', 850, False)]


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(types.KeyboardButton("Боже, храни ВФТМ! \u2764\uFE0F\u2764\uFE0F\u2764\uFE0F"))
    mess = 'Дорогие друзья! Мы рады приветствовать Вас на ВФТМ 2022!'
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
                                           '- Только самовывоз и только во время проведения ВФТМ 8-12 декабря😎', reply_markup=types.ReplyKeyboardRemove())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(types.KeyboardButton("ДА!"), types.KeyboardButton("НЕТ!"))
    mess = 'Познакомимся с Ассортиментом ВФТМ 2022?'
    bot.send_message(message.from_user.id, mess, reply_markup=keyboard)

@bot.message_handler(commands=['shop'])
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    keyboard.add(types.KeyboardButton("Одежда"), types.KeyboardButton("Сувенирка"), types.KeyboardButton("Лекции"))
    mess = "Одежда, сувениры или лекции?"
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
    mess = "Упс..мы кажется все продали \U0001F62C Рекомендую обратиться к организаторам!"
    bot.answer_pre_checkout_query(checkout_q.id, ok=search_good(checkout_q.invoice_payload).availability, error_message=mess)


@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message):
    bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAEGFbVje2QQ_w5QhFFMUowHORFG4vI-pQAC1B0AAqdekUu4h9vEFWLtyisE')
    bot.send_message(GROUP_CHAT_ID, f'\tИмя в телеграм:\n<b>{message.from_user.first_name, message.from_user.last_name, message.from_user.username}</b>\n'
                                       f'\tИмя при оплате:<b>\n{message.successful_payment.order_info.name}</b>\n'
                                       f'\tОплатил:\n<b>{message.successful_payment.invoice_payload}</b>\n'
                                       f'\tСтоимостью:\n<b>{message.successful_payment.total_amount/100} RUB</b>\n'
                                       f'\tНомер телефона:\n<b>{message.successful_payment.order_info.phone_number}</b>', reply_markup=types.ReplyKeyboardRemove(), parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    buy(call, search_good(call.data))


@bot.message_handler(content_types=['text', 'voice', 'photo', 'video', 'audio', 'document', 'sticker'])
def get_text_messages(message):
    if message.chat.id == GROUP_CHAT_ID and message.text == '/наличие':
        bot.send_message(GROUP_CHAT_ID, "Через это меню можно будет менять наличие любого товара.", reply_markup=types.ReplyKeyboardRemove())
        for good in goods:
            bot.send_message(GROUP_CHAT_ID, f'{good.name} = {good.availability_text}')
        bot.send_message(GROUP_CHAT_ID, 'Для смены отображения в боте наличия того или иного товара нужно:\n'
                                           'Переслать один из товаров выше в этот же чат с надписью "+" или "-".\n'
                                           '\t"+" есть в наличии\n'
                                           '\t"-" нет в наличии.')
    elif message.chat.id == GROUP_CHAT_ID and message.reply_to_message:
        for good in goods:
            if message.text == '-' and message.reply_to_message.text == f'{good.name} = {good.availability_text}' and good.availability:
                good.availability = False
                good.availability_text = 'нет в наличии'
                bot.send_message(GROUP_CHAT_ID, f'{good.name} = {good.availability_text}', reply_to_message_id=message.id)
            elif message.text == '+' and message.reply_to_message.text == f'{good.name} = {good.availability_text}' and not good.availability:
                good.availability = True
                good.availability_text = 'есть'
                bot.send_message(GROUP_CHAT_ID, f'{good.name} = {good.availability_text}', reply_to_message_id=message.id)
    elif message.text == "Боже, храни ВФТМ! \u2764\uFE0F\u2764\uFE0F\u2764\uFE0F":
        start2(message)
    elif message.text == "Привет БОТ!":
        start3(message)
    elif message.text == "ДА!" or message.text == "Ну давайте!":
        menu(message)
    elif message.text == "Одежда":
        clothes(message)
    elif message.text == "Сувенирка":
        accessories(message)
    elif message.text == "Лекции":
        bot.send_message(message.from_user.id, 'http://vftmfest.ru/lecture')
    elif message.text == "НЕТ!":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(types.KeyboardButton("Ну давайте!"), types.KeyboardButton("НЕТ!"))
        mess = 'Коллега, этот бот умеет только продавать... Познакомимся с Ассортиментом ВФТМ 2022?'
        bot.send_message(message.from_user.id, mess, reply_markup=keyboard)
    else:
        if not message.chat.id == GROUP_CHAT_ID:
            if message.text: 
                bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAEGsmBjjiOi5DQWPXweQAsEWnxm4NydewACeCMAAhVEkEsJ59SLsvBtqCsE')
            elif message.document:
                bot.send_message(message.from_user.id, 'Ну и что в нем? Сценарий к 2023?')
            else:
                bot.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAEGsmJjjiOxgYCoadMbk1ms18YSrwz-GQACMSIAAr7DmEuSTkj5I6jAuysE')



bot.infinity_polling()


def print_hi(name):
    print(f'БОТ {name}')


if __name__ == '__main__':
    print_hi('ПРЕКРАТИЛ РАБОТУ!')
    bot.send_message(GROUP_CHAT_ID, "БОТ ПРЕКРАТИЛ РАБОТУ!!!")
