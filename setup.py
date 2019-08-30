# -*- encoding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='ecode',
    packages=find_packages("src"),
    package_dir={"": "src"},
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
