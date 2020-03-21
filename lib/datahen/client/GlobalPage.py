from lib.datahen.client.Base import Base
import json

class GlobalPage(Base):

    def find(self, gid):
        return self.get("/global_pages/{}".format(gid), self._options)

    def find_content(self, gid):
        return self.get("/global_pages/{}/content".format(gid), self._options)
