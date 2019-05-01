# -*- coding: utf-8 -*-
"""Story: yubijo chapter04.
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
    return (w.maintitle("第四話　地縛霊がストーカーでも問題ないよね？"),
            w.zenzo.be(w.stage.office, w.day.meet),
            w.zenzo.hear(w.murako, w.i.ghostbuster),
            w.cap.come(w.stage.office),
            w.cap.talk(w.zenzo),
            w.zenzo.look(w.cap, "幽霊じゃない"),
            w.cap.ask(w.zenzo, w.i.ability),
            w.zenzo.reply(w.cap, "今までにない"),
            w.zenzo.ask(w.cap, w.i.salary),
            w.murako.talk(w.zenzo, w.i.ghostbuster),
            w.zenzo.do(w.i.ghost, w.i.goheaven, "$must"),
            w.zenzo.have(w.i.salary),
            w.zenzo.look(w.i.ghost),
            w.zenzo.go(w.stage.apart),
            w.zenzo.do("sleep"),
            w.zenzo.go(w.stage.city13, w.day.meet2),
            w.stage.city13.explain("都心から離れた少しのんびりした空気"),
            w.zenzo.meet(w.minako, w.stage.ghostschool),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

