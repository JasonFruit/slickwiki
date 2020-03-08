#!/usr/bin/env python

import setuptools
from distutils.core import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(name='SlickWiki',
      version='0.1',
      description='Personal wiki tool',
      long_description=readme,
      # long_description_content_type="text/markdown",
      author='Jason R. Fruit',
      author_email='jasonfruit@fastmail.com',
      license="MIT",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
      ],
      packages=['slickwiki'],
      scripts=['slick'],
      install_requires=['cherrypy',
                        'markdown',
                        'pystache']
)
