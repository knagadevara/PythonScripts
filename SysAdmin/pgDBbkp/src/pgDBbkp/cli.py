#!/usr/bin/env python

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Sat May  9 09:16:59 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

import argparse , sys

parse_drivers = ['local' , 'remote' , 's3']
class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in parse_drivers:
            parser.error("Unknown driver given")
            sys.exit(1)
        else:
            namespace.driver = driver.lower()
            namespace.destination = destination
        #    return super().__call__(parser, namespace, values)

def create_parser():
    parser = argparse.ArgumentParser(prog='pgDBbkp', description=""" Backup PostgreSQL DB locally or to AWS S3 """)
    parser.add_argument('--url' , '-u', help='URL for the DB to backup' , type= str)
    parser.add_argument('--driver',  '-d', type= str , metavar=('DRIVER' , 'DESTINATION'),
    help='type of driver and destination should be provided' , nargs=2,
    action=DriverAction , required=True)
    return parser