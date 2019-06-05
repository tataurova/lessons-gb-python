# ------- Журналирование (логгирование) с использованием модуля logging -------
#           Расширенная настройка. Форматирование, обработчики

import logging
import sys

# Создать логгер - регистратор верхнего уроовня
# с именем app.main
log = logging.getLogger('app.main')

# Создать обработчик
fh = logging.FileHandler("app.log", encoding='utf-8')
# выводит сообщения с уровнем DEBUG
#fh.setLevel(logging.DEBUG)

# Создать объект Formatter
# Определить формат сообщений
_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")

# подключить объект Formatter к обработчику
fh.setFormatter(_format)

# Добавить обработчик к регистратору
log.addHandler(fh)
log.setLevel(logging.DEBUG)

# Передать сообщение обработчику
log.info('Замечательный день для релиза!')
