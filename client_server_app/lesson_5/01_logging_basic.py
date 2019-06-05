# ------- Журналирование (логгирование) с использованием модуля logging -------
#                             Базовая настройка

import logging


# Быстрая настройка логгирования может быть выполнена так:
logging.basicConfig(
    # файл, в который добавляются журналируемые сообщения
    filename="app_01.log",
    # формат формирования сообщения
    # %(levelname)s - уровень важности
    # %(asctime)s - дата попадания записи в журнал
    # %(message)s - текст сообщения
    format="%(levelname)s %(asctime)s %(message)s",
    # будут обрабатывать сообщения с уровнем важности, равным указанному или выше
    level=logging.INFO
    #level = logging.DEBUG,
)

# Для использования логгера его нужно получить/создать функцией getLogger
log = logging.getLogger('basic')


# После этого можно использовать логгирование таким образом
log.debug('There will be debug information')
log.info('Hello, World!')
log.warning('It seems to be a bug...')
log.critical('Critical bug in app! Hello, World!')

# Обратите внимание, что не все сообщения попали в лог-файл. Почему?

