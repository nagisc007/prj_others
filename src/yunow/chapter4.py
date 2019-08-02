# -*- coding: utf-8 -*-
"""Story: chapter 2 'Adventure'
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
        "Re: 教会なう",# NOTE:再び教会も、世界がループしていると認識
        "",
        ]

# scenes
## ep14 scene
def sc_awaking(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    return w.scene("再びの目覚め",
            h.be(w.stage.church1, w.day.awake2),
            h.look("$Sである少年は冷たい床の感触と共に目覚めた"),
            h.think("モンスターの大群に襲われて絶命した。",
                "そのはずなのに", "自分の手も足も体も",
                "それに頭の方もどうにか無事のようだ"),
            yula.talk("気が付かれましたか？"),
            h.look("声がして", "自分のすぐ傍にいつも神父が着ている紺のローブを羽織った女が立っているのが分かった。",
                "耳が隠れる程度のふわりとした金髪と笑みを浮かべた口に微かに見える八重歯が印象的なその女性は",
                "$Sが以前ここで目覚めた時にも神父の代理をしていたという彼女だ。",
                "確か名前は……"),
            yusha.ask("あんた$yulaとか言ったっけ？"),
            yula.talk("え！？", "なぜ$meの名を知っているの？"),
            h.look("一度会ったはずなのに目を大きくして不自然なくらいに彼女は驚いた"),
            yusha.talk("いや", "前にあんたから教わったんだよ。",
                "確か", "$n_priest1神父が旅行中だからって代理をしているんだろ？"),
            h.look("周囲をゆっくり確認すると",
                "いつも遊びに来る教会だ。",
                "高い天井で",
                "窓に誂えた申し訳程度のステンドグラスが色鮮やかな光を取り込んでいる。",
                "そういえばあれだけのモンスターの進軍を受けながら",
                "損傷一つない"),
            yusha.talk("なあ",
                "大魔王の軍勢にあんたは襲われなかったのか？"),
            h.look(""),
            )

def sc_reunion(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("仲間との再会",
            )

# episodes
def ep14(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_awaking(w),
            sc_reunion(w),
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
    return (w.maintitle(cnf.TITLE["chap2"]),
            ep14(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

