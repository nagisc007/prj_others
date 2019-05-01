# -*- coding: utf-8 -*-
"""Story: yubijo chapter03.
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
    return (w.maintitle("第三話　退魔師が恋に落ちても問題ないよね？"),
            w.zenzo.meet(w.murako, w.stage.ghosthome, w.day.meet),
            w.zenzo.look(w.murako, "セクシーな出で立ち"),
            w.murako.talk(w.zenzo, w.i.ability),
            w.zenzo.look(w.i.ghost_real),
            w.zenzo.ask(w.murako, w.i.ghost),
            w.murako.reply(w.zenzo, w.i.ghost),
            w.zenzo.know(w.murako, w.i.ghost),
            w.zenzo.look(w.i.ghost, w.i.beauty),
            w.murako.deal("誘う", w.zenzo, w.i.ghostbuster),
            w.zenzo.look(w.i.job, "$must"),
            w.zenzo.be(w.i.firejob),
            w.zenzo.talk(w.murako, w.i.ghostbuster),
            w.zenzo.be(w.i.ghostbuster),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

