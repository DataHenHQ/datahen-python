from lib.datahen.client.Base import Base
import json


class ScraperJobPage(Base):
    def find(self, scraper_name, gid):
        return self.get("/scrapers/{}/current_job/pages/{}".format(scraper_name, gid), self._options)

    def all(self, scraper_name, opts={}):
        opts.update(self._options)
        return self.get("/scrapers/{}/current_job/pages".format(scraper_name), opts)

    def update(self, scraper_name, gid, opts={}):
        body = {}
        if 'page_type' in opts and opts['page_type']: body['page_type'] = opts['page_type']
        if 'priority' in opts and opts['priority']: body['priority'] = opts['priority']
        if 'vars' in opts and opts['vars']: body['vars'] = opts['vars']
        opts.update({'body': json.loads(body)})
        opts.update(self._options)

        return self.post("/scrapers/{}/current_job/pages/{}".format(scraper_name, gid), opts)

    def refetch(self, scraper_name, opts={}):
        opts.update(self._options)
        return self.put("/scrapers/{}/current_job/pages/refetch".format(scraper_name), opts)

    def refetch_by_job(self, job_id, opts={}):
        opts.update(self._options)
        return self.put("/jobs/{}/pages/refetch".format(job_id), opts)

    def reparse(self, scraper_name, opts={}):
        opts.update(self._options)
        return self.put("/scrapers/{}/current_job/pages/reparse".format(scraper_name), opts)

    def reparse_by_job(self, job_id, opts={}):
        opts.update(self._options)
        return self.put("/jobs/{}/pages/reparse".format(job_id), opts)

    def enqueue(self, scraper_name, method, url, opts={}):
        body = {}

        if method != "":
            body['method'] = method
        else:
            body['method'] = "GET"
        body['url'] = url
        if 'page_type' in opts and opts['page_type']: body['page_type'] = opts['page_type']
        if 'priority' in opts and opts['priority']: body['priority'] = opts['priority']
        if 'fetch_type' in opts and opts['fetch_type']: body['fetch_type'] = opts['fetch_type']
        if 'body' in opts and opts['body']: body['body'] = opts['body']
        if 'headers' in opts and opts['headers']: body['headers'] = opts['headers']
        if 'vars' in opts and opts['vars']: body['vars'] = opts['vars']
        if 'force_fetch' in opts and opts['force_fetch']: body['force_fetch'] = opts['force_fetch']
        if 'freshness' in opts and opts['freshness']: body['freshness'] = opts['freshness']
        if 'ua_type' in opts and opts['ua_type']: body['ua_type'] = opts['ua_type']
        if 'no_redirect' in opts and opts['no_redirect']: body['no_redirect'] = opts['no_redirect']
        if 'cookie' in opts and opts['cookie']: body['cookie'] = opts['cookie']
        opts.update({'body': json.loads(body)})
        opts.update(self._options)

        return self.post("/scrapers/{}/current_job/pages".format(scraper_name), opts)

    def find_content(self, scraper_name, gid):
        return self.get("/scrapers/{}/current_job/pages/{}/content".format(scraper_name, gid), self._options)

    def find_failed_content(self, scraper_name, gid):
        return self.get("/scrapers/{}/current_job/pages/{}/failed_content".format(scraper_name), self._options)
