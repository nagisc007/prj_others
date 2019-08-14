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
        "パンツにも穴はあるんだよな",
        "パンツにも痛みを",
        "門番とパンツ",# NOTE: 門番のミノタウロスとその使役者
        "崩壊パンツ",# NOTE: 迷宮崩壊
        "パンツとストッキング",# NOTE: 監獄迷宮出たら妹が待っていた
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
            ery.talk("一応説明したとは思うが", "この$st_prisonを造ったのは$meなのだぞ？",
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
            h.look("ペットという言葉があることは安心しつつも",
                "どうやらそれは$meが住んでいたアパートで飼ったりできる類の可愛らしい生き物ではないことは確かだった"),
            h.look("巨大になった影は輪郭がはっきりとし",
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
                    "そいつが甘噛みをしたという訳ではないだろう。",
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
                    "ひょっとすると彼女には$meが知る人間らしい思考というものは無いのかも知れない"),
            h.think("もしそうなら", "$meは穴の開いたパンツのまま",
                    "いつかは要らなくなって捨てられてしまう。",
                    "そんな可能性を常に考えながらこれから彼女と行動を共にすべきなのかも知れなかった"),
            )

## ep11 scenes
def sc_inthelabyrinth(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("迷宮の中で",
            h.be(w.stage.prison1, w.day.outprison),
            h.think("階層にすると全部で百はあったんじゃないか", "と$eryは言った"),
            hero.talk("そんなに深いんだったら一日二日ではとても脱出はできないだろうな"),
            h.think("$meは食料や体力的な心配をして口に出したのだが",
                "そもそも彼女にとってそういったものが生命維持に必要なのだろうか", "という疑問がある。",
                "少なくともパンツになってしまった自分にとっては", "今のところ空腹感や疲労感といったものは無縁だ。",
                "それでも思考活動をしているということは$meの今まで生きてきた常識からすれば",
                "そこには何らかのエネルギィが必要で", "だからこそ「食べる」ということは重要事項だった"),
            ery.talk("$meがそんな簡単に脱出できるものを造ると思うのか？",
                "そもそも当初の計画では各階層ごとに番兵を配置して幽閉者の$i_energyを浪費させ",
                "出口にたどり着くまでに$i_energyを限りなくゼロに近づける予定だったのだ"),
            hero.talk("おい。", "それじゃあこの先まだあんな危険な怪物が待ってるってのか？"),
            ery.talk("ちゃんと話を聞いておったか？",
                "計画ではと言っておろう。", "配備を済ませる前に$meが捕まってしまったから",
                "この$st_prisonは未完成品のままなのだ"),
            h.think("未完成", "という言葉を聞いて若干ほっとして胸を撫で下ろしたいところだが",
                "生憎とパンツに胸はない。", "下着に胸を求めるなら", "それはやはりブラということになると思うが",
                "そうなるとパンツの顔の遥か頭上に胸があることになり", "おまけに手もないからやはり撫で下ろすことはできないのだなあ",
                "と思い至り", "少し寂しさを覚えた"),
            h.deal("それでも光のパン屑作戦により同じ道を何度も通ることがなくなった$meたちは",
                "順調に階段やスロープを見つけては上の階層へと上っていく"),
            h.deal("ただ景色に変化はなく", "ずっと彼女が指先の光で前方を照らしているだけなので",
                "注意をしていないと延々同じ通路を歩かされているんじゃないかという気になってくる。",
                "それに話している時以外は彼女のぺたぺたという素足が地面を叩く音しか響かないので",
                "出張でＪＲの走っていない田舎町に出かけた時",
                "ローカル線を使ってガタンゴトンと目的地までの長い時間を眠気と共に過ごしたことを思い出した"),
            h.feel("その所為だろうか。", "不意に強烈な眠気に襲われる"),
            ery.talk("……おい", "聞いておるのか、$hero？"),
            h.deal("感覚はない。", "彼女に履かれているという以外の感覚は確かになかった。",
                "だからこそそれに気づくのが遅れたのだろう"),
            ery.talk("どうした？", "……まさか"),
            h.deal("彼女は慌てて自分の右腿の上", "つまり$meであるパンツの右側面に触れる。",
                "そこは彼女の元ペットに牙を突き立てられ風穴を開けられてしまった箇所だった"),
            ery.talk("$meが平気だから勝手に$heroの方も無事と思っておったわ。",
                "だがこれは……$i_energyが漏れておるな"),
            h.deal("全く感触はないのだが", "それでも彼女の指が穴に触れる度に空腹感にも似た脱力を感じる"),
            hero.talk("漏れてるって……パンツから血でも出てるのか？"),
            h.think("有り得ない想像に苦笑したい気分だったが",
                "とてもそんな元気がない。",
                "気を張っていなければ今すぐ意識がシャットダウンしてしまいそうだ"),
            ery.talk("血ではない。", "お主には見えぬだろうが", "$i_energyがどんどん漏れて$meの右腿を伝って地面に流れていっておる。",
                "ほれ", "見えるようにしてやろう"),
            h.deal("そう言うなり彼女は回れ右をすると",
                "$meの目元に手をしばらく置き", "一瞬フラッシュのように光ってから", "その手を離した。",
                "何が変わったのかとゆっくり目を開くと",
                "暗い通路でもよく分かるような", "ナメクジの通り道にも似たぬらっと紫色に光る細い筋がどこまでも伸びている"),
            hero.talk("あれが全部", "その$i_energyってやつなのか？"),
            ery.talk("誰もが持っておるが", "どうやらお主の$i_energyは可視化すると紫色を帯びておるようだな"),
            h.look("その紫のぬらぬらは彼女の足元まで続いていて",
                "確かに右太腿の上をそれが流れ落ちていくのも見ることができた。",
                "ただ見ているうちにもどんどんと量は増え", "それに比例するように$meの意識も薄くなっていく。",
                "もうこのまま途切れてしまいそうで", "彼女に対して色々と質問したかったがそれすら叶わない"),
            ery.talk("まだ$meの声が聞こえるな？"),
            h.think("ああ"),
            ery.talk("それでは一つ提案してやろう。",
                    "これから$meがその穴を埋めてやる。",
                    "しかし埋めるといっても$meの体毛を使うことになるので",
                    "お主の一部が$meになる。",
                    "それでも構わぬか？"),
            h.think("彼女のどこの毛を使うのかは知らないが",
                    "ともかくこのまま意識が消えたら二度と戻ってこられないだろう。",
                    "そんな$meにとって選択肢はないに等しかった"),
            hero.talk("頼む"),
            h.deal("それだけを何とか絞り出すと", "$meの張り詰めていた気力は潰えた"),
            )

## ep12 scenes
def sc_hairandpants(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("髪の毛とパンツ",
            h.be(w.stage.prison1, w.day.outprison),
            h.feel("チクリ", "とした痛みに$meの意識は気づいた"),
            h.think("痛み？"),
            hero.talk("どういうことだ？"),
            h.think("ひょっとするとあのパンツになったという悪夢から目覚めることができたのか"),
            h.look("そんな期待で目を開いたのだが",
                "その視線の先には相変わらず幼女になった$eryの", "長い紫の髪の毛を持て余した顎の小さな顔があった。",
                "じっと$meを見ながら唇を真一文字に結んで気難しそうにしている"),
            hero.talk("何だ？"),
            h.deal("どうやら彼女は座って$meの顔を覗き込んでいるようだが",
                "その視線の先は$meではなくその右側を注視している"),
            ery.talk("気づいたのか"),
            h.deal("その問いかけに「ああ」と答えたが", "先程から続くチクリといった感覚は無くならない。",
                "何度も何度もチクチクとされ", "小さくて細い鉄の棒を突きつけられたかのような鋭い痛みが連続していた"),
            hero.talk("何を", "しているんだ？"),
            h.deal("その小さな痛みに伴って", "今度は自分の右半分が何度も引っ張られているのも分かるようになった"),
            hero.talk("なんか……変だぞ。", "$eryさん", "だから何をしているか訊いているんだが？"),
            ery.talk("先程の約束をもう忘れてしまったのか？",
                "お主の開いた穴を埋めておるのだ……$meの髪の毛で"),
            h.think("ああそういえばそんなことを言われたような気がするが", "意識が途切れる前の記憶が酷く曖昧だ。",
                "それに加えて今まではなかった痛覚や触覚がある。", "全体が変化したという訳ではなさそうだが",
                "ともかく久々に与えられた痛みに思わず声を漏らした"),
            hero.talk("……痛い"),
            ery.talk("痛覚を与えた覚えはないのだが", "どうやら今縫い込んでおる$meの髪が妙な作用をしているようだの"),
            hero.talk("穴を塞いでくれたのはありがたいが", "その……まだ終わらないのか？"),
            h.feel("チクチクと何度も続けられているのに我慢する為の腕や足がないというのは",
                "何とも堪らえようがない"),
            ery.talk("もうすぐだから少しだけ辛抱するのだ"),
            h.deal("しかし五分", "十分と待ってみても一向にチクチクが収まる気配がなかった"),
            hero.talk("一つ訊いてみるんだが", "$eryさんよ。", "あんたって裁縫は得意なのかな？"),
            ery.talk("裁縫？", "ああ縫い物のことか。",
                "物心ついた頃には全てを魔法で賄っておったからな。", "当然一度として針仕事などしたことはない"),
            hero.talk("は？", "じゃあ今$meを縫っているのって"),
            ery.talk("喜べ。", "$meの初体験だぞ"),
            h.think("$meはこの世界には存在していないかも知れない神とやらに", "心底祈った。",
                "早くこの苦行を終わらせて欲しいと"),
            w.tag.br(),
            ery.talk("ふぅ……これで良かろう"),
            h.think("やっと終わった"),
            h.deal("一体どれくらいの間", "$meの右側に開いた小さな穴は縫い続けられていたのだろうか"),
            ery.talk("$meながら上手くできたであろう？"),
            hero.talk("残念ながら$meの目では上手いかどうかは確認できない"),
            ery.talk("視界だけ分離すればよかろう。", "そんなこともできんのか？"),
            h.think("視界を分離", "という言葉について十時間くらい考えたいが", "おそらくそれをするだけ無駄だろうと一秒で結論付けた"),
            hero.talk("とにかくありがとうな。", "何とか$i_energyの流出は止まったみたいだ。",
                "もしあのまま出続けていたら$meはどうなったんだ？"),
            ery.talk("$i_energyが枯れた者は石になる。",
                "またある者は木になる。", "他にも砂や灰", "中には花や実になる者もおったな。",
                "多くは自ら動くことのない木偶と化す。",
                "そいつらに$meのような力ある者が$i_energyを注いでやることで再び動けるようになる者もいるが",
                "全てではないな"),
            h.think("だからパンツである$meが意志を持っていてもそれほど驚かなかったという訳か"),
            hero.talk("この世界には死という概念は存在しないのか？"),
            ery.talk("お主の考えておるものとは少し違っているようだな。",
                    "$meらの世界で死とは動かないという意味に近い。",
                    "つまり今$meらがいるこの$st_prison1は死そのもので出来ているということだな"),
            h.think("それなら少し前に彼女が自身の手で首を切断して動かなくなったあの凶暴な元ペットも",
                    "首を縫い付けて$i_energyを注ぎ込めばまた動くようになるということだろうか"),
            h.think("そういう認識が一般的なら", "この世界では$meが思っているほど生死というのは重要ではないのかも知れない。",
                    "寧ろもっと簡単に殺したり生き返らせたりができるとすれば",
                    "大切な誰かであっても殺すのに躊躇うようなことすら無いだろう"),
            ery.talk("しかし折角綺麗に縫えたというのにお主に見てもらえないというのも",
                    "それはそれで何だか寂しいな。",
                    "よし。", "では一瞬だけ$meの目を貸してやろう。",
                    "そして感想を言うのだ。", "綺麗にできたことを褒めてくれて良いぞ"),
            hero.talk("目を貸す？"),
            h.deal("$meの頭にクエスチョンマークが浮かんだのは一瞬だった"),
            h.look("すぐに視界が彼女の見たままとなり",
                    "パンツである$meを見下ろしていた。",
                    "だがそれはクマがプリントされたパンツを履いている幼女の股間でもある。",
                    "$meは慌てて意識を集中して彼女が懸命に縫合したという右側面だけを見るようにした"),
            ery.talk("どうだ？"),
            h.look("彼女は楽しげに$meの感想を待っているが",
                    "そもそも子供向けのパンツをじっくりと見たことなどないし",
                    "結婚も機会を逸したままで子供なんていないから親として目にしたこともなく",
                    "そういった訳で一般的な穴が開いたパンツに対して何とかしたもの",
                    "を目にした時の心境というのは案外こんなものかも知れない"),
            hero.talk("お、おう"),
            ery.talk("何が、おう、なのだ？"),
            h.look("紫色のふさふさした髪の毛が", "無数に$meの右側を走っていた。",
                    "言うなれば小さい子が色鉛筆で何とか塗りつぶそうとした", "雑な線が穴の上を沢山埋めているようなものだ"),
            hero.talk("よくできました"),
            h.deal("$meが感情の篭もらない声でそう言うと",
                    "彼女はやや不満そうに「ふん」とだけ頷き", "視界を戻してくれた"),
            h.think("もしパンツに気持ちがあったなら", "せめてもう少しきちんと縫い合わせてくれ",
                    "できるならきちんと当て布をしてそれを縫い付けてくれ", "と真摯に訴えていたことだろう"),
            h.think("ただ$meはパンツの姿と形をしているが", "精神だけはまだ人間だ。", "そのはずだ。",
                    "だからこそ敢えて言おう"),
            h.think("気にするな$me"),
            ery.talk("……うまくできたと思うんだがなあ"),
            h.deal("そうぼやきながら立ち上がると", "彼女は再び歩き始めた"),
            )

## ep13 scenes
def sc_gatekeeper(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("門番とその下僕",
            h.be(w.stage.prison1, w.day.outprison),
            h.feel("初めて触覚を得た生き物の感想というのを", "パンツである$meは猛烈に知りたくなった"),
            ery.talk("先程から何をもぞもぞとしておるか、$hero"),
            hero.talk("何ってな", "こう、何だ。",
                "動くと内側が擦れる"),
            h.think("人間だった頃のことだ。", "仕事が忙しくて帰って寝るだけという生活を続けていたある日",
                "体の右側に帯状疱疹が出来たことがあった。",
                "所謂皮膚にブツブツが発生して", "それがシャツなんかに触れる度に痛むのだ"),
            h.think("今$meはそのことを思い出していた"),
            h.think("ただ当時と違うのは", "体の外側ではなく内側がむず痒いということだ。",
                "喩えるなら内蔵をくすぐられているようだと言ったら伝わるだろうか"),
            h.deal("ともかく彼女が歩く度に彼女の髪の毛が縫い込まれた部分が何とももどかしい。",
                "そして彼女の毛が縫い込まれたことでその一部分だけが地力で動かせるようになってしまったから",
                "ついつい布地を絞るようにぎゅっと縮めてしまう。",
                "それが$eryにとっては”もぞもぞ”と表現したくなる感覚のようだ"),
            ery.talk("お主からすればかつてはあった感覚であろう？",
                "その失われたものが部分的にとはいえ戻ってきたのだから",
                "もっと喜んでも良いと思うのだが？"),
            hero.talk("痛覚というか触覚というのは外界を認識する手段の一つだから",
                "生き物としては確かに大事な感覚だ。",
                "けどな", "流石にパンツに触覚は不要だと思うんだ。",
                "自分が着ているものが痛いとか痒いとか言い出したら迷惑甚だしい"),
            ery.talk("そういうものか？"),
            h.think("パンツというものが存在しない世界の人間にしてみれば",
                "$meの訴えなど微塵も理解できないものなのだろう"),
            h.move("彼女は階段を登りながら「仕方ないな」と",
                "$meの右側面", "彼女の紫の毛が縫い込まれた部分に触れる"),
            hero.talk("熱っ！"),
            h.feel("アイロンでも当てられたかと思うような一瞬の熱だった"),
            ery.talk("どうだ？", "少しはマシになったであろう？"),
            h.think("確かに痛痒感は消え去った"),
            hero.talk("何をしたんだ？"),
            ery.talk("お主の内側のみ", "感覚を遮断してみた。", "少なくともこれでもぞもぞとする必要は無くなるだろう？"),
            h.feel("確かに右側の内蔵を擦り上げられるような感覚は完全に消えていた。",
                "彼女がぽんぽんと$meの右側面を叩くとその感覚はちゃんとあって",
                "内側のみがきれいさっぱりと無感覚になっているのが分かる"),
            hero.talk("どういう仕組みかは分からんが",
                "$eryさんが凄いということだけは確かなようだな"),
            ery.talk("だから$meは元大賢者だと言うておろうが……ん？"),
            h.hear("階段を登り切る前に",
                "彼女の足が止まった"),
            ery.talk("ほお……"),
            h.hear("$eryは何か気づいたようだが", "$meにはそれが分からない。",
                "いや", "鎖の音が微かに響いている。",
                "金属の輪が触れ合い", "澄んだ高い音を空間に響かせ",
                "それが遠くから近づいてくる。",
                "パンツである$meの聴覚でもそれがいよいよはっきりしてくると",
                "彼女は再び階段を登り始めた"),
            ery.talk("面白い"),
            h.deal("それは子供の声ではなかった。", "低く喉の奥だけで鳴らしたような",
                    "今までに彼女が聞かせたことのない類の邪悪さに満ちたそれだった"),
            h.deal("ただ口ではそう言いながらも緊張しているのか",
                    "感覚こそないが",
                    "$meを履いている彼女の筋肉が普段よりも緊張していると思えた。",
                    "歩き方か", "それとも息遣いか",
                    "空気のようなものだろうか。",
                    "それを感じ取った所為か", "$meまで緊張気味になり",
                    "ぎゅっと彼女の下腹部に張り付く"),
            h.look(""),
            # NOTE: 出口近くまできたら門番がいた、服と下着の存在意義を知る
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

def ep11(w: wd.World):
    return (w.chaptertitle(TITLE[2]),
            sc_inthelabyrinth(w),
            )

def ep12(w: wd.World):
    return (w.chaptertitle(TITLE[3]),
            sc_hairandpants(w),
            )

def ep13(w: wd.World):
    return (w.chaptertitle(TITLE[4]),
            sc_gatekeeper(w),
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
            ep11(w),
            ep12(w),
            ep13(w),
            )

def main(): # pragma: no cover
    from src.pants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

