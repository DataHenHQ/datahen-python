from lib.datahen.client.Base import Base


class ScraperFinisher(Base):
    def reset(self, scraper_name, opts={}):
        opts.update(self._options)
        return self.get("/scrapers/{}/current_job/finisher/reset".format(scraper_name), opts)
