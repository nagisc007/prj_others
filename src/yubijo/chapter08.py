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
def ep_avant(w: wd.World):
    return [w.chaptertitle("彼女の姉"),
            w.zenzo.go(w.stage.apart, w.day.meet4, w.machiko),
            w.zenzo.meet(w.machiko),
            w.zenzo.know(w.machiko, w.murako, "sister"),
            w.machiko.talk(w.zenzo, w.flag.secret_murako),
            w.zenzo.hear(w.machiko, w.flag.secret_murako),
            w.zenzo.know(w.machiko, "$want"),
            w.zenzo.do(w.machiko, "救出"),
            w.zenzo.go(w.machiko, "ついていく"),
            w.zenzo.go(w.stage.ghosttonnel),
            w.zenzo.go(w.stage.murakohome),
            w.zenzo.be("監禁"),
            ]

def ep_bounded(w: wd.World):
    return [w.chaptertitle("囚われの善蔵"),
            w.zenzo.be("監禁", w.stage.murakohome, w.day.meet4),
            w.zenzo.know(w.flag.secret_murako, "$must"),
            w.zenzo.deal("search", w.murako),
            w.zenzo.go(w.stage.ghosttonnel),
            w.zenzo.go(w.stage.murakohome),
            w.zenzo.look("research", w.stage.murakohome),
            w.zenzo.go("逃げ出す"),
            w.zenzo.ask(w.machiko, w.i.machiko_reason),
            w.zenzo.know(w.i.firstlove, "関係している"),
            ]

def ep_secretfirstlove(w: wd.World):
    return [w.chaptertitle("初恋の秘密"),
            w.zenzo.be(w.stage.murakohome, w.day.meet4),
            w.zenzo.know(w.deflag.secret_murako),
            w.zenzo.deal(w.machiko, "監禁"),
            # TODO: secret world
            w.zenzo.know(w.deflag.secret_world),
            w.zenzo.know(w.murako, "$must"),
            w.zenzo.remember(w.i.firstlove, w.murako),
            w.zenzo.ask(w.machiko),
            w.zenzo.know(w.i.murako_dead),
            ]



# main
def story(w: wd.World):
    return (w.maintitle("第八話　初恋が失われても問題ないよね？"),
            ep_avant(w),
            ep_bounded(w),
            ep_secretfirstlove(w),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

