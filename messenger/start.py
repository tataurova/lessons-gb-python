# Служебный скрипт запуска/останова нескольких клиентских приложений

from subprocess import Popen, CREATE_NEW_CONSOLE
import time

# список запущенных процессов
p_list = []

while True:
    user = input("Запустить сервер и клиентов (s) / Выйти (q)")

    if user == 's':
        # запускаем сервер
        # Запускаем серверный скрипт и добавляем его в список процессов
        p_list.append(Popen('python -i server.py', creationflags=CREATE_NEW_CONSOLE))
        print('Сервер запущен')
        # Ждем
        time.sleep(1)
        # Запускаем клиентов
        console_count = 2
        for i in range(console_count):
            # Запускаем клиентский скрипт и добавляем его в список процессов
            client_name = f'Console{i}'
            p_list.append(Popen('python -i client.py localhost 7777 r {}'.format(client_name), creationflags=CREATE_NEW_CONSOLE))
        print('Клиенты запущены')
    elif user == 'q':
        print('Открыто процессов {}'.format(len(p_list)))
        for p in p_list:
            print('Закрываю {}'.format(p))
            p.kill()
        p_list.clear()
        print('Выхожу')
        break
