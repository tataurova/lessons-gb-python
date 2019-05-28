import unittest
from utils import presence_response, get_message, get_message


class TestServer(unittest.TestCase):
    # ответ 200 на правильное сообщение
    def test_presence_response_200(self):
        self.assertEqual(presence_response({'action': 'presence', 'time': '25-05-2019 23:59:46', 'user':
            {'account name': 'Ольга'}, 'message': 'привет'}),
                         {'response': 200}, 'Ошибка: неправильный запрос')

    # ответ 400 на неправильное сообщение
    def test_presence_response_400(self):
        self.assertEqual(presence_response({'action': 'presence', 'time': '25-05-2019 23:59:46', 'user':
            {'account name': 'Ольга'}}), {'response': 400, 'error': 'Не верный запрос'}, 'Ошибка: неправильный запрос')


if __name__ == "__main__":
    unittest.main()