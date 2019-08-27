# -*- coding: utf-8 -*-
"""Story: chapter 4 'Goodbye home'
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
       "ゴブリンいないなう",
        "洞窟なう",# NOTE:洞窟内で
        "野営なう",# NOTE:野宿編１から
        ]

# scenes
## ep40 scenes
def sc_bridge(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    return w.scene("橋がある",
            )

# episodes
def ep40(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
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
    return (w.maintitle(cnf.TITLE["chap4"]),
            ep40(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

