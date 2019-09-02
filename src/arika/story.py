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
    h = mio = w.mio
    return w.scene("目覚め",
            h.be(w.stage.myroom, w.day.first),
            # NOTE: 部屋、自分は誰か、二度目の感覚、呼びに来る母は知らない人
            )

def sc_myfamily(w: wd.World):
    h = mio = w.mio
    return w.scene("わたしの家族",
            h.be(w.stage.dyning),
            # NOTE: 朝食、知らない家族、知らない自分、高校生？　二学期
            )

def sc_myschool(w: wd.World):
    h = mio = w.mio
    return w.scene("わたしの学校",
            h.be(w.stage.school),
            # NOTE: 登校、知らない道、学校、教室も知らず、友達に声かけられ
            )

def sc_myfriend(w: wd.World):
    h = mio = w.mio
    return w.scene("わたしのともだち",
            h.be(w.stage.classroom),
            # NOTE: 友人、自分をよく知る、いつもと違う、雰囲気変わったって
            )

def sc_herboyfriend(w: wd.World):
    h = mio = w.mio
    return w.scene("わたしの彼氏",
            # NOTE: 彼氏がやってくる、放課後、初めて自分の本音を告げる
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("目覚めたら知らないわたし"),
            sc_awaking(w),
            )

def ep_unknownme(w: wd.World):
    return (w.chaptertitle("わたしの知らないわたし"),
            sc_myfamily(w),
            sc_myschool(w),
            sc_myfriend(w),
            sc_herboyfriend(w),
            )

def ep_X1(w: wd.World):
    return (w.chaptertitle("二日目の展開"),
            )

def ep_X2(w: wd.World):
    return (w.chaptertitle("その後はずっと自分で自分て何だろうと"),
            )

def ep_X3(w: wd.World):
    return (w.chaptertitle("迷うわたし"),
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

