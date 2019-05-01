# -*- coding: utf-8 -*-
"""Story: yubijo.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.yubijo import config as cnf
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


# episodes


# main
def world():
    w = wd.World("yubijo project")
    w.set_db(cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS,
            cnf.ITEMS,
            cnf.INFOS,
            cnf.FLAGS,
            )
    return w


def story(w: wd.World):
    return (w.maintitle("幽霊が美少女なら問題ないよね？"),
            w.zenzo.hear(w.i.firejob, w.stage.chineseshop, w.day.meet),
            w.zenzo.look(w.wallet, w.i.poor),
            w.zenzo.know(w.i.despair),
            w.zenzo.remember(w.GAnovel),
            w.zenzo.do(w.i.suicide),
            w.zenzo.look(w.truck),
            w.zenzo.do(w.i.hittruck),
            w.zenzo.do("rescue", w.akebi),
            w.zenzo.know(w.akebi, w.i.deadzenzo),
            w.zenzo.do("rescue", w.murako),
            chap01.story(w),
            chap02.story(w),
            chap03.story(w),
            chap04.story(w),
            chap05.story(w),
            chap06.story(w),
            chap07.story(w),
            chap08.story(w),
            chap09.story(w),
            chap10.story(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

