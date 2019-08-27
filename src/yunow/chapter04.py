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
            yula.talk("それにしてもまだ夏は遠いのにやけに日差しがきついわね。",
                "もっと多めに日焼け止め塗っておくべきだったわ"),
            h.deal("三人の後について歩く金髪の女性は", "自称大盗賊の$yulaだ。",
                "口を開けるとよく尖った八重歯が目立つ。",
                "先程から空を見上げながらハーフパンツから出た脚やベストの上着から露出した腕を気にしている。",
                "肌は白く", "$Sの見立てではスタイルが良さそうに見える"),
            yusha.talk("痛っ！", "急に何すんだよ$mako"),
            mako.talk("何でもないですぅ！", "ふんだ！"),
            h.deal("$yulaをちらりと見やった$Sの脛を$n_makoが手にした杖で殴って離れる。",
                "$Sに対してあかんべえと舌を出すが", "彼は自分が彼女に対して変なことをしたつもりはなかった"),
            h.deal("そんな四人でところどころに立て看板の設置された街道を歩いていく"),
            h.look("かつては毎日行商人や旅の人間の往来で賑わっていたというが",
                "今や気軽に出歩いている冒険者すら見かけなくなってしまった"),
            yusha.talk("お！", "$n_slimeなう！"),
            h.look("と、$Sが遠くの草陰から伸びて出てきた緑色をした粘性のあるモンスター、$n_slimeを発見して喜んで$phoneを向けた"),
            yusha.talk("おい$sol", "あれ$n_slimeだよな？"),
            sol.talk("そうだけど襲ってこないんだからさっさと素通りするぞ？",
                "相手にしても何もいいことなんかないからな。", "無駄に苦戦して", "最悪命を落とすだけだ"),
            h.deal("自分の腰につけた$shortswordに手を掛けていた$Sだったが",
                "$solの態度は素っ気なく", "立ち止まった彼の肩を掴んで先に歩かせる"),
            yusha.talk("そういやなんか前に殺されたことあるんだった……忘れてたわ。", "ハハハ"),
            sol.talk("あん？", "$yusha", "お前$n_slimeとやったことあんの？",
                "一度でも戦ったことあるんだったら尚更やめとけよ。",
                "あんなのはそれこそ遠くから魔法使いに炎で焼き払ってもらうくらいの方が良いんだよ。",
                "なまじ力自慢の戦士が武器片手に向かった日にゃ", "丸ごと呑み込まれて何日も掛けて体内で溶かされて骨になっちまうからな"),
            h.think("$Sは前も$n_slimeのことで$solに注意されたことを思い出したが",
                "やはり$solの方は何も覚えていないようだ"),
            yula.talk("それよりこの先どうするの？", "$gmapで見てるけど",
                "湖畔脇を抜けるか", "橋を渡って一端西に出るかの二択よ"),
            yusha.talk("ちょっと見せて"),
            h.deal("そう言って$yulaの$phoneを覗き込もうとしたのだが、"),
            yula.talk("嫌よ。", "自分ので見なさいよ"),
            h.deal("彼女に拒否され", "$Sは仕方なく自分の$phoneで$gmapを使って近隣の地図を見てみる"),
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
