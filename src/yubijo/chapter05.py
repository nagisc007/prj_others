# -*- coding: utf-8 -*-
"""Story: yubijo chapter05.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.yubijo import config as cnf


# episodes
def ep_avant(w: wd.World):
    return [w.chaptertitle("美女幽霊ストーカー"),
            w.zenzo.meet(w.minako, w.stage.ghostschool, w.day.meet2),
            w.zenzo.hear(w.minako, w.i.minako_reason),
            w.zenzo.ask(w.minako, w.i.minako_death),
            w.zenzo.do("help", w.minako),
            w.minako.ask(w.zenzo, w.i.minako_dream),
            ]


def ep_marryghost(w: wd.World):
    return [w.chaptertitle("幽霊婚"),
            w.zenzo.do(w.minako, "願望を叶える"),
            w.zenzo.reply(w.minako, "yes"),
            w.zenzo.do("live with", w.minako, w.stage.ghostschool),
            w.zenzo.be("衰弱"),
            w.murako.come(w.stage.ghostschool),
            w.murako.talk(w.zenzo, "このままじゃ死ぬ"),
            w.zenzo.reply(w.murako, w.minako, w.i.minako_dream),
            w.murako.talk("忠告", w.zenzo),
            ]


def ep_ghosthappy(w: wd.World):
    return [w.chaptertitle("幽霊の幸福"),
            w.zenzo.be("衰弱"),
            w.zenzo.talk(w.minako, "幸せ"),
            w.murako.come(w.stage.ghostschool),
            w.murako.talk(w.minako),
            w.zenzo.do("rescue", w.murako, w.i.crisis),
            ]


# main
def story(w: wd.World):
    return (w.maintitle("第五話　退魔師が籠絡されても問題ないよね？"),
            ep_avant(w),
            ep_marryghost(w),
            ep_ghosthappy(w),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

