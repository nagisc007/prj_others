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
            h.deal("目を覚ましたら$Sを感じた"),
            h.think("$Sって", "誰だ？"),
            h.look("部屋だ。",
                "真っ白な壁紙の", "天井も同じ素材の", "菓子箱の内側のような部屋で$Sは目覚めた。",
                "$Sは……$Sのままだ"),
            h.deal("自分自身の感覚を確かめるように右手を握る。",
                "ズレた掛け布団から曝露していたそれは上手く$Sに馴染んで握られてくれたけれど",
                "綿の軽さに埋まったもう片方はうまく力が入れられない。",
                "体を左側に捻ってから引き抜くと動いたシャツで乳首が擦れた"),
            h.deal("体を起こして改めて部屋を見回す。",
                "緑色のカーテンは日差しを遮っているけれどそれは完全ではなく",
                "外の明るさをほんのり伝えている。",
                "サイドに目の大きな女の子のキャラクターのステッカーが貼られた机の上には大学ノートが開かれたままで",
                "シャーペンと三色ボールペンが転がしてあった"),
            h.look("そのノートの手前で", "携帯電話が光っている。", "ワインレッドのフレームをしたそれは小さく震え",
                "息絶えるように止まった"),
            h.deal("$Sは息を詰め", "手を伸ばす。",
                "ひやりとした手応えは特別新しいものではなかったが",
                "指を触れて表示された画面には$Sの知らない名前があった"),
            mio.talk("$ln_"),
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
            ep_X1(w),
            ep_X2(w),
            ep_X3(w),
            ep_itsme(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

