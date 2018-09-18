from setuptools import setup, find_packages
from pip.req import parse_requirements
import sys, os, pip

version = '0.1'

requirements = [
    str(requirement.req)
    for requirement in parse_requirements('requirements.txt', session = pip.download.PipSession())
]

setup(name='reko',
      version=version,
      description="",
      long_description="""\
Image recognition using aws rekognition""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='rekognition image classification aws',
      author='geeawa',
      author_email='gee.awa@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
