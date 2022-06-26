from threading import Thread
import tg_bot
import data_updater


# запускаем два потока со скриптами для бота и для обновления данных
Thread(target=tg_bot.start).start()
Thread(target=data_updater.start).start()