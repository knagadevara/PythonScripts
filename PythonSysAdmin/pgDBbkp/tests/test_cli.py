import pytest
from pgDBbkp import cli

url = 'postgres://ted:password@example.com:5432/db_one'

def test_parser_without_driver():
    """ Program Exits Without a DRIVER """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_without_destination():
    """ Program Exits With DRIVER But Without a DESTINATION """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver' , 'local'])

#def test_parser_with_driver_destination():
