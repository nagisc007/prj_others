# -*- coding: utf-8 -*-
"""Story: the kyoko-san
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.kyoko import config as cnf


# scenes

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("彼との安寧"),
            w.kyoko.be(w.stage.apart, w.day.current, w.hiiragi),
            )

def ep_box(w: wd.World):
    return (w.chaptertitle("贈り物"),
            w.kyoko.look(w.hisfambox),
            w.kyoko.think(w.i.departing),
            )

def ep_breakmemory(w: wd.World):
    return (w.chaptertitle("思い出を壊す"),
            w.kyoko.think(w.i.myreason),
            w.kyoko.talk().d("私の存在"),
            )

def ep_hersinks(w: wd.World):
    return (w.chaptertitle("彼女は沈む"),
            w.kyoko.meet(w.hiiragi),
            )

# main
def world():
    w = wd.World("The kyoko-san project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("今日子さんの夕沈み"),
            ep_intro(w),
            ep_box(w),
            ep_breakmemory(w),
            ep_hersinks(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

