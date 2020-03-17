from lib.datahen.client.Base import Base
import sys

class Scraper(Base):

    def find(self, scraper_name):
        return self.get("/scrapers/{}".format(scraper_name))

    def all(self,opts={}):
        opts.update(self._options)
        return self.get("/scrapers",opts)

    def create(self,scraper_name, git_repository, opts={}):
        opts.update(self._options)
        body = {}
        body['name'] = scraper_name
        body['git_repository'] = git_repository
        body['git_branch'] = (opts['branch'] or opts['git_branch'] or "master" ) if opts['branch'] else opts['git_branch']
        if 'freshness_type' in opts and opts['freshness_type'] : body['freshness_type'] = opts['freshness_type']
        if  'force_fetch' in opts  and opts['force_fetch'] : body['force_fetch'] = opts['force_fetch']
        body['standard_worker_count'] = opts['workers'] or opts['standard_worker_count'] if opts['workers'] else opts['standard_worker_count']
        body['browser_worker_count'] = (opts['browsers'] or opts['browser_worker_count']) if opts['browsers'] else  opts['browser_worker_count']
        if 'proxy_type' in opts and opts['proxy_type'] : body['proxy_type'] = opts['proxy_type']
        if 'disable_scheduler' in opts and opts['disable_scheduler']:  body['disable_scheduler'] = opts['disable_scheduler']
        if 'cancel_current_job' in opts and  opts['cancel_current_job']:  body['cancel_current_job'] = opts['cancel_current_job']
        if 'schedule' in opts and opts['schedule']  :   body['schedule'] = opts['schedule']
        if 'timezone' in opts and opts['timezone'] : body['timezone'] = opts['timezone']





"""

def create(scraper_name, git_repository, opts={})
        body = {}
        body[:name] = scraper_name
        body[:git_repository] = git_repository
        body[:git_branch] = opts[:branch] || opts[:git_branch] || "master" if opts[:branch] || opts[:git_branch]
        body[:freshness_type] = opts[:freshness_type] if opts[:freshness_type]
        body[:force_fetch] = opts[:force_fetch] if opts[:force_fetch]
        body[:standard_worker_count] = opts[:workers] || opts[:standard_worker_count] if opts[:workers] || opts[:standard_worker_count]
        body[:browser_worker_count] = opts[:browsers] || opts[:browser_worker_count] if opts[:browsers] || opts[:browser_worker_count]
        body[:proxy_type] = opts[:proxy_type] if opts[:proxy_type]
        body[:disable_scheduler] = opts[:disable_scheduler] if opts[:disable_scheduler]
        body[:cancel_current_job] = opts[:cancel_current_job] if opts[:cancel_current_job]
        body[:schedule] = opts[:schedule] if opts[:schedule]
        body[:timezone] = opts[:timezone] if opts[:timezone]
        params = @options.merge({body: body.to_json})
        self.class.post("/scrapers", params)
      end




"""