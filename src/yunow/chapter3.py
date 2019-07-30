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
        "mamazonなう",# NOTE: 何でもamazon
        "代行なう",# NOTE: 代行業を依頼
        "全滅なう",# NOTE: 旅立ち編終了、ラストで死に戻り体験
        ]

# scenes
## ep11 scene
def sc_preparation(w: wd.World):
    h = yusha = w.yusha
    sol, mako, mam = w.sol, w.mako, w.mother
    return w.scene("旅立ちの準備だ",
            h.be(w.stage.myliving, w.day.firstawake2),
            h.deal("魔王退治の旅の準備について相談"),
            h.deal("目の前には大量のお菓子"),
            yusha.talk("いやその前にこれは何なんだよ？"),
            mako.talk("$meの朝ご飯。", "折角だから$taroと一緒に食べようと思って"),
            mako.talk("足りなかったらもっと言ってね。",
                "いくらでも持ってこさせるから"),
            sol.talk("こまけえことは気にすんな。",
                "それよりこの三人だけで本当に旅する気か？"),
            yusha.talk("いや気にしろよ！",
                "疑問に思えよ！",
                "そもそもこんなに沢山のお菓子どうしたんだ？"),
            mako.talk("え？", "これ"),
            h.look("$n_makoは$phoneを見せる。",
                "そこには$st_amazonと表示され",
                "大量のあれやこれやが価格と共に映っていた"),
            yusha.talk("コレは何？"),
            mako.talk("$st_amazonよ。",
                "例えば飲み物が欲しいなあって思うでしょ？",
                "で、ここからタピオカミルクティー選ぶでしょ？",
                "当日配送選ぶでしょ？",
                "はい終わり"),
            h.deal("$Sも$solも彼女が何をしているのかさっぱり分からないまま「お、おう」と頷く"),
            h.deal("しかし彼女が中央にピンクの甘いゼリーの乗ったクッキーを一つ食べ終えたところで",
                "何か届けられた"),
            mam.talk("ねえ$yusha。", "こんなものが着たんだけど？"),
            h.look("それは小さな紙の箱に入れられていたが",
                "中にはガラスのコップを満たす",
                "何か小さな粒状の黒いものがころころと入っているのが分かる不思議な薄茶色の液体が入っていた"),
            mako.talk("最近これ流行ってるんだって……美味しい"),
            h.deal("彼女は気にする様子もなく飲み始める"),
            )

def sc_mamazon(w: wd.World):
    h = yusha = w.yusha
    sol, mako, mam, daima = w.sol, w.mako, w.mother, w.daimaou
    return w.scene("mamazonは何でも揃う",
            mako.talk("だから$st_amazonなら何でも揃えられるのよ"),
            sol.talk("何でもってこたぁねえだろ？",
                "それじゃあ"),# NOTE:何か簡単なもの
            h.deal("すぐに届いた"),
            yusha.talk("じゃあ……これは？"),# NOTE:ちょっと無理め
            h.deal("しかしそれもすぐ届いた"),
            sol.talk("もうこれで魔王退治すればいいんじゃね？"),
            mako.talk("魔王退治までは流石に……あ"),
            h.look("魔王退治代行と書かれたものが見つかった"),
            mako.talk("とりあえず注文してみるね……"),
            h.deal("何も起こらない"),
            mako.talk("そうよね。流石に魔王退治までは"),
            h.look("その時", "空が唸った"),
            h.deal("慌てて外に出る三人"),
            h.look("誰もが真っ赤に焼けるような空を見上げていた。",
                "そこに浮かんでいた紫の雲が別の姿になる"),
            daima.talk("$meは大魔王。",
                "既に魔王は何者かによって倒されたが",
                "今度は$meがこの世界を支配することにした。",
                "人間どもよ怯えるが良い！", "フハハハハ"),
            yusha.talk("嘘だろ……$st_amazon最高かよ"),
            )

# episodes
def ep11(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_preparation(w),
            sc_mamazon(w),
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
            ep7(w),
            ep8(w),
            ep9(w),
            ep10(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

