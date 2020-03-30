import os
import sys
import unittest

sys.path.append(os.path.abspath('../..'))
from lib.datahen.client.AuthToken import AuthToken


class TestDeployKey(unittest.TestCase):


    def test_find(self):
        pass


    def test_create(self):
        pass


    def test_delete(self):
        token = ""
        #self.assertRegexpMatches(AuthToken().delete(token), "created_at")



if __name__ == "__main__":
    unittest.main()
