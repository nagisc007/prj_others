# -*- coding: utf-8 -*-
"""Story: yubijo chapter06.
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
    return (w.maintitle("第六話　ハーレムが地獄でも問題ないよね？"),
            w.zenzo.be(w.stage.office, w.day.meet3),
            w.zenzo.remember(w.minako),
            w.zenzo.do("失恋"),
            w.zenzo.look("new love", "$want"),
            w.murako.ask(w.zenzo, "仕事したら？"),
            w.zenzo.ask(w.murako, w.i.ability),
            w.murako.reply("よく知らない"),
            w.murako.talk(w.zenzo, w.stage.ghosthospital),
            w.zenzo.ask(w.stage.ghosthospital),
            w.murako.talk(w.i.ghospital_info),
            w.zenzo.go(w.stage.ghosthospital),
            w.zenzo.meet(w.beniko),
            w.zenzo.meet(w.mia),
            w.zenzo.meet(w.kii),
            w.zenzo.hear(w.i.beniko_reason),
            w.zenzo.hear(w.i.mia_reason),
            w.zenzo.hear(w.i.kii_reason),
            w.zenzo.do("selection", "三人から"),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

