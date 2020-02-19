from datahen import API

def all(params = {}):
  client = API.BaseClient()

  return client.get('/scrapers', params=params)

def get(scraper_name):
  client = API.BaseClient()

  result = client.get(f"/scrapers/{scraper_name}")
  
  if 'message' in result and result['message'] == "dbr: not found":
    raise ValueError(f"Scraper named {scraper_name} was not found")
  else:
    return result

def create(scraper_name, git_repository, params = {}):
  client = API.BaseClient()

  query = {}
  for key in params:
    query[key] = params[key]

  query['name'] = scraper_name
  query['git_repository'] = git_repository

  result = client.post(f"/scrapers", params=query)

  return result

def update(scraper_name, params = {}):
  client = API.BaseClient()

  query = {}
  for key in params:
    query[key] = params[key]

  query['name'] = scraper_name

  result = client.put(f"/scrapers/{scraper_name}", params=query)

  return result

def delete(scraper_name):
  client = API.BaseClient()

  result = client.delete(f"/scrapers/{scraper_name}")

  return result

def get_by_name(scraper_name):
  client = API.BaseClient()

  result = client.get(f"/scrapers/{scraper_name}")

  return result

def get_current_job_stats(scraper_name):
  client = API.BaseClient()

  result = client.get(f"/scrapers/{scraper_name}/current_job/stats/current")
  
  if 'message' in result and result['message'] == "dbr: not found":
    raise ValueError(f"Scraper named {scraper_name} was not found or no active job is present")
  else:
    return result