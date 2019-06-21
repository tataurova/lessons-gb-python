# Служебный скрипт запуска/останова нескольких клиентских приложений

from subprocess import Popen, CREATE_NEW_CONSOLE
import time

# список запущенных процессов
p_list = []

while True:
    user = input("Запустить сервер и n клиентов (n) / Выйти (q) ")
    if user == 'q':
        print('Открыто процессов {}'.format(len(p_list)))
        for p in p_list:
            print('Закрываю {}'.format(p))
            p.kill()
        p_list.clear()
        print('Выхожу')
        break
    else:
        try:
            console_ammount = int(user)
            if ((console_ammount > 1) and (console_ammount <= 10)):
                # запускаем сервер
                # Запускаем серверный скрипт и добавляем его в список процессов
                p_list.append(Popen('python -i server.py', creationflags=CREATE_NEW_CONSOLE))
                print('Сервер запущен')
                # Ждем
                time.sleep(1)
                # Запускаем клиентов
                console_count = int(user)
                for i in range(console_count):
                    # Запускаем клиентский скрипт и добавляем его в список процессов
                    client_name = f'Console{i}'
                    p_list.append(Popen('python -i client.py localhost 7777 r {}'.format(client_name),
                                        creationflags=CREATE_NEW_CONSOLE))
                print('Клиенты запущены')
            else:
                print('Недопустимое значение, количество клиентов должно быть от 2 до 10')
                pass
        except ValueError:
            print('Допустимые команды: q | 1..10')



