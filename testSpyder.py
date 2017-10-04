import unittest
from Spyder import Spyder


class MyTestCase(unittest.TestCase):
    def test_something(self):
        testUrl = "http://testfire.net/bank/login.aspx"
        max_pages = 10

        spyder = Spyder(testUrl,max_pages)

        spyder.spyder()

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
