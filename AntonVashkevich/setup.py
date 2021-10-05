#!/usr/bin/env python

from distutils.core import setup

setup(name='RSSparser',
      version='2.0',
      description='Final task for EPAM training',
      author='Anton Vashkevich',
      author_email='ant.vash94@gmail.com',
      packages=['rssparser'],
      entry_points={
        'console_scripts': ['rss-parser=rssparser.main:main'],
                    }

     )