#!/usr/bin/env python

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

	# By Author: knagadevara
	# Date: Sat May  9 06:59:32 IST 2020
	# Scripting Language: python
	# Copyright:: 2020, The Authors, All Rights Reserved. 

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

from setuptools import setup, find_packages

with open('README.rst' , 'r') as readme:
    readme = readme.read()

setup(  name='pgDBbkp', 
        version='0.2.0',
        description='DB Backup utility for local and cloud usage.',
        long_description=readme,
        author='Karthik Nagadevara',
        author_email='vnsk.1991@gmail.com',
        packages=find_packages('src'),
        package_dir={'':'src'},
        install_requires=[]
    )
