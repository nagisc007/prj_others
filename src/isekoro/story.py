# -*- coding: utf-8 -*-
"""Story: re_isekai_koroshi
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.noplot import config as cnf

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story", story(w), w.cameraman, w.koroshi),
            ]

def story_outline(w: wd.World):
    return [
            ("story", story(w),
                w.cameraman.be(),
                w.cameraman.be(),
                w.cameraman.be(),
                w.cameraman.be(),
                True),
            ]

# main
def world():
    w = wd.World("Re_isekai_koroshi")
    w.set_db(cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS,
            cnf.ITEMS,
            cnf.INFOS,
            cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("Re:異世界殺し"),
            w.cameraman.be(w.koroshi, w.stage.cherryhill, w.day.current),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

