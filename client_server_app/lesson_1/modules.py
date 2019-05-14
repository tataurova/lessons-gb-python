# результат работы модуля subprocess при проверке качества подключения по сети(команда ping)
'''
import subprocess

args = ['ping', 'google.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    # выводим результат в байтах
    print(line)

    # изменяем кодировку результата
    line = line.decode('cp866').encode('utf-8')
    # выводи результат в кодировке utf-8
    print(line.decode('utf-8'))
'''

# тестирование модуля telnetlib
import telnetlib
import time


# создаем экземпляр класса Telnet и передаем адрес машины
tn_connect = telnetlib.Telnet('62.148.227.52')

# получаем поле ввода логина и записываем в него значение
tn_connect.read_until(b'Username:')
tn_connect.write(b'user\n')

# получаем поле ввода пароля и записываем в него значение
t.read_until(b'Password:')
t.write(b'pass\n')

time.sleep(5)

# получаем результат в байтовом формате и выполняем конвертацию
output = tn_connect.read_very_eager().decode('cp866').encode('utf-8')
#print(output.decode('utf-8'))

