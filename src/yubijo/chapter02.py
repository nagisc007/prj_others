# -*- coding: utf-8 -*-
"""Story: yubijo chapter02.
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
    return (w.maintitle("第ニ話　ファーストキスが幽霊でも問題ないよね？"),
            w.zenzo.meet(w.akebi, w.stage.ghosthome, w.day.meet),
            w.zenzo.look(w.akebi, "自分好み"),
            w.zenzo.do(w.akebi, w.i.makelove),
            w.akebi.ask(w.zenzo, "幽霊でも良いのか？"),
            w.zenzo.reply(w.akebi, "yes"),
            w.zenzo.talk(w.akebi, "寧ろ幽霊の方が良い"),
            w.akebi.think(w.zenzo, "呆れる"),
            w.zenzo.talk(w.akebi, "彼女のことを知る"),
            w.zenzo.ask(w.akebi, w.i.akebi_reason),
            w.akebi.talk(w.i.akebi_death),
            w.zenzo.talk(w.akebi, "解決する"),
            w.zenzo.do("resolve", w.i.akebi_death),
            w.zenzo.do(w.akebi, w.i.kiss),
            w.akebi.be("vanish"),
            w.murako.come(w.stage.ghosthome),
            w.zenzo.know(w.murako, w.i.ghostbuster),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

