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
        "逃走中なう",# NOTE: アプリで逃走
        "水没なう",# NOTE: 溺死で四度目
        "Re:Re:Re:教会なう",# NOTE: 四度目教会、最初からGPS使ってモンスターから距離取りつつ森を抜ける
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
            h.be(w.stage.forest1, w.day.awake3),
            h.look("$Sである少年と赤髪の戦士$sol", "ピンク髪の魔法使い$n_makoの三人は",
                "互いの背中を合わせて自分たちの四方八方を取り囲む気配に対峙していた"),
            h.look("木々が風に揺られてざわめくが",
                "それとは別のざわめきが目に付く全ての茂みから起こっている"),
            yusha.talk("どうすればいいんだ", "なあ", "これ絶対やばいやつだよ？", "$sol"),
            sol.talk("分かってるが", "それを知恵のない$meに言うかね"),
            h.deal("$Sの問いかけに答えた$solだったが", "流石にいつもの楽観さは微塵もない"),
            mako.talk("何匹ってレベルじゃないですね。",
                "いくら下級な$n_goblinと言ってもこれだけの数だと森そのものを焼き払うくらいしか……"),
            yusha.talk("え？", "$makoってそんな破壊力のある魔法使えるの？"),
            h.look("地図上では$st_town2近郊の森はそれなりの大きさで書かれている。",
                "これを焼き払うほどの炎となると",
                "$Sは本や伝聞の中でしか知らない伝説の魔法使いのレベルになるんじゃないだろうか"),
            h.look("そう思って彼女の方に顔をやるが",
                "何か考え込んでいるようで$Sの視線には気づかない"),
            h.hear("ガサガサ", "という音は徐々に近づき",
                "茂みの隙間には時折$n_goblinと思われる濃い緑色をした皮膚が見え隠れする"),
            h.think("$Sは思った。",
                "また死ねばこの窮地から抜け出して勝手に教会に戻ることができるはずだと"),
            h.think("けれど一方では「本当にそうなのか？」と自問する彼もいた"),
            h.think("答えを出すには簡単だ。", "もう一度死んでみればいい"),
            h.deal("彼は喉を鳴らして唾を呑み込んだが",
                "震える手で握る$shortswordを振り回しながら茂みの中に突っ込んでいく勇気は持ち合わせていなかった"),
            yusha.talk("……やっぱ死にたくない"),
            sol.talk("そんなことは分かってんだよ！",
                "とにかくどこかに突破口作って逃げるしかねえよ"),
            h.think("そうだ。",
                "逃げればいいんだ"),
            h.think("そんな単純なことに気付かされ",
                "$Sは$solの肩を叩いた"),
            yusha.talk("とりあえず入り口か出口の方に逃げようぜ。",
                "で", "どっちに行けばいいんだ？"),
            h.look("何言ってんだコイツ", "という目で$solは$Sを見ると",
                "大きな声でジリ貧だということを教えてやった"),
            sol.talk("今$meたちは$n_goblinに取り囲まれてんだよ。",
                "それも十や二十なんて数じゃない。", "下手すりゃ百だ。",
                "模擬戦なら白旗上げて助けて下さいってなもんだよ。",
                "分かるか？", "冒険素人君よ"),
            h.hear("その声に反応したのか",
                "$Sの前方の茂みが大きく動いた。",
                "明らかに棍棒を振り上げて飛び出そうとしていたのだが",
                "どういう訳か出てこない"),
            yusha.talk("……おい。", "どうなってるんだ？"),
            h.deal("声を殺して$solに尋ねたが", "彼も「分からん」と首を横に振っている"),
            h.look("それでも明らかに$Sたちを取り囲む$n_goblinの輪は小さくなっているようで",
                "茂みの音だけでなく", "奴らの笑い声だろうか",
                "キュルキュルと虫の鳴くようなそれが幾つも聞こえてくる"),
            yusha.talk("ああもうコレ絶対ダメじゃん。",
                "$meやっぱ死ぬわ"),
            sol.talk("はぁ！？", "んな簡単に諦めんな$yusha"),
            yusha.talk("けどさあ"),
            mako.talk("あった！", "ありましたよ$taro"),
            h.deal("そんな最中に声を上げたのは$n_makoだった"),
            yusha.talk("今更何があったって言うんだよ。", "もうこのまま$meらは$n_goblinの群れにボコボコにされて終わるんだ……"),
            mako.talk("これです。",
                    "見て下さい"),
            h.look("そう言って彼女が二人に見せたのは彼女の$phoneだった。",
                    "そこには上から見たこの森の地図らしき灰色の図面と",
                    "その図面で光る幾つもの赤い点", "それに二つの青い点だった。",
                    "青い方は一箇所にまとまっているが",
                    "他の赤い点はその青を取り囲むようにして数多くが円状に広がっている"),
            mako.talk("これは大好きな人をストーカーする……じゃなくて",
                    "相手の現在地がほぼ分かるというアプリなんです。",
                    "その名も$karebashoと言って",
                    "$phoneを持っている者なら大半の位置を特定できます。",
                    "ただ近くでないとうまく位置を把握できないんですけど……今は問題ないですね"),
            h.deal("彼女の説明を受けた$Sと$solは互いの顔を見合わせて「分かったか？」と確認をしている。",
                    "どうやらどちらも首を傾げていたが", "悠長に説明している時間がなかったので",
                    "$n_makoは思考停止になっている二人に声を掛けて",
                    "彼女が考えた作戦を伝えた"),
            mako.talk("これを見てもらえば分かるように",
                    "今$meたちは$n_goblinの群れに囲まれています。",
                    "けどココ……この西側の区画だけ赤い点の数が少ないでしょ？",
                    "たぶん何かがあって$n_goblinが入れないか",
                    "あるいはこの場所に$meたちを誘い込むつもりかも知れません"),
            yusha.talk("それじゃあ何もなかったらいいけど", "ひょっとしたらそこに罠があるかも知れないの？"),
            h.deal("$Sは嫌な予感を覚えつつもそう尋ねる"),
            mako.talk("確かに罠かも知れませんが",
                    "このままここでボコられるのを待っているよりはマシかも知れません。",
                    "それに地形によってはうまく利用すればここで取り囲まれるよりはずっと対処し易いということも考えられますよ"),
            h.deal("どうします？",
                    "という彼女の問いかけに$solは「それしかないな」という表情で頷いたが",
                    "$Sの方はどうも納得がいかないようだ"),
            yusha.talk("罠に飛び込んで死ぬのも", "このままここでボコボコにされて死ぬのもどっちも同じだと思うんだ。",
                    "だったらさ",
                    "そのアプリってのを使って赤い点がいないところを縫って逃げた方がいいんじゃないか？"),
            mako.talk("あの、$taro……ちゃんと理解してますか？",
                    "全部囲まれていてこの空いている部分しか逃げるところがないっていう話なんですよ？"),
            yusha.talk("違うって。", "ほらココ"),
            h.look("そう言って二人に示したのは",
                    "このまま真っ直ぐ北上したところにある湖だった"),
            yusha.talk("そこまでに赤い点があるけど",
                    "そこさえ抜ければ後は全然ないじゃん。",
                    "こっち行った方がいいよ"),
            sol.talk("湖を泳げってのか？"),
            yusha.talk("あれ？", "ここって湖なの？", "そっかー。", "じゃダメだな"),
            mako.talk("いえ。", "いけますよ。", "だってあいつら……泳げませんから"),
            h.deal("諦めかけたところで$n_makoが二人の顔を見て言った"),
            mako.talk("$n_goblinは綺麗な水が苦手なんです。",
                    "だからここに赤い点が全くないんですよ。",
                    "二人とも泳ぎは大丈夫ですか？"),
            sol.talk("山育ちだが", "漁師の仕事手伝ったこともあるからな。", "$meは大丈夫だ"),
            yusha.talk("小さい頃に教会で習ったきりだけど", "たぶん何とかなるよ"),
            mako.talk("それじゃあ", "この湖逃亡コースでいきますよ？"),
            h.deal("彼女の声に二人とも頷くと",
                    "$solを先頭にして一列になる"),
            sol.talk("後ろから指示してくれ。",
                    "赤い点が近づいたらとにかく$meが片っ端からやっつけてやる"),
            mako.talk("分かりました。", "もうすぐ二匹", "来ます"),
            yusha.talk("よーし。", "一匹は$meがやってやるぞ！"),
            h.deal("$shortswordを手に意気込んだ$Sであったが",
                    "彼は知らなかった。",
                    "$karebashoは相手も使うことができるということを"),
            )

