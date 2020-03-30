from lib.datahen.client.Base import Base
import json


class Job(Base):
    def all(self, opts={}):
        opts.update(self._options)
        return self.get("/jobs", self._options)

    def find(self, job_id):
        return self.get("/jobs/{}".format(job_id), self._options)

    def update(self, job_id, opts={}):

        body = {}
        if 'status' in opts and opts['status']: body['status'] = opts['status']
        if 'workers' in opts and opts['workers']: body['standard_worker_count'] = opts['workers']
        if 'browsers' in opts and opts['browsers']: body['browser_worker_count'] = opts['browsers']
        opts.update({'body': json.loads(body)})
        opts.update(self._options)

        return self.put("/jobs/{}".format(job_id), opts)

    def cancel(self, job_id, opts={}):
        opts['status'] = 'cancelled'
        return self.update(job_id, opts)

    def resume(self, job_id, opts={}):
        opts['status'] = 'active'
        return self.update(job_id, opts)

    def pause(self, job_id, opts={}):
        opts['status'] = 'paused'
        return self.update(job_id, opts)

    def seeding_update(self, job_id, opts={}):

        body = {}
        if 'outputs' in opts and opts['outputs']:
            body['outputs'] = opts['outputs']
        else:
            body['outputs'] = []

        if 'pages' in opts and opts['pages']:
            body['pages'] = opts['pages']
        else:
            body['pages'] = []

        if 'seeding_status' in opts and opts['seeding_status']:
            body['seeding_status'] = opts['seeding_status']
        else:
            body['seeding_status'] = None

        if 'log_error' in opts and opts['log_error']: body['log_error'] = opts['log_error']

        opts.update({'body': json.loads(body)})
        opts.update(self._options)

        return self.put("/jobs/{}/seeding_update".format(job_id), opts)

    def finisher_update(self, job_id, opts={}):
        body = {}
        if 'outputs' in opts and opts['outputs']:
            body['outputs'] = opts['outputs']
        else:
            body['outputs'] = []

        if 'finisher_status' in opts and opts['finisher_status']:
            body['finisher_status'] = opts['finisher_status']
        else:
            body['finisher_status'] = None

        if 'log_error' in opts and opts['log_error']: body['log_error'] = opts['log_error']

        opts.update({'body': json.loads(body)})
        opts.update(self._options)
        return self.put("/jobs/{}/finisher_update".format(job_id), opts)
