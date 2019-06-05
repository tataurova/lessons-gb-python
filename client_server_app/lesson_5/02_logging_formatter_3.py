# ------- Журналирование (логгирование) с использованием модуля logging -------
#           Расширенная настройка. Форматирование, обработчики

import logging
import sys

# Создать логгер - регистратор верхнего уроовня
# с именем app
app_log = logging.getLogger('app')
# Установить уровень важности
app_log.setLevel(logging.INFO)

# Создать обработчик который выводит сообщения с уровнем CRITICAL в поток stderr
crit_hand = logging.StreamHandler(sys.stderr)
#crit_hand.setLevel(logging.INFO)

# Создать обработчик который выводит сообщения в файл
applog_hand = logging.FileHandler('app.log')
#applog_hand.setLevel(logging.CRITICAL)

# Создать объект Formatter
# Определить формат сообщений
_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")

# подключить объект Formatter к обработчикам
crit_hand.setFormatter(_format)
applog_hand.setFormatter(_format)

# Добавить обработчики к регистратору
#app_log.addHandler(crit_hand)
app_log.addHandler(applog_hand)

# Передать сообщение обработчику
app_log.info('Замечательный день для релиза!')
