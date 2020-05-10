#!/usr/bin/env python

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Sat May  9 20:20:56 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

import pytest
import subprocess
from pgDBbkp import pgdump

url = 'postgres://ted:password@example.com:5432/db_one'

def test_dump_call_pgdump(mocker):
    """ Utilize pgdumpo to interact with Database3 """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump' , url] , stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
    """ If pgdump doesnot exist """
    mocker.patch('subprocess.Popen' , side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)
