import json
import time
from pyrogram import Client

print("===Этот скрипт позволит вам авторизоваться в программе.===")

with open('data.json') as json_file:
    data = json.load(json_file)

app = Client("basic", api_id=data["api_id"],
             api_hash=data["api_hash"])

app.start()
app.stop()


print("Успешная авторизация!")
time.sleep(1)
