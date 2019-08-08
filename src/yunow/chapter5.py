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
        "逃走中なう",# NOTE: 冒険に出てモンスター遭遇、GPSで位置把握して逃げる
        "宿屋なう",# NOTE: 隣町、宿の主人から色々聞くことに
        "はじめてのおつかいなう",# NOTE:初クエスト
        "洞窟なう",# NOTE:洞窟内で
        "野営なう",# NOTE:野宿編１から
        ]

# scenes
## ep21 scenes
def sc_lookfield(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("はじめてのフィールド",
            h.be(w.stage.homefield, w.day.awake3),
            h.feel("遠くに臨む$st_homemountからの吹き下ろしの風が頬を撫でていく"),
            yusha.talk("草原なう"),
            h.look("見渡す限りに広がる背の低い草原に$phoneを向け",
                "$Sである少年は満足そうにそう呟いては",
                "今自分が魔王退治の旅に出ているのだと実感していた"),
            yusha.talk("森なう"),
            sol.talk("おいおい。", "見るもの何でも画像にしてなうなう言ってんじゃねえよ。",
                "そんなもんこれから腐るほど見られるぞ？"),
            h.deal("立ち止まっては$phoneを向けている$Sに苦言を漏らすのは",
                "赤い髪が特徴的な長身の戦士$solだ"),
            # TODO: 人物紹介
            )

def sc_meetmonsters(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("モンスターに遭遇！",
            # TODO: モンスター見つける、最初は一匹、それを勇者が倒してしまう、続いてゴブリンの群れ、スライム混じり
            )

def sc_smartrunaway(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("賢く逃げろ！",
            # TODO: 逃げてもらちがあかない、GPSで位置把握して、逃亡
            h.deal("しかし彼らは知らなかった。彼らもまた別の誰かによって同じように位置を把握されているということを"),
            )

# episodes
def ep21(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_lookfield(w),
            sc_meetmonsters(w),
            sc_smartrunaway(w),
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
            ep21(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

