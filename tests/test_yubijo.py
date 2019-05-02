# -*- coding: utf-8 -*-
"""Test: yubijo
"""
import unittest
from storybuilder.builder import testutils as utl
from src.yubijo.story import world, story
from src.yubijo import chapter01 as chap01
from src.yubijo import chapter02 as chap02
from src.yubijo import chapter03 as chap03
from src.yubijo import chapter04 as chap04
from src.yubijo import chapter05 as chap05
from src.yubijo import chapter06 as chap06
from src.yubijo import chapter07 as chap07
from src.yubijo import chapter08 as chap08
from src.yubijo import chapter09 as chap09
from src.yubijo import chapter10 as chap10


_FILENAME = "yubijo.story.py"


class StoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        utl.print_test_title(_FILENAME, "yubijo project")

    def setUp(self):
        self.w = world()
        self.story = story(self.w)
        self.chap1 = chap01.story(self.w)
        self.chap2 = chap02.story(self.w)
        self.chap3 = chap03.story(self.w)
        self.chap4 = chap04.story(self.w)
        self.chap5 = chap05.story(self.w)
        self.chap6 = chap06.story(self.w)
        self.chap7 = chap07.story(self.w)
        self.chap8 = chap08.story(self.w)
        self.chap9 = chap09.story(self.w)
        self.chap10 = chap10.story(self.w)

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
                # chapter1
                ("chapter1", self.chap1, self.w.zenzo, self.w.akebi),
                # chapter2
                ("chapter2", self.chap2, self.w.zenzo, self.w.akebi),
                # chapter3
                ("chapter3", self.chap3, self.w.zenzo, self.w.murako),
                # chapter4
                ("chapter4", self.chap4, self.w.zenzo, self.w.minako),
                # chapter5
                ("chapter5", self.chap5, self.w.zenzo, self.w.minako),
                # chapter6
                ("chapter6", self.chap6, self.w.zenzo, self.w.beniko),
                # chapter7
                ("chapter7", self.chap7, self.w.zenzo, self.w.akebi),
                # chapter8
                ("chapter8", self.chap8, self.w.zenzo, self.w.akebi),
                # chapter9
                ("chapter9", self.chap9, self.w.zenzo, self.w.akebi),
                # chapter10
                ("chapter10", self.chap10, self.w.zenzo, self.w.akebi),
                ])

    def test_has_outline_infos(self):
        w = self.w
        utl.exists_outline_infos_by_data(self,
                [
                ("story", self.story,
                    w.zenzo.do(w.i.suicide),
                    w.zenzo.be(w.i.despair),
                    w.zenzo.do(w.i.hittruck),
                    w.zenzo.know(w.akebi, w.i.deadzenzo),
                    True),
                # chapter1
                ("chapter1", self.chap1,
                    w.zenzo.do(w.i.suicide, "$want"),
                    w.zenzo.be(w.i.despair),
                    w.zenzo.do(w.i.suicide),
                    w.zenzo.meet(w.akebi),
                    True),
                # chapter2
                ("chapter2", self.chap2,
                    w.zenzo.do(w.akebi, w.i.makelove),
                    w.zenzo.look(w.akebi, "自分好み"),
                    w.zenzo.talk(w.akebi, "彼女のことを知る"),
                    w.zenzo.do(w.akebi, w.i.kiss),
                    True),
                # chapter3
                ("chapter3", self.chap3,
                    w.zenzo.look(w.i.job, "$must"),
                    w.zenzo.be(w.i.firejob),
                    w.zenzo.talk(w.murako, w.i.ghostbuster),
                    w.zenzo.be(w.i.ghostbuster),
                    True),
                # chapter4
                ("chapter4", self.chap4,
                    w.zenzo.do(w.i.ghost, w.i.goheaven, "$must"),
                    w.zenzo.have(w.i.salary),
                    w.zenzo.look(w.i.ghost),
                    w.zenzo.meet(w.minako),
                    True),
                # chapter5
                ("chapter5", self.chap5,
                    w.zenzo.do("help", w.minako),
                    w.zenzo.meet(w.minako),
                    w.zenzo.do(w.minako, "願望を叶える"),
                    w.zenzo.do("rescue", w.murako, w.i.crisis),
                    True),
                # chapter6
                ("chapter6", self.chap6,
                    w.zenzo.look("new love", "$want"),
                    w.zenzo.do("失恋"),
                    w.zenzo.go(w.stage.ghosthospital),
                    w.zenzo.do("selection", "三人から"),
                    True),
                # chapter7
                ("chapter7", self.chap7,
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    True),
                # chapter8
                ("chapter8", self.chap8,
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    True),
                # chapter9
                ("chapter9", self.chap9,
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    True),
                # chapter10
                ("chapter10", self.chap10,
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    True),
                ])

