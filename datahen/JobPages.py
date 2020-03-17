from datahen import API
import json

def find(job_id, gid, params = {}):
  client = API.BaseClient()

  return client.get(f"/jobs/{job_id}/pages/{gid}", params)

def all(job_id, params):
  client = API.BaseClient()

  return client.get(f"/jobs/{job_id}/pages", params)

def parsing_update(job_id, gid, options):
  client = API.BaseClient()

  body = {}
  body['outputs'] = options['outputs']
  body['pages'] = []
  body['parsing_status'] = options['status']

  return client.put(f"/jobs/{job_id}/pages/{gid}/parsing_update", body)