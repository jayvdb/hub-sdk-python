#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

readme_contents = 'A Python SDK to access the Storyscript Hub, '
'which supports caching and more'

setup(
    name='story-hub',
    version='0.1.4',
    description='A Python SDK to access the Storyscript Hub, '
                'which supports caching and more',
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author='Storyscript',
    author_email='support@storyscript.io',
    url='https://github.com/storyscript/hub-sdk-python',
    packages=find_packages(exclude=('build.*', 'tests', 'tests.*')),
    python_requires='>=3.5',
    install_requires=[
        'requests~=2.21',
        'peewee==3.9.3',
        'cachetools==3.1.0'
    ],
    tests_require=[
        'pytest',
        'pytest-mock',
        'pytest-cov'
    ],
    setup_requires=['pytest-runner==4.4']
)
