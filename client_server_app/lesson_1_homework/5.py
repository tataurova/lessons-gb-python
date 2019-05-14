# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
# в строковый тип на кириллице.

import subprocess

ya_args = ['ping', 'yandex.ru']
youtube_args = ['ping', 'youtube.com']

print('Проверка доступности YANDEX')

ya_ping = subprocess.Popen(ya_args, stdout=subprocess.PIPE)
for line in ya_ping.stdout:
    # выводим результат в байтах
    print(line)

    # изменяем кодировку результата
    line = line.decode('cp866').encode('utf-8')
    # выводи результат в кодировке utf-8
    print(line.decode('utf-8'))

print('Проверка доступности YOUTUBE')

youtube_ping = subprocess.Popen(youtube_args, stdout=subprocess.PIPE)
for line in youtube_ping.stdout:
    # выводим результат в байтах
    print(line)

    # изменяем кодировку результата
    line = line.decode('cp866').encode('utf-8')
    # выводи результат в кодировке utf-8
    print(line.decode('utf-8'))
