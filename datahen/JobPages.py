from datahen import API

def all(job_id, params):
  client = API.BaseClient()

  return client.get(f"/jobs/{job_id}/pages", params)