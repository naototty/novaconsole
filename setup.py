# -*- coding: utf-8 -*-

import setuptools
from codecs import open
from os import path
import re


package_name = "novaconsole"


root_dir = path.abspath(path.dirname(__file__))


def _requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requires.txt')).readlines()]


def _devel_requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'devel-pip-freeze-requirements.txt')).readlines()]


with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    license = re.search(r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author = re.search(r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author_email = re.search(r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    url = re.search(r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    
    assert version
    assert license
    assert author
    assert author_email
    assert url


with open('README.md', encoding='utf-8') as f:
        long_description = f.read()


setuptools.setup(
    install_requires=open('requires.txt').readlines(),
    tests_requires=_devel_requirements(),

    version='2.0.1',
    name='novaconsole',
    packages=['novaconsole'],

    license=license,

    author=author,
    author_email=author_email,

    description='openstack compute serial console client: novaconsole',
    long_description=long_description,
    keywords='openstack, novaconsole, nova, serial console client',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: OpenStack',
        'Environment :: Console',
        'Topic :: System :: Shells',
        'Topic :: Terminals :: Serial',
        ],

    entry_points={
        'console_scripts': [
            'novaconsole = novaconsole.main:main',
        ],
    }
)
