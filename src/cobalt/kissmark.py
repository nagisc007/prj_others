# -*- coding: utf-8 -*-
"""Story: The kissmark
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.cobalt import config as cnf
THM = cnf.THEMES


# scenes

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            )

def ep_ramen(w: wd.World):
    return (w.chaptertitle("ラーメン屋"),
            )

def ep_oldstory(w: wd.World):
    return (w.chaptertitle("昔話"),
            )

def ep_univ(w: wd.World):
    return (w.chaptertitle("大学生"),
            )

def ep_kissmark(w: wd.World):
    return (w.chaptertitle("キスマーク"),
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
    return (w.maintitle("キスマーク"),
            ep_intro(w),
            ep_ramen(w),
            ep_oldstory(w),
            ep_univ(w),
            ep_kissmark(w),
            )

def main(): # pragma: no cover
    from src.cobalt.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

