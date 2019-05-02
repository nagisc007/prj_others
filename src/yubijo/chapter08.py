# -*- coding: utf-8 -*-
"""Story: yubijo chapter08.
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
    return (w.maintitle("第八話　初恋が失われても問題ないよね？"),
            w.zenzo.go(w.stage.office, w.day.meet4, w.murako),
            w.zenzo.meet(w.machiko),
            w.zenzo.know(w.machiko, w.murako, "sister"),
            w.machiko.talk(w.zenzo, w.flag.secret_murako),
            w.zenzo.hear(w.machiko, w.flag.secret_murako),
            w.zenzo.know(w.flag.secret_murako, "$must"),
            w.zenzo.deal("search", w.murako),
            w.zenzo.go(w.stage.ghosttonnel),
            w.zenzo.go(w.stage.murakohome),
            w.zenzo.look("research", w.stage.murakohome),
            w.zenzo.know(w.deflag.secret_murako),
            w.zenzo.deal(w.machiko, "監禁"),
            # TODO: secret world
            w.zenzo.know(w.deflag.secret_world),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

