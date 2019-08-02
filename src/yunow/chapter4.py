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
            h.look("$yulaは不思議な目で彼を見ている"),
            h.deal("状況確認をしていく$S。どうやら自分が以前の世界に戻ったと知る"),
            h.move("教会を出ようとして", "彼女に声をかける$S"),
            yusha.talk("なああんた。", "もし神官や僧侶のような治癒魔法を習得しているなら一緒に旅をしないか。どうも魔王退治の前にこの世界のことをよく知らなきゃいけないみたいなんだわ"),
            yula.talk("残念ながら$meはここにいて悩みごとを聞いてあげるくらいしかできないわ。ごめんなさいね"),
            yusha.talk("そうか。", "まあ……何かあったらまた頼む"),
            h.think("近いうちに再会しそうだという予感を抱きながら",
                "$Sは教会を出た"),
            )

def sc_reunion(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("仲間との再会",
            h.think("とりあえず仲間だな。",
                "とは考えたが",
                "酒場に行ってもまともに冒険もしたことない未成年についてきてくれる傭兵はいない"),
            yusha.talk("こんな$meでも仲間として扱ってくれそうな奴か……"),
            h.think("あ……"),
            h.deal("咄嗟に赤い頭とピンクの頭が思い浮かび",
                "$Sはまず彼と出会った路地に向かった"),
            h.look("時間帯こそ違うが",
                "レンガ造りの住居が並び", "その家々から賑やかな声が漏れ聞こえる"),
            sol.talk(""),
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

