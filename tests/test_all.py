# -*- coding: utf-8 -*-
"""Test suite for all tests.
"""
import unittest
import test_yubijo
import test_kyoko
import test_zebra


def suite():
    '''Packing all tests.

    Returns:
        obj:`TestSuite`: testing suite object contained test cases.
    '''
    suite = unittest.TestSuite()

    suite.addTests((
        # GA
        unittest.makeSuite(test_yubijo.StoryTest),
        # novema
        # cobalt
        unittest.makeSuite(test_kyoko.StoryTest),
        unittest.makeSuite(test_zebra.StoryTest),
        ))

    return suite
