import os
import sys
import unittest

sys.path.append(os.path.abspath('../..'))

from lib.datahen.client.Export import Export


class TestExport(unittest.TestCase):

    def test_all(self):
        self.assertRegexpMatches( Export().all() , "exporter_name")


if __name__ == "__main__":
    unittest.main()
