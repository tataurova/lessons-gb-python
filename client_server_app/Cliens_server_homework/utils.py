import json
from errors import MandatoryKeyError


def presence_response(presence_message):

    if 'action' in presence_message and \
        presence_message['action'] == 'presence' and \
        'time' in presence_message and \
        'user' in presence_message and \
        'message' in presence_message and \
            isinstance(presence_message['time'], str):
        return {'response': 200}
    else:
        return {'response': 400, 'error': 'Не верный запрос'}


def dict_to_bytes(message_dict):
    if isinstance(message_dict, dict):
        jmessage = json.dumps(message_dict)
        bmessage = jmessage.encode('utf-8')
        return bmessage
    else:
        raise TypeError


def bytes_to_dict(message_bytes):
    if isinstance(message_bytes, bytes):
        jmessage = message_bytes.decode('utf-8')
        message = json.loads(jmessage)
        if isinstance(message, dict):
            return message
        else:
            raise TypeError
    else:
        raise TypeError


def send_message(sock, message):
    bprescence = dict_to_bytes(message)
    sock.send(bprescence)


def get_message(sock):
    bresponse = sock.recv(1024)
    response = bytes_to_dict(bresponse)
    return response


def translate_message(response):
    if not isinstance(response, dict):
        raise TypeError
    if 'response' not in response:
        raise MandatoryKeyError('response')
    return response




