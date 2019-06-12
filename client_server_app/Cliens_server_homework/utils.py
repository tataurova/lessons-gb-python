import json


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
        response = 'MandatoryKeyError'
    return response




