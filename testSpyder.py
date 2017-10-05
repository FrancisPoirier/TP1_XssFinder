import unittest
from Spyder import Spyder


class MyTestCase(unittest.TestCase):
    def test_something(self):
        testUrl = "http://remikya.com"
        max_pages = 4

        spyder = Spyder(testUrl,max_pages)

        spyder.gather()

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
