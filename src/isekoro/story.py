# -*- coding: utf-8 -*-
"""Story: re_isekai_sunami
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.isekoro import config as cnf
THM = cnf.THEMES


# scenes
def sc_vanish(w: wd.World):
    h, kasagi = w.hiiragi, w.kasagi
    return w.scene("また異世界が消えた",
            h.be(w.stage.apart, w.day.current),
            h.look("また異世界が消えた"),
            h.deal("手に取ったスマートフォンのモニタには",
                "すぐに同じフレーズで何十という呟きが流れる"),
            h.talk("どうしてなんだ……なあ", "$sunami"),
            h.deal("ほどなく編集の$n_kasagiから電話があった"),
            h.talk("何ですか", "$kasagi"),
            kasagi.talk("ツイート見たか？"),
            h.talk("ええ"),
            h.look("そう答えつつ",
                "ノートパソコンの画面に映っていた原稿を一旦閉じてブラウザを表示する。",
                "国内の主要なニュースサイトでは特に扱われていないが",
                "一部",
                "特にライトノベルやアニメーション関連のニュースを載せているサイトでは",
                "最近よく見るワードが踊っていた"),
            kasagi.talk("またなんだろうな……$isekoro"),
            )

def sc_gotomyworld(w: wd.World):
    return w.scene("私の異世界に",
            )

def sc_facetoface(w: wd.World):
    return w.scene("対峙",
            w.hiiragi.come(w.stage.cherryhill, w.day.current),
            )

def sc_confession(w: wd.World):
    return w.scene("告白",
            )

def sc_awake(w: wd.World):
    return w.scene("そして目覚めた",
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("異世界を殺すモノ"),
            sc_vanish(w),
            )

def ep_lastisekai(w: wd.World):
    return (w.chaptertitle("最後の異世界に"),
            sc_gotomyworld(w),
            sc_facetoface(w),
                w.hiiragi.think(w.i.stop_isekoro),
                w.hiiragi.know(w.i.isekoro),
                w.hiiragi.go(w.stage.cherryhill),
            )

def ep_isekaikoroshi(w: wd.World):
    return (w.chaptertitle("異世界殺し"),
            sc_confession(w),
            sc_awake(w),
                w.hiiragi.know(w.sunami, w.i.truth),
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story", story(w), w.hiiragi, w.sunami),
            ]

def story_outline(w: wd.World):
    return [
            ("story", story(w),
                w.hiiragi.think(w.i.stop_isekoro),
                w.hiiragi.know(w.i.isekoro),
                w.hiiragi.go(w.stage.cherryhill),
                w.hiiragi.know(w.i.truth),
                True),
            ]

# main
def world():
    w = wd.World("Re_isekai_sunami")
    w.set_db(cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS,
            cnf.ITEMS,
            cnf.INFOS,
            cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("Re:異世界殺し"),
            ep_intro(w),
            ep_lastisekai(w),
            ep_isekaikoroshi(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

