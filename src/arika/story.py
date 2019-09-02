# -*- coding: utf-8 -*-
"""Story: The whereabouts
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.arika import config as cnf
THM = cnf.THEMES


# scenes
def sc_awaking(w: wd.World):
    return w.scene("目覚め",
            )

def sc_myfriend(w: wd.World):
    return w.scene("わたしのともだち",
            )

def sc_herboyfriend(w: wd.World):
    return w.scene("わたしの彼氏",
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("目覚めたら知らないわたし"),
            sc_awaking(w),
            )

def ep_unknownme(w: wd.World):
    return (w.chaptertitle("わたしの知らないわたし"),
            sc_myfriend(w),
            sc_herboyfriend(w),
            )

def ep_itsme(w: wd.World):
    return (w.chaptertitle("それがわたし"),
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ]

def story_outline(w: wd.World):
    return [
            ]

# main
def world():
    w = wd.World("The whereabouts project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("わたしの在り処"),
            ep_intro(w),
            ep_unknownme(w),
            ep_itsme(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

