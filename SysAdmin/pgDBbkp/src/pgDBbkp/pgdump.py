#!/usr/bin/env python

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Sat May  9 23:04:02 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

import subprocess
import sys

def dump(url):
    try:
        return subprocess.Popen(['pg_dump' , url] , stdout=subprocess.PIPE)
    except (OSError , SystemError) as err:
        print(err)
        sys.exit(2)