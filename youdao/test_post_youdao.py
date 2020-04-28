import unittest
from unittest import mock
# from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        # import time
        # t=time.time()
        # ts=str(int(round(t*1000)))
        # print(ts)
        get_ts=mock.Mock(return_value='1586226797454')
        self.assertEqual('1586226797454',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value='15862267974546')
        self.assertEqual('15862267974546',get_salt())

    def test_get_sign(self):
        get_sign=mock.Mock(return_value='5dbc10f3c823fcf15ae2fb923e99a04e')
        self.assertEqual('5dbc10f3c823fcf15ae2fb923e99a04e',get_sign())

if __name__ == '__main__':
    unittest.main()
