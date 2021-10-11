#!/usr/bin/env python

from setuptools import setup

setup(name='RSSparser',
      version='2.0',
      description='Final task for EPAM training',
      author='Anton Vashkevich',
      author_email='ant.vash94@gmail.com',
      packages=['rssparser','rssparser.utils'],
      entry_points={
        'console_scripts': ['rss-parser=rssparser.main:main'],
                    }

     )
