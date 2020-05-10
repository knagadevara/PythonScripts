#!/usr/bin/env python

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Mon May 11 02:22:27 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

import boto3
from pgDBbkp import cli , pgdump , storage


def main():
    args = cli.create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        storage.s3AWS(client, dump.stdout , args.destination , 'example.sql')
    else:
        outfile = open(args.destination , 'r+b')
        storage.locally(dump.stdout,outfile)