#!/usr/bin/python3

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Tue Apr 28 15:08:31 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

import os
from datetime import datetime

## Anticipating for a Enviornment variable to set if not given default is set to development

ApplicationStage = (os.getenv('APP_STAGE') or 'development' ).upper()
OutputInfo = 'We are running in {0}'.format(ApplicationStage)

if ApplicationStage.startswith('PROD')  or ApplicationStage.startswith('PRD'):
    OutputInfo = 'Warning: Please be aware that this is Production Envioenment'

print('{0} \n{1}'.format(OutputInfo,datetime.datetime.now()))