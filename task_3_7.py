"""Сценарий Foursquare
Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
Используйте API Foursquare для поиска заведений в указанной категории.
Получите название заведения, его адрес и рейтинг для каждого из них.
Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.
"""

import requests
import json

client_id = "__"
client_secret = "__"

endpoint = "https://api.foursquare.com/v3/places/search"

city = input("Введите название города: ")
name_category = input('Ведите название категории на английском языке (например: coffee shop, museum, park): ')
params = {
    'limit': 20,
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    'query': name_category,
    'fields': 'name,location,rating'
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

response = requests.get(endpoint, params=params,headers=headers)

if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        print("Название:", venue["name"])
        try:
            print("Адрес:", venue["location"]["address"])
            # print("Рейтинг", venue['rating'])
        except Exception:
            print('Адрес не найден: ')
        try:
            print("Рейтинг", venue['rating'])
        except Exception:
            print('Рейтинг не определён: ')
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)

