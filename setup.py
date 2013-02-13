#!/usr/bin/env python

from setuptools import setup

setup(name='AlienFeed',
      version='0.1.0',
      description='AlienFeed is a commandline application made for displaying and interacting with Reddit submissions.',
      author='Jared Wright',
      license='LICENSE',
      keywords = "AlienFeed alien reddit feed rss tool cli",
      author_email='jawerty210@gmail.com',
      url='http://github.com/jawerty/AlienFeed',
      scripts=['alienfeed/alien.py'],
      install_requires=['praw'],
      entry_points = {
        'console_scripts': [
            'alienfeed = alien:main'
        ],
	  }
     )