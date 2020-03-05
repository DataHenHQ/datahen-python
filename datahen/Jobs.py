from datahen import API

def get_recent_jobs(scraper_name):
  client = API.BaseClient()

  result = client.get(f"/scrapers/{scraper_name}/jobs")
  
  if 'message' in result and result['message'] == "dbr: not found":
    raise ValueError(f"Scraper named {scraper_name} was not found")
  else:
    return result

def get_job_history(scraper_name):
  client = API.BaseClient()

  result = client.get(f"/scrapers/{scraper_name}/current_job/stats/history")
  
  if 'message' in result and result['message'] == "dbr: not found":
    raise ValueError(f"Scraper named {scraper_name} was not found")
  else:
    return result

def seeding_update(job_id, options):
  client = API.BaseClient()

  body = {}
  body['outputs'] = options['outputs']
  body['pages'] = options['pages']
  body['seeding_status'] = options['status']

  return client.put(f"/jobs/{job_id}/seeding_update", body)
