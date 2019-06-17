import unittest
import time
from utils import translate_message
from client import create_presence


class TestClientCreatePresence(unittest.TestCase):
    # имя юзера не пустое
    def test_create_presence_user(self):
        self.assertTrue(create_presence()['user']['account_name'], not None)

    # время записывается корректно
    def test_create_presence_time(self):
        self.assertEqual(create_presence()['time'], time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()))


# тестируем функцию разбора ответа сервера
class TestClientTranslateMessage(unittest.TestCase):

    # все правильно
    def test_translate_message_cor_resp(self):
        self.assertEqual(translate_message({'response': 200}), {'response': 200})


if __name__ == "__main__":
    unittest.main()
