#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sphinxdoc

name = sphinxdoc.__name__
description = sphinxdoc.__description__
version = sphinxdoc.__version__
author = sphinxdoc.__author__
author_email = sphinxdoc.__author_email__
copyright = sphinxdoc.__copyright__
license = sphinxdoc.__license__
url_proyect = sphinxdoc.__url_proyect__
maintainer = sphinxdoc.__maintainer__
maintainer_email = sphinxdoc.__maintainer_email__

with open('README.rst') as file:
    long_description = file.read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()    

with open('dependencies.txt') as f:
    dependency_links = f.read().splitlines() 

classifiers = [
	'Environment :: Console',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
	'Natural Language :: Spanish',
	'Operating System :: Unix',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3.2',
	'Programming Language :: Python :: 3.3',
	'Programming Language :: Python :: 3.4',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'Topic :: Software Development :: User Interfaces',
	'Topic :: Utilities'
]
keywords = [
	'teminal',
	'console',
	'elmijo'
]

setup(
	name=name,
    version=version,
    url=url_proyect,
    license=license,
    description=description,
    long_description=long_description,
    author=author,
    author_email=author_email,
    maintainer=maintainer,
    maintainer_email=maintainer_email,    
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=install_requires,
    dependency_links=dependency_links,
    classifiers = classifiers,
	keywords = keywords,
	platforms='any',
	scripts=['scripts/ generate_modules','scripts/sphinxdoc']
)