from lib.datahen.client.Base import Base
import json

class EnvVar(Base):
    def find(self, name):
        return self.get("/env_vars/{}".format(name), self._options)

    def all(self, opts={}):
        opts.update(self._options)
        return self.get("/env_vars", opts)

    def set(self, name, value, opts={}):
        body = {}
        body['value'] = value
        if 'secret' in opts: body['secret'] = opts['secret']
        params = {}
        params.update({'data': json.dumps(body)})
        params.update(self._options)
        return self.post("/env_vars/{}".format(name), params)

    def unset(self, name, opts={}):
        opts.update(self._options)

        return self.delete("/env_vars/{}".format(name), opts)
