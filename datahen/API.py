import requests
import yaml
import json
import os
from pathlib import Path

class BaseClient:
  CONFIG_PATH = Path(f"{str(Path.home())}/.datahen.yml")

  def __init__(self, auth_token = None):
    self._config = self._load_yaml_config()
    self._init_token(auth_token)

    self._base_headers = {
      "Authorization": f"Bearer {self._auth_token}",
      "Content-Type": "application/json",
    }
    
    self._base_api_url = "https://app.datahen.com/api/v1"

  def _load_yaml_config(self):
    if self.CONFIG_PATH.exists():
      with open(self.CONFIG_PATH, 'r') as f:
        try:
          yaml_data = yaml.safe_load(f)
        except yaml.scanner.ScannerError:
          yaml_data = {}

    return yaml_data

  def _init_token(self, auth_token):
    if 'DATAHEN_TOKEN' in os.environ:
      self._auth_token = os.environ['DATAHEN_TOKEN']
    elif 'api_token' in self._config:
      self._auth_token = self._config['api_token']
    elif auth_token is not None:
      self._auth_token = auth_token
    else:
      raise ValueError("Datahen token was not defined")

  def get(self, relative_url, params={}):
    url = f"{self._base_api_url}{relative_url}"
    
    query = {}
    if 'page' in params:
      query['p'] = params['page']
    
    if 'per_page' in params:
      query['pp'] = params['per_page']

    for key in params:
      if params[key] == True:
        query[key] = 'true'
      elif params[key] == False:
        query[key] = 'false'
      else:
        query[key] = params[key]

    r = requests.get(url, headers=self._base_headers, params=query)

    return r.json()

  def post(self, relative_url, params={}):
    url = f"{self._base_api_url}{relative_url}"
    
    query = {}

    for key in params:
      query[key] = params[key]

    r = requests.post(url, headers=self._base_headers, data=json.dumps(query))

    return r.json()

  def put(self, relative_url, params={}):
    url = f"{self._base_api_url}{relative_url}"
    
    query = {}

    for key in params:
      query[key] = params[key]

    r = requests.put(url, headers=self._base_headers, data=json.dumps(query))

    return r.json()

  def delete(self, relative_url, params={}):
    url = f"{self._base_api_url}{relative_url}"
    
    query = {}

    for key in params:
      query[key] = params[key]

    r = requests.delete(url, headers=self._base_headers, data=json.dumps(query))

    return r.json()