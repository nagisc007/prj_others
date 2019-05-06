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
        self.chap1ep1 = chap01.ep_avant(self.w)
        self.chap1ep2 = chap01.ep_meetbijo(self.w)
        self.chap1ep3 = chap01.ep_bijoghost(self.w)
        self.chap2 = chap02.story(self.w)
        self.chap2ep1 = chap02.ep_avant(self.w)
        self.chap2ep2 = chap02.ep_goodyubijo(self.w)
        self.chap2ep3 = chap02.ep_ghostbuster(self.w)
        self.chap3 = chap03.story(self.w)
        self.chap3ep1 = chap03.ep_avant(self.w)
        self.chap3ep2 = chap03.ep_ghostbuster(self.w)
        self.chap3ep3 = chap03.ep_ghosthunter(self.w)
        self.chap4 = chap04.story(self.w)
        self.chap4ep1 = chap04.ep_avant(self.w)
        self.chap4ep2 = chap04.ep_ghostschool(self.w)
        self.chap4ep3 = chap04.ep_ghostjk(self.w)
        self.chap5 = chap05.story(self.w)
        self.chap5ep1 = chap05.ep_avant(self.w)
        self.chap5ep2 = chap05.ep_marryghost(self.w)
        self.chap5ep3 = chap05.ep_ghosthappy(self.w)
        self.chap6 = chap06.story(self.w)
        self.chap6ep1 = chap06.ep_avant(self.w)
        self.chap6ep2 = chap06.ep_gotohospital(self.w)
        self.chap6ep3 = chap06.ep_haremghosts(self.w)
        self.chap7 = chap07.story(self.w)
        self.chap7ep1 = chap07.ep_avant(self.w)
        self.chap7ep2 = chap07.ep_ghostworld(self.w)
        self.chap7ep3 = chap07.ep_anotherbuster(self.w)
        self.chap8 = chap08.story(self.w)
        self.chap8ep1 = chap08.ep_avant(self.w)
        self.chap8ep2 = chap08.ep_bounded(self.w)
        self.chap8ep3 = chap08.ep_secretfirstlove(self.w)
        self.chap9 = chap09.story(self.w)
        self.chap10 = chap10.story(self.w)

    def test_is_all_actions(self):
        self.assertTrue(utl.is_all_actions_in(self.story))

    @unittest.skip('use each current')
    def test_exists_looking(self):
        self.assertTrue(utl.exists_looking_from_master(self.story, self.ma))

    def test_followed_flags(self):
        self.assertTrue(utl.followed_all_flags_with_error_info(self, self.story))

    def test_has_basic_infos(self):
        utl.exists_basic_infos_by_data(self,
                [
                ("story", self.story, self.w.zenzo, self.w.murako),
                # chapter1
                ("chapter1", self.chap1, self.w.zenzo, self.w.akebi),
                ("chapter1-avant", self.chap1ep1, self.w.zenzo, self.w.truckdriver),
                ("chapter1-A", self.chap1ep2, self.w.zenzo, self.w.akebi),
                ("chapter1-B", self.chap1ep3, self.w.zenzo, self.w.akebi),
                # chapter2
                ("chapter2", self.chap2, self.w.zenzo, self.w.akebi),
                ("chapter2-avant", self.chap2ep1, self.w.zenzo, self.w.akebi),
                ("chapter2-A", self.chap2ep2, self.w.zenzo, self.w.akebi),
                ("chapter2-B", self.chap2ep3, self.w.zenzo, self.w.akebi),
                # chapter3
                ("chapter3", self.chap3, self.w.zenzo, self.w.murako),
                ("chapter3-avant", self.chap3ep1, self.w.zenzo, self.w.murako),
                ("chapter3-A", self.chap3ep2, self.w.zenzo, self.w.murako),
                ("chapter3-B", self.chap3ep3, self.w.zenzo, self.w.murako),
                # chapter4
                ("chapter4", self.chap4, self.w.zenzo, self.w.minako),
                ("chapter4-avant", self.chap4ep1, self.w.zenzo, self.w.murako),
                ("chapter4-A", self.chap4ep2, self.w.zenzo, self.w.minako),
                ("chapter4-B", self.chap4ep3, self.w.zenzo, self.w.minako),
                # chapter5
                ("chapter5", self.chap5, self.w.zenzo, self.w.minako),
                ("chapter5-avant", self.chap5ep1, self.w.zenzo, self.w.minako),
                ("chapter5-A", self.chap5ep2, self.w.zenzo, self.w.minako),
                ("chapter5-B", self.chap5ep3, self.w.zenzo, self.w.minako),
                # chapter6
                ("chapter6", self.chap6, self.w.zenzo, self.w.beniko),
                ("chapter6-avant", self.chap6ep1, self.w.zenzo, self.w.murako),
                ("chapter6-A", self.chap6ep2, self.w.zenzo, self.w.beniko),
                ("chapter6-B", self.chap6ep3, self.w.zenzo, self.w.beniko),
                # chapter7
                ("chapter7", self.chap7, self.w.zenzo, self.w.beniko),
                ("chapter7-avant", self.chap7ep1, self.w.zenzo, self.w.beniko),
                ("chapter7-A", self.chap7ep2, self.w.zenzo, self.w.beniko),
                ("chapter7-B", self.chap7ep3, self.w.zenzo, self.w.machiko),
                # chapter8
                ("chapter8", self.chap8, self.w.zenzo, self.w.machiko),
                ("chapter8-avant", self.chap8ep1, self.w.zenzo, self.w.machiko),
                ("chapter8-A", self.chap8ep2, self.w.zenzo, self.w.machiko),
                ("chapter8-B", self.chap8ep3, self.w.zenzo, self.w.machiko),
                # chapter9
                ("chapter9", self.chap9, self.w.zenzo, self.w.murako),
                # chapter10
                ("chapter10", self.chap10, self.w.zenzo, self.w.cap),
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
                ("chapter1-avant", self.chap1ep1,
                    w.zenzo.do(w.i.suicide, "$want"),
                    w.zenzo.be(w.i.despair),
                    w.zenzo.do(w.i.suicide),
                    w.zenzo.do(w.i.hittruck),
                    True),
                ("chapter1-A", self.chap1ep2,
                    w.zenzo.do(w.akebi, "love", "$want"),
                    w.zenzo.meet(w.akebi),
                    w.zenzo.talk(w.akebi, w.i.gosteady),
                    w.zenzo.do(w.akebi, w.i.gosteady, "yes"),
                    True),
                ("chapter1-B", self.chap1ep3,
                    w.zenzo.do(w.akebi, w.i.kiss, "$want"),
                    w.zenzo.be(w.akebi, w.i.gosteady),
                    w.zenzo.know(w.akebi),
                    w.zenzo.know(w.akebi, w.i.ghost),
                    True),
                # chapter2
                ("chapter2", self.chap2,
                    w.zenzo.do(w.akebi, w.i.makelove),
                    w.zenzo.look(w.akebi, "自分好み"),
                    w.zenzo.talk(w.akebi, "彼女のことを知る"),
                    w.zenzo.do(w.akebi, w.i.kiss),
                    True),
                ("chapter2-avant", self.chap2ep1,
                    w.zenzo.think(w.akebi, "付き合えないか"),
                    w.zenzo.know(w.akebi, w.i.ghost),
                    w.zenzo.be(w.akebi, "一緒に暮らす"),
                    w.zenzo.be(w.akebi, w.i.lostlife),
                    True),
                ("chapter2-A", self.chap2ep2,
                    w.zenzo.be(w.akebi, "恋人になる"),
                    w.zenzo.be(w.akebi, "好きになる"),
                    w.zenzo.talk(w.akebi, "思いを伝える"),
                    w.zenzo.do(w.akebi, w.i.kiss),
                    True),
                ("chapter2-B", self.chap2ep3,
                    w.zenzo.think(w.akebi, w.i.gotodeath),
                    w.zenzo.know(w.akebi, w.i.betogether, w.i.gotodeath),
                    w.zenzo.do(w.akebi, w.i.kiss),
                    w.zenzo.meet(w.murako),
                    True),
                # chapter3
                ("chapter3", self.chap3,
                    w.zenzo.look(w.i.job, "$must"),
                    w.zenzo.be(w.i.firejob),
                    w.zenzo.talk(w.murako, w.i.ghostbuster),
                    w.zenzo.be(w.i.ghostbuster),
                    True),
                ("chapter3-avant", self.chap3ep1,
                    w.zenzo.know(w.murako, "$want"),
                    w.zenzo.do("rescue", w.murako),
                    w.zenzo.hear(w.murako, w.i.job),
                    w.zenzo.meet(w.cap),
                    True),
                ("chapter3-A", self.chap3ep2,
                    w.zenzo.know(w.murako, w.i.ghostbuster),
                    w.zenzo.know(w.i.ghost),
                    w.zenzo.hear(w.murako, w.i.job),
                    w.zenzo.know(w.i.ghostbuster),
                    True),
                ("chapter3-B", self.chap3ep3,
                    w.zenzo.have(w.i.salary),
                    w.zenzo.be(w.i.poor),
                    w.zenzo.talk(w.murako, "頼む"),
                    w.zenzo.be(w.i.ghostbuster),
                    True),
                # chapter4
                ("chapter4", self.chap4,
                    w.zenzo.do(w.i.ghost, w.i.goheaven, "$must"),
                    w.zenzo.be(w.i.poor),
                    w.zenzo.look(w.i.ghost),
                    w.zenzo.meet(w.minako),
                    True),
                ("chapter4-avant", self.chap4ep1,
                    w.zenzo.have(w.i.salary, "$want"),
                    w.zenzo.be(w.i.poor),
                    w.zenzo.go(w.i.ghost, w.murako, "探しに行く"),
                    w.zenzo.have(w.i.rumor_ghostschool),
                    True),
                ("chapter4-A", self.chap4ep2,
                    w.zenzo.go(w.stage.ghostschool),
                    w.zenzo.look(w.i.ghost),
                    w.zenzo.look("search", w.stage.ghostschool),
                    w.zenzo.meet(w.minako),
                    True),
                ("chapter4-B", self.chap4ep3,
                    w.zenzo.do(w.i.goheaven, w.i.ghost),
                    w.zenzo.look("search", w.minako),
                    w.zenzo.talk(w.minako),
                    w.zenzo.be(w.minako, "取り憑かれた"),
                    True),
                # chapter5
                ("chapter5", self.chap5,
                    w.zenzo.do("help", w.minako),
                    w.zenzo.meet(w.minako),
                    w.zenzo.do(w.minako, "願望を叶える"),
                    w.zenzo.do("rescue", w.murako, w.i.crisis),
                    True),
                ("chapter5-avant", self.chap5ep1,
                    w.zenzo.do(w.i.goheaven, w.minako),
                    w.zenzo.be("付き合う", w.minako),
                    w.zenzo.be(w.i.kiss, w.minako),
                    w.zenzo.be("birth", w.ghostjk),
                    True),
                ("chapter5-A", self.chap5ep2,
                    w.zenzo.be("叶える", w.i.minako_dream),
                    w.zenzo.know(w.i.minako_dream),
                    w.zenzo.do(w.i.kiss),
                    w.zenzo.be("surround", w.ghostjk),
                    True),
                ("chapter5-B", self.chap5ep3,
                    w.zenzo.be("rescue", w.murako),
                    w.zenzo.meet(w.murako),
                    w.zenzo.go(w.minako, "runaway"),
                    w.zenzo.be(w.stage.ghostschool, "broken"),
                    True),
                # chapter6
                ("chapter6", self.chap6,
                    w.zenzo.look("new love", "$want"),
                    w.zenzo.do("失恋"),
                    w.zenzo.go(w.stage.ghosthospital),
                    w.zenzo.do("selection", "三人から"),
                    True),
                ("chapter6-avant", self.chap6ep1,
                    w.zenzo.look("診察", w.i.badhealth),
                    w.zenzo.feel(w.i.badhealth),
                    w.zenzo.look("安い病院を探す"),
                    w.zenzo.go(w.stage.ghosthospital),
                    True),
                ("chapter6-A", self.chap6ep2,
                    w.zenzo.know(w.i.badhealth),
                    w.zenzo.feel(w.i.badhealth),
                    w.zenzo.look("診察", w.beniko),
                    w.zenzo.know(w.beniko, w.i.ghost),
                    True),
                ("chapter6-B", self.chap6ep3,
                    w.zenzo.do(w.i.goheaven, w.beniko),
                    w.zenzo.meet(w.beniko, w.i.ghost),
                    w.zenzo.talk(w.beniko),
                    w.zenzo.meet(w.mia, w.kii),
                    True),
                # chapter7
                ("chapter7", self.chap7,
                    w.zenzo.think("決める", "marry", w.beniko, "$must"),
                    w.zenzo.do(w.i.propose, w.beniko),
                    w.zenzo.meet(w.murako),
                    w.zenzo.go(w.stage.ghosthospital, "$not"),
                    True),
                ("chapter7-avant", self.chap7ep1,
                    w.zenzo.think("ここは天国？"),
                    w.zenzo.look("美女だらけの世界"),
                    w.zenzo.do("enjoy harem"),
                    w.zenzo.look("女幽霊同士で孕む"),
                    True),
                ("chapter7-A", self.chap7ep2,
                    w.zenzo.meet(w.murako, "$must"),
                    w.zenzo.be("どんどん増える", w.i.ghost),
                    w.zenzo.go("runaway", w.stage.ghosthospital),
                    w.zenzo.be("幽霊だらけ"),
                    True),
                ("chapter7-B", self.chap7ep3,
                    w.zenzo.do(w.i.goheaven, "$must"),
                    w.zenzo.know(w.i.ghost, "大量"),
                    w.zenzo.be("need", "手助け"),
                    w.zenzo.meet(w.machiko),
                    True),
                # chapter8
                ("chapter8", self.chap8,
                    w.zenzo.know(w.flag.secret_murako, "$must"),
                    w.zenzo.hear(w.machiko, w.flag.secret_murako),
                    w.zenzo.deal("search", w.murako),
                    w.zenzo.deal(w.machiko, "監禁"),
                    True),
                ("chapter8-avant", self.chap8ep1,
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    True),
                ("chapter8-A", self.chap8ep2,
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    True),
                ("chapter8-B", self.chap8ep3,
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    w.zenzo.be(),
                    True),
                # chapter9
                ("chapter9", self.chap9,
                    w.zenzo.remember(w.flag.case_murako),
                    w.zenzo.hear(w.machiko, w.flag.case_murako),
                    w.zenzo.talk(w.murako),
                    w.zenzo.know(w.flag.secret_zenzo),
                    True),
                # chapter10
                ("chapter10", self.chap10,
                    w.zenzo.do(w.murako, "もう一度殺す", "$must"),
                    w.zenzo.know(w.murako, "原因"),
                    w.zenzo.meet(w.murako),
                    w.zenzo.do(w.murako, w.i.goheaven),
                    True),
                ])

