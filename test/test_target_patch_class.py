#! /usr/bin/env python3

import unittest
from unittest.mock import patch, DEFAULT
import src,pdb
import src.target as target
import src.run as run


class TargetTest(unittest.TestCase):

    def test_run1(self):
        with patch.multiple(src.target, Target=DEFAULT) as mocks:
            mocks['Target'].return_value.method1.return_value = "other result"
            ret = run.run1()
            self.assertEqual(ret, "other result")


if __name__ == '__main__':
    unittest.main()
