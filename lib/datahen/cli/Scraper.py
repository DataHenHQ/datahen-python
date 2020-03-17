import argparse
import sys

class Scraper:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Actions related to scrapers')
        parser.add_argument('action')
        args = parser.parse_args(sys.argv[2:3])

        if not hasattr(self, args.action):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        getattr(self, args.action)(args)

    def page(self, args):
        #@todo update page scraper
        #CLIScraperPage()

    def list(self, args):
        parser = argparse.ArgumentParser(description='List all scrapers on the account')
        parser.add_argument('-p', '--page', help="Page number", type=int, default=1)
        parser.add_argument('-P', '--per-page', help="Amount of records per page", type=int, default=100)
        args = parser.parse_args(sys.argv[3:])

        params = {
            'page': args.page,
            'per_page': args.per_page
        }

        output = datahen.Scrapers.all(params=params)

        pp.pprint(output)

    def create(self, args):
        parser = argparse.ArgumentParser(description='Create a scraper')
        parser.add_argument('scraper_name')
        parser.add_argument('git_repository')
        parser.add_argument('-b', '--branch', help="Set the Git branch to use. Default: master", type=str,
                            default='master')
        parser.add_argument('-t', '--freshness-type',
                            help="Set how fresh the page cache is. Possible values: day, week, month, year. Default: any",
                            type=str, default='any')
        parser.add_argument('--proxy-type', help="Set the Proxy type. Default: standard", type=str, default='standard')
        parser.add_argument('-f', '--force-fetch',
                            help="Set true to force fetch page that is not within freshness criteria. Default: false",
                            action='store_true')
        parser.add_argument('-w', '--workers', help="Set how many standard workers to use. Default: 1", type=int,
                            default=1)
        parser.add_argument('--browsers', help="Set how many browser workers to use. Default: 0", type=int, default=0)
        parser.add_argument('--disable-scheduler', help="Set true to disable scheduler. Default: false",
                            action='store_true')
        parser.add_argument('--cancel-current-job',
                            help="Set true to cancel currently active job if scheduler starts. Default: false",
                            action='store_true')
        parser.add_argument('--schedule', help="Set the schedule of the scraper to run. Must be in CRON format.",
                            type=str)
        parser.add_argument('--timezone',
                            help="Set the scheduler's timezone. Must be in IANA Timezone format. Defaults to \"America/Toronto\"",
                            type=str)
        args = parser.parse_args(sys.argv[3:])

        params = {
            'git_branch': args.branch,
            'freshness_type': args.freshness_type,
            'force_fetch': args.force_fetch,
            'standard_worker_count': args.workers,
            'browser_worker_count': args.browsers,
            'proxy_type': args.proxy_type,
            'disable_scheduler': args.disable_scheduler,
            'cancel_current_job': args.cancel_current_job,
            'schedule': args.schedule,
            'timezone': args.timezone
        }

        output = datahen.Scrapers.create(args.scraper_name, args.git_repository, params=params)

        pp.pprint(output)

    def update(self, args):
        parser = argparse.ArgumentParser(description='Update a scraper')
        parser.add_argument('scraper_name')
        parser.add_argument('-b', '--branch', help="Set the Git branch to use. Default: master", type=str,
                            default='master')
        parser.add_argument('-t', '--freshness-type',
                            help="Set how fresh the page cache is. Possible values: day, week, month, year. Default: any",
                            type=str, default='any')
        parser.add_argument('--proxy-type', help="Set the Proxy type. Default: standard", type=str, default='standard')
        parser.add_argument('-f', '--force-fetch',
                            help="Set true to force fetch page that is not within freshness criteria. Default: false",
                            action='store_true')
        parser.add_argument('-w', '--workers', help="Set how many standard workers to use. Default: 1", type=int,
                            default=1)
        parser.add_argument('--browsers', help="Set how many browser workers to use. Default: 0", type=int, default=0)
        parser.add_argument('--disable-scheduler', help="Set true to disable scheduler. Default: false",
                            action='store_true')
        parser.add_argument('--cancel-current-job',
                            help="Set true to cancel currently active job if scheduler starts. Default: false",
                            action='store_true')
        parser.add_argument('--schedule', help="Set the schedule of the scraper to run. Must be in CRON format.",
                            type=str)
        parser.add_argument('--timezone',
                            help="Set the scheduler's timezone. Must be in IANA Timezone format. Defaults to \"America/Toronto\"",
                            type=str)
        args = parser.parse_args(sys.argv[3:])

        params = {
            'git_branch': args.branch,
            'freshness_type': args.freshness_type,
            'force_fetch': args.force_fetch,
            'standard_worker_count': args.workers,
            'browser_worker_count': args.browsers,
            'proxy_type': args.proxy_type,
            'disable_scheduler': args.disable_scheduler,
            'cancel_current_job': args.cancel_current_job,
            'schedule': args.schedule,
            'timezone': args.timezone
        }

        output = datahen.Scrapers.update(args.scraper_name, params=params)

        pp.pprint(output)

    def show(self, args):
        parser = argparse.ArgumentParser(description='Show a scraper')
        parser.add_argument('scraper_name')
        args = parser.parse_args(sys.argv[3:])

        output = datahen.Scrapers.get_by_name(args.scraper_name)

        pp.pprint(output)

    def delete(self, args):
        parser = argparse.ArgumentParser(description='Delete a scraper and related records')
        parser.add_argument('scraper_name')
        args = parser.parse_args(sys.argv[3:])

        output = datahen.Scrapers.delete(args.scraper_name)

        pp.pprint(output)