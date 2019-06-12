# ======================= Потоки и многозадачность ============================
# ---------------- Обзор возможностей модуля multiprocessing ------------------

#             Синхронизация процессов через очередь JoinableQueue

import multiprocessing
import time

def consumer(input_q):
    while True:
        print('извлекаю')

        # извлечь элемент из очереди
        item = input_q.get()
        # Обработать элемент
        print(item) # <- Здесь может быть некоторая обработка элемента
        # Сообщить о завершении обработки
        # task_done - используется потребителем, чтобы сообщить,
        # что элемент очереди, полученный методом q.get(), был обработан
        input_q.task_done()
        time.sleep(4)

# функция, в которой производитель добавляет элементы в очередь
def producer(sequence, output_q):
    for item in sequence:
        # Добавить элемент в очередь
        print('помещаю')
        output_q.put(item)
        time.sleep(4)


# Настройка
if __name__ == '__main__':
    # создает необособленный процесс очереди, доступной для совместного использования.Очереди
    # этого типа похожи на Queue, но позволяют потребителю известить поставщика, что
    # элементы были благополучно обработаны.
    q = multiprocessing.JoinableQueue()
    # Создать процесс-потребитель
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.daemon = True
    # запустить процесс-потребитель
    cons_p.start()

    # Воспроизвести элементы.
    # Переменная sequence представляет последовательность элементов, которые
    # будут передаваться потребителю. На практике вместо переменной можно
    # использовать генератор или воспроизводить элементы каким-либо другим
    # способом.
    # sequence - некоторые элементы-которые по очереди получает потребитель для обработки
    sequence = [1,2,3,4]
    # запуск ф-ции производителя
    producer(sequence, q)

    # Дождаться, пока все элементы не будут обработаны
    # если забыть его вызвать, процесс-потребитель будет завершен еще до того,
    # как успеет обработать все элементы в очереди
    q.join()