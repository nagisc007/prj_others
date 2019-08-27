# -*- coding: utf-8 -*-
"""Story: chapter 4 'Goodbye home'
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
       "ゴブリンいないなう",
        "洞窟なう",# NOTE:洞窟内で
        "野営なう",# NOTE:野宿編１から
        ]

# scenes
## ep40 scenes
def sc_bridge(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    return w.scene("橋がある",
            h.be(w.stage.homefield, w.day.awake5),
            h.look("城下町を出た$Sと愉快な仲間たちは街道沿いに北の$st_town2の町を目指していた"),
            yusha.talk("澄み渡る風なう！"),
            h.deal("元気に何もない草原に向かって$phoneを向けているのは短い黒髪に太眉が特徴的な$Sである少年だ。",
                "彼は$phoneと呼ばれる不思議な道具で見た景色を画像に収めつつ",
                "呟きを投稿するのが日課になっていた"),
            sol.talk("おい$yusha。",
                "風なんて画像にできないだろ？", "そもそも”なうなう”うるせえんだよ"),
            h.deal("その$Sに文句を垂れるのは赤髪で長身の戦士$sol。",
                "背中に大きな両手剣を背負い", "右肩には食料や簡易の寝袋の入った大きな袋を担いでいる"),
            mako.talk("いいんですよ$taroは。", "こうやって旅を楽しむことも魔王退治に大事なことなんだと……$meは思いますよ！"),
            h.deal("ピンクのおかっぱ頭の少女、$n_makoは", "被った尖り帽子を揺らしながら$Sに近づくと",
                "その手を握ろうとする。", "だが$Sはすっとそれを躱すと",
                "遠くの大きな岩に向けて$phoneで「岩なう」と呟いた"),
            yula.talk(""),
            # NOTE: ユラの言葉から、人物簡易紹介、関係性紹介、森がきえ、クレーベまでが簡単に行けるように。そして橋がかかっていて村が変わっている
            )

# episodes
def ep40(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_bridge(w),
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
    return (w.maintitle(cnf.TITLE["chap4"]),
            ep40(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

