#!/usr/bin/env python

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Sat May  9 09:17:57 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

import pytest
from pgDBbkp import cli

url = 'postgres://ted:password@example.com:5432/db_one'

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """ Program Exits Without a DRIVER and DESTINATION """
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_without_destination(parser):
    """ Program Exits With DRIVER But Without a DESTINATION """
    for driver in ['local' , 'remote' , 's3']:
        with pytest.raises(SystemExit):
            parser.parse_args([url, '--driver' , driver])

def test_parser_without_destination(parser):
    """ Program Exits Without DRIVER But With a DESTINATION """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver' , '/some/path'])