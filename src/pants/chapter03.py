# -*- coding: utf-8 -*-
"""Story: chapter 3 ''
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
        # chapter3
        # NOTE: １話あたり2000から3000字程度、増えたら前後編
        "パンツとストッキング",# NOTE: 彼女の妹
        ]

# scenes
## ep23 scenes
def sc_mysister(w: wd.World):
    h = hero = w.hero
    ery, dran, lily = w.ery, w.dran, w.lily
    return w.scene("我が妹",
            h.be(w.stage.left_prison, w.day.outprison),
            h.look("お姉ちゃん", "と$eryのことを呼んだピンク髪のガーターストッキング女は",
                "大量の滝のような髪で隠した豊満なバストを揺するように胸を張りながら",
                "もう一度アッハと笑った"),
            ery.talk("その下品な笑い方は五百年経っても治っておらんようだの"),
            lily.talk("そんな小さな体で$meに品を説こうだなんて",
                "それこそ五百万年早いわよ。",
                "かつて最悪の大賢者と恐れられた頃の面影が全然なくなってしまって",
                "あらあら", "お可哀そうに"),
            h.deal("彼女は口元に手を当てて", "アッハと笑う"),
            h.look("$n_dranはその巨大な体を一ミリと震わさずに沈黙したままだが",
                "この二人の関係を知っているのだろうか"),
            ery.talk("色々と事情があっての",
                "今はこのような成りになってしまったが", "それを言うなら$lilyの方はどうなのだ？",
                "そのパンツの上下にある奇妙なものは？"),
            h.look("$lilyと呼ばれた女性は「これか？」と舐めるようにこちらを見たまま口元を歪ませる"),
            lily.talk("$eryは知らないでしょうけど", "これねパンティとストッキングっていう神具なのよ。",
                "この力のお陰で今$meは賢者になれているの。", "この世界の大賢者になるのも時間の問題よ"),
            h.think("パンティとストッキング", "という言葉の強烈さに頭がくらくらしそうになったが",
                "パンツである$meにはそんな頭部の中身はなかったことに気づいて",
                "今一度彼女の身につけている下着を凝視した"),
            h.look("ぴったりとそのスリムな下半身に張り付いている黒の下着は",
                "赤い刺繍が入れられた大人向けのものに思える。",
                "ただ$meよりも随分と股布の面積が小さく",
                "何よりオプションというよりもそっちが本体と思えるようなガーターベルトとストッキングが一緒に身に付けられている"),
            h.look("臍《へそ》の下あたりから手を置いたような布の付いたベルトが巻かれ",
                "そこから黒のバンドがストッキングまで伸びている。",
                "そのストッキングの方も黒一色ではなくところどころに赤い糸で柄が編まれ",
                "脹脛から足首に掛けては薔薇の花だろうか", "薄っすらと浮かび上がって見える"),
            ery.talk("ほお。",
                "神具とな？", "そのようなものでもなければ$meの足元にも及ばなかったお前の$i_energyが",
                "それで一体如何ほどのものとなったのだ？",
                "少なくとも$meには何も変わらぬようにしか見えぬが？"),
            h.think("$lilyと呼ばれた彼女も$eryと同じようにパンツを知らないとすれば",
                "彼女は一体あれをどこで手に入れたのだろう。", "神具と言っていたが",
                "パンツそのものの概念が存在しない世界には流石にパンティもストッキングもないだろう"),
            lily.talk("五百年も地下深くで引き籠ってた$eryには分からないわよ。",
                "$meがあんたのことでどれだけ苦労して",
                "どれほどの苦渋を味わったかなんて。",
                "$meはね", "ずっとあんたに復讐することだけを願って今日まで生き延びてきたんだよ。",
                "それなのに……いつまでその馬鹿にした態度で$meのことを見てんだよ！"),
            h.look("$lilyは姿勢を低くすると",
                "ストッキングに覆われた自身の太腿を膝頭まで撫でた"),
            h.look("刹那", "彼女の背中から何かの燃料を燃やしたような赤黒い炎が翼のように吹き出す"),
            ery.talk("くっ"),
            h.deal("$eryの体が後ろに弾き飛ばされたのは一瞬の出来事だった"),
            ery.talk("……落ちる！"),
            h.deal("両腕を前にクロスさせて直撃こそ防いだようだが",
                "崖から宙へと飛び出した$eryの体は支えるものを失い", "そのまま落下する。",
                "$meは背中側が見られずにただ遠ざかる崖の切っ先と",
                "そこに顔を出してこちらを見やる$lilyの姿が確認できただけだ"),
            hero.talk("$eryさん？"),
            ery.talk("力が……抜ける"),
            h.deal("小さく呻いた後で彼女は胸の前にやっていた腕をだらりと垂らし",
                    "そのまま頭から木々の間へと突っ込んだ"),
            hero.talk("$eryさん！"),
            h.deal("$meが声を掛けても反応がなく",
                    "体とパンツが鋭く細い葉"),
            # NOTE: 落下して、タロウが彼女の体を何とかして動かそうとする、そこに現れた謎の女性
            )

# episodes
def ep23(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_mysister(w),
            )

# outlines
def story_baseinfo(w: wd.World):
    return [
            ]

def story_outline(w: wd.World):
    return [
            ]

# main
def story(w: wd.World):
    return (w.maintitle(cnf.TITLES["chap03"]),
            ep23(w),
            )

def main(): # pragma: no cover
    from src.pants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

