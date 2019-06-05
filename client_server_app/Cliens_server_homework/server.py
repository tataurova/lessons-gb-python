from socket import *
from utils_server import get_message, presence_response, send_message
from log.server_log_config import *

logger = logging.getLogger('server')


# Запуск сервера


if __name__ == '__main__':

    server = socket(AF_INET, SOCK_STREAM)
    try:
        port = 7777
        server.bind(('', port))
    except Exception:
        port = 7778
        server.bind(('', port))
        res = 'Port 7777 unreachable. Port used 7778'
        logger.warning('{} {} - {}'.format(res, server.bind.__name__, __name__))
    server.listen(5)
    while True:
        res = 'Waiting for client'
        logger.info('{}'.format(res))
        client, address = server.accept()
        res = 'Client connected from address {}'.format(address)
        logger.info('{}'.format(res))
        presence = get_message(client)
        print(presence)
        response = presence_response(presence)
        send_message(client, response)
        client.close()



