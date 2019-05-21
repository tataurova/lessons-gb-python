'''

2. Задание на закрепление знаний по модулю json.
    Есть файл orders в формате JSON с информацией о заказах.
    Написать скрипт, автоматизирующий его заполнение данными. Для этого:
        a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
            количество (quantity),
            цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
            в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
        b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений
            каждого параметра.
'''
import json


def write_order_to_json(a, b, c, d, e):
    with open('orders.json') as f_n:
        all_orders = json.load(f_n)
        print(all_orders)
        order = {"item": a,
                 "quantify": b,
                 "price": c,
                 "buyer": d,
                 "date": e}

        all_orders['orders'].append(order)
    with open('orders.json', 'w') as f_n:
        json.dump(all_orders, f_n, indent=4)

    print(all_orders)


write_order_to_json("Apple", "4", "10", "Olya", "18-05-2019")
write_order_to_json("Banana", "80", "20", "Vadim", "17-05-2019")
write_order_to_json("Orange", "48", "30", "Maria", "18-05-2019")
write_order_to_json("Juice", "85", "40", "Nikita", "17-05-2019")
write_order_to_json("Mango", "43", "50", "Artem", "18-05-2019")
write_order_to_json("Kiwi", "70", "60", "Vera", "17-05-2019")

# {"orders": []}
