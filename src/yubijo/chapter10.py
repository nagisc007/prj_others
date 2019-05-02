# -*- coding: utf-8 -*-
"""Story: yubijo chapter10.
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
    return (w.maintitle("第十話"),
            w.zenzo.be(w.stage.office, w.day.meet4),
            w.zenzo.meet(w.cap),
            w.zenzo.do(w.murako, w.i.goheaven),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

