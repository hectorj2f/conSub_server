#!/usr/bin/env python
import os
import sys

from setuptools import setup

description = '''This package provides a server consumer-subscriber'''

if os.path.isfile('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = description

setup_options = dict(
    name='consub',
    version='0.0.1',
    description='Server consumber-subscriber.',
    long_description=long_description,
    author='hectorj2f',
    author_email='hectorj@gmail.com',
    scripts=['consub', 'README.rst'],
    py_modules=['conSub_server'],
    install_requires=['tornado', 'PyYAML', 'psycopg2'],
    license="Apache License 2.0",
    classifiers=(
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)

setup(**setup_options)
