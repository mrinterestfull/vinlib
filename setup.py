from setuptools import setup, find_packages
import sys, os

version = '0.5'

setup(name='vinlib',
      version=version,
      description="Vehicle Identification Number Library",
      long_description="""\
Vehicle Identification Library written in Python. Check if vin# is authentic.""",
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
