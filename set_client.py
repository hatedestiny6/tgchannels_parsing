import json
import time
import os
from pyrogram import Client

print("===Этот скрипт позволит вам авторизоваться в программе.===")

with open('data.json') as json_file:
    data = json.load(json_file)

try:
    os.remove("basic.session")

except FileNotFoundError:
    pass

app = Client("basic", api_id=data["api_id"],
             api_hash=data["api_hash"])

app.start()
app.stop()


print("Успешная авторизация!")
time.sleep(1)
