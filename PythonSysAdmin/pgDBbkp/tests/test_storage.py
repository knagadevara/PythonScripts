#!/usr/bin/env python

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Sun May 10 18:20:43 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

import pytest , tempfile
from pgDBbkp import storage

def test_local():
    """ Will test the storage functionality of writing the content of IN=FileA to OUT=FileB """
    infile = tempfile.TemporaryFile('r+b')
    infile.write(b"Testing")
    infile.seek(0)
    outfile = tempfile.NamedTemporaryFile(delete=False)
    storage.locally(infile, outfile)
    with open(outfile.name , 'r+b') as f:
        assert f.read() == b"Testing"
