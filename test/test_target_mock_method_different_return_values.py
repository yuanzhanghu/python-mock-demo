#! /usr/bin/env python3

import unittest
from unittest.mock import MagicMock
import src.target as target


class TargetTest(unittest.TestCase):

    def test_method1(self):
        t = target.Target()
        t.method1 = MagicMock()
        t.method1.side_effect = ['result1', 'result2', 'result3']
        self.assertEqual(t.method1(1, 2, 3), "result1")
        self.assertEqual(t.method1(1, 2, 3), "result2")
        self.assertEqual(t.method1(1, 2, 3), "result3")


if __name__ == '__main__':
    unittest.main()
