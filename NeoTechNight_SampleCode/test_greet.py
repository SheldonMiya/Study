import unittest
from greet import greet

class TestGreet(unittest.TestCase):
    def test_greet_returns_hello_taro(self):
        self.assertEqual(greet("Taro"), "Hello, Taro")

if __name__ == '__main__':
    unittest.main()
