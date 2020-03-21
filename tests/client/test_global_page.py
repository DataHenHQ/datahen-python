import os
import sys
import unittest

sys.path.append(os.path.abspath('../..'))

from lib.datahen.client.GlobalPage import GlobalPage


class TestGlobalPage(unittest.TestCase):

    def test_find(self):
        gid = 'www.google.com-02392d39a869010149a9c2f1070a6179'
        self.assertRegexpMatches( GlobalPage().find(gid) , "created_at")

    def test_find_content(self):
        gid = 'www.google.com-02392d39a869010149a9c2f1070a6179'
        self.assertRegexpMatches( GlobalPage().find_content(gid) , "signed_url")



if __name__ == "__main__":
    unittest.main()
