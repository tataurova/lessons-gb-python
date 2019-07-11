import unittest
from client import create_presence, process_response_ans
from errors import ReqFieldMissingError, ServerError


# Тестируем функцию разбора ответа сервера
class TestClientTranslateMessage(unittest.TestCase):

    # Все правильно
    def test_200_ans(self):
        self.assertEqual(process_response_ans({'response': 200}), '200 : OK')

    # Тест корректного разбора 400
    def test_400_ans(self):
        self.assertRaises(ServerError, process_response_ans, {'response': 400, 'error': 'Bad Request'})


if __name__ == "__main__":
    unittest.main()
