pgDBbkp
=======

CLI to backup PostgreSQL DB to local/remote or AWS S3.

Preparing for Development
-------------------------

        1. Ensure ``pip`` and ``pipenv`` are installed
        2. Clone git repository: ``git clone git@github.com:knagadevara/PythonScripts.git``
        3. Fetch Development dependencies: ``make install``


Usage
-----
Pass in full DB URL, type of storage driver and destination

S3 example with bucker name:

::
        $ pgDBbkp postgres://{USER_NAME}:{USER_PASS}@{HOST_NAME}:{PORT}/{DB_NAME} --driver s3/local/remote {S3_BUCKET_NAME}/{LOCAL_PATH}/{REMOTE_PATH}

Running Tests
-------------

Run Tests locally using ``make``:

::
        $virtualenv
        $activate
        $make
                or
        $pipenv run make
