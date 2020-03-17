from datahen import API

def get_recent_exports(scraper_name):
  client = API.BaseClient()

  result = client.get(f"/scrapers/{scraper_name}/exports")
  
  if 'message' in result and result['message'] == "dbr: not found":
    raise ValueError(f"Scraper named {scraper_name} was not found")
  else:
    return result

def get_export_by_id(export_id):
  client = API.BaseClient()

  result = client.get(f"/scrapers/exports/{str(export_id)}")
  
  if 'message' in result and result['message'] == "dbr: not found":
    raise ValueError(f"Export with ID {str(export_id)} was not found")
  else:
    return result

def get_download_url_by_export_id(export_id):
  client = API.BaseClient()

  result = client.get(f"/scrapers/exports/{str(export_id)}/download")['signed_url']
  
  if 'message' in result and result['message'] == "dbr: not found":
    raise ValueError(f"Export with ID {str(export_id)} was not found")
  else:
    return result