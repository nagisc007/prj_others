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
        "モンスターなう",# NOTE: 冒険に出てモンスター遭遇、GPSで位置把握して逃げる
        "逃走中なう",# NITE: アプリで逃走
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
                "赤い髪が特徴的な長身の戦士$solだ。",
                "旅慣れた彼は初めての冒険に出てはしゃぐ$Sに対して何度も溜息を零している"),
            mako.talk("少しくらい良いじゃないですか。", "$meだって$taroの立場だったらいっぱいなうしたいですよ？"),
            w.combine(
            h.deal("そう言って微笑ましく$phoneを操作する$Sを自分の$phoneで画像にして"),
            mako.talk("楽しそうな$yusha"),
            h.deal("等と実況しているのは",
                "ピンクのおかっぱ頭をした小柄な魔法使いの$n_makoだ。",
                "彼女も$solほどではないがそれなりに旅慣れているようで",
                "おまけに$phoneの使い方にも習熟していて", "何か困り事があれば$phoneを使って解決していた"),
            ),
            yusha.talk("お前ら", "これを見て何も思わないのか？", "感じないのか？"),
            h.deal("$Sは自分を遠巻きに見る二人に対して大きく手を広げて抗議する"),
            yusha.talk("モンスターを遠ざける為の高い壁もなく",
                "どこまでも草原が広がり",
                "見上げれば青い空"),
            h.look("だがどう見ても九割ほどが雲で覆われている"),
            yusha.talk("遠くにはかつて多くの英雄たちが修行の場として使ったという$st_homemountが見えて",
                "こうして気持ちよく空気を吸いながら街道を歩いていく。",
                "この冒険している感をもっと大事にしようと", "そう思わないのか？",
                "……あ", "なんか知らない鳥なう"),
            h.deal("彼らの頭上を飛んでいったよく分からない翼のあるそれに$phoneを向け",
                "$Sは言った"),
            sol.talk("別に"),
            mako.talk("そんなことより先を急ぎましょうよ。",
                "夕方までに$st_town2に入りたいです。", "流石に初日から野宿とか", "しないですよね？"),
            yusha.talk("わかったよ。",
                "さっさと歩きますよ……ったく。",
                "冒険者の旅情ってものがないのかね"),
            h.move("一人ぶつくさと言いながらも",
                "三人は草で周囲を覆われる街道を北上する"),
            h.look("モンスターが現れるようになり",
                "護衛を雇えないような人の行き来がほとんどなくなり",
                "立て看板や橋の補修もままならない状況のようだった"),
            h.move("そんな状況だからもっとモンスターが現れるかと思っていたのだが",
                "時間帯なのか", "それとも精霊様の加護の力でも働いているのか",
                "太陽が高くなるまで割と平穏無事な時間が続いた"),
            )

def sc_meetmonsters(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    gob = w.goblin
    return w.scene("モンスターに遭遇！",
            yusha.talk("森の中なうっと"),
            h.deal("そろそろ一休みしようか", "といった心地で木陰に入った$Sたちだったが",
                "木立の間を小鳥たちが慌てて逃げていく"),
            sol.talk("なんか……いるな"),
            h.feel("その不穏に最初に気づいたのは", "やはり旅慣れた$solだった"),
            mako.talk("いますね"),
            h.look("続いて$n_makoも日よけにと身につけていた鍔広のトンガリ帽子を被り直して",
                "その何かに備える"),
            yusha.talk("どこだよ？"),
            h.deal("その気配が分からないのはどうやら$Sだけのようだが",
                "$shortswordを抜くことすらしていない彼の背後だった。",
                "そいつは突然茂みを破って現れた"),
            mako.talk("$taro！"),
            h.deal("$n_makoは慌てて掌を向けると詠唱もなく小さな炎の弾を放つ"),
            h.hear("ギャアァァ", "という耳障りな声を上げて転がったのは醜い凹凸を顔に持つ$n_goblinと呼ばれる子鬼だ。",
                "丈の短い丸太の棍棒を手にして", "仰向けになって暴れている。",
                "見れば$n_makoの魔法の火が筋肉質な胸元で燃え続けていた"),
            yusha.talk("も、もも", "モンスターなう！"),
            sol.talk("何バカ言ってんだ！",
                "お嬢も何したか分かってんのか？"),
            h.deal("腰を抜かして倒れ込んだ$Sを左腕一本で引き起こしながら",
                "右手に剣を握った$solがどういう訳か慌てた様子で言った"),
            mako.talk("仕方ないじゃないですか。",
                "あのままだとまた$taro殺されるところだったし"),
            yusha.talk("あいつやっつけないでいいの？"),
            h.look("$n_goblinはまだジタバタしていたが", "徐々にその動きも緩慢になっていく。",
                "その姿に$Sはやっと自分の武器を引き抜くと",
                "とりあえず構えて$n_goblinに向き直った"),
            yusha.talk("ねえ？", "こいつ$meがやっちゃってもいい？",
                "まだモンスター退治したことないんだよなあ……"),
            h.deal("呑気なことを言っている$Sを挟むようにして",
                "$solと$n_makoは目線で「どうしよう」というやり取りを続けている"),
            yusha.talk("ん？", "何何？",
                "何か問題あるの？"),
            sol.talk("問題だらけだ"),
            yusha.talk("え？"),
            h.deal("$solは苛立った様子で吐き捨てるように言うと",
                "何も事情を知らない$Sに変わってその$n_goblinの首元に剣を突き刺し", "絶命してやった"),
            mako.talk("$taro……実はこの$n_goblinというのは基本的に集団で行動するモンスターなのです。",
                "それが一匹だけで生息しているということはまずない。",
                "わかりますか？"),
            yusha.talk("うーん", "つまり……たまたま一匹だから良かったねってこと？"),
            h.deal("その返答に$solは自分の顔面を押さえつけた。",
                "文句の一つも言いたそうだが",
                "解説の役割を彼女に譲る"),
            mako.talk("そうじゃなくてですね",
                "おそらくこの$n_goblinは斥候なんです。",
                "たぶん$meたちがこの場を離れようとする時には周囲を十匹から多い時だと百匹が取り囲んでいます"),
            yusha.talk("え……"),
            h.deal("$Sの声は裏返っていた"),
            h.hear("続いてガサゴソと茂みが動くのが分かった。",
                    "それも一箇所じゃない。",
                    "あっちもこっちも", "目に入るところ全てだ"),
            yusha.talk("えっと", "これって……"),
            h.deal("彼はやっと自分たちが置かれた状況というものを理解し",
                    "お漏らししそうになったが何とかそれを堪えて", "考えた。",
                    "うん。", "もう一度死のうと"),
            sol.talk("一匹や二匹ならな", "$me一人でどうにかしてやらあ。",
                    "だが……これだけの数となると", "$meでも初体験だわ"),
            mako.talk("参りましたね……どうします", "$taro"),
            h.deal("三人はそれぞれの思惑を持ちながらも背中合わせになって",
                    "もぞもぞと動く茂みの向こう側のいくつあるか分からない気配に対峙した"),
            )

## ep22 scenes
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
            )

def ep22(w: wd.World):
    return (w.chaptertitle(TITLE[1]),
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
            ep22(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

