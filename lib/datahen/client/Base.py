import requests
import os
import json
import sys


class Base():
    def __init__(self, opts={}):

        self._ignore_ssl = opts.get('ignore_ssl')
        if 'auth_token' in opts and opts['auth_token']:
            self._auth_token = opts['auth_token']
        self._options = {
            'headers': {
                "Authorization": "Bearer {}".format(self.auth_token()),
                "Content-Type": "application/json",
            },
            'verify': self._ignore_ssl

        }
        query = {}
        if 'page' in opts and opts['page']:  query['p'] = opts['page']
        if 'per_page' in opts and opts['per_page']: query['pp'] = opts['per_page']
        if 'fetch_fail' in opts and opts['fetch_fail']: query['fetchfail'] = opts['fetch_fail']
        if 'parse_fail' in opts and opts['parse_fail']: query['parsefail'] = opts['parse_fail']
        if 'status' in opts and opts['status']: query['status'] = opts['status']
        if 'page_type' in opts and opts['page_type']: query['page_type'] = opts['page_type']
        if 'gid' in opts and opts['gid']: query['gid'] = opts['gid']
        if 'min-timestamp' in opts and opts['min-timestamp']: query['min-timestamp'] = opts['min-timestamp']
        if 'max-timestamp' in opts and opts['max-timestamp']: query['max-timestamp'] = opts['max-timestamp']
        if 'limit' in opts and opts['limit']:  query['limit'] = opts['limit']
        if 'order' in opts and opts['order']: query['order'] = opts['order']
        if 'query' in opts and opts['query']:
            if isinstance(opts['query'], dict):
                query['q'] = json.dumps(opts['query'])
            elif isinstance(opts['query'], str):
                query['q'] = json.loads(opts['query'])
        if query:
            self._options.update({'query': query})

    def ignore_ssl(self):
        if self._ignore_ssl is not None:
            return self._ignore_ssl
        self._ignore_ssl = self._env_ignore_ssl
        return self._ignore_ssl

    def env_auth_token(self):
        return os.getenv('DATAHEN_TOKEN')

    def env_ignore_ssl(self):
        return str(os.getenv('DATAHEN_IGNORE_SSL')).strip() == "1"

    def env_api_url(self):
        datahen_api_url = 'https://app.datahen.com/api/v1' if os.getenv('DATAHEN_API_URL') == None else os.getenv(
            'DATAHEN_API_URL')
        return datahen_api_url

    def auth_token(self, value=None):
        if value:
            return value
        return self.env_auth_token()

    def make_url(self, uri):
        return self.env_api_url() + uri

    def get(self, uri,options):
        url = self.make_url(uri)
        ans = requests.get(url, **options).text
        return ans

    def delete(self, uri,options):
        url = self.make_url(uri)
        ans = requests.delete(url, **options).text
        return ans

    def post(self, uri, post_data,options):
        url = self.make_url(uri)
        ans = requests.post(url, data=post_data, **options).text
        return ans
