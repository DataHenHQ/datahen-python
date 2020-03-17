from lib.datahen.client.Base import Base
import sys

class AuthToken(Base):

    def find(self, token):
        return self.get("/auth_tokens/{}".format(token),self._options)

    def all(self,opts={}):
        opts.update(self._options)
        return self.get("/auth_tokens",opts)



    def create(self,role, description, opts={}):
        pass

    def create_on_account(self,account_id, role, description):
        pass

    def update(self,token, role, description="", opts={}):
        pass


    def  delete(self,token, opts={}):
        pass