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


# main
def story(w: wd.World):
    return (w.maintitle("第七話　世界が滅んでも問題ないよね？"),
            w.zenzo.be(w.stage.ghosthospital, w.day.meet3),
            w.zenzo.be("life", w.beniko, w.mia, w.kii),
            w.beniko.do(w.zenzo, "取り合う"),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

