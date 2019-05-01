# -*- coding: utf-8 -*-
"""Story: yubijo chapter01.
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
    return (w.maintitle("第一話　無職が自殺しても問題ないよね？"),
            w.zenzo.be(w.stage.chineseshop, w.day.meet),
            w.zenzo.know(w.i.firejob),
            w.zenzo.be(w.i.despair),
            w.zenzo.do(w.i.suicide, "$want"),
            w.zenzo.do(w.i.hittruck, w.i.suicide),
            w.zenzo.look(w.akebi, "美女"),
            w.zenzo.meet(w.akebi),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

