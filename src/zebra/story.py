# -*- coding: utf-8 -*-
"""Story: The zebra-bra
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.zebra import config as cnf
THM = cnf.THEMES


# scenes
# TODO: scene structure

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("思春期と下着について"),
            )

def ep_mylover(w: wd.World):
    return (w.chaptertitle("大好きな人"),
            )

def ep_underwear(w: wd.World):
    return (w.chaptertitle("大嫌いな下着"),
            )

def ep_mymind(w: wd.World):
    return (w.chaptertitle("私の気持ち"),
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story", story(w), w.emi, w.ken),
            ]

def story_outline(w: wd.World):
    return [
            ]

# main
def world():
    w = wd.World("The zebra-bra project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("ぜぶらぶら"),
            ep_intro(w),
            ep_mylover(w),
            ep_underwear(w),
            ep_mymind(w),
            # base
            w.emi.be(w.stage.hometown, w.day.getzebra),
            w.emi.think(w.ken, w.info("小さい頃からずっと好き")),
            w.emi.deal(w.info("下着をプレゼントされる")),
            w.emi.think(w.info("嫌いなゼブラ柄で付けるか迷う")),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

