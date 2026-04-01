import json

with open("filePr.json.txt", "r") as my_file:
    orders = json.load(my_file)

# Инициализация
max_price = 0
max_price_order = ""

max_quantity = 0
max_quantity_order = ""

orders_by_day = {}
orders_by_user = {}
total_price_by_user = {}

total_orders_price = 0
total_orders_count = len(orders)
total_items_quantity = 0

for order_num, order_data in orders.items():
    # Извлекаем день из даты (вторая часть)
    day = order_data['date'].split('-')[1]
    user_id = order_data['user_id']
    quantity = order_data['quantity']
    price = order_data['price']

    # 1. Какой номер самого дорого заказа за июль?
    if price > max_price:
        max_price = price
        max_price_order = order_num

    # 2. Заказ с самым большим количеством товаров
    if quantity > max_quantity:
        max_quantity = quantity
        max_quantity_order = order_num

    # 3. Количество заказов по дням
    orders_by_day[day] = orders_by_day.get(day, 0) + 1

    # 4. Количество заказов по пользователям
    orders_by_user[user_id] = orders_by_user.get(user_id, 0) + 1

    # 5. Суммарная стоимость по пользователям
    total_price_by_user[user_id] = total_price_by_user.get(user_id, 0) + price

    # Для средних значений
    total_orders_price += price
    total_items_quantity += quantity

# 3. Какой номер заказа с самым большим количеством товаров?
max_orders_day = max(orders_by_day, key=orders_by_day.get)
max_orders_count = orders_by_day[max_orders_day]

# 4. В какой день в июле было сделано больше всего заказов?
max_orders_user = max(orders_by_user, key=orders_by_user.get)
max_orders_user_count = orders_by_user[max_orders_user]

# 5. Какой пользователь сделал самое большое количество заказов за июль?
max_total_price_user = max(total_price_by_user, key=total_price_by_user.get)
max_total_price_value = total_price_by_user[max_total_price_user]

# 6. Какая средняя стоимость заказа была в июле?
average_order_price = total_orders_price / total_orders_count

# 7. Какая средняя стоимость товаров в июле?
average_item_price = total_orders_price / total_items_quantity

# Выводим результаты
print(f"1. Номер самого дорогого заказа: {max_price_order}, стоимость: {max_price}")
print(f"2. Номер заказа с самым большим количеством товаров: {max_quantity_order}, количество: {max_quantity}")
print(f"3. День с наибольшим количеством заказов: {max_orders_day} июля ({max_orders_count} заказов)")
print(f"4. Пользователь с наибольшим количеством заказов: {max_orders_user} (заказов: {max_orders_user_count})")
print(
    f"5. Пользователь с наибольшей суммарной стоимостью заказов: {max_total_price_user} (сумма: {max_total_price_value})")
print(f"6. Средняя стоимость заказа: {average_order_price:.2f}")
print(f"7. Средняя стоимость товара: {average_item_price:.2f}")