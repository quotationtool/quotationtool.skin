# -*- coding: utf-8 -*-
"""Setup for quotationtool.skin package

$Id$
"""
from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

name='quotationtool.skin'

setup(
    name = name,
    version='0.1.0',
    description="Browser skin for the quotationtool application",
    long_description=(
        read('README')
        + '\n' +
        'Detailed Documentation\n'
        '**********************\n'
        + '\n' +
        read('src', 'quotationtool', 'skin', 'README.txt')
        + '\n' +
        'Download\n'
        '********\n'
        ),
    keywords='quotationtool',
    author=u"Christian Lueck",
    author_email='cluecksbox@googlemail.com',
    url='',
    license='ZPL 2.1',
    # Get more from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Programming Language :: Python',
                 'Environment :: Web Environment',
                 'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                 'Framework :: BlueBream',
                 ],
    packages = find_packages('src'),
    namespace_packages = ['quotationtool',],
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires = [
        'setuptools',
        'zope.interface',
        'zope.component',
        'zope.i18n',
        'zope.i18nmessageid',
        'zope.annotation',
        'zope.dublincore',
        'zope.location',
        'zope.security',
        'zope.securitypolicy',
        'zope.authentication',
        'zope.pluggableauth',
        'zope.app.authentication',
        'zope.traversing',
        'zope.tales',
        'zope.app.component',

        'z3c.template',
        'z3c.macro',
        'z3c.pagelet',
        'z3c.layer.pagelet',
        'zope.app.publication',
        'zope.browserpage',
        'zope.publisher',
        'z3c.formui',
        'z3c.form',
        'zc.resourcelibrary',
        'z3c.menu.ready2go',

        'zope.app.pagetemplate',
        'zope.viewlet',
        ],
    extras_require = dict(
        test = [
            'zope.testing',
            'zope.configuration',
            ],
        ),
    )
