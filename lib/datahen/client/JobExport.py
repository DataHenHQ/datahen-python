from lib.datahen.client.Base import Base


class JobExport(Base):
    def create(self,job_id, exporter_name):
        
        return self.post("/jobs/{}/exports/{}".format(job_id,exporter_name), self._options)
