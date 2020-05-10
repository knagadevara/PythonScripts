from os import mkdir, makedirs
from shutil import move
from glob import glob
from json import dump , load

logger={}

## Path of files
processed_path = r'/tmp/processed'
created_path = r'/tmp/created'

## Checking if the directory aalready exists, else creating it.
for path in [processed_path , created_path ]:
    try:
        makedirs(path, mode=0o755, exist_ok=False)
    except Exception as err:
        logger['fileError {0}'.format(path)] = err

files_to_process = glob('{0}/receipt[0-9].json'.format(created_path))
##
#  Getting the list of recipts to process

subTotal = 0.0

for path in files_to_process:
    with open(path, 'r') as pf:
        content = load(pf)
        subTotal += float(content['amount'])

    dflname = path.split('/')[-1]
    destnation_path = '{0}/{1}'.format(processed_path, dflname)
    move(path,destnation_path)
    logger['Source {0}'.format(path)] = 'Destination {0}'.format(destnation_path)

print(subTotal)