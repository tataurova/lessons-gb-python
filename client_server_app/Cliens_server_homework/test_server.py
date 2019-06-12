import unittest
from server import presence_response


class TestServer(unittest.TestCase):

    # ответ 200 на правильное сообщение
    def test_presence_response_200(self):
        self.assertEqual(presence_response({'action': 'presence', 'time': '25-05-2019 23:59:46', 'user':
            {'account_name': 'Guest'}}),
                         {'response': 200}, 'Ошибка: неправильный запрос')

    # ответ 900 на неправильное сообщение
    def test_presence_response_900(self):
        self.assertEqual(presence_response({'time': '25-05-2019 23:59:46'}), {'response': 900, 'error': 'Неправильный запрос'}, 'Ошибка: неправильный запрос')


if __name__ == "__main__":
    unittest.main()


