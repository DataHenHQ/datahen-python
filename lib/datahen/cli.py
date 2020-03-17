import datahen.Scrapers, datahen.ScraperJobPages, datahen.JobPages, datahen.Executor, datahen.ScraperJobs
import sys, argparse
import pprint

pp = pprint.PrettyPrinter(indent=1)

class DatahenCLI:
  def __init__(self):
    parser = argparse.ArgumentParser(description='Datahen python client')
    parser.add_argument('command', help='Subcommand to run')
    args = parser.parse_args(sys.argv[1:2])

    if not hasattr(self, args.command):
      print('Unrecognized command')
      parser.print_help()
      exit(1)

    getattr(self, args.command)()

  def scraper(self):
    CLIScraper()

  def seeder(self):
    CLISeeder()

  def parser(self):
    CLIParser()





class CLISeeder():
  def __init__(self):
    parser = argparse.ArgumentParser(description='Actions related to seeders')
    parser.add_argument('action')
    args = parser.parse_args(sys.argv[2:3])

    if args.action not in ['try', 'exec']:
      print('Unrecognized command')
      parser.print_help()
      exit(1)
    elif args.action == 'try':
      self.try_seeder(args)
    elif args.action == 'exec':
      self.exec_seeder(args)

  def try_seeder(self, args):
    parser = argparse.ArgumentParser(description='Tries a seeder file')
    parser.add_argument('scraper_name')
    parser.add_argument('seeder_file')
    parser.add_argument('-j', '--job', help="Set a specific job ID", type=int, default=None)
    args = parser.parse_args(sys.argv[3:])
    
    if args.job:
      datahen.Executor.PythonSeeder.exec_seeder(args.seeder_file, args.job)
    else:
      job = datahen.ScraperJobs.find(args.scraper_name)
      job_id = job['id']
      datahen.Executor.PythonSeeder.exec_seeder(args.seeder_file, job_id)

  def exec_seeder(self, args):
    parser = argparse.ArgumentParser(description="Executes a seeder script onto a scraper's current job.")
    parser.add_argument('scraper_name')
    parser.add_argument('seeder_file')
    parser.add_argument('-j', '--job', help="Set a specific job ID", type=int, default=None)
    args = parser.parse_args(sys.argv[3:])
    
    if args.job:
      datahen.Executor.PythonSeeder.exec_seeder(args.seeder_file, args.job, True)
    else:
      job = datahen.ScraperJobs.find(args.scraper_name)
      job_id = job['id']
      datahen.Executor.PythonSeeder.exec_seeder(args.seeder_file, job_id, True)

class CLIParser():
  def __init__(self):
    parser = argparse.ArgumentParser(description='Actions related to parsers')
    parser.add_argument('action')
    args = parser.parse_args(sys.argv[2:3])

    if args.action not in ['try', 'exec']:
      print('Unrecognized command')
      parser.print_help()
      exit(1)
    elif args.action == 'try':
      self.try_parser(args)
    elif args.action == 'exec':
      self.exec_parser(args)

  def try_parser(self, args):
    parser = argparse.ArgumentParser(description='Tries a parser on a Job Page')
    parser.add_argument('scraper_name')
    parser.add_argument('parser_file')
    parser.add_argument('gid')
    parser.add_argument('-j', '--job', help="Set a specific job ID", type=int, default=None)
    args = parser.parse_args(sys.argv[3:])
    
    if args.job:
      datahen.Executor.PythonParser.exec_parser_page(args.parser_file, args.gid, args.job)
    else:
      job = datahen.ScraperJobs.find(args.scraper_name)
      job_id = job['id']
      datahen.Executor.PythonParser.exec_parser_page(args.parser_file, args.gid, job_id)

  def exec_parser(self, args):
    parser = argparse.ArgumentParser(description="Executes a parser script on one or more Job Pages within a scraper's current job")
    parser.add_argument('scraper_name')
    parser.add_argument('parser_file')
    parser.add_argument('gid')
    parser.add_argument('-j', '--job', help="Set a specific job ID", type=int, default=None)
    args = parser.parse_args(sys.argv[3:])
    
    if args.job:
      datahen.Executor.PythonParser.exec_parser_page(args.parser_file, args.gid, args.job, True)
    else:
      job = datahen.ScraperJobs.find(args.scraper_name)
      job_id = job['id']
      datahen.Executor.PythonParser.exec_parser_page(args.parser_file, args.gid, job_id, True)

def main():
  DatahenCLI()

if __name__ == '__main__':
  main()