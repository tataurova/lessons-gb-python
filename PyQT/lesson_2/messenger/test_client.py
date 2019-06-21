import unittest
import time
from utils import translate_message
from client import create_presence


# Тестируем функцию формирования сообщения от клиента
class TestClientCreatePresence(unittest.TestCase):
    # Имя юзера не пустое
    def test_create_presence_user(self):
        self.assertTrue(create_presence()['user']['account_name'], not None)

    # Время записывается корректно
    def test_create_presence_time(self):
        self.assertEqual(create_presence()['time'], time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()))


# Тестируем функцию разбора ответа сервера
class TestClientTranslateMessage(unittest.TestCase):

    # Все правильно
    def test_translate_message_cor_resp(self):
        self.assertEqual(translate_message({'response': 200}), {'response': 200})


if __name__ == "__main__":
    unittest.main()
