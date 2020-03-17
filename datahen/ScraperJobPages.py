from datahen import API

def all(scraper_name, params):
  client = API.BaseClient()

  return client.get(f"/scrapers/{scraper_name}/current_job/pages", params=params)

def find_content(scraper_name, gid):
  client = API.BaseClient()

  return client.get(f"/scrapers/{scraper_name}/current_job/pages/{gid}/content", {'get_raw': 1})