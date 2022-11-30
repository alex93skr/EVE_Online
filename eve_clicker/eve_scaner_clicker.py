import configparser
import random
import time
import winsound
from threading import Thread, Lock

import keyboard

config = configparser.ConfigParser()
config.read('settings.ini')
KEY_WAIT = config.get("Settings", "key_wait")
KEY_PUSH = config.get("Settings", "key_push")
SLEEP_START = int(config.get("Settings", "sleep_start"))
SLEEP_END = int(config.get("Settings", "sleep_end"))

lock = Lock()

# сразу закрыть
lock.acquire()
print(lock)
print(lock.locked())

# pyinstaller --onefile D:\code\eve_clicker\eve_scaner_clicker.py


# Lock.acquire() устанавливает блокировку,
# Lock.release() снимает блокировку,
# Lock.locked() проверяет состояние блокировки,


def switch():
    while True:
        keyboard.wait(KEY_WAIT)

        # если закрыт - запускаем
        if lock.locked():
            print('go')
            winsound.Beep(600, 400)
            lock.release()
            Thread(target=worker).start()


        # если открыт - стопаем
        else:
            print('stop')
            winsound.Beep(300, 800)
            lock.acquire()


def worker():
    while True:
        if lock.locked():
            break
        print('- click')
        keyboard.press(KEY_PUSH)
        # random.randint(4, 7)
        time.sleep(random.randint(SLEEP_START, SLEEP_END))


def main():
    Thread(target=switch).start()
    # Thread(target=worker).start()


main()

# ттаймингит
# бтипт
