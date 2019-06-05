# ------- Журналирование (логгирование) с использованием модуля logging -------
#           Расширенная настройка. Форматирование, обработчики

import logging
import sys

# Создать логгер - регистратор верхнего уроовня
# с именем basic
log = logging.getLogger('basic')

# Создать обработчик, который выводит сообщения в поток stderr
# обработчики позволяют переопределить поведение корневого регистратора - log
crit_hand = logging.StreamHandler(sys.stderr)
# выводит в поток сообщения с уровнем CRITICAL
#crit_hand.setLevel(logging.CRITICAL)

# Создать объект Formatter
# Определить формат сообщений
_format = logging.Formatter("%(levelname)-10s %(asctime)s %(message)s")

# подключить объект Formatter к обработчику
crit_hand.setFormatter(_format)

# Добавить обработчик к регистратору
log.addHandler(crit_hand)
log.setLevel(logging.CRITICAL)

# Передать сообщение обработчику
log.critical('Oghr! Kernel panic!')