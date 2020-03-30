from lib.datahen.client.Base import Base


class ScraperJobOutput(Base):
    def find(self, scraper_name, collection, id):
        return self.get(
            "/scrapers/{}/current_job/output/collections/{}/records/{}".format(scraper_name, collection, id),
            self._options)

    def all(self, scraper_name, collection='default'):
        return self.get(
            "/scrapers/{}/current_job/output/collections/{}/records".format(scraper_name, collection, id),
            self._options)

    def collections(self, scraper_name):
        return self.get(
            "/scrapers/{}/current_job/output/collections".format(scraper_name),
            self._options)
