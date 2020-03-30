from lib.datahen.client.Base import Base


class JobOutput(Base):
    def find(self, job_id, collection, id):
        return self.get("/jobs/{}/output/collections/{}/records/{}".format(job_id, collection, id), self._options)

    def all(self, job_id, collection='default'):
        return self.get("/jobs/{}/output/collections/{}/records".format(job_id, collection), self._options)

    def collections(self, job_id):
        return self.get("/jobs/{}/output/collections".format(job_id), self._options)
