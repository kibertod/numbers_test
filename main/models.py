from django.db.models import *


class Order(Model):
    usd_price = FloatField()
    rub_price = FloatField()
    term = DateField()
    expires_today = BooleanField(default=False)
    expired = BooleanField(default=False)


class TelegramUser(Model):
    tg_id = IntegerField()
