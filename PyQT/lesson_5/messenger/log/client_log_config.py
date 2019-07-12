import logging.handlers
import sys


# путь до папки с логом
CLIENT_LOG_FILE_PATH = '../log/client.log'

# # Создаем именованный логгер с именем client
client_logger = logging.getLogger('client')
# устанавливаем уровень логгера
client_logger.setLevel(logging.DEBUG)

# обработчик будет логгер, который пишет в файл
client_handler = logging.handlers.TimedRotatingFileHandler(CLIENT_LOG_FILE_PATH, encoding='utf-8', when='d')
print(client_handler)

# задаем уровень обработчика
client_handler.setLevel(logging.DEBUG)

# настраиваем форматтер вывода
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# связываем с форматером
client_handler.setFormatter(formatter)

# связываем с обработчиком
client_logger.addHandler(client_handler)