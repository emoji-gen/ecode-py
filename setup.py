# -*- encoding: utf-8 -*-

import re

from setuptools import setup


with open('ecode/__init__.py', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


setup(
    name='ecode',
    version=version,
    url='https://github.com/emoji-gen/ecode-py',
    project_urls={
        'Code': 'https://github.com/emoji-gen/ecode-py',
        'Issue tracker': 'https://github.com/emoji-gen/ecode-py/issues',
    },
    license='MIT',
    author='Emoji Generator',
    author_email='ultimate.emoji.gen@gmail.com',
    maintainer='Emoji Generator',
    maintainer_email='ultimate.emoji.gen@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=['ecode'],
    include_package_data=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
