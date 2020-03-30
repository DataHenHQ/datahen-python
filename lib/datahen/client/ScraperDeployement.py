from lib.datahen.client.Base import Base


class ScraperDeployment(Base):
    def all(self, scraper_name, opts={}):
        opts.update(self._options)
        return self.get("/scrapers/{}/deployments".format(scraper_name), opts)

    def deploy(self, scraper_name, opts={}):
        opts.update(self._options)
        return self.post("/scrapers/{}/deployments".format(scraper_name), opts)
