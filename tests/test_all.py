# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest
import test_yubijo
import test_noplot
import test_kyoko
import test_koroshi


def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    suite.addTests((
        # GA
        unittest.makeSuite(test_yubijo.StoryTest),
        # novelup
        unittest.makeSuite(test_noplot.StoryTest),
        unittest.makeSuite(test_koroshi.StoryTest),
        # novema
        # cobalt
        unittest.makeSuite(test_kyoko.StoryTest),
        ))

    return suite
