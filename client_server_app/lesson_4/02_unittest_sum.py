import unittest


def sum_kv_ij(i, j):
    return i*i+j*j


# создаем тестовый случай
class TestSumKV(unittest.TestCase):
    # создаем сам тест
    def testequal(self):
        # используем функцию assertEqual модуля unittest
        self.assertEqual(sum_kv_ij(2, 3), 13)
        self.assertRaises()


if __name__ == '__main__':
    unittest.main()

