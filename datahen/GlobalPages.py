from datahen import API

def find(gid):
  client = API.BaseClient()

  result = client.get(f"/global_pages/{gid}")
  
  return result

def find_content(gid):
  client = API.BaseClient()

  result = client.get(f"/global_pages/{gid}/content")
  
  return result

def find_failed_content(gid):
  client = API.BaseClient()

  result = client.get(f"/global_pages/{gid}/failed_content")

  return result