# -*- coding: utf-8 -*-
"""Story: The whereabouts
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.arika import config as cnf
THM = cnf.THEMES


# scenes
def sc_awaking(w: wd.World):
    h = mio = w.mio
    mam = w.mam
    return w.scene("目覚め",
            h.be(w.stage.myroom, w.day.first),
            h.deal("目を覚ましたら$Sを感じた"),
            h.think("$Sって", "誰だ？"),
            h.look("部屋だ。",
                "真っ白な壁紙の", "天井も同じ素材の", "菓子箱の内側のような部屋で$Sは目覚めた。",
                "$Sは……$Sのままだ"),
            h.deal("自分自身の感覚を確かめるように右手を握る。",
                "ズレた掛け布団から曝露していたそれは上手く$Sに馴染んで握られてくれたけれど",
                "綿の軽さに埋まったもう片方はうまく力が入れられない。",
                "体を左側に捻ってから引き抜くと動いたシャツで乳首が擦れた"),
            h.deal("体を起こして改めて部屋を見回す。",
                "緑色のカーテンは日差しを遮っているけれどそれは完全ではなく",
                "外の明るさをほんのり伝えている。",
                "サイドに目の大きな女の子のキャラクターのステッカーが貼られた机の上には大学ノートが開かれたままで",
                "シャーペンと三色ボールペンが転がしてあった"),
            h.look("そのノートの手前で", "携帯電話が光っている。", "ワインレッドのフレームをしたそれは小さく震え",
                "息絶えるように止まった"),
            h.deal("$Sは息を詰め", "手を伸ばす。",
                "ひやりとした手応えは特別新しいものではなかったが",
                "指を触れて表示された画面には$Sの知らない名前があった"),
            mio.talk("$ln_haru、$fn_haru？"),
            h.think("その発音が合っているかも怪しいけれど", "字面からはそうとしか読めない。",
                "ただ口に出してみても記憶にはなかった"),
            h.deal("指を動かしてそのメッセージを表示させる"),
            h.look("――会社帰りに寄るから映画でも見に行こう"),
            h.think("ただそれだけの文面なのに", "$Sは頭の中に手を突っ込まれたみたいに酷く混乱した"),
            h.look("改めて", "$Sは誰だ。", "そしてこの$n_haruは誰だ。", "どんな関係だ"),
            h.look("黄色に赤い花柄のハーフパンツの下", "露出した肌は張りがあってつるりとしていたけれど膝頭を超えた先",
                "脛の一部で産毛が触れた。",
                "右足の小指の爪だけが赤く色づいていて", "引っ掻くとそれが剥げる"),
            h.deal("$Sはベッドから起き出し", "その足をカーペットに着けた。",
                "その足裏の感覚に違和感はない"),
            h.hear("と、足音が上がってきた"),
            mam.talk("$mio", "まだ起きてないの？"),
            h.hear("女性の声だ。", "それもおそらく$meの母親か", "それに近い保護者のものだろう"),
            h.look("壁のハンガーには紺のスカートと赤いタイが引っ掛けてある。",
                "アッシュブラウンのスクールバッグが床に倒れていて", "そこから教科書がはみ出している"),
            mam.talk("ねえ$mio？"),
            h.hear("ドアが二度、三度とノックされる"),
            # NOTE: 部屋、自分は誰か、二度目の感覚、呼びに来る母は知らない人
            )

def sc_myfamily(w: wd.World):
    h = mio = w.mio
    return w.scene("わたしの家族",
            h.be(w.stage.dyning),
            # NOTE: 家族の中の自分
            # NOTE: 朝食、知らない家族、知らない自分、高校生？　二学期
            )

def sc_myschool(w: wd.World):
    h = mio = w.mio
    return w.scene("わたしの学校",
            h.be(w.stage.school),
            # NOTE: 学校の自分
            # NOTE: 登校、知らない道、学校、教室も知らず、友達に声かけられ
            )

def sc_myfriend(w: wd.World):
    h = mio = w.mio
    return w.scene("わたしのともだち",
            h.be(w.stage.classroom),
            # NOTE: 友達の前の自分
            # NOTE: 友人、自分をよく知る、いつもと違う、雰囲気変わったって
            )

def sc_herboyfriend(w: wd.World):
    h = mio = w.mio
    return w.scene("わたしの彼氏",
            # NOTE: 彼の前の自分
            # NOTE: 彼氏がやってくる、放課後、初めて自分の本音を告げる
            )

def sc_sleeping(w: wd.World):
    return w.scene("眠りにつくか",
            # NOTE: 帰ってきて、自室、眠れず、SNSを見つける、知らない自分
            )

def sc_awake2day(w: wd.World):
    return w.scene("目覚めたら知らないわたし",
            # NOTE: 目覚めたらまた知らない部屋、私を見つける作業、SNSには同じ私
            )

def sc_unknownfamily(w: wd.World):
    return w.scene("知らない家族",
            # NOTE: 前の家族と違うギャップ、また知らない私、妙に気遣う家族、違う私
            )

def sc_newschool(w: wd.World):
    return w.scene("違う学校",
            # NOTE: 違う学校に違うクラス、違う制服、女子校、不登校だった私
            )

def sc_samehim(w: wd.World):
    return w.scene("同じ彼",
            # NOTE: 彼の前だけ同じ私、それが安寧、好きということ、でも彼はそろそろ別れたそう
            )

def sc_alonenight(w: wd.World):
    return w.scene("一人の夜",
            # NOTE: 好きな曲をききながら考え込む、わたしって何、わたしの在り処を知りたい
            )

def sc_everydayme(w: wd.World):
    return w.scene("毎日違うわたし",
            # NOTE: 目覚める度にわたしを探す、その日々の中、彼だけがわたしを安定させてくれていた
            )

def sc_brokenme(w: wd.World):
    return w.scene("破壊されるわたし",
            # NOTE: わたしは壊れた、彼がいなくなった
            )

def sc_lostme(w: wd.World):
    return w.scene("わたしはどこにもいない",
            # NOTE: 自分を見失い、意識も心も漂う
            )

def sc_oldfriend(w: wd.World):
    return w.scene("SNSの幼馴染",
            # NOTE: SNSで幼馴染が声をかけてくれる、小さな頃のわたし、
            )

def sc_meetfriend(w: wd.World):
    return w.scene("幼馴染との再会",
            # NOTE: 再会し、わたしを取り戻す、わたしの在り処の鍵を知る
            )

def sc_findme(w: wd.World):
    return w.scene("わたしを見つけた",
            # NOTE: 色々なところに自分の面影を見つける
            )

def sc_me(w: wd.World):
    return w.scene("わたし",
            # NOTE: 色々なわたしがいる、でもどれもわたしだ
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("目覚めたら知らないわたし"),
            sc_awaking(w),
            )

def ep_unknownme(w: wd.World):
    return (w.chaptertitle("わたしの知らないわたし"),
            sc_myfamily(w),
            sc_myschool(w),
            sc_myfriend(w),
            sc_herboyfriend(w),
            )

def ep_notme(w: wd.World):
    return (w.chaptertitle("わたしで無いわたし"),
            sc_sleeping(w),
            sc_awake2day(w),
            sc_newschool(w),
            sc_samehim(w),
            sc_alonenight(w),
            )

def ep_denyme(w: wd.World):
    return (w.chaptertitle("わたしを否定する"),
            sc_everydayme(w),
            sc_brokenme(w),
            sc_lostme(w),
            sc_oldfriend(w),
            )

def ep_itsme(w: wd.World):
    return (w.chaptertitle("それがわたし"),
            sc_meetfriend(w),
            sc_findme(w),
            sc_me(w),
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ]

def story_outline(w: wd.World):
    return [
            ]

# main
def world():
    w = wd.World("The whereabouts project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("わたしの在り処"),
            ep_intro(w),
            ep_unknownme(w),
            ep_notme(w),
            ep_denyme(w),
            ep_itsme(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

