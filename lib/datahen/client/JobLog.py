from lib.datahen.client.Base import Base



class JobLog(Base):
    def all_job_page_log(self, job_id, gid, opts={}):
        opts.update(self._options)
        return self.get("/jobs/{}/pages/{}/log".format(job_id, gid), opts)

    def scraper_all_job_page_log(self, scraper_name, gid, opts={}):
        opts.update(self._options)
        return self.get("/scrapers/{}/current_job/pages/{}/log".format(scraper_name, gid), opts)

    def all_job_log(self, job_id, opts={}):
        opts.update(self._options)
        return self.get("/jobs/{}/log".format(job_id), opts)

    def scraper_all_job_log(self, scraper_name, opts={}):
        opts.update(self._options)

        return self.get("/scrapers/{}/current_job/log".format(scraper_name), opts)
