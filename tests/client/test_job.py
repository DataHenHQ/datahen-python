import os
import sys
import unittest

sys.path.append(os.path.abspath('../..'))
from lib.datahen.client.Job import Job


class TestJob(unittest.TestCase):
    def test_all(self):
        self.assertRegexpMatches( Job().all() , "job_id")

    def test_find(self):
        job_id = 'xxxxx'
        self.assertRegexpMatches( Job().find(job_id) , "deployed_git_repository")



if __name__ == "__main__":
    unittest.main()
