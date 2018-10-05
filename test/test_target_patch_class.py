#! /usr/bin/env python3

import unittest
from unittest.mock import patch, DEFAULT
import src
import src.target as target
import src.run as run


class TargetTest(unittest.TestCase):

    def test_run1_no_mock(self):
        ret = run.run1()
        self.assertEqual(ret, [1, 2, 3])

    def test_run1(self):
        with patch.multiple(src.target, Target=DEFAULT) as mocks:
            mocks['Target'].return_value.method1.return_value = "other result"
            t = src.target.Target()
            ret = t.method1(1,2,3)
            self.assertEqual(ret, "other result")


if __name__ == '__main__':
    unittest.main()