## ep23 scenes
def sc_gooutmonsters(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("敵から逃亡せよ！",
            h.be(w.stage.forest1, w.day.awake3),
            h.explain("森の中で$n_goblinに囲まれてしまった$S一行であったが",
                "$n_makoが見つけた$phoneのアプリ『$karebasho』により",
                "敵の位置を把握することができるということに気づいたことで",
                "この窮地を脱する為の妙案を思いついたのであった"),
            sol.talk("なーに物語の解説っぽく語ってるんだよ！"),
            yusha.talk("いやだって", "これから$n_goblin包囲網突破して湖に逃げ込もうっていうんだから",
                "それなりに心の準備ってもんが必要だろ？"),
            h.look("$Sは自分の$phoneにそれを語り終えてから「なう」と呟くと",
                "板の上には彼の言葉が森の画像付きで流れた"),
            h.deal("それを見て満足そうにした$Sは",
                "$phoneを肩から掛けたズタ袋に仕舞うと",
                "やっと$shortswordを構えて茂みを割って現れた二匹の$n_goblinに対峙する"),
            sol.talk("低級モンスターとはいえ油断はすんなよ$yusha"),
            yusha.talk("分かってる"),
            h.deal("とはいえ$Sにとっては初めてのモンスターとのちゃんとした戦闘である。",
                "一歩踏み出そうとした右足の膝が小刻みに震え",
                "上手く前に足を出せない"),
            mako.talk("$taro？", "やっぱり$meが倒しますよ？"),
            h.look("その様子に背後で見ていたピンク髪の魔法使い$n_makoが",
                "右の人差し指を立ててその先端に小さな炎を灯したが、"),
            yusha.talk("いや", "ここは$meの本気の見せ所だから"),
            h.deal("そう言って空いている左手で彼女を制すと",
                "やっと震えの収まった右足から大地を蹴って",
                "棍棒を振り上げて向かってくる$n_goblinに$shortswordを向けた"),
            yusha.talk("来いや！"),
            h.deal("右手でしっかりと握った$shortswordを振り下ろされた相手の太い棍棒にぶつける"),
            yusha.talk("痛っ！！"),
            h.deal("だが案の定$Sの力では太刀打ちできず",
                "右手から$shortswordは跳ね飛ばされて", "大きく仰け反る形になった"),
            sol.talk("何やってんだ", "全く！"),
            h.deal("応戦していた$solは何とか目の前の$n_goblinの胴体を引き裂いて",
                "$Sを助けに向かおうとする"),
            h.look("けれどそれよりも早く$Sの額へと$n_goblinの第二撃目が降り注ぎ――"),
            mako.talk("$taro！"),
            h.deal("ぶつかる！？", "と感じて彼が目を閉じたのとほぼ同時に",
                "$n_goblinの首を風の刃が切り裂いていった"),
            mako.talk("危なかったですね", "$taro"),
            yusha.talk("う、うん……"),
            h.deal("後ろに手をついて腰を抜かしながら", "$Sは自分の左頬を掠めて大地に振り下ろされたままの棍棒を見つめ",
                "$n_makoに感謝をした"),
            sol.talk("それで次はどこから来る？"),
            mako.talk("待って下さい。", "確認します"),
            h.deal("$n_makoが$phoneで敵の位置を確認している間にも一匹",
                "茂みから飛び出してまだ立ち上がらない$Sに襲いかかる"),
            yusha.talk("うぉぉぉ！？"),
            sol.talk("戦場でいつまでも寝てんじゃねえよ！"),
            h.deal("駆けつけた$solの大剣が棍棒を持った$n_goblinの手を強く打ち",
                "あらぬ方向へと曲げた。",
                "緑の子鬼は汚い悲鳴を上げ",
                "自分の右手を押さえたが", "その心臓に$solの大剣が突き立てられ", "子鬼は絶命してしまった"),
            yusha.talk("……あ、ありがとう"),
            sol.talk("さっさと立てよ。", "先行くぞ"),
            h.look("手を差し出され", "$Sはそれをしっかりと握り", "立ち上がる。",
                    "赤髪の長身の彼をじっと見て$Sはニコリとしたが、"),
            sol.talk("何笑ってんだ！", "今度は助けてやらねえからな！"),
            h.look("$solは背を向けて先に歩いて行った"),
            mako.talk("この先", "更に四匹待ってます。", "徐々にこっちに敵の赤い点が集結しつつありますね"),
            h.deal("$n_makoはそう言って二人に$phoneを見せる。",
                    "そこには彼女と$Sの青い点が二つと", "彼らを囲むように徐々にその輪を狭めている無数の赤い点が映っている"),
            sol.talk("あのさ", "思ったんだけど何で青は二つなんだ？"),
            mako.talk("この$karebashoってアプリは$phoneを持ってないと反応しないんですよ"),
            sol.talk("え……じゃあ今$phone持ってないのって", "$meだけってこと？",
                    "$n_goblinでも持ってるのに！？"),
            h.deal("顔を歪ませた$solに$n_makoは「そうですよ」と冷淡に返すと",
                    "茂みから飛び上がった二匹の$n_goblinに火の弾を放った"),
            yusha.talk("なんかどんどん赤い点", "増えてない？"),
            h.look("$Sも自分の$phoneで$karebashoを使ってみたが", "確かに湧いてきた虫のように次々と赤い点が灯っていく。",
                    "その数は既に五十を超えていた"),
            yusha.talk("ねえ", "これってやっぱり無理なんじゃない？"),
            h.deal("つい$Sは口から弱音を吐き出してしまうが",
                    "$solも$n_makoも冷静だ。",
                    "特に彼女は「五匹だけ」と言ってから", "$Sの$phoneを指差す"),
            yusha.talk("どう見ても五匹じゃないだろ？"),
            mako.talk("ニ手に分かれて$meが正面の奴らを引きつけます。",
                    "$taroと$solはここの細い脇道を使って湖に抜けて下さい"),
            h.look("確かに彼女が示した脇道には五つしか赤い点がない"),
            yusha.talk("けどそれじゃあ$makoが"),
            h.deal("そう言って$solの顔を見るが", "彼も「それしかねえな」と頷いている"),
            yusha.talk("じゃ、じゃあ", "$meが囮になって"),
            sol.talk("無理だろ、てめぇじゃ？"),
            mako.talk("$taroじゃ無理です"),
            h.look("二人が異口同音に言うと",
                    "しょぼくれた$Sの腕を引っ張って$solは脇道に逸れて行った"),
            w.tag.symbol("◆"),
            yusha.talk("何だよ何だよ二人ともさ", "$meがまるで役立たずみたいなこと言いやがって。",
                    "これでも$Sなんだぞ……$yumarkは持ってないけど。", "金策で売ったけど"),
            sol.talk("ごちゃごちゃ言ってないで$yushaも戦えよ！",
                    "さっきから$meばっか$n_goblin倒してるだろうが！"),
            h.look("既に$solが相手した子鬼の数は五匹を超えていたが",
                    "まるで倒しただけ新しいのが湧いてくるかのように",
                    "次々と新しい子鬼が現れる。",
                    "それは$Sが手にした$phone上の表示でも同じで",
                    "どういう訳か$Sたちの方にばかり赤い点が寄ってくるのだ"),
            yusha.talk("なあ", "コレ見て思ったんだけどさ"),
            sol.talk("あんだよ！", "このクソ忙しい時に！"),
            yusha.talk("どうも$meたちの居場所がバレてるみたいなんだよ", "コレ見てると。",
                    "$makoの方はあっという間に赤い点が消えて", "もう湖に着いちゃってるんだけど",
                    "$meたちの前にはどんどん赤い点が増えてるの。",
                    "後ろなんか行列してるのかと思うくらい赤い点が連なってるの。",
                    "これって絶対バレてるよね……"),
            sol.talk("マジかよ！？"),
            h.look("剣に付いた$n_goblinの緑の体液を振り払い", "慌てて$solが振り返る"),
            yusha.talk("どうも", "そうみたい……"),
            h.look("$Sが自分の後方を見ると", "もはや隠れる気のない子鬼のゴツゴツとした頭が無数に列を成している姿を確認することができた"),
            sol.talk("とにかく逃げるぞ！"),
            yusha.talk("は、走ろう！"),
            h.deal("二人とも武器を手に",
                    "腰までの高さの草木が覆う獣道を突き進む"),
            h.look("$solが先頭となり", "倒すことよりも前に進むことを優先して大剣の腹で殴りつけた$n_goblinたちの中から",
                    "立ち上がろうとしているヤツを$Sは$shortswordで突き刺していく"),
            h.deal("それは単純作業にも見えて", "命を削るような重労働だった"),
            h.think("しかし止めることはできない。", "何故ならもうすぐ目的の湖だからだ"),
            sol.talk("おい$yusha！", "生きてるか！？"),
            yusha.talk("何とか！"),
            h.deal("二人とも$n_goblinの体液で緑に染まりつつも",
                    "最後の茂みを突破する"),
            h.look("そこには"),
            # TODO: 戦闘後、湖に抜けて、あとで合流しよう。そして水没し、水中なう、で死んでいく
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

def ep23(w: wd.World):
    return (w.chaptertitle(TITLE[2]),
            sc_gooutmonsters(w),
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
            ep23(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

