import json
import time

with open('data.json') as json_file:
    data = json.load(json_file)


print("===Этот скрипт позволит вам заполнить api_id и api_hash поля.===")
print("===Инструкция по получению этих данных указана в файле README.===\n")

data["api_id"] = int(input("Введите ваш api_id: "))
data["api_hash"] = input("Введите ваш api_hash: ")

with open('data.json', 'w') as f:
    json.dump(data, f)

print("Данные успешно записаны!")
time.sleep(1)
