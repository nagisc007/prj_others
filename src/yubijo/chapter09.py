# -*- coding: utf-8 -*-
"""Story: yubijo chapter09.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.yubijo import config as cnf


# episodes


# main
def story(w: wd.World):
    return (w.maintitle("第九話　真実が残酷でも問題ないよね？"),
            w.zenzo.be(w.stage.ghostworld, w.day.meet4, "監禁"),
            w.machiko.talk(w.zenzo, w.murako),
            w.machiko.ask(w.zenzo, w.flag.case_murako),
            w.zenzo.hear(w.machiko, w.flag.case_murako),
            w.zenzo.remember(w.flag.case_murako),
            w.machiko.talk(w.zenzo, "監禁は説明の為"),
            w.machiko.talk(w.zenzo, "自分が本物の退魔師"),
            w.zenzo.talk(w.murako),
            w.zenzo.meet(w.murako),
            w.zenzo.know(w.flag.secret_zenzo),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

