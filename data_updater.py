from requests import get
import json
from main.models import *
from datetime import date, timedelta
from xml.etree import ElementTree
from time import sleep
import telebot
import os


bot = telebot.TeleBot("5411411957:AAHytHjnViT_oOvirMHa1H_1P_RSBCctH5U", parse_mode=None)


def update():
    data = json.loads(
        get(f"https://sheets.googleapis.com/v4/spreadsheets/{os.environ.get('GOOGLE_API_KEY')}/"
            "values/Лист1?key=AIzaSyDODmMUDqS6eLfk7jYDpu9asp_cTsDxUfU").text
    )

    today = date.today()
    month = str(today.month).rjust(2, "0")
    day = str(today.day).rjust(2, "0")
    year = today.year
    rate_root = ElementTree.fromstring(
        get(f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}").text
    )

    for currency in rate_root:
        if currency[3].text == "Доллар США":
            usd_rate = float(currency[4].text.replace(",", "."))
            break
    else:
        usd_rate = 53

    active_orders = []

    for value in data.get("values")[1:]:

        order_id = value[1]
        usd_price = float(value[2])
        rub_price = round(usd_price * usd_rate, 2)
        term = date.fromisoformat("-".join(value[3].split(".")[::-1]))

        active_orders.append(order_id)

        if not Order.objects.filter(id=order_id):
            order = Order.objects.create(
                id=order_id,
                usd_price=usd_price,
                rub_price=rub_price,
                term=term,
            )
        else:
            order = Order.objects.get(id=order_id)

            order.usd_price = usd_price
            order.rub_price = rub_price

            if order.term != term:
                order.term = term
                order.expired = False
                order.expires_today = False

            if date.today() == order.term and not order.expires_today:
                order.expires_today = True

                for user in TelegramUser.objects.all():
                    bot.send_message(user.tg_id, f"Сегодня истекает срок поставки №{order.id}")

            elif date.today() == order.term + timedelta(days=1):
                order.expired = True

                for user in TelegramUser.objects.all():
                    bot.send_message(user.tg_id, f"Срок поставки №{order.id} истёк")

            order.save()

    for order in Order.objects.all():
        if order.id not in active_orders:
            order.delete()


def start():
    while True:
        print("updating data")
        update()
        sleep(60)
