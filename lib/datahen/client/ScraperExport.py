from lib.datahen.client.Base import Base


class ScraperExport(Base):
    def all(self, scraper_name, opts={}):
        opts.update(self._options)
        return self.get("/scrapers/{}/exports".format(scraper_name), opts)

    def find(self, export_id):
        return self.get("/scrapers/exports/{}".format(export_id), self._options)

    def create(self, scraper_name, exporter_name):
        return self.post("/scrapers/{}/exports/{}".format(scraper_name, exporter_name), self._options)

    def download(self, export_id):
        return self.post("/scrapers/exports/{}/download".format(export_id), self._options)
