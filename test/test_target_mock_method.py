#! /usr/bin/env python3

import unittest
from unittest.mock import MagicMock
import src.target as target


class TargetTest(unittest.TestCase):

    def test_method1(self):
        t = target.Target()
        t.method1 = MagicMock(return_value="other result")
        ret = t.method1(1, 2, 3)
        self.assertEqual(ret, "other result")


if __name__ == '__main__':
    unittest.main()
