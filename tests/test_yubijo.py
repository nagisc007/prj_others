# -*- coding: utf-8 -*-
"""Test: yubijo
"""
import unittest
from storybuilder.builder import testutils as utl
from src.yubijo.story import world, story


_FILENAME = "yubijo.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "yubijo project")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    @unittest.skip('use each current')
    def test_exists_looking(self):
        self.assertTrue(utl.exists_looking_from_master(self.story, self.ma))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags(self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self,
                [
                ("story", self.story, self.w.zenzo, self.w.murako),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                ("story", self.story,
                    w.zenzo.do(w.i.suicide),
                    w.zenzo.know(w.i.despair),
                    w.zenzo.do(w.i.hittruck),
                    w.zenzo.know(w.akebi, w.i.deadzenzo),
                    True),
                ])

