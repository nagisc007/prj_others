# -*- coding: utf-8 -*-
"""Story: chapter 1 ''
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.pants import config as cnf
THM = cnf.THEMES

# titles
TITLE = [
        # chapter2
        # NOTE: １話あたり2000から3000字程度、増えたら前後編
        "監獄パンツ",# NOTE: 彼女の名前と監獄迷宮説明
        "",# NOTE: 初めての戦闘、番犬ども
        "",# NOTE: 迷宮崩壊
        "",# NOTE: 監獄迷宮出たら妹が待っていた
        ]

# scenes
## ep9 scenes
def sc_intheprison(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("監獄の中で輝いて",
            h.be(w.stage.prison1, w.day.outprison),
            h.hear("ぺたりぺたりと", "小さな足が歩いていく音を$meは聞いていた……パンツで"),
            hero.talk("なあ", "ここって一応迷宮になってるんだろ？",
                "あんたは迷わずに出られる自信でもあるのか？"),
            h.think("先程から全く悩むことなく分岐路を選ぶ様から勝手にそう判断していたのだが",
                "どうも"),
            # NOTE: i_mean_taroは勤勉な者、名誉な名前
            # NOTE: 前方に敵影（番犬ども）
            h.look("その吠え声は徐々に近づいてくる。突き当りの通路の先にいる。彼女の掌の光で照らし出されたそこには$meが知る犬とは似ても似つかない、三つ首の化物が二匹、姿を見せた"),
            )

# episodes
def ep9(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_intheprison(w),
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
    return (w.maintitle(cnf.TITLES["chap02"]),
            ep9(w),
            )

def main(): # pragma: no cover
    from src.pants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

