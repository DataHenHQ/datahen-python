from lib.datahen.client.Base import Base


class ScraperExporter(Base):
    def all(self, scraper_name, opts={}):
        opts.update(self._options)
        return self.get("/scrapers/{}/exporters".format(scraper_name), opts)

    def find(self, exporter_name):
        return self.get("/scrapers/exporters/{}".format(exporter_name), self._options)
