from lib.datahen.client.Base import Base


class Export(Base):
    def all(self, opts={}):
        opts.update(self._options)
        return self.get("/scrapers/exports", opts)
