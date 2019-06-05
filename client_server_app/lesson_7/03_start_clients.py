# Служебный скрипт запуска/останова нескольких клиентских приложений

from subprocess import Popen
import os

p_list = []

while True:
    user = input("Запустить 10 клиентов (s) / Закрыть клиентов (x) / Выйти (q) ")

    if user == 'q':
        break
    elif user == 's':    
        for _ in range(10):
            #p_list.append(subprocess.Popen([os.getcwd()+"/example_application/02_time_client_random.py", "--url=http://127.0.0.1:8888"]))
            # Флаг CREATE_NEW_CONSOLE нужен для ОС Windows,
            # чтобы каждый процесс запускался в отдельном окне консоли
            #p_list.append(os.system('open -a "02_time_client_random.py" --args --url-http://127.0.0.1:8888'))
            #p_list.append(Popen('python 02_time_client_random.py', creationflags=CREATE_NEW_CONSOLE))
            p_list.append(Popen('python 01_time_client_random_2.py', shell=True))
            #my_str = raw_input('Your string here: ')
        print(' Запущено 10 клиентов')
    elif user == 'x':
        for p in p_list:
            p.kill()
        p_list.clear()    
