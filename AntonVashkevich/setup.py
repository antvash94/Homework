#!/usr/bin/env python

from setuptools import setup

setup(name='RSSparser',
      version='2.0',
      description='Final task for EPAM training',
      author='Anton Vashkevich',
      author_email='ant.vash94@gmail.com',

      packages=['rss_parser', 'rss_parser.utils'],
      package_data={"rss_parser.utils": ["templates/*", "templates/fonts/*", "image/*"]},
      entry_points={
        'console_scripts': ['rss-parser=rss_parser.main:main'],
                    }

     )
