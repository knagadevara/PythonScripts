import argparse

class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination
        return super().__call__(parser, namespace, values, option_string)
    

def create_parser():
    parser = argparse.ArgumentParser(prog='pgDBbkp', description=""" Backup PostgreSQL DB locally or to AWS S3 """)
    parser.add_argument('url', '-u' , help='URL for the DB to backup')
    parser.add_argument('driver', '-d' ,
    help='type of driver and destination should be provided' , nargs=2,
    action=DriverAction, required=True)
    return parser
