from datahen import API

def all(scraper_name, params):
  client = API.BaseClient()

  return client.get(f"/scrapers/{scraper_name}/current_job/pages", params=params)