import re

import json
import time


with open('data.json') as json_file:
    data = json.load(json_file)

result = data["links"] if "links" in data.keys() else []

regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

print("===Этот скрипт позволит вам добавить ссылки в фильтр.===")


link = input("Введите ссылку для фильтра.\n"
             "Если хотите выйти, просто нажмите Enter: ")
while True:
    if not link:
        break

    if re.match(regex, link):
        result.append(link)
        print("Принято!")

    else:
        print("Некорректная ссылка!")

    link = input("Введите ссылку для фильтра.\n"
                 "Если хотите выйти, просто нажмите Enter: ")


data["links"] = result

with open('data.json', 'w') as f:
    json.dump(data, f)

print("Данные успешно записаны!")
time.sleep(1)
