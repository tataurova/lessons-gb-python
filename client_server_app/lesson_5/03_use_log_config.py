# ------- Журналирование (логгирование) с использованием модуля logging -------
#            Вынесение настройки логгирования в отдельный модуль


import logging

import log_config

# Обратите внимание, логгер уже создан в модуле log_config,
# теперь нужно его просто получить
logger = logging.getLogger('app.main')


def main():
    ''' Тестовая главная функция
    '''
    logger.debug('Старт приложения')


if __name__ == '__main__':
    main()
