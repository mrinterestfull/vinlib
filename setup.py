from setuptools import setup, find_packages
import sys, os

version = '0.6.5'

setup(name='vinlib',
      version=version,
      description="Vehicle Identification Number Library",
      long_description="""\

.. contents::
   :depth: 3

vinlib
------

vinlib is a Vehicle Identification Number Package that allows you to verify and decode parts of the vin number.

Currently it can:
1) vinlib.check_vin will return whether the entered vin number is authentic/correct.
2) decode function coming soon.

Install vinlib
~~~~~~~~~~~~~~

PYPI
====

You can install vinlib from PyPi::

 easy_install vinlib

Done.

Using vinlib
~~~~~~~~~~~~

In python code you can::

 import vinlib
 myvinnumber='1hasomenumberhere'
 print vinlib.check_vin(myvinnumber)

This will return true or false depending if the vin number is correct or not.

Enjoy,

vinlib team.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='vin vinlib authentic',
      author='Lukasz Szybalski',
      author_email='szybalski@gmail.com',
      url='http://lucasmanual.com/mywiki/vinlib',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
        
      """,
      )
