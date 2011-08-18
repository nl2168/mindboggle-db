#!/usr/bin/env python

from distutils.core import setup

setup(name='mindboggle-db',
      version='0.1',
      description='Mindboggle graph database',
      author='Noah Lee',
      author_email='nl2168@columbia.edu',
      url='https://github.com/nl2168/mindboggle-db',
      license='OpenSource',
      platforms='Cross',
      packages=['3rd',
                'bin',
                'data',
                'db',
                'doc',
                'mindboggle-db',
                'mindboggle-db.algo',
                'mindboggle-db.core',
                'mindboggle-db.config',
                'mindboggle-db.db',
                'mindboggle-db.io',
                'mindboggle-db.misc',
                'mindboggle-db.sandbox',
                'mindboggle-db.testing',
                'mindboggle-db.tests',
                'tools',
                'web']
      )
