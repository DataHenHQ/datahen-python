import argparse
import sys
class ScraperPage:
  def __init__(self):
    parser = argparse.ArgumentParser(description='Actions related to scraper pages')
    parser.add_argument('action')
    args = parser.parse_args(sys.argv[3:4])

    if not hasattr(self, args.action):
      print('Unrecognized command')
      parser.print_help()
      exit(1)

    getattr(self, args.action)(args)

  def list(self, args):
    parser = argparse.ArgumentParser(description='Actions related to scraper pages')
    parser.add_argument('scraper_name')
    parser.add_argument('-j', '--job', help="Set a specific job ID", type=int)
    parser.add_argument('-t', '--page-type', help="Filter by page_type", type=str)
    parser.add_argument('-p', '--page', help="Get the next set of records by page.", type=int)
    parser.add_argument('-P', '--per-page', help="Number of records per page. Max 500 per page.", type=int)
    parser.add_argument('--fetch-fail', help="Returns only pages that fails fetching.", action='store_true')
    parser.add_argument('--parse-fail', help="Returns only pages that fails parsing.", action='store_true')
    args = parser.parse_args(sys.argv[4:])

    params = {
      'page': args.page,
      'per_page': args.per_page,
      'page_type': args.page_type,
      'fetch_fail': args.fetch_fail,
      'parse_fail': args.parse_fail
    }

    if args.job:
      output = datahen.JobPages.all(args.job, params=params)
    else:
      output = datahen.ScraperJobPages.all(args.scraper_name, params=params)

    pp.pprint(output)