from lib.datahen.client.Base import Base


class JobStat(Base):
    def job_current_stats(self, job_id):
        return self.get("/jobs/{}/stats/current".format(job_id), self._options)

    def scraper_job_current_stats(self, scraper_name):
        return self.get("/scrapers/{}/current_job/stats/current".format(scraper_name), self._options)

    def job_stats_history(self, job_id):
        return self.get("/jobs/{}/stats/history".format(job_id), self._options)

    def scraper_job_stats_history(self,scraper_name):
        return self.get("/scrapers/{}/current_job/stats/history".format(scraper_name), self._options)
