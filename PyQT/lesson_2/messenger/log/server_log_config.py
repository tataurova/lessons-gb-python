import logging.handlers

# путь до папки с логом
SERVER_LOG_FILE_PATH = 'log/server.log'

# Создаем именованный логгер с именем server
server_logger = logging.getLogger('server')

# Создаем обработчик с ротацией файлом по дням
server_handler = logging.handlers.TimedRotatingFileHandler(SERVER_LOG_FILE_PATH, when='d')
server_handler.setLevel(logging.DEBUG)

# Определяем Форматтер сообщения
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Связываем обработчик с форматером
server_handler.setFormatter(formatter)

# Связываем логгер с обработчиком
server_logger.addHandler(server_handler)

# Устанавливаем уровень сообщений логгера
server_logger.setLevel(logging.DEBUG)
