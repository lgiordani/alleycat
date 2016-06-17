#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

requirements = [
    'six'
]

test_requirements = [
    'pytest',
    'tox'
]

scripts = [
    'scripts/alleycat'
]

setup(
    name='alleycat',
    version='0.0.1',
    description="A cat chasing simulation",
    long_description="",
    author="Leonardo Giordani",
    author_email='giordani.leonardo@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements,
    scripts=scripts,
)
