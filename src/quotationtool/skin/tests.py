import unittest
import doctest
from zope.component.testing import setUp, tearDown, PlacelessSetup
import zope.interface
import zope.component
from zope.configuration.xmlconfig import XMLConfig, xmlconfig

import quotationtool.skin


class SkinTests(PlacelessSetup, unittest.TestCase):

    def testConfig(test):
        XMLConfig('configure.zcml', quotationtool.skin)()


def test_suite():
    return unittest.TestSuite((
            unittest.makeSuite(SkinTests),
            ))

