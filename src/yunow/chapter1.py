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
        "勇者なう！",
        ]

# scenes
def sc_Iamyusha(w: wd.World):
    yusha = w.yusha
    return w.scene("俺は勇者だ",
            yusha.be(w.stage.castle1gate, w.day.callyusha),
            yusha.deal("勇者なう"),
            yusha.deal("黒光りする石版の上で指を滑らせると",
                "自分の呟いた言葉がそのまま表示され",
                "文字の川に流れていった"),
            yusha.talk("おお", "すげえ"),
            yusha.look("思わず声を上げてその石版を見た$Sは",
                "苦笑を浮かべる門番たちの視線に気づいて慌てて歩き出す"),
            yusha.move("堀の上に渡された丸太を組んだ橋は気をつけて歩かないと滑って転びそうだが",
                "$Sは支給された真新しい革のブーツを履いてご機嫌で進んでいく。",
                "仕立ててが良いらしく",
                "このまま走っても大丈夫なくらい靴底が安定している"),
            yusha.talk("いやあ",
                "しかし$meが勇者かあ"),
            yusha.look("一見すると彼はごく普通の十六歳の鼻水垂らした少年に見えるのだが",
                "この度$n_kingより直々に勇者の称号を冠され",
                "魔王退治を依頼された英雄の卵であった"),
            yusha.look("彼が手にしている$phoneと呼ばれる漆黒の石版は",
                "同じ石版を持つ者に対して呟いた文字を流すことができるという特性がある"),
            yusha.talk("お？", "$meって早速話題になってね？"),
            yusha.look("次々と流れてくる”勇者”という文字の洪水に",
                "彼の表情筋は緩み",
                "空の雲行きが怪しくなっていることにも気づかないでいる"),
            )

def sc_strangetown(w: wd.World):
    yusha = w.yusha
    return w.scene("町の様子がおかしいぜ",
            yusha.be(w.stage.hometown),
            yusha.ask("ん？"),
            yusha.look("彼が異変を感じ取ったのは",
                "$st_castle1を出てその城下町の中央広場までやってきた時だった"),
            yusha.talk("あれ？", "さっきまでここって露店いっぱい並んでたはずじゃ"),
            yusha.look("右肩から提げたズタ袋をまさぐり王様から貰った支度金の硬貨の感触を楽しもうとした彼は",
                "立ち止まってぐるりと周囲を見回す"),
            yusha.look("広場の真ん中にある五メートルほどの建国記念碑の周りを花壇が囲み",
                "その外側に円形に並ぶようにしてマーケットが広がっていた。",
                "それが今朝のことだ。",
                "彼は眉を顰めた母親にわざわざ王直々の呼び出しだと叩き起こされ", "不機嫌さを抱えてここを通ったのだが",
                "その時には客も集まり", "賑やかな有様だった"),
            yusha.feel("生温かい風を感じて",
                "彼は自分の背後を振り返る"),
            yusha.look("そこには彼が持つのより一回り小さな$phoneを持つ老人が立っていて",
                "それを彼に向けて小声で何か呟く"),
            yusha.talk("おい"),
            yusha.look("一瞬の眩しさを感じて顔の前に手をやったが",
                "視界が戻るとその老人の姿は既に小さくなってしまっていた"),
            yusha.talk("何なんだよ……"),
            yusha.move("$Sは舌打ちをし", "とりあえずと酒場の方に歩き出す。",
                "流石に魔王退治の旅に一人で出かける訳にもいかない。",
                "傭兵か", "あるいは仲間でも見繕おうという算段だ"),
            )

def sc_theend(w: wd.World):
    yusha, bar = w.yusha, w.barmaster
    return w.scene("そして終わりは突然に",
            yusha.go(w.stage.homefield),
            yusha.talk("何すんだ！"),
            yusha.deal("$Sの胸倉を掴んで店の外へと押し出して追い出した大男は",
                "$st_bar1の店主だった。",
                "その巨躯で睨みを利かせ", "手を叩きながら太い声を唸らせる"),
            bar.talk("あんた勇者だろ？",
                "それを全世界に向けて呟いたことの意味", "理解してんのか？"),
            yusha.look("何をそんなに怒っているんだろう",
                "という表情しか彼は返せない"),
            bar.talk("今がどんなご時世か考えろってんだよ"),
            yusha.look("そう吐き捨てると大男は店内に戻っていき",
                "ドアを閉める前に看板を『ＣＬＯＳＥＤ』に変えた"),
            yusha.talk("ハァ！？",
                "$meが何したってんだよ", "ったくう"),
            yusha.move("意味も分からないまま彼は立ち上がる"),
            yusha.move("とりあえず別の酒場を当たろうと思ったが",
                "どこも開いていない"),
            yusha.talk("何が起こってんだよ……"),
            yusha.feel("そうぼやいて$phoneを取り出した彼の頭に",
                "粘性の強い液体が滴った"),
            yusha.talk("ん？"),
            yusha.look("見上げるとそこには鳥の頭をした人型のモンスターが翼を広げて浮かび",
                "その手にした剣を振り上げている"),
            yusha.talk("あん！？"),
            yusha.look("鼻から紫の煙を吐き出したそいつは",
                "どう考えても今の彼では太刀打ちできそうにない"),
            yusha.talk("何でだよ！"),
            yusha.move("$Sは慌てて頭を下げてから一気に駆け出す"),
            yusha.look("彼の頭のあった場所を鋭い刃が抜けていったが",
                "間一髪で助かったようだ"),
            yusha.look("しかしその$Sの前方には巨大なハンマーを持った豚面の筋肉質や",
                "ガイコツ兵士", "真っ白なお面を被って髑髏の杖を手にした奴らといった",
                "この近隣では見たことのないモンスターが大挙していた"),
            yusha.talk("ど", "どういうことだよ！？"),
            yusha.look("立ち止まった彼の視線の先で",
                "紫色の顔色をした細長い頭の男が笑いながら",
                "その手にした$phoneを見せた"),
            yusha.look("彼も慌てて自身の$phoneを見たが",
                "そこにはもの凄い勢いで、"),
            yusha.look().emphasis("勇者特定なう"),
            yusha.look("彼がいる場所", "その背格好",
                "本名に幼少期の出来事",
                "全然知らない架空の元恋人の話までが文字の渦となって流れていた"),
            yusha.talk("何……だよ", "これは"),
            yusha.look("逃げ場を失った彼は叫びながらそのモンスターの群れへと突っ込んでいく"),
            yusha.think("彼は知らなかったのだ。",
                "魔王たちもまた",
                "$phoneを手に",
                "日夜活動を行っていることを"),
            yusha.look("勇者ボコボコなう"),
            yusha.look("その呟きは",
                    "画像付きで瞬く間に世界に広められたのであった"),
            )

# episodes
def ep1(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
                w.yusha.deal(w.i.beat_maou),
                w.yusha.know(w.i.destroy_peace),
                w.yusha.deal(w.phone),
                w.yusha.go(w.i.trouble),
            sc_Iamyusha(w),
            sc_strangetown(w),
            sc_theend(w),
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
            ep1(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

