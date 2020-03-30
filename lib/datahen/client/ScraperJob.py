from lib.datahen.client.Base import Base

from lib.datahen.client.Base import Base
import json


class ScraperJob(Base):
    def all(self, scraper_name, opts={}):
        opts.update(self._options)
        return self.get("/scrapers/{}/jobs".format(scraper_name), self._options)

    def find(self, scraper_name):
        return self.get("/scrapers/{}/current_job".format(scraper_name), self._options)

    def update(self, scraper_name, opts={}):

        body = {}
        if 'status' in opts and opts['status']: body['status'] = opts['status']
        if 'workers' in opts and opts['workers']: body['standard_worker_count'] = opts['workers']
        if 'browsers' in opts and opts['browsers']: body['browser_worker_count'] = opts['browsers']
        if 'proxy_type' in opts and opts['proxy_type']: body['proxy_type'] = opts['proxy_type']
        opts.update({'body': json.loads(body)})
        opts.update(self._options)

        return self.put("/scrapers/{}/current_job".format(scraper_name), opts)

    def cancel(self, scraper_name, opts={}):
        opts['status'] = 'cancelled'
        return self.update(scraper_name, opts)

    def resume(self, scraper_name, opts={}):
        opts['status'] = 'active'
        return self.update(scraper_name, opts)

    def pause(self, scraper_name, opts={}):
        opts['status'] = 'paused'
        return self.update(scraper_name, opts)

    def create(self, scraper_name, opts={}):

        body = {}
        if 'workers' in opts and opts['workers']: body['standard_worker_count'] = opts['workers']
        if 'browsers' in opts and opts['browsers']: body['browser_worker_count'] = opts['browsers']
        if 'proxy_type' in opts and opts['proxy_type']: body['proxy_type'] = opts['proxy_type']
        opts.update({'body': json.loads(body)})
        opts.update(self._options)

        return self.post("/scrapers/{}/jobs".format(scraper_name), opts)
