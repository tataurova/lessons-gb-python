from threading import Thread
import time

class ClockThread(Thread):
    ''' Класс-наследник потока
    '''
    def __init__(self, interval):
        super().__init__()
        self.daemon = True
        self.interval = interval

    def run(self):
        while True:
            print("Текущее время: %s" % time.ctime())
            time.sleep(self.interval)

t = ClockThread(3)
t.start()

'''
Чтобы проследить работу потока после вызова метода t.start(),
необходимо также добавить вызов метода t.join(). 
Иначе приложение завершится сразу после запуска потока.
'''
t.join()