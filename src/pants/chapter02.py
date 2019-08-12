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
        "パンツを喰らう犬",# NOTE: 初めての戦闘、番犬ども
        "",# NOTE: 門番のミノタウロスとその使役者
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
                "どうも迷っているんじゃないだろうか", "という疑惑が生まれた"),
            hero.talk("ここ", "さっきも曲がった気がするんだが",
                "同じところを歩いているってことはないよな？"),
            ery.talk("一応説明したとは思うが", "この$st_prisonを造ったのはこの$meなのだぞ？",
                "創造主が出られない迷宮を造るなど", "そんなことがあると思うか", "なあ$hero？"),
            h.deal("フハハ", "と笑い声を響かせつつもどう考えてもさっきも通ったと思われる通路をまた曲がる"),
            h.look("天井の低い通路は固い一枚岩を彫り抜いて造ったというのだが",
                "光源もなく", "空気が循環しているかも怪しい。",
                "それでも指先に灯した小さな光だけで歩いていく彼女は特別苦しそうでもないし",
                "パンツである$meは当然息をする必要がないのでそういった苦痛は微塵もない"),
            hero.talk("いやどう考えても同じところをさっきからぐるぐるぐるぐる回っていると思うんだが",
                "ひょっとしてあんた", "方向音痴ってことはないだろうな？"),
            ery.talk("$meが？", "方向に疎いとそう申すのか？"),
            h.think("道に迷う人間は何故か自分は迷うはずがないという自信に満ちている。",
                "$meの元彼女もそうで",
                "デートの待ち合わせにいつも遅れてくるのは「道路が勝手に動いくから」という",
                "彼女の方向音痴加減がその大きな要因だった"),
            ery.talk("万に一つも迷うなどといったことはなかろうが",
                "仮にいつまでもここを出られないというのであれば",
                "最悪全てを破壊して脱出してしまえば良い"),
            h.think("その言葉を聞いて$meには",
                "天井が崩落して閉じ込められて泣きじゃくる彼女の姿しか思い浮かべられなかった"),
            ery.talk("何か不満があるようだな", "$heroよ"),
            h.think("そんな$meの不安を察してか不機嫌さの声で尋ねたが",
                "$meが問い返したのは別の疑問だった"),
            hero.talk("ところでその太郎というのを変える気はないのか？",
                "なんと言うか安直で", "小馬鹿にされているような気分になるんだ"),
            ery.talk("何を言っておるか$hero。",
                "$heroというのは”$i_mean_taro”という意味があってだな",
                "そもそも名を与えられるということそのものが大変に名誉なことなのだぞ？"),
            h.think("どうやら名前に対しての認識も$meの生きてきた世界とは異なるらしい。",
                "逆らったところで所詮はパンツ。", "何もできないので仕方なく太郎という呼び名を受け入れることにした"),
            ery.talk("分かれば良いのだ", "パンツ$heroよ"),
            hero.talk("いやせめてパンツは取ってくれよ"),
            ery.talk("何故だ？", "お主はパンツであり", "実に勤勉な$heroでもある。",
                "故にパンツ$heroというのはお主そのものの名ではないか？"),
            hero.talk("何でもだ。", "パンツよりは太郎と呼ばれた方が$meの世界ではまだマシなんだよ"),
            h.deal("お気に入りなのにな", "とぼやいた彼女は",
                "やはり何度も見たことがある分岐路で同じ方向に曲がる"),
            hero.talk("いやだから！", "何故考えることもなく右に曲がれるんだ？", "ここはさっき通っただろう？"),
            ery.talk("$heroはパンツの癖によく道順を覚えておるな……それならいっそのこと",
                "お主に道案内を頼みたい。", "どうだ$hero？"),
            h.deal("彼女はわざわざ自分の股間を覗き込むように体を丸めて$meと目を合わせると",
                "$meが「分かった」というまでじっと見つめていた"),
            h.deal("だから仕方なく承諾したものの",
                    "主導権が方向音痴から非方向音痴に代わったところで",
                    "地図を渡されている訳でもないし",
                    "もともと$st_prisonと呼ぶだけあってそれなりに入り組んだ通路になっているだろう。",
                    "対策なしに出口まで辿り着けるとは思えない"),
            hero.talk("ちょっと訊いてみるんだが",
                    "あんた", "名前はあるのか？", "それとも元大賢者とでも呼べばいいか？"),
            ery.talk("名など知ってどうする？"),
            hero.talk("ということはあるんだな？", "いや$meの暮らしていた世界では相手にあんたやお前と言うのはどちらかと言えば失礼に当たるんだ。",
                    "もし可能なら名前で呼んだ方が$meの気持ちがすっきりとする。", "$fn_heroの頼みは聞けないか？"),
            h.deal("仕事上の付き合いなら簡単な自己紹介から始めるが",
                    "いきなりパンツと人間という奇妙な関係で始まったから",
                    "すっかり調子を狂わされてしまっていた。",
                    "何事も規則と手順を大事にすることで$meという人間は安定を得ていたのだ。",
                    "それを忘れてしまっていた"),
            ery.talk("そうだな……"),
            h.deal("彼女は歩みを止めて思案する。",
                    "パンツである$meからはその表情は見えないが",
                    "うむ", "という考えをまとめたらしき頷きだけは聞くことができた"),
            ery.talk("では$eryと呼ぶが良い"),
            hero.talk("$ery。", "それがあんたの名か？"),
            ery.talk("本当の名前は教える訳にはいかんが", "字《あざな》であれば良いだろう"),
            h.deal("$ery……と", "自分の中で復唱する。",
                    "彼女の存在とその名前を思考の中でブレンドし",
                    "同じものだと認識する。",
                    "しかし今パンツである$meの思考の座は一体どこにあるのだろう。",
                    "腰にピッタリフィットする為のゴム紐だろうか。",
                    "それとももっと超常的な", "$meの思考回路だけがどこかの施設に安置されていて",
                    "それと絶えず通信をすることで思考を成立させているような絡繰りでも使われているのだろうか"),
            hero.talk("じゃあ$ery。", "宜しく頼む"),
            ery.talk("改めて呼ばれると", "お主がパンツとはいえ", "何だか妙なものだな。",
                    "それで$hero。", "$meに何を頼みたい？"),
            hero.talk("$eryさん。",
                    "あんたは$meを履いていることで力が抑えられているというが",
                    "それでも今やっているように小さな光を作ったりはできる。", "そうだな？"),
            h.deal("ああ", "という頷きを聞いて$meは続ける"),
            hero.talk("では一度通った場所に何か目印を付けておくことは可能か？",
                    "例えばパン屑を落としていくみたいに"),
            ery.talk("パン……それはパンツとは違うのか？"),
            h.think("彼女の疑問の声に",
                    "$meの頭の中では沢山のホテルの焼き立てトーストやフレンチトースト",
                    "フランスパンにデニッシュ", "といった数々の歯ざわりと旨味が過ぎ去っていく"),
            ery.talk("ん？", "どうした？"),
            hero.talk("いや、何でもない。",
                    "とにかく後で同じ場所を通過した時にそれと分かる印を残しておけるだろうか？"),
            ery.talk("これで良いのか？"),
            h.deal("彼女はそう言うなり",
                    "指先から小さな光の玉を壁へと投げつけた。",
                    "それはホタルのようにそこに張り付いて仄かな明滅を繰り返している"),
            hero.talk("ああ", "十分だ。",
                    "だがこれはずっとこのまま光っててくれるのか？"),
            h.think("もし数分程度で消失してしまうなら", "目印としてはやや心許ない"),
            ery.talk("今の$i_energyの影響範囲がちと分からぬが",
                    "それでも数キロ半径はあるだろう。",
                    "$meが消そうとせぬ限りは", "そうそう消えることにはならない"),
            hero.talk("分かった。",
                    "それじゃあこいつを使ってこの$st_prisonを脱出するとしよう。",
                    "最悪虱潰しになるが", "それでも同じ場所をぐるぐると", "なんてことにはならないはずだ"),
            h.deal("では頼むぞ。", "と頷いて彼女は歩き出す"),
            h.think("その足取りは先程までよりずっと自信に満ちていたが",
                    "よく考えてみるとここが普通の", "何の細工もない迷路状の洞窟であるという保証はどこにもない。",
                    "それについて彼女に問いただそうとしたところで",
                    "通路に反響して別の生き物の声が聞こえた"),
            hero.talk("何だ……"),
            h.hear("それは獣の吠える声だった"),
            h.look("その吠え声は徐々に近づいてくる。",
                    "すぐに突き当りの通路の先までやってきて",
                    "彼女の掌の光で照らし出された先に大きく引き伸ばされた",
                    "どう見ても普通の犬とは思えない影を$meに見せた"),
            )

