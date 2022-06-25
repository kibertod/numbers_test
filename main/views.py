from django.shortcuts import render
from main.models import *
from datetime import date


def index(request):
    data = {"orders": []}
    orders = data["orders"]

    number = 0
    for order in Order.objects.all():
        number += 1
        orders.append({
            "number": number,
            "id": order.id,
            "usd_price": order.usd_price,
            "rub_price": order.rub_price,
            "term": order.term.strftime("%d/%m/%y")
        })

    return render(request, "index.html", data)

