# -*- coding: utf-8 -*-
"""Story: chapter 1 'Depature'
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.yunow import config as cnf
THM = cnf.THEMES

# titles
TITLE = [
        "ストーカーなう",
        "mamazonなう",
        ]

# scenes
## ep6 scenes
def sc_mystalker(w: wd.World):
    h = yusha = w.yusha
    sol, mam, mako = w.sol, w.mother, w.mako
    return w.scene("勇者のストーカー",
            )

def sc_threaten(w: wd.World):
    h = yusha = w.yusha
    sol, mam, mako = w.sol, w.mother, w.mako
    return w.scene("脅迫される勇者",
            )

# episodes
def ep6(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_mystalker(w),
            sc_threaten(w),
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ]

def story_outline(w: wd.World):
    return [
            ]

# main
def story(w: wd.World):
    return (w.maintitle(cnf.TITLE["chap1"]),
            ep6(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

