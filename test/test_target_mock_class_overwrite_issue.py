#! /usr/bin/env python3

import unittest
from unittest.mock import MagicMock
import src
import src.run as run


class TargetTest(unittest.TestCase):

    def test_run1_mock(self):
        src.run.Target = MagicMock()
        src.run.Target.return_value.method1.return_value = "other result"
        ret = run.run1()
        self.assertEqual(ret, "other result")

    """ #uncomment this will cause test failure, cuz mock function not restored
    def test_run1_no_mock(self):
        ret = run.run1()
        self.assertEqual(ret, [1, 2, 3])
    """


if __name__ == '__main__':
    unittest.main()
