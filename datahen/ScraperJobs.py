from datahen import API

def find(scraper_name, options = {}):
  client = API.BaseClient()

  result = client.get(f"/scrapers/{scraper_name}/current_job", options)
  
  if 'message' in result and result['message'] == "dbr: not found":
    raise ValueError(f"Scraper with name {scraper_name} or current job was not found")
  else:
    return result

def get_by_id(job_id):
  client = API.BaseClient()
  input_job_id = str(job_id)

  result = client.get(f"/jobs/{input_job_id}")
  
  if 'message' in result and result['message'] == "dbr: not found":
    raise ValueError(f"Job with ID {input_job_id} was not found")
  else:
    return result

def get_recent_jobs(scraper_name):
  client = API.BaseClient()

  result = client.get(f"/scrapers/{scraper_name}/jobs")
  
  if 'message' in result and result['message'] == "dbr: not found":
    raise ValueError(f"Scraper named {scraper_name} was not found")
  else:
    return result

def get_current_job_history(scraper_name):
  client = API.BaseClient()

  result = client.get(f"/scrapers/{scraper_name}/current_job/stats/history", {'limit': 1000})
  
  if 'message' in result and result['message'] == "dbr: not found":
    raise ValueError(f"Scraper named {scraper_name} was not found")
  else:
    return result