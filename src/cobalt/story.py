# -*- coding: utf-8 -*-
"""Story: summary stories
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.cobalt import config as cnf
from src.cobalt import zebra
from src.cobalt import kissmark
THM = cnf.THEMES

# outline
def story_baseinfo(w: wd.World):
    return [
            ] + zebra.story_baseinfo(w) \
                + kissmark.story_baseinfo(w)

def story_outline(w: wd.World):
    return [
            ] + zebra.story_outline(w) \
                + kissmark.story_outline(w)

# main
def world():
    w = wd.World("The Cobalt short novel project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("Cobaltまとめ"),
            zebra.story(w),
            kissmark.story(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

