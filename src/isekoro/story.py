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
            # TODO: 異世界消えた現象と、作家ということ、そして異世界殺しは作品の主人公と提示
            )

def sc_gotomyworld(w: wd.World):
    h = w.hiiragi
    return w.scene("私の異世界に",
            # TODO: パソコンに向かって書く、原稿世界に没入する、そして作中の人物を追い詰める、作品の簡易説明
            )

def sc_deadworld(w: wd.World):
    h = w.hiiragi
    return w.scene("死にゆく異世界",
            h.look("頬を打った冷たさにゆっくりと目を開ける"),
            h.look(""),
            # TODO: 雪がどんどん積もる世界、異世界の死が近づいている
            )

def sc_facetoface(w: wd.World):
    h = w.hiiragi
    return w.scene("対峙",
            w.hiiragi.come(w.stage.cherryhill, w.day.current),
            # TODO: 丘でやっと追いつく、そこにいると思った
            )

def sc_confession(w: wd.World):
    h = w.hiiragi
    return w.scene("告白",
            # TODO: 彼女に真実を告げる、彼女の告白
            )

def sc_truth(w: wd.World):
    h = w.hiiragi
    return w.scene("真実",
            # TODO: 真実の曝露、実は犯人は柊
            )

def sc_awake(w: wd.World):
    h = w.hiiragi
    return w.scene("そして目覚めた",
            # TODO: 夢オチ？　パソコンに残された言葉
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("異世界を殺すモノ"),
            sc_vanish(w),
            )

def ep_lastisekai(w: wd.World):
    return (w.chaptertitle("最後の異世界に"),
            sc_gotomyworld(w),
            sc_deadworld(w),
            sc_facetoface(w),
                w.hiiragi.think(w.i.stop_isekoro),
                w.hiiragi.know(w.i.isekoro),
                w.hiiragi.go(w.stage.cherryhill),
            )

def ep_isekaikoroshi(w: wd.World):
    return (w.chaptertitle("異世界殺し"),
            sc_confession(w),
            sc_truth(w),
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

