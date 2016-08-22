"""Pylint Sqlalchemy setup."""

from setuptools import setup, find_packages

VERSION = '0.1'

SHORT_DESC = ('pylint-sqlalchemy is a Pylint plugin for improving code'
              'analysis for when analysing code using Sqlalchemy.')

REQUIRES = [
    'SQLAlchemy',
    'pylint >= 1.6'
]

TESTS_REQUIRES = [
    'pytest',
    'pytest-cov'
]

setup(
    name='pylint_sqlalchemy',
    version=VERSION,
    description=SHORT_DESC,
    classifiers=[
        'Programming Language :: Python',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Topic :: Software Development :: Quality Assurance',
    ],
    author='lagel',
    author_email='lagel@live.com',
    url='http://lagelalegal.github.io/',
    packages=find_packages(),
    extras_require={
        'testing': TESTS_REQUIRES
    },
    install_requires=REQUIRES
)
