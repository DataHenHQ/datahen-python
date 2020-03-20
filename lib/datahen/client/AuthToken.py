from lib.datahen.client.Base import Base
import sys
import json


class AuthToken(Base):
    def find(self, token):
        return self.get("/auth_tokens/{}".format(token), self._options)

    def all(self, opts={}):
        opts.update(self._options)
        return self.get("/auth_tokens", opts)

    def create(self, role, description, opts={}):
        body = {
            "role": role,
            "description": description
        }

        opts.update({'data': json.dumps(body)})
        opts.update(self._options)
        return self.post("/auth_tokens",opts)

    def create_on_account(self, account_id, role, description):
        opts = {}

        body = {
            "role": role,
            "description": description
        }

        opts.update({'data': json.dumps(body)})
        opts.update(self._options)
        return self.post("/{}/auth_tokens".format(account_id), opts)

    def update(self, token, role, description="", opts={}):
        body = {
            "role": role,
            "description": description
        }

        opts.update({'data': json.dumps(body)})
        opts.update(self._options)
        return self.put("/auth_tokens/{}".format(token), opts)



    def delete(self, token, opts={}):
        body = {}
        opts.update({'data': json.dumps(body)})
        opts.update(self._options)

        return self.delete("/auth_tokens/{}".format(token), opts)

