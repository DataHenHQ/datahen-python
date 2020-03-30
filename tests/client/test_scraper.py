import os
import sys
import unittest

sys.path.append(os.path.abspath('../..'))
from lib.datahen.client.Scraper import Scraper


class TestScraper(unittest.TestCase):
    def test_all(self):
        self.assertRegexpMatches( Scraper().all() , "parsing_failed")

    def test_find(self):
        scraper_name = 'ebay'
        self.assertRegexpMatches( Scraper().find(scraper_name) , "deployed_git_repository")


    def test_create(self):
        pass
        #self.assertRegexpMatches( Scraper().all() , "parsing_failed")

    def test_update(self):
        pass
        #self.assertRegexpMatches( Scraper().all() , "parsing_failed")



if __name__ == "__main__":
    unittest.main()
