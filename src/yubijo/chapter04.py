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
def ep_avant(w: wd.World):
    return [w.chaptertitle("幽霊探し"),
            w.zenzo.go(w.stage.apart),
            w.zenzo.do("sleep"),
            w.zenzo.come(w.stage.office, w.day.meet2),
            w.zenzo.hear(w.murako, w.i.ghostbuster),
            w.cap.come(w.stage.office),
            w.cap.talk(w.zenzo),
            w.zenzo.look(w.cap, "幽霊じゃない"),
            w.cap.ask(w.zenzo, w.i.ability),
            w.zenzo.reply(w.cap, "今までにない"),
            w.zenzo.ask(w.cap, w.i.salary),
            w.murako.talk(w.zenzo, w.i.ghost),
            w.murako.talk(w.zenzo, w.i.goheaven, w.akebi),
            w.murako.talk(w.zenzo, w.i.ghostbuster),
            w.zenzo.ask(w.murako, w.i.salary),
            w.zenzo.have(w.i.salary, "$want"),
            w.zenzo.be(w.i.poor),
            w.zenzo.do(w.i.ghost, w.i.goheaven, "$must"),
            w.zenzo.go(w.i.ghost, w.murako, "探しに行く"),
            w.zenzo.have(w.i.rumor_ghostschool),
            ]

def ep_ghostschool(w: wd.World):
    return [w.chaptertitle("廃校の怪"),
            w.zenzo.go(w.stage.street, w.day.meet2, w.murako),
            w.zenzo.go(w.stage.city13, w.day.meet2),
            w.stage.city13.explain("都心から離れた少しのんびりした空気"),
            w.zenzo.look(w.i.ghost),
            w.zenzo.go(w.stage.ghostschool),
            w.zenzo.look("search", w.stage.ghostschool),
            w.zenzo.meet(w.minako, w.stage.ghostschool),
            ]

def ep_ghostjk(w: wd.World):
    return [w.chaptertitle("幽霊JK"),
            w.zenzo.be(w.stage.ghostschool, w.day.meet2),
            w.zenzo.do(w.i.goheaven, w.i.ghost),
            w.zenzo.look("search", w.minako, "幽霊かどうか"),
            w.zenzo.talk(w.minako),
            w.zenzo.hear(w.i.minako_reason),
            w.zenzo.look(w.minako, "好みのタイプ"),
            w.zenzo.be(w.minako, "取り憑かれた"),
            ]



# main
def story(w: wd.World):
    return (w.maintitle("第四話　地縛霊がストーカーでも問題ないよね？"),
            ep_avant(w),
            ep_ghostschool(w),
            ep_ghostjk(w),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

