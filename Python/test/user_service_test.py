import unittest
from unittest import mock


class TestUserService(unittest.TestCase):
    def test_login_fail_when_password_is_wrong(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
