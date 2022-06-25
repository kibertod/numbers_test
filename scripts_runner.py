from threading import Thread
import tg_bot
import data_updater


Thread(target=tg_bot.start).start()
Thread(target=data_updater.start).start()