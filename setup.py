from setuptools import setup, find_packages
import sys, os

version = '2017.01.03'

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

2) Vin('somevinhere') will return object that has vehicle year and vin check true/false flag.

Install vinlib
~~~~~~~~~~~~~

PYPI
====

You can install vinlib from PyPi::

 easy_install vinlib
 #or
 pip install vinlib

Done.

Using vinlib
~~~~~~~~~~~

In python code you can batch through the vins to see if they are valid:

 import vinlib
 myvinnumber='1hasomenumberhere'
 print(vinlib.check_vin(myvinnumber))

This will return true or false depending if the vin number is correct or not.


To get more details on vin use the class based decoding::
 from vinlib import Vin
 myvin=Vin('1FA6p8Th8F1234567')

#prints the vin number we passed
 myvin.vin
 '1FA6P8TH8F1234567'

#prints if the check digit is correct. If False the vin# is invalid
 myvin.check
 False

#wmi tells you the World Manufacturer Identifier
 myvin.wmi
 'FORD'

#year tells you the year of the car
 myvin.year
 '2015'

#toJSON returns the data about vin for json style cosumption. jquery .ajax call,etc
myvin.toJSON()
outputs...well see yourself!


or more copy paste examples:

 import vinlib
 #get year from a vin
 print vinlib.Vin('1ZVIHaveAVinNumber17').year
 #check if vin is valid.
 print vinlib.Vin('1ZVIHaveAVinNumber17').check


Enjoy,

vinlib team.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='vin vinlib authentic, wmi, decode, check digit',
      author='Lukasz Szybalski',
      author_email='szybalski@gmail.com',
      url='http://lucasmanual.com/mywiki/vinlib',
      license='AGPL v3.0.  \
      Commercial licenses are also available from vinlib.org',
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
