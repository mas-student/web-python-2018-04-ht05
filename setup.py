from setuptools import setup, find_packages
from os.path import join, dirname

import os

setup(
    name='INPUT YOUR PROJECT NAME',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
    ],
    tests_require=[
    ],
)
