from bs4 import BeautifulSoup
from datahen import Jobs, JobPages, GlobalPages
import gzip, pprint, requests

pp = pprint.PrettyPrinter(indent=1)

class PythonParser:
  @classmethod
  def exec_parser_page(self, filename, gid, job_id = None, save = False, vars = {}):
    executor = ParserExecutor(filename, gid, job_id, vars)

    executor.exec_parser(save)

class PythonSeeder:
  @classmethod
  def exec_seeder(self, filename, job_id = None, save = False):
    executor = SeederExecutor(filename, job_id)

    executor.eval_seeder_script(save)

class Executor:
  def __init__(self):
    self.job_id = None

  def get_content(self, gid):
    content_data = GlobalPages.find_content(gid)

    if 'available' in content_data and content_data['available']:
      compressed_content = requests.get(content_data['signed_url']).content
      content = gzip.decompress(compressed_content)
    else:
      content = ''

    return content

  def get_failed_content(self, gid):
    failed_content_data = GlobalPages.find_failed_content(gid)

    if 'available' in failed_content_data and failed_content_data['available']:
      compressed_content = requests.get(failed_content_data['signed_url']).content
      failed_content = gzip.decompress(compressed_content)
    else:
      failed_content = ''

    return failed_content

  def parsing_update(self, options):
    job_id = options.get('job_id', None)
    gid = options.get('gid', None)

    JobPages.parsing_update(job_id, gid, options)

  def update_to_server(self, options):
    None

  def eval_with_context(self, filename, context):
    parser_code = open(filename).read()
    exec(parser_code, context)

  def save_pages_and_outputs(self, pages, outputs, status, save = False):
    if save:
      print(f"Saving {len(pages)} pages and {len(outputs)} outputs")
      self.update_to_server({
        'job_id': self.job_id,
        'pages': pages,
        'outputs': outputs,
        'status': status
      })
    else:
      if len(pages) > 0:
        print('----------------------------------------')
        print(f"Would've saved {len(pages)} pages")
        pp.pprint(pages)

      if len(outputs) > 0:
        print('----------------------------------------')
        print(f"Would've saved {len(outputs)} outputs")
        pp.pprint(outputs)


class ParserExecutor(Executor):
  def __init__(self, filename, gid, job_id = None, vars = {}):
    self.filename = filename
    self.gid = gid
    self.job_id = job_id
    self.vars = vars

  def exec_parser(self, save = False):
    self.save = save
    
    if save:
      print("Executing parser script")
    else:
      print("Trying parser script")

    self.eval_parser_script(save)

  def eval_parser_script(self, save = False):
    if save:
      self.update_to_server({
        'job_id': self.job_id,
        'gid': self.gid,
        'pages': [],
        'outputs': [],
        'status': 'starting'
      })

    page = self.init_page()
    outputs = []
    pages = []
    content = self.get_content(self.gid)
    failed_content = self.get_failed_content(self.gid)

    context = {
      'BeautifulSoup': BeautifulSoup,
      'page': page,
      'content': content,
      'failed_content': failed_content,
      'outputs': outputs,
      'pages': pages
    }

    self.eval_with_context(self.filename, context)

    print("=========== Parsing Executed ===========")

    self.save_pages_and_outputs(pages, outputs, 'parsing', save)

    if save:
      self.update_to_server({
        'job_id': self.job_id,
        'gid': self.gid,
        'pages': [],
        'outputs': [],
        'status': 'done'
      })

  def init_page(self):
    if self.job_id:
      print("getting Job Page")
      return self.init_job_page()
    else:
      print("getting Global Page")
      return self.init_global_page()

  def init_job_page(self):
    return JobPages.find(self.job_id, self.gid)

  def init_global_page(self):
    return GlobalPages.find(self.gid)

  def update_to_server(self, options):
    JobPages.parsing_update(self.job_id, self.gid, {
      'pages': options['pages'],
      'outputs': options['outputs'],
      'status': options['status']
    })

class SeederExecutor(Executor):
  def __init__(self, filename, job_id):
    self.filename = filename
    self.job_id = job_id

  def update_to_server(self, options):
    Jobs.seeding_update(options['job_id'], {
      'pages': options['pages'],
      'outputs': options['outputs'],
      'status': options['status']
    })

  def eval_seeder_script(self, save = False):
    if save:
      self.update_to_server({
        'job_id': self.job_id,
        'pages': [],
        'outputs': [],
        'status': 'seeding'
      })

    outputs = []
    pages = []

    context = {
      'outputs': outputs,
      'pages': pages
    }

    self.eval_with_context(self.filename, context)

    print("=========== Seeding Executed ===========")

    self.save_pages_and_outputs(pages, outputs, 'seeding', save)

    if save:
      self.update_to_server({
        'job_id': self.job_id,
        'pages': [],
        'outputs': [],
        'status': 'done'
      })
