# -*- coding: utf-8 -*-
"""Story: yubijo chapter07.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.yubijo import config as cnf


# episodes
def ep_avant(w: wd.World):
    return [w.chaptertitle("幽霊ハーレム"),
            w.zenzo.be(w.stage.ghosthospital, w.day.meet3),
            w.zenzo.be("life", w.beniko, w.mia, w.kii),
            w.beniko.do(w.zenzo, "取り合う"),
            w.zenzo.do(w.i.propose, w.beniko),
            w.zenzo.do(w.i.propose, w.mia),
            w.zenzo.be(w.stage.ghosthospital, w.day.meet3, w.beniko),
            w.zenzo.look("美女だらけの世界"),
            w.zenzo.think("ここは天国？"),
            w.zenzo.do("enjoy harem"),
            w.zenzo.look("女幽霊同士で孕む"),
            ]


def ep_ghostworld(w: wd.World):
    return [w.chaptertitle("幽霊で満たされる世界"),
            w.zenzo.be(w.stage.ghosthospital, w.day.meet3, w.beniko),
            w.zenzo.do(w.i.propose, w.kii),
            w.zenzo.think("決める", "marry", w.beniko, w.mia, w.kii, "$must"),
            w.zenzo.think(w.i.propose),
            w.zenzo.know(w.deflag.secret_hospital),
            w.zenzo.think(w.flag.secret_world),
            w.zenzo.be("どんどん増える", w.i.ghost),
            w.zenzo.be("手に負えない"),
            w.zenzo.meet(w.murako, "$must"),
            w.zenzo.go("runaway", w.stage.ghosthospital),
            w.zenzo.be("幽霊だらけ"),
            w.zenzo.know("病院から世界に幽霊が供給"),
            ]


def ep_anotherbuster(w: wd.World):
    return [w.chaptertitle("もう一人の退魔師"),
            w.zenzo.be(w.stage.ghosthospital, w.day.meet3, w.beniko),
            w.zenzo.talk(w.murako, w.flag.secret_hospital),
            w.zenzo.meet(w.murako),
            w.zenzo.go(w.stage.ghosthospital, "$not"),
            w.zenzo.do(w.i.goheaven, "$must"),
            w.zenzo.know(w.i.ghost, "大量"),
            w.zenzo.be("need", "手助け"),
            w.zenzo.look("次々除霊", w.X()),
            w.zenzo.meet(w.machiko),
            ]


# main
def story(w: wd.World):
    return (w.maintitle("第七話　世界が滅んでも問題ないよね？"),
            ep_avant(w),
            ep_ghostworld(w),
            ep_anotherbuster(w),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

