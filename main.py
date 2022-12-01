#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import types
from telebot import types

bot = telebot.TeleBot('5810807628:AAFbLp5CQpn-YANuVytQbUqPBplKW8semqw')
PAYMENTS_TOKEN = '381764678:TEST:46304'
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


goods = [Good('hoodie', 'Худи oversize', 'https://downloader.disk.yandex.ru/preview/e8ffd5e66f6e48e6b68d87e3a1424ace5c0813e4c6f813c36d90b5ab97c79835/637e228f/rfxXmPbxn4XpIWyLBCMqqYQEwxCg4I2e0_B2dpixROBfKhpOOVBEII0AcpGlJrApNxYxKX7HHKs5VErryCFbyw%3D%3D?uid=0&filename=%D0%A5%D1%83%D0%B4%D0%B8.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Худи черный оверсайз “Мы справимся”', 4500, True),
         Good('shirt', 'Футболка oversize', 'https://downloader.disk.yandex.ru/preview/7e63314552b363b88a7dbe49d49167b03d27d88ea517116fcda8275ca1e59a48/637e2275/zaG-o_OWA_lKVdmEbCXrN35OkJChHTg5HmV7a3Dy_UwDK780O1zkNTuo9B8S7mADP9pvFY_yTXMmPsC90zMOGA%3D%3D?uid=0&filename=%D0%A4%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Футболка черная оверсайз “Продюсер”', 2500, True),
         Good('shirt', 'Футболка oversize long', 'https://downloader.disk.yandex.ru/preview/7e63314552b363b88a7dbe49d49167b03d27d88ea517116fcda8275ca1e59a48/637e2275/zaG-o_OWA_lKVdmEbCXrN35OkJChHTg5HmV7a3Dy_UwDK780O1zkNTuo9B8S7mADP9pvFY_yTXMmPsC90zMOGA%3D%3D?uid=0&filename=%D0%A4%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Футболка черная оверсайз - лонг “Продюсер”', 2500, True),
         Good('sock', 'Носки one size', 'https://downloader.disk.yandex.ru/preview/72bef04504007d0b16250428569d783638b9a594531eab47b5568a249b62c3fd/63891a18/vR0yglLIvLHWmU9BOSZcCNOiNFoh7dGQoW_rj8KjDfd8ftRf8h2eumm-KrOAWZY8AOjIF1IZCyXritQtcVO3dQ%3D%3D?uid=0&filename=%D0%9D%D0%BE%D1%81%D0%BA%D0%B8.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Носки черные универсального размера с надписью “Тренируй душу - ходи в театр”', 550, True),
         Good('hat', 'Шапка', 'https://downloader.disk.yandex.ru/preview/2d7b11d124471f10693a8341ade1edf4ef64c8ac3dfa20bebef9880d1dca8aad/63891a43/CBSeuMWTOpTyAoiiJcIKtGZDamRRtza3VurjjY4Uzv_uapKUTQgFiRBiu77rzc0gJE5q2KnDGGmwewLnQAs1Rg%3D%3D?uid=0&filename=hat.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Шапка черная с вышивкой “Продюсер”', 1500, True),
         Good('doping', 'Таблетница', 'https://downloader.disk.yandex.ru/preview/bea5c5d2a0a349c741cd23b55f4a4e74d82ff69170ce75e4439d6d15b744acf6/63891b21/QHxQE270CVgBXe0vbECRvdOiNFoh7dGQoW_rj8KjDfdNaQ7S6xu74MvQyzGOreZ1_gsj1g06JklHV9N9ggCoRg%3D%3D?uid=0&filename=%D0%94%D0%BE%D0%BF%D0%B8%D0%BD%D0%B32.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Драже аскорбиновой кислоты в металлической коробке “Для тех, кто уже не вывозит”', 350, False),
         Good('therm_mug', 'Термокружка', 'https://downloader.disk.yandex.ru/preview/2cfc80d2eb778bb3d5c6718e780594d9ca8276b49b976a0167a1ea560a29c5e4/63891b45/cl8slIqwhSnrUtW9m_aDY9OiNFoh7dGQoW_rj8KjDfdV00_bUnI_sOu8xzFxBd7TEhpojkn3BjlsRhQNrLfHfw%3D%3D?uid=0&filename=%D0%A2%D0%B5%D1%80%D0%BC%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%BA%D0%B0.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048', 'Термостакан софт-тач с гравировкой “У меня антракт”', 1550, False),
         Good('plaid', 'Плед', 'https://downloader.disk.yandex.ru/preview/5e5298df389adb191541e0562857f98ac1c9daf42840fa08f160fe4bcdd66d76/63891b60/hRwzepJKQBDDh_qjer2VTtPL9EKIhaHyIz0Lq1cpNRTO1SXzOBFZ8RIcpNCty1aT1cpIKPLO2ATd4ieCKITFBw%3D%3D?uid=0&filename=%D0%9F%D0%BB%D0%B5%D0%B4.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Плед флисовый с вышивкой на бирке “Теплый прием”', 1500, False),
         Good('ball', 'Новогодний шар', 'https://downloader.disk.yandex.ru/preview/82d7b2a2bbccc2308a79dc70f5a83f7a5da3ce0af210977991a2041ead10453d/63891b7f/pA5zBOz1fuxOwT6yucvbqdOiNFoh7dGQoW_rj8KjDfezLvaGv6EJjIUzYBPGn6__EegygdvD8bSkwtX8VvvQlw%3D%3D?uid=0&filename=%D0%A8%D0%B0%D1%80.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Елочный шар “С любовью, ВФТМ”', 550, False),
         Good('shopper', 'Шоппер', 'https://downloader.disk.yandex.ru/preview/530683eceb4218df8bbd688447a88f7df557ab564f2c9e89e87bb3ed8db0dfd7/63891bac/nVLtOjqqkW8XXdDZT7YWvtOiNFoh7dGQoW_rj8KjDfe2EedX-ayFSav7CyHg731OUMU5TtTL5als8KuKezOaRw%3D%3D?uid=0&filename=%D0%A8%D0%BE%D0%BF%D0%B5%D1%802.png&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048', 'Шоппер из чёрной саржи с принтом “Реквизит”', 850, False)]


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
    keyboard.add(types.KeyboardButton("Одежда"), types.KeyboardButton("Сувенирка ВФТМ"), types.KeyboardButton("Лекции"))
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
    mess = "Извините, кто-то только что купил последний такой товар."
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
    elif message.voice:
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
    elif message.text == "Боже, храни ВФТМ! \u2764\uFE0F\u2764\uFE0F\u2764\uFE0F":
        start2(message)
    elif message.text == "Привет БОТ!":
        start3(message)
    elif message.text == "ДА!" or message.text == "Ну давайте!":
        menu(message)
    elif message.text == "Одежда":
        clothes(message)
    elif message.text == "Сувенирка ВФТМ":
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
            bot.send_message(message.from_user.id, "Я умею общаться только с помощью меню и кнопок")


bot.infinity_polling()


def print_hi(name):
    print(f'БОТ {name}')


if __name__ == '__main__':
    print_hi('ПРЕКРАТИЛ РАБОТУ!')
    bot.send_message(GROUP_CHAT_ID, "БОТ ПРЕКРАТИЛ РАБОТУ!!!")
