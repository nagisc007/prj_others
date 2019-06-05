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
def sc_gotojob(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("仕事に出掛けてしまった",
            w.kyoko.be(w.stage.apart, w.day.current, w.hiiragi),
            w.kyoko.do("wait", w.hiiragi),
            w.hiiragi.go("仕事に出た"),
            w.kyoko.be("部屋で一人"),
            w.kyoko.deal("宅配が届く"),
            )

def sc_delivered(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("宅配便",
            kyoko.be(w.stage.apart, w.day.current),
            kyoko.have(w.hisfambox),
            w.kyoko.look(w.hisfambox),
            kyoko.look(w.hiiragi, w.famphoto),
            kyoko.think(w.i.hisgone),
            )

def sc_thinkfamily(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("彼の家族",
            kyoko.be(w.stage.apart, w.day.current),
            w.kyoko.think(w.i.departing),
            kyoko.think("どうすればいい？"),
            kyoko.do("涙"),
            )

def sc_herproblem(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("彼女の悩み",
            kyoko.be(w.stage.apart, w.day.current),
            w.kyoko.think(w.i.myreason),
            w.kyoko.talk().d("私の存在"),
            kyoko.feel(w.i.anxiety),
            kyoko.think(w.i.break_anxiety),
            )

def sc_breaker(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("破壊衝動",
            kyoko.be(w.stage.apart, w.day.current),
            kyoko.talk(hiiragi, "なんでいないの"),
            kyoko.do("break"),
            kyoko.do("部屋を空っぽ"),
            )

def sc_sink(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("沈む世界",
            kyoko.be(w.stage.apart, w.day.current),
            kyoko.look("空虚"),
            kyoko.think("別れ"),
            kyoko.do(w.i.sink),
            )

def sc_hishand(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("彼の手",
            kyoko.be(w.stage.apart, w.day.current),
            w.kyoko.meet(w.hiiragi),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("彼との安寧"),
            sc_gotojob(w),
            )

def ep_box(w: wd.World):
    return (w.chaptertitle("贈り物"),
            sc_delivered(w),
            sc_thinkfamily(w),
            )

def ep_breakmemory(w: wd.World):
    return (w.chaptertitle("思い出を壊す"),
            sc_herproblem(w),
            sc_breaker(w),
            )

def ep_hersinks(w: wd.World):
    return (w.chaptertitle("彼女は沈む"),
            sc_sink(w),
            sc_hishand(w),
            )

# outline
def episode_basics(w: wd.World):
    return [
            ("ep1", ep_intro(w), w.kyoko, w.hiiragi),
            ("ep2", ep_box(w), w.kyoko, w.hiiragi),
            ("ep3", ep_breakmemory(w), w.kyoko, w.hiiragi),
            ("ep4", ep_hersinks(w), w.kyoko, w.hiiragi),
            ]

def episode_outlines(w: wd.World):
    return [
            ("ep1", ep_intro(w),
                w.kyoko.do("wait", w.hiiragi),
                w.hiiragi.go("仕事に出た"),
                w.kyoko.be("部屋で一人"),
                w.kyoko.deal("宅配が届く"),
                True),
            ("ep2", ep_box(w),
                w.kyoko.think(w.i.hisgone),
                w.kyoko.have(w.hisfambox),
                w.kyoko.think("どうすればいい？"),
                w.kyoko.do("涙"),
                True),
            ("ep3", ep_breakmemory(w),
                w.kyoko.think(w.i.break_anxiety),
                w.kyoko.feel(w.i.anxiety),
                w.kyoko.do("break"),
                w.kyoko.do("部屋を空っぽ"),
                True),
            ("ep4", ep_hersinks(w),
                w.kyoko.think("別れ"),
                w.kyoko.look("空虚"),
                w.kyoko.do(w.i.sink),
                w.kyoko.meet(w.hiiragi),
                True),
            ]

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

