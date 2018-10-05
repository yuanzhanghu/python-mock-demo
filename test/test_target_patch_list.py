#! /usr/bin/env python3

import unittest
from unittest.mock import MagicMock


class TargetTest(unittest.TestCase):

    def test_mock_list(self):
        m = MagicMock()
        m.__getitem__.side_effect = [1, 2]
        self.assertEqual(m[0], 1)
        self.assertEqual(m[1], 2)

        m.__iter__.return_value = iter([1, 2])
        result = [x for x in m]
        self.assertEqual(result, [1, 2])

        m.__contains__.return_value = True
        self.assertEqual(3 in m, True)
        self.assertEqual('anything' in m, True)


if __name__ == '__main__':
    unittest.main()
