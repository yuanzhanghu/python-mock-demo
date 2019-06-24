#! /usr/bin/env python3

import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import src
import src.run as run
import src.target


class TargetTest(unittest.TestCase):

    @patch('src.target.func1')
    def test_run1_mock(self, mockedFunc1):
        mockedFunc1.return_value = 'mocked func1'
        t = src.target.Target()
        self.assertEqual(t.method2(), 'mocked func1')

    """ #uncomment this will cause test failure, cuz mock function not restored
    def test_run1_no_mock(self):
        ret = run.run1()
        self.assertEqual(ret, [1, 2, 3])
    """


if __name__ == '__main__':
    unittest.main()
