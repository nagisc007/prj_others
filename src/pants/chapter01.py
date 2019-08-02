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
        "プロローグ",
        ]

# scenes
def sc_hardday(w: wd.World):
    h = hero = w.hero
    robber = w.robber
    return w.scene("ハードな一日",
            h.be(w.stage.train, w.day.deadman),
            h.think("最後に君にパンツを履かせてから", "もう三年になるのか"),
            h.look("と、スマートフォンに着信したメールの日付を見て唐突に思い出す"),
            h.think("八月二日がパンツの日だと知ったのは",
                "今朝のテレビ番組のおちゃらけたアナウンサー同士のやり取りの中でのことだ"),
            w.sufferer1.talk("……やめて……ださ……"),
            h.look("いつもと変わらぬ速度で満員の電車はカーブに差し掛かり",
                "強烈なＧで背中側に引っ張られる。",
                "それを感じながらも$meは上司から送られてきた『辞めないで下さい』という懇願の内容に一通り目を通していた"),
            h.think("果たしてブラックだったろうか。",
                "仕事内容に特に不満はなかったし",
                "入社して六年", "それなりに仕事はしてきた。",
                "ただこのまま上から流れてきた指示通りにプログラムという小さな部品を作り続けていて",
                "果たして自分の人生には何が残るのだろうか",
                "そんな疑問を抱いてしまったことからは目を逸らせない"),
            w.sufferer1.talk("……お願い……やめて……"),
            hero.look().d("ドア付近に立つ鞄を肩から下げた髪の短い女性だった。",
                "自分よりも少し若いくらいだろう。",
                "ノースリーブに短いスカートから出た脚が$meの立ち位置からも見えたが",
                "その彼女がもぞもぞと体を動かして移動しようとしている"),
            hero.look("けれど周囲に立つ他の客に阻まれ",
                "そこから逃げ出せないでいるようだ"),
            hero.look().d("その彼女の右手側",
                "一人の別の女性を挟んだ先に",
                "暗灰色の帽子をしたマスク姿の男性が",
                "競馬新聞を持っていない方の左手をすっと",
                "彼女のスカートに差し入れたのが見えた"),
            hero.think().d("痴漢",
                "という言葉が真っ先に浮かんで",
                "$meはそっと体を捩りながらそっち足を進める"),
            hero.think().emphasis("$i_herword001"),
            hero.think("そう言っていつも憤っていた元彼女は",
                "満員電車のない土地で元気にしているだろうか"),
            hero.look().d("男の手はその女性の臀部をまさぐっているのか",
                "スカートがややまくれ上がり気味になって小さく動いている"),
            hero.look().d("女性の顔は見えない。",
                "じっと我慢しているのかも知れないと考えると",
                "さっさとその苦悶から解放してあげたかった"),
            hero.think().d("もうすぐでその男の手を掴める"),
            hero.look().d("そう思った刹那", "男の手が彼女のスカートから引き抜かれた"),
            hero.look().d("$meはその手が掴んでいたものを目にして思わず心の中で唸ってしまう"),
            hero.look("彼の手には四つの紐がだらりと垂れ下がる",
                "女性ものの布地面積の少ない白の下着が", "握られていたのだ。",
                "彼はそれをスマートフォンでも仕舞うかのような動作で",
                "自分のジャケットの内側へと差し入れる"),
            hero.deal().d("だがそれが完全に彼のものとなる前に",
                "$meの右手がそこから下着ごと引きずり出した"),
            hero.talk().t("この男",
                "痴漢だ"),
            hero.look().d("振り返ったマスクの男は",
                "やたらと血走った目を$meに向けたが",
                "観念したのか",
                "藻掻くことも否定することもせず",
                "ただ大人しくその下着を女性に差し出し",
                "こう言った"),
            robber.talk("あんたには似合わないパンツだ。",
                    "だから$meが供養してやろうとしたんだよ"),
            hero.hear().d("喉に下着を詰め込んだような",
                    "潰れた声だった"),
            hero.deal("$meの右拳が思い切りそいつの頬に叩きつけられると",
                    "車内から控えめに拍手が起こる"),
            hero.look().d("けれど下着を返してもらった彼女は俯いたままで",
                    "電車が停車してドアが開くと一目散にそこから逃げ出して行ってしまった"),
            )

def sc_gotoheaven(w: wd.World):
    h = hero = w.hero
    robber = w.robber
    return w.scene("そして天国へ",
            hero.move(w.stage.sta_home).d("目的の駅ではなかったが",
                "一旦犯罪者を駅員に引き渡そうと思い", "ホームに降り立った"),
            hero.talk().t("おい"),
            hero.deal().d("しかし大人しくしていた痴漢男は$meの右手からするりと身を捻って抜け出すと",
                "そのまま車両の進行方向と反対側へと駆け出した"),
            hero.talk().t("待て！",
                "すみません！",
                "そいつ痴漢なんです！"),
            hero.think().d("僅かな油断だった"),
            hero.move().d("とにかく$meも後追いで駆け出したが",
                "人の多いホームではなかなか全速力で走ることもままならない"),
            hero.look().d("だがその痴漢男の方はこういった状況に慣れているのか",
                "上手く人を躱しながら駆け抜けていくと",
                "車両が切れたところで線路へと飛び降りる。",
                "そのまま駅を出ていこうという気だろう"),
            hero.think().d("逃がすかよ"),
            hero.move().d("$meも後追いで飛び降りると",
                "心臓がどんどん熱くなるのも構わずに思い切り足を蹴る"),
            hero.think().d("もう少し。",
                "あと三メートル……"),
            hero.think().d("届かないか"),
            hero.look().d("踏切の遮断器が上がり",
                "男は道路側へと曲がる"),
            hero.think().d("逃げられる"),
            hero.think().d("そう思った時だった"),
            hero.look().d("$meの目の前を横っ飛びで痴漢男の体が吹き飛んでいく"),
            hero.look().d("続いてトラックの厳ついフロントが頭を覗かせたが",
                "そいつは真っ直ぐに進むことを拒否し",
                "運悪く",
                "$meの方へと向きを変えて",
                "正面からそのまま$meの意識を刈り取っていった"),
            hero.do("dead").d("そう。",
                "$meはちっぽけな正義感を振り回した挙句",
                "この世界を去ったのだ"),
            )

# episodes
def ep1(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_hardday(w),
            sc_gotoheaven(w),
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
    return (w.maintitle(cnf.TITLES["chap01"]),
            ep1(w),
            )

def main(): # pragma: no cover
    from src.pants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

