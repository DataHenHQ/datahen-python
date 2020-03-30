from lib.datahen.client.Base import Base


class DeployKey(Base):
    
    def find(self, opts={}):
        opts.update(self._options)
        return self.get("/deploy_key", opts)

    def create(self, opts={}):
        opts.update(self._options)
        return self.post("/deploy_key", opts)

    def delete(self, opts={}):
        opts.update(self._options)

        return self.delete("/deploy_key", opts)
