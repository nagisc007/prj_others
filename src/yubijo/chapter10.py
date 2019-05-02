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
    return (w.maintitle("第十話　退魔師が幽霊になっても問題ないよね？"),
            w.zenzo.do(w.murako, "もう一度殺す", "$must"),
            w.zenzo.know(w.murako, "原因"),
            w.zenzo.go(w.stage.ghosttonnel, w.day.meet4),
            w.zenzo.meet(w.cap),
            w.zenzo.meet(w.murako),
            w.zenzo.ask(w.murako, w.flag.case_murako),
            w.zenzo.know(w.deflag.case_murako),
            w.murako.reply(w.zenzo, "恩人"),
            w.murako.talk(w.zenzo, w.flag.secret_zenzo),
            w.zenzo.remember(w.deflag.secret_zenzo),
            w.zenzo.do(w.murako, w.i.goheaven),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

