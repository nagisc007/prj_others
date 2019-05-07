# -*- coding: utf-8 -*-
"""Story: yubijo chapter09.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd


# episodes
def ep_avant(w: wd.World):
    return [w.chaptertitle("上司が幽霊でも問題ない？"),
            w.zenzo.be(w.stage.ghostworld, w.day.meet4, "監禁"),
            w.machiko.talk(w.zenzo, w.murako),
            w.machiko.ask(w.zenzo, w.flag.case_murako),
            w.zenzo.hear(w.machiko, w.flag.case_murako),
            w.zenzo.remember(w.flag.case_murako),
            w.zenzo.be(w.stage.office, w.day.meet4, w.murako),
            ]


def ep_facemurako(w: wd.World):
    return [w.chaptertitle("邑子との対峙"),
            w.machiko.talk(w.zenzo, "監禁は説明の為"),
            w.machiko.talk(w.zenzo, "自分が本物の退魔師"),
            w.zenzo.talk(w.murako),
            w.zenzo.meet(w.murako),
            w.zenzo.know(w.flag.secret_zenzo),
            w.zenzo.be(w.stage.office, w.day.meet4, w.murako),
            ]


def ep_whichghost(w: wd.World):
    return [w.chaptertitle("どちらが幽霊？"),
            w.zenzo.be(w.stage.office, w.day.meet4, w.murako),
            ]


# main
def story(w: wd.World):
    return (w.maintitle("第九話　真実が残酷でも問題ないよね？"),
            ep_avant(w),
            ep_facemurako(w),
            ep_whichghost(w),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

