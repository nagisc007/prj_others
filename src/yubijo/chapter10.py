# -*- coding: utf-8 -*-
"""Story: yubijo chapter10.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd


# episodes
def ep_avant(w: wd.World):
    return [w.chaptertitle("幽霊でもいい"),
            w.zenzo.be(w.stage.murakohome, w.day.meet4, w.murako),
            w.zenzo.do(w.murako, "もう一度殺す", "$must"),
            w.zenzo.know(w.murako, "原因"),
            w.zenzo.go(w.stage.ghosttonnel),
            w.zenzo.meet(w.cap),
            w.zenzo.meet(w.murako),
            w.zenzo.know(w.i.zenzo_ghost),
            w.zenzo.think(w.i.goheaven),
            w.zenzo.talk(w.murako),
            w.zenzo.talk("告白", w.murako),
            ]

def ep_ghostworld(w: wd.World):
    return [w.chaptertitle("世界が幽霊でも問題？"),
            w.zenzo.be(w.stage.ghostworld, w.day.meet4),
            w.zenzo.ask(w.murako, w.flag.case_murako),
            w.zenzo.know(w.deflag.case_murako),
            w.murako.reply(w.zenzo, "恩人"),
            w.zenzo.know(w.i.world_crisis),
            w.zenzo.talk(w.murako, "この世界"),
            w.zenzo.look(w.i.ghost_world),
            w.zenzo.think(w.i.goheaven, "$not"),
            ]

def ep_noproblem(w: wd.World):
    return [w.chaptertitle("何も問題なんてなかった"),
            w.murako.talk(w.zenzo, w.flag.secret_zenzo),
            w.zenzo.remember(w.deflag.secret_zenzo),
            w.zenzo.do(w.murako, w.i.goheaven),
            w.zenzo.be(w.stage.ghostworld, w.day.meet4),
            w.zenzo.know(w.i.crisis_cause),
            w.zenzo.think(w.murako, w.i.goheaven),
            w.zenzo.talk(w.murako, "何とかなる"),
            w.zenzo.do(w.murako, w.i.goheaven),
            w.cap.come(w.stage.office),
            w.cap.talk(w.zenzo, w.murako),
            ]


# main
def story(w: wd.World):
    return (w.maintitle("第十話　退魔師が幽霊になっても問題ないよね？"),
            ep_avant(w),
            ep_ghostworld(w),
            ep_noproblem(w),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

