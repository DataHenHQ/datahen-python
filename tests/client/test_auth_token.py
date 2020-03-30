import os
import sys
import unittest

sys.path.append(os.path.abspath('../..'))
from lib.datahen.client.AuthToken import AuthToken


class TestAuthToken(unittest.TestCase):
    def test_all(self):
        self.assertRegexpMatches( AuthToken().all() , "account_id")

    def test_find(self):
        token_name = ''
        #self.assertRegexpMatches( AuthToken().find(token_name) , "account_id")


    def test_create(self):
        #self.assertRegexpMatches( AuthToken().create('basic','test token 2') , "created_at")
        pass

    #@todo test create on account
    def test_create_on_account(self):
        pass

    def test_update(self):
        token = ""
        #self.assertRegexpMatches(AuthToken().update(token , 'basic', 'token updated'), "created_at")

    #@todo test delete again
    def test_delete(self):
        token = ""
        #self.assertRegexpMatches(AuthToken().delete(token), "created_at")



if __name__ == "__main__":
    unittest.main()
