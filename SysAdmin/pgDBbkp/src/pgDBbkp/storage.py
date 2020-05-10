#!/usr/bin/env python

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Sun May 10 19:28:35 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

def locally(INfile,OUTfile):
    OUTfile.write(INfile.read())
    OUTfile.close()
    INfile.close()

def s3AWS(botoS3_client, INfile , bucketName , OUTfile):
    return botoS3_client.upload_fileobj(INfile , bucketName , OUTfile)