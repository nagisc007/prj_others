# -*- coding: utf-8 -*-
"""Story: chapter 3 ''
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.pants import config as cnf
THM = cnf.THEMES

# titles
TITLE = [
        # chapter3
        # NOTE: １話あたり2000から3000字程度、増えたら前後編
        "パンツとストッキング",# NOTE: 彼女の妹
        ]

# scenes
## ep23 scenes
def sc_mysister(w: wd.World):
    h = hero = w.hero
    ery, dran, lily = w.ery, w.dran, w.lily
    return w.scene("我が妹",
            h.be(w.stage.left_prison, w.day.outprison),
            )

# episodes
def ep23(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_mysister(w),
            )

# outlines
def story_baseinfo(w: wd.World):
    return [
            ]

def story_outline(w: wd.World):
    return [
            ]

# main
def story(w: wd.World):
    return (w.maintitle(cnf.TITLES["chap03"]),
            ep23(w),
            )

def main(): # pragma: no cover
    from src.pants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

