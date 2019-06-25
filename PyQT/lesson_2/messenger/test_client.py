import unittest
import time
from client import create_presence, process_response_ans
from errors import ReqFieldMissingError, ServerError


# Тестируем функцию формирования сообщения от клиента
class TestClass(unittest.TestCase):

    # Время записывается корректно
    def test_create_presence_time(self):
        self.assertEqual(create_presence('Test_user')['time'], time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()))


# Тестируем функцию разбора ответа сервера
class TestClientTranslateMessage(unittest.TestCase):

    # Все правильно
    def test_200_ans(self):
        self.assertEqual(process_response_ans({'response': 200}), '200 : OK')

    # тест корректного разбора 400
    def test_400_ans(self):
        self.assertRaises(ServerError, process_response_ans, {'response': 400, 'error': 'Bad Request'})


if __name__ == "__main__":
    unittest.main()
