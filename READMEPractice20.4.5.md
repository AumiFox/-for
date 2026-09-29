Практически работы по основам Python

Practice20.4.5.py
Анализ заказов за июль 2023
Учебный проект: чтение JSON-файла с заказами интернет-магазина и ответы на 7 вопросов о данных.

Входные данные
orders_july_2023.json:

json
{
    "Номер заказа": {
        "date": "Дата заказа",
        "user_id": "id клиента",
        "quantity": "количество товаров",
        "price": "стоимость заказа"
    }
}
Задачи
Номер самого дорогого заказа

Номер заказа с самым большим количеством товаров

День с наибольшим числом заказов

Пользователь с наибольшим числом заказов

Пользователь с наибольшей суммарной стоимостью заказов

Средняя стоимость заказа за июль

Средняя стоимость товара за июль

Запуск
bash
python main.py
Требуется Python 3.7+. Файл orders_july_2023.json должен лежать рядом со скриптом.

Пример
python
import json

with open("orders_july_2023.json", "r", encoding="utf-8") as f:
    orders = json.load(f)

max_price, max_order = 0, ""
for order_num, data in orders.items():
    if data["price"] > max_price:
        max_order, max_price = order_num, data["price"]

print(f"Самый дорогой заказ: {max_order}, стоимость: {max_price}")
