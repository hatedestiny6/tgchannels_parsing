from pyrogram import Client
from pyrogram.errors.exceptions.bad_request_400 import UsernameInvalid

import json
import time


with open('data.json') as json_file:
    data = json.load(json_file)


app = Client("basic", api_id=data["api_id"],
             api_hash=data["api_hash"])


print("===Этот скрипт позволит вам сменить ссылки на приемники.===")

app.start()

link_1 = input("Введите новую ссылку для приемника 1.\n"
               "Если хотите оставить текущую, просто нажмите Enter: ")
while True:
    if link_1:
        try:
            data["RECEIVER_1"] = app.get_chat(link_1.split('/')[-1]).id

            print("Принято!")
            break

        except UsernameInvalid:
            link_1 = input("Некорректная ссылка! Введите новую ссылку для приемника 1.\n"
                           "Если хотите оставить текущую, просто нажмите Enter: ")

    else:
        break

link_2 = input("Введите новую ссылку для приемника 2.\n"
               "Если хотите оставить текущую, просто нажмите Enter: ")

while True:
    if link_2:
        try:
            data["RECEIVER_2"] = app.get_chat(link_2.split('/')[-1]).id

            print("Принято!")
            break

        except UsernameInvalid:
            link_2 = input("Некорректная ссылка! Введите новую ссылку для приемника 2.\n"
                           "Если хотите оставить текущую, просто нажмите Enter: ")

    else:
        break

with open('data.json', 'w') as f:
    json.dump(data, f)

print("Данные успешно записаны!")
time.sleep(1)

app.stop()
