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
def ep_avant(w: wd.World):
    return [w.chaptertitle("幽霊でも美少女なら大丈夫かも"),
            w.zenzo.meet(w.akebi, w.stage.ghosthome, w.day.meet),
            w.zenzo.look(w.akebi, "自分好み"),
            w.zenzo.know(w.akebi, w.i.ghost),
            w.zenzo.do(w.akebi, w.i.makelove),
            w.akebi.ask(w.zenzo, "幽霊でも良いのか？"),
            w.zenzo.think(w.akebi, "付き合えないか"),
            w.zenzo.reply(w.akebi, "yes"),
            w.zenzo.be(w.akebi, "一緒に暮らす"),
            w.zenzo.be(w.akebi, w.i.lostlife),
            ]

def ep_goodyubijo(w: wd.World):
    return [w.chaptertitle("どうせなら美少女の幽霊と付き合いたい"),
            w.zenzo.be(w.akebi, w.stage.ghosthome, w.day.meet),
            w.zenzo.talk(w.akebi, "寧ろ幽霊の方が良い"),
            w.akebi.think(w.zenzo, "呆れる"),
            w.zenzo.talk(w.akebi, "彼女のことを知る"),
            w.zenzo.ask(w.akebi, w.i.akebi_reason),
            w.akebi.talk(w.i.akebi_death),
            w.zenzo.talk(w.akebi, "解決する"),
            w.zenzo.be(w.akebi, "好きになる"),
            w.zenzo.be(w.akebi, "恋人になる"),
            w.zenzo.do("resolve", w.i.akebi_death),
            w.zenzo.talk(w.akebi, "思いを伝える"),
            w.zenzo.do(w.akebi, w.i.kiss),
            ]

def ep_ghostbuster(w: wd.World):
    return [w.chaptertitle("退治されるべき存在"),
            w.zenzo.do(w.akebi, w.i.kiss, "$not"),
            w.murako.come(w.stage.ghosthome, w.day.meet),
            w.zenzo.do(w.akebi, "守る"),
            w.zenzo.know(w.akebi, w.i.betogether, w.i.gotodeath),
            w.zenzo.think(w.akebi, w.i.gotodeath),
            w.akebi.be("vanish"),
            w.zenzo.meet(w.murako),
            w.zenzo.know(w.murako, w.i.ghostbuster),
            ]


# main
def story(w: wd.World):
    return (w.maintitle("第ニ話　ファーストキスが幽霊でも問題ないよね？"),
            ep_avant(w),
            ep_goodyubijo(w),
            ep_ghostbuster(w),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