## ep10 scenes
def sc_maddog(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("魔獣がペット",
            h.be(w.stage.prison1, w.day.outprison),
            h.hear("大型犬のような吠え声の主は",
                "$eryの手から出た光で照らされた通路の突き当りに巨大な影を作っていた"),
            hero.talk("一つ訊いておくのを忘れたんだが",
                "この迷宮にはおかしな仕掛けとか番をする怪物とか",
                "そういったものはあるのか？"),
            ery.talk("基本的には$i_energyが高い者を封じ込めておく為の檻でしかないから",
                "最深部のあの特殊な牢屋以外は長く複雑な迷宮になっているだけだ。",
                "ただ", "何もいないというのも心許ないからな。",
                "一応$meのペットを数匹", "野放しにはしておいたぞ"),
            h.look("ペットおいう言葉があることは安心しつつも",
                "どうやらそれは$meが住んでいたアパートで飼ったりできる類の可愛らしい生き物ではないことは確かだった"),
            h.look("巨大になった影はその輪郭がはっきりとし",
                "やがて$meたちの前にそのガリガリに痩せて細くなった四本足で姿を現した"),
            ery.talk("おお。", "やはり$n_kerberos1と$n_kerberos2か。",
                "よくぞ五百年も無事に生き延びておったな"),
            h.look("$n_kerberos1と$n_kerberos2と呼ばれたその二匹は",
                "首が三つとそれぞれに赤い目玉が六つずつという",
                "$meの常識からすれば恐ろしい容貌の犬に似た何かだった"),
            h.deal("口角がぐっと引き上げられ", "鋭い牙が唾液を伴って光を反射する。",
                "もう一匹の方は紫色の長いベロを出して", "ゼェゼェと荒い息だ。",
                "時折唸るようにして首を振り", "$meたちを牽制していた"),
            ery.talk("なに、それほど恐怖を感じずとも良い。",
                "これは$meが番犬として家で飼っていた愛犬だ。",
                "人懐こいし", "飼い主の命令は絶対に守る。",
                "頭も良く", "何より不用意に噛み付くといったことは――"),
            h.deal("彼女の言葉が終わる前に二匹は襲いかかってきた"),
            hero.talk("どう考えてもアレは大丈夫じゃないだろ！？"),
            h.look("そうか？", "と疑問の声を漏らしながら彼女が向かってくる二匹に光を向けると",
                "その形相は明らかに獲物に襲いかかるそれにしか思えない。",
                "それとも$n_kerberos1と$n_kerberos2は普段からあんな顔で飼い主に向かってくるのだろうか"),
            hero.talk("いや", "それはないな"),
            h.deal("逃げる様子のない$eryに唸り声を撒き散らして駆け寄ってくると",
                "その内の一匹はそのまま真っ直ぐ$me目掛けて跳躍した。",
                "鋭い牙から唾液が滴り",
                "$meを呑み込もうとでもいうようなほどしっかりと開いた口が",
                "そのまま$meというパンツの布地に食い込む"),
            hero.talk("痛……くはないけど", "全然大丈夫じゃないだろ？", "ちょっと$eryさん？"),
            ery.talk("何故だ！"),
            h.deal("驚きの声で彼女が左腕を振り払うと",
                "上半身目掛けて飛び上がったもう一匹がキャンと高い声を上げて壁にぶつかった"),
            ery.talk("貴様らの主のことを忘れてしまったのか！", "この馬鹿犬どもが！"),
            h.deal("続いて$meに牙を突き立てているもう一匹の首根っこを掴んで無理やり引き剥がすと",
                "そのまま地面に激しく叩きつける。",
                "汚れた唾液塗れの嗚咽を漏らして転がっていったが",
                "その程度では息絶えることなく", "低く唸り声を漏らしながら立ち上がると六つある赤い瞳でこっちを睨みつけた"),
            hero.talk("流石にちょっと様子がおかしいと思うんだ。",
                "そもそも五百年も放っておいてこいつらよく生きてたな？"),
            h.think("自分の世界の常識が通用しないことは多少理解できているつもりだったが",
                "それでも食べもの飲み水といった栄養源がなさそうなこの迷宮内で",
                "五百年という長きに渡って生き永らえているというのは通常の生物では有り得ないだろう。",
                "まあ見た目が明らかに常識の範囲内にないので",
                "飲まず食わずでも五百年くらいこいつらは生きられるのかも知れないが"),
            ery.talk("何を言うておるか。",
                    "アレは$meが生命を与えた生き物だぞ。",
                    "頭を全て破壊でもされん限りは永遠に生き続ける"),
            hero.talk("それじゃあ", "ちょっとばかり可哀想だろうが思い切って頭をぶっ壊してはくれないだろうか？"),
            h.deal("パンツの右側", "腿の上あたりに二本ばかり穴が開けられていた。",
                    "痛みはない。", "それは彼女も同様らしく", "特に苦悶の声も漏らさないし",
                    "内側から血も滲み出てこない。",
                    "$n_kerberos1なのか$n_kerberos2なのか知らないが",
                    "そいつの噛み方が弱かったという訳ではないだろう。",
                    "何かしら特殊なコーティングが彼女の肉体には成されているのかも知れない"),
            h.think("それでも今やパンツの$meとしては自分の肉体に穴が開いているというのはあまり気持ちの良いものではない"),
            hero.talk("飼い主としては万感の思いがあるだろうが", "今はこのピンチを脱出する方が大事だと思うんだ"),
            ery.talk("何を分からぬことを申しておるのか。",
                    "$meは飼い主であり", "やつらはペットに過ぎん。",
                    "飼い主に手を出すような駄犬は首を切るしかないだろう？"),
            h.deal("彼女は特に戸惑う様子もなくそう言ってのけると",
                    "小さな光の円盤を二つ放ち",
                    "一匹の首を三つとも切断して頭を落としてしまった"),
            ery.talk("この程度の力は幼女の体でも十分だな"),
            h.deal("そう言うと", "唸り声を上げてはいるものの",
                    "警戒したのかこっちには向かってこないもう一匹に目掛けて",
                    "同じような光の円盤を", "今度は三つ放った"),
            h.look("犬的な怪物の片割れは悲鳴にも似た声を上げながら背を向けて逃げ出したが",
                    "容赦なく振り返った一本の首を落とし",
                    "続いて牙を向いたもう一つの頭を落とし",
                    "最後にはどうしていいか分からなくなってじっと$meを見た残りの一本を落とした。",
                    "すっと斜めに入った光の線が消えるように首がズレていき",
                    "その頭は音を立てて転がった"),
            ery.talk("ふぅ……五百年ぶりの再会だったが", "何とも味気ないものだな"),
            h.look("彼女はつまらなさそうに呟くと",
                    "骸となった元ペットの傍を通り抜けていく"),
            h.think("そこに何の感情もなかったのだろうか。",
                    "$meは少しだけこの$eryという存在が分からなくなった。",
                    "ひょっとすると彼女には$meが知る人間らしい思考というものは無いのかも知れない。",
                    "だとすると", "$meは穴の開いたパンツのまま",
                    "いつかは要らなくなって捨てられてしまう。",
                    "そんな可能性を常に考えながらこれから彼女と行動を共にすべきなのかも知れなかった"),
            )

# episodes
def ep9(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_intheprison(w),
            )

def ep10(w: wd.World):
    return (w.chaptertitle(TITLE[1]),
            sc_maddog(w),
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
            ep10(w),
            )

def main(): # pragma: no cover
    from src.pants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())
