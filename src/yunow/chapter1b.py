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
        "実況なう",
        "mamazonなう",
        ]

# scenes
## ep6 scenes
def sc_mystalker(w: wd.World):
    h = yusha = w.yusha
    sol, mam, mako = w.sol, w.mother, w.mako
    return w.scene("勇者のストーカー",
            h.be(w.stage.myhome, w.day.firstawake),
            mako.talk("$taroのこと特定しました"),
            h.think("何……だと！？"),
            h.look("$Sである少年は",
                "目の前のどう考えても彼より五歳程度は若いだろうと思われるピンクのおかっぱ娘の笑みに",
                "戦慄していた"),
            yusha.talk("あの……どうして$meの名前を？"),
            h.look("右側の膝が小刻みに震え始めたのを強引に手で押さえ込み",
                "$Sは尋ねる"),
            mako.talk("コレですよ"),
            h.look("愛らしい声と絶えない笑顔で彼女が見せたのは",
                "その小さな手にはやや余る$phoneと呼ばれる鉱石を加工した板状の道具だ。",
                "それは同じものを持つ者同士", "どんなに離れていても文字や映像をやり取りできるという",
                "不思議な能力があった"),
            h.look("$n_yusha様のご自宅なう"),
            h.look("そう書かれ",
                "家の玄関のドアと彼女がはにかむ様子が映っていた"),
            yusha.ask("……コレ",
                "何してるの？"),
            mako.talk("実況です"),
            yusha.talk("じっきょう？"),
            mako.talk("はい。", "$taro実況なうです"),
            h.look(""),
            # TODO: 魔子の話、説明、実況なう
            )

def sc_threaten(w: wd.World):
    h = yusha = w.yusha
    sol, mam, mako = w.sol, w.mother, w.mako
    return w.scene("脅迫される勇者",
            # TODO: ストーカーぶり、勇者とばらす、仲間増えたね
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

