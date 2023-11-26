''' Нельзя делать await None или await "Hello, World!". Можно await только то, что так и называют — «awaitable»
Не меняйте цифру 0 внутри asyncio.sleep(0). Без нуля она потребует родной event loop от asyncio и все сломается. Меняйте количество вызовов await.

Подробнее о том, почему asyncio.sleep(1) вызывает ошибку,
можно прочитать в статье про моделирование бомбы - https://dvmn.org/encyclopedia/async_python/coroutine_bomb/


https://www.youtube.com/watch?v=_4QY1nGFRY8  Асинхрон гайд
'''

import asyncio
import tkinter as tk

from multiprocessing import Process
from threading import Thread
from tkinter import ttk
from time import sleep


'''
# один поток без асинхронного выполнения
def main_win():
    win = tk.Tk()
    win.geometry("500x300")

    label = ttk.Label(win, text="text before press")
    label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def sleep_func():
        print(f"start sleeping 5 sec")
        sleep(5)
        print("end sleeping")
        label["text"] = "After press button"

    btn = ttk.Button(win, text="Run in one thread", command=sleep_func)
    btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    btn.pack(expand=True)

    win.mainloop()


if __name__ == "__main__":
    main_win()
'''




'''
# multiprocessing

def check_process(proc):
    if not proc.is_alive():
        label["text"] = 20
        print("label is changed")
    win.after(20000, check_process, proc)


def process():
    print("start changing label")
    sleep(20)


def new_process():
    proc = Process(target=process)
    proc.start()
    check_process(proc)


if __name__ == "__main__":
    win = tk.Tk()
    win.geometry("500x300")

    btn = tk.Button(win, text="Run another process", command=new_process)
    # btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    btn.pack(expand=True, anchor=tk.CENTER)

    label = tk.Label(win, text="0", font=5)
    label.pack(expand=True, anchor=tk.CENTER)

    win.mainloop()
'''


'''
# threading
def main_win():
    win = tk.Tk()
    win.geometry("500x300")

    def thread_sleep():
        sleep(10)
        print("label is changed")
        label["text"] = "label is changed"

    def new_thread():
        t1 = Thread(target=thread_sleep)
        t1.start()
        print("start thread")

    btn = ttk.Button(win, text="Run thread", command=new_thread)
    btn.pack(expand=True, anchor=tk.CENTER)

    label = ttk.Label(win, text="0", font=5)
    label.pack(expand=True, anchor=tk.CENTER)

    win.mainloop()


if __name__ == "__main__":
    main_win()
'''


# asincio
# Преимущество асинхронного выполнения над многопоточным в том,
# что асинхроное выполнение не тратит ресурсы на переключение между потоками, а выполняет все в одном,
# пепеключаясь между задачами
# Так же нет состояния Гонки, когда поток ожидает одну переменную, а другой поток уже изменил данные в ней

# Но есть и свои минусы. Нужно работать только с либами, поддерживающими асинхронность.
# Либа request синхронная, т.е. запрос get будет ожидать ответа от сервера до конца.
# httpx - асинхронная либа (aiohttp - backend, aiogram - tg bot)
# Django, telegrambotapi для многопоточности и из коробки не поддерживают асинхрон, но поддерживают asyncio,
# поэтому можно делать асинхронные задачи

# Подключения к бд тоже касается это правило.
# SQLite, redis, psycopg - Синхронные либы
# aiosqlite, aioredis, psycopg2 - асинхронные

async def print1():
    print(1)


async def print2():
    await asyncio.sleep(3)
    print(2)


async def print3():
    print(3)


async def corutine_print():
    task1 = asyncio.create_task(print1())
    task2 = asyncio.create_task(print2())
    task3 = asyncio.create_task(print3())

    # await task1
    # await task2
    # await task3
    # Вместо прописывания каждой таски лучше записать в кортеж и распаковать в методе asyncio.gather(*tuple)
    tasks = (task1, task2, task3)
    await asyncio.gather(*tasks)


# Можно создать класс группы тасков через контекстный менеджер   (Для Python 3.11 +)
# async def corutine_print():
#     async with asyncio.TaskGroup() as tg:
#         tg.create_task(print1())
#         tg.create_task(print2())
#         tg.create_task(print3())


# asyncio.run(corutine_print())


# Пример 2

async def do_someth(sec):
    await asyncio.sleep(sec)
    print(f"Hi! I'm sleeping {sec} sec")

async def print_iter(sec: int):
    await asyncio.sleep(sec)
    print(sec)
    await do_someth(sec)


async def cor_print():
    # for python 3.11+
    # async with asyncio.TaskGroup() as tg:
    #     for i in range(1, 15):
    #         tg = asyncio.create_task(print_iter(i))

    # for python 3.11-
    tasks = []
    for i in range(1, 15):
        task = asyncio.create_task(print_iter(i))
        tasks.append(task)
    await asyncio.gather(*tuple(tasks))


asyncio.run(cor_print())

