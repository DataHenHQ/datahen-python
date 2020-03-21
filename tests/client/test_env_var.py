import os
import sys
import unittest

sys.path.append(os.path.abspath('../..'))

from lib.datahen.client.EnvVar import EnvVar


class TestEnvVar(unittest.TestCase):

    def test_all(self):
        self.assertRegexpMatches( EnvVar().all() , "secret")

    def test_find(self):
        var_name = 'test'
        self.assertRegexpMatches( EnvVar().find(var_name) , "secret")


    def test_set(self):
        var_name = 'test_2'
        var_value  = 'test2'
        self.assertRegexpMatches( EnvVar().set(var_name,var_value) , "created_at")




    def test_unset(self):
        var_name = 'test'
        self.assertRegexpMatches(EnvVar().unset(var_name), "Deleted")



if __name__ == "__main__":
    unittest.main()
