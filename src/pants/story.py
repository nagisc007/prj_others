# -*- coding: utf-8 -*-
"""Story: The pants project.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.pants import config as cnf
from src.pants import chapter01 as chap01
from src.pants import chapter02 as chap02
THM = cnf.THEMES


# outline
def story_baseinfo(w: wd.World):
    return [
            ("story", story(w), w.hero, w.hero),
            ] + chap01.story_baseinfo(w) \
                + chap02.story_baseinfo(w)

def story_outline(w: wd.World):
    return [
            ("story", story(w),
                w.hero.be(),
                w.hero.be(),
                w.hero.be(),
                w.hero.be(),
                True),
            ] + chap01.story_outline(w) \
                + chap02.story_outline(w)

# main
def world():
    w = wd.World("The pants project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS,
            )
    return w


def story(w: wd.World):
    return (w.maintitle("大賢者さまのパンツ！"),
            chap01.story(w),
            chap02.story(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

