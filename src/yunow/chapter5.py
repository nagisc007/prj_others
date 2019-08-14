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
        "逃走中なう・その２",# NOTE: 逃げる
        "水中なう",# NOTE: 溺死で四度目
        "Re:Re:Re:教会なう",# NOTE: 四度目教会、最初からGPS使ってモンスターから距離取りつつ森を抜ける
        "ゴーゴンマップなう",# NOTE: スマフマップ使うで
        "村なう",
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
            h.deal("のんびりと自分の$phoneを構えている$Sを見て赤髪の戦士$solは怒鳴りつける"),
            yusha.talk("いやだって", "これから$n_goblin包囲網突破して湖に逃げ込もうっていうんだから",
                "それなりに心の準備ってもんが必要だろ？"),
            h.look("$Sは自分の$phoneにそれを語り終えてから「なう」と呟くと",
                "板の上には彼の言葉が森の画像付きで流れた"),
            h.deal("それを見て満足そうにした彼は",
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
            )

## ep24 scenes
def sc_gooutmonsters2(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("敵から逃亡せよ！",
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
            h.look("そこには雲間から顔を覗かせた太陽の光を受けてきらめく湖面が",
                    "鬱蒼とした草木を押し広げるように存在していた"),
            yusha.talk("おお！", "やった！", "湖だ！", "これで助かる！"),
            h.deal("$Sは$solを見て喜んだが",
                    "彼はそんな素振りもなく大剣を背中に戻すと、"),
            sol.talk("向こう岸で合流な！"),
            h.deal("さっさと飛び込んで飛沫を上げて泳ぎ始めた"),
            yusha.talk("ちょっと待ってよ！", "まだ心と体の準備が！"),
            h.look("だが振り返れば数十という$n_goblinの頭が迫っている"),
            yusha.talk("ええい！", "精霊様よろしく！"),
            h.deal("そう叫んで小さな十字を切ると",
                    "$Sは鼻を摘んで尻から飛び込んだ"),
            h.hear("ウギャァ！", "という子鬼どもの汚い唸り声が沢山聞こえたが",
                    "やはり綺麗な水は苦手なようで飛び込んでこない"),
            h.think("これならイケる"),
            h.think("そう感じた$Sは余裕をぶっこいて「水中なう」と呟こうとして$phoneを見た。",
                    "板は真っ黒なままだ"),
            yusha.think("あれ？", "おかしいな？", "壊れたかな？"),
            h.deal("何度か叩いたり撫でたりしてみたが一向に動く様子はない"),
            h.deal("とにかくまずは無事なところまで逃げようと",
                    "$Sが水草揺蕩う湖底から浮上しようとした時だった"),
            h.think("何か", "苦しい……"),
            h.think("それに", "痛い……？"),
            h.deal("背中が強烈に熱い。", "それに自分から何かが頭上へ流れている。",
                    "やや黒っぽいものだ"),
            h.think("嘘", "だろ……"),
            h.deal("背中に手を回すと", "そこにはいつ投げつけられたのだろう",
                    "折れた木の枝が突き出ているのが分かって",
                    "痛みを我慢して引き抜くと", "その先端には鋭利な金属が取り付けられていた。",
                    "おそらく槍だ。", "それも投げ槍"),
            yusha.talk("うわぁぁぁ！"),
            h.deal("$Sは水中で泡と共に叫びを絞り出しながら", "暗い暗い意識の底へと沈んでいった"),
            )

## ep25 scenes
def sc_churchagain4(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    pri = w.priest1
    return w.scene("４度目の教会",
            h.be(w.stage.church1, w.day.awake4),
            yusha.talk("溺れる！"),
            h.look("思わず出た大声にびっくりして",
                "$Sは起き上がった"),
            h.deal("よく見れば教会の礼拝堂の長椅子の上で",
                "彼は横たえられている"),
            pri.talk("おや。", "お目覚めのようですね"),
            h.look("声は$n_priest1神父だった。",
                "彼は宣誓台に肘をついて分厚い本を開いている。",
                "そこには数々の精霊の言葉が書かれているらしいが",
                "精霊文字を読むことのできない$Sにとっては模様を見せられているみたいなものだった"),
            yusha.talk("あの", "神父さまは昨夜旅から帰ってきたところですか？"),
            pri.talk("そう話したはずだよね？",
                "それともまだ眠いのですか？"),
            h.think("やはり戻っていた。", "これで四度目になる。",
                "何故いつも教会で目覚めるのか分からないが",
                "とにかく死んでしまうとどうやら教会に戻るという不可思議な現象が起こるらしい"),
            h.look("$Sは慌てて隣に置いてあったズタ袋から$phoneを取り出し",
                "自分の過去の呟きを確認してみる。",
                "そこには冒険に出かけるまでのものは残っていたが",
                "森に入る前に見た景色と共に呟いたものや$n_goblinの大群に囲まれた時のものが一切消え去っていた"),
            yusha.talk("神父さま。",
                "ちょっとおかしなこと訊いてもいいですか？"),
            pri.talk("何でしょう？"),
            yusha.talk("人間は死んだらどうなるんですか？"),
            h.look("その質問に明らかに顔色を変えた神父だったが",
                "しばらく思案した後で重々しく口を開くと", "まずこう言った"),
            pri.talk("どなたか大切な方が亡くなったのですか？"),
            yusha.talk("いえ。", "ちょっと$me自身が死んだだけなんですけど",
                "どういう訳かいつも教会で目覚めるんですよ"),
            h.deal("$n_priest1神父は首を捻り", "真顔になって$Sを見ている"),
            yusha.talk("いや、ひょっとすると人間って死んでも死なないで人生やり直せるのかなって思って。",
                "まあ別に今こうして生きてるみたいだからいいんですけど"),
            h.look("笑いながらそう言った彼に", "神父はゆっくりと首を横に振る"),
            pri.talk("何があったかは分かりませんが",
                "$n_yushaさん。",
                "あなたは何度か夢を見たのでしょう。",
                "それは精霊神様が見せた仮初《かりそめ》の人生なのかも知れません。",
                "もし間違っていたと感じたなら",
                "今ある生を大切にして下さいね。",
                "きっとそういうメッセージをあなたに伝えたかったのだと思いますよ"),
            h.look("いつも以上に優しい表情と声音で神父は彼に語りかけたが",
                "$Sの方は何を言われたのか意味が理解できなかったらしい"),
            yusha.talk("分かりました。",
                "とにかくまた世話になった時は宜しくお願いします"),
            h.deal("それだけ言うと",
                "彼はズタ袋を担いで立ち上がる。",
                "$phoneを手にしたまま歩き出すと",
                "それを待ち構えていたかのように教会の入り口に赤髪の長身の男性とピンクのおかっぱ頭の少女が姿を見せた"),
            sol.talk("いつまで祈ってんだよ、$yusha？"),
            mako.talk("$taro", "早く出発しないと今日中に$st_town2に着けませんよ？"),
            )

def sc_avoidgoblin(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("ゴブリン回避",
            h.be(w.stage.homefield),
            h.deal("無事に城下町を出た$Sと$sol", "$n_makoの三人は",
                "地図を手に北にある町$st_town2を目指して街道を歩いていた"),
            h.look("遠くには$st_homemountの稜線が見え", "相変わらず$Sはその光景を$phoneに収めつつも「なう」と呟いている"),
            sol.talk("おい$yusha。", "何度言ったら分かるんだ？",
                "そんなもんすぐに見慣れちまうからいい加減にやめて", "先に行くぞっつってるだろ？"),
            h.deal("何度も立ち止まる$Sを見かねて$solが注意する"),
            yusha.talk("いやいや", "これは大事な記録なんだよ。",
                "何かあった時の為の大事な保険なんだから少しくらい大目に見てくれよ"),
            sol.talk("なーに訳の分からねえこと言ってんだよ。",
                "ともかくこの先の森はモンスターが潜んでるだろうから",
                "そんな風に油断してたらすぐやられちまうからな"),
            h.deal("旅の先輩風を吹かせた$solに", "しかし$Sは含み笑いを返す"),
            sol.talk("何だよ？"),
            yusha.talk("コレを見るが良い！"),
            h.look("そう言うと$Sは自分の$phoneを二人に見せた。",
                "そこには『$karebasho』というアプリが表示されていて",
                "森の方には既に赤い点がいくつかあるのが確認できた"),
            sol.talk("な、何だよコレは？"),
            mako.talk("$taro", "$karebasho知ってたんですか？"),
            h.deal("驚く二人に満足そうに頷くと",
                "以前$n_makoから聞いた説明をそのまま二人に伝えた"),
            sol.talk("え？", "じゃあコレ使えばモンスターがどこに潜んでるとか全部分かんのか？",
                "何だよその便利道具は！"),
            yusha.talk("見れば分かるけど", "森には$n_goblinが大挙して待ち構えてるんだ。",
                "だからいっそのこと", "$meらはここを通らないという選択をするべきだと思うんだ"),
            h.deal("自分を注目している二人に対して",
                "これこそリーダーだという提案をした$Sだったが、"),
            sol.talk("ここ通らないでどうやって$st_town2に行くつもりなんだ？"),
            mako.talk("最短がこの街道通りに森を抜けるコースなんですけど",
                "それ以外っていうともう山越えしかなくなりますよ？",
                "けどそんなことしてたら何日かかるでしょうかね……"),
            h.look("四度目の教会での目覚めの時からずっと考えていた案だったのに",
                "即座に否定されてしまう。",
                "しかしもう一度$Sは地図をよく見る。",
                "本当に迂回路は山越えしかないのだろうか"),
            yusha.talk("なあ。", "ココ。",
                "一旦西側の川を渡ってから", "この$st_town3って村を経由すればいいんじゃないのか？"),
            h.look("確かに川を挟んだ西側に小さく$st_town3村と書かれている"),
            mako.talk("でも橋の記載がないから川を渡れるかどうか分かりませんよ？"),
            h.look("彼女の指摘通りなのだが", "$Sは今一度あの$n_goblinの群れと一戦交えるつもりは毛頭なかった"),
            yusha.talk("とにかく行ってみればいいじゃないか。",
                "それこそ歩いて渡れるかも知れないし"),
            sol.talk("そんなちっぽけな川ならわざわざ地図には書かねえよ。",
                "けどそのアプリとかってのが本当なら", "確かに森にはモンスターの大群がいる訳だし……どうよお嬢"),
            h.deal("どうやら$solも$Sの意見に賛成してくれそうだが",
                "$n_makoの方は渋い表情のままだ"),
            mako.talk("まあ、$meは$taroとずっと一緒にいられればそれでいいんで……構いませんよ？"),
            yusha.talk("よし！", "決まりだ！"),
            h.think("とにかくこれで$n_goblin死は防げる"),
            h.deal("そう考えて笑みを漏らした$Sは", "意気揚々と街道を逸れて西に進路を取った"),
            h.deal("何も考えていない$solと不安を浮かべる$n_makoもその後に続いたが",
                    "その後を追うもう一つの影には誰も気づいていなかった"),
            )

## ep26 scenes
def sc_vanishriver(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("消え去った川",
            h.be(w.stage.river1, w.day.awake4),
            h.look("$Sたち一行は街道を逸れて地図上に描かれていた$st_river1という",
                "$st_homeregionの西側を南北に蛇行しながら流れている川があるはずの場所へとやってきたのだが",
                "三人は誰もが口を開けたまま", "その場で固まっていた"),
            yusha.talk("川なんてなかった"),
            sol.talk("いや待てよ！", "これでも最新の地図を手に入れてきたんだぞ？",
                "こんなに力強く描かれている川がそう簡単に消えると思うか？"),
            h.look("渡れるんだからいいじゃないか",
                "といつになく楽観的な$Sに対して", "そのそそり立つ赤髪を掻き毟りながら$solが「おかしいだろ！」と文句をつける"),
            sol.talk("こういう明らかに大きな変化があった時ってのはな",
                "近くに危険が迫っていることが多いんだよ！",
                "噴火するとか地面に穴が開くとか",
                "見たこともないようなモンスターが悪さしてるとか",
                "ほんとシャレになんねんだって！"),
            h.deal("何か相当嫌なことでも経験したのだろう。",
                "$Sはああだこうだと力説する$solの顔に$phoneを向けると、"),
            yusha.talk("マジギレなう"),
            h.deal("と呟いて彼の表情を切り取った"),
            sol.talk("ちょ", "おま！", "何してんだよ？"),
            h.look("$phoneに表示される$solの真剣な表情と「マジギレなう」には",
                "次々と反応のコメントが寄せられる。",
                "大半が嘲笑の類だったが", "中には「イケメンちゃう？」というよく分からないものも含まれていた"),
            yusha.talk("$sol大人気じゃん"),
            sol.talk("お？", "これって人気あるってこと？"),
            h.look("次々と増えていく数字に気を良くした彼に「そんなとこ」と答えた$Sを",
                "事情を知る$n_makoは目を細くして見た"),
            mako.talk("それでどうします？", "渡れるから", "渡っちゃいますか？"),
            h.look("彼女は川が流れていたと思われる大きな溝に足を一歩踏み出してみたが",
                "何かトラップが仕掛けられている様子はない。",
                "川底だったらしい場所に立つと", "振り返って二人を見た"),
            yusha.talk("そりゃあ渡るしかないでしょ？",
                "$sol君はどうするのかなー？"),
            sol.talk("渡るよ！", "渡ればいいんだろがよ、こんちくしょう！"),
            h.deal("思い切り不満をぶちまけて渋面になった$solより先に", "$Sが川底に飛び降りる。",
                "少し湿り気があったが魚が横たわっているようなこともないし",
                "一体どういう事情で川の水が引いてしまったのだろう。",
                "考えても分かりそうにはなかったので気にせず$Sは対岸に向かって歩き出した"),
            h.deal("$solも後に続いたが", "何だかおっかなびっくりな足取りだ"),
            h.look("先に渡り切った$n_makoは自分の$phoneを見ながら何かしている。",
                "何度も顔を上げては$phoneと地形を見比べているようだ"),
            yusha.talk("どうかしたの、$mako？"),
            h.deal("土手を登ってきた$Sが声を掛けながら近寄ると",
                "彼女は「見て下さい」と自分の$phoneを見せた"),
            h.look("そこには地図が映し出されている。",
                "それも手書きしたよりもずっと精巧な図面だ。",
                "鳥になって上空から俯瞰するとこういう風に描けるかも知れない。",
                "それはもう地図というよりも天空から見下ろした大地の絵そのもので",
                "その地図上では$st_river1は姿を消していた"),
            )

def sc_gogonmap(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    return w.scene("マップアプリだ",
            yusha.talk("これ何？"),
            mako.talk("$gmapですよ？", "知りません？"),
            h.deal("初めて耳にするものだった。",
                "$Sは土手を上ってきた$solにも訊いてみたが", "$phoneを持たない彼が知るはずもない。",
                "首を横に振られただけだった"),
            mako.talk("$gmapというのはですね",
                "空から見た地形をそのまま地図にして$phoneさえあればどこからでもそれが利用できるという",
                "地図アプリなんです。",
                "目的地を選べばその経路も図示してくれるし", "わざわざ地図を買わなくてもいいってことで",
                "みんなコレを使っているんですよ"),
            h.deal("$phoneを使いこなしている彼女に二人は驚きの表情を見せる"),
            yusha.talk("$phoneって何でもできるんだな……"),
            mako.talk("何でもはできませんよ。", "アプリがあるだけ"),
            h.look("そう答えて", "けれど少し得意げな顔を$Sに見せた"),
            sol.talk("でもよぉ", "この何とかップってのだと$st_town2近郊の森がごっそり無いんだが"),
            h.look("$solに言われて見てみると", "確かにあの$n_goblinの森が姿を消している。",
                "森がないというよりは森があった場所が全部砂漠に書き換えられているといった方が正しい"),
            sol.talk("やっぱこの地図おかしいんじゃね？"),
            mako.talk("データが古いのかな……"),
            h.deal("$n_makoは何度か$phoneを操作してみたが首を捻るばかりでやはり森は砂漠のままらしい"),
            yusha.talk("だけど川は実際なかったし", "こっちの地図の方が合ってるんじゃないの？"),
            h.deal("$Sは言う"),
            h.think("ただそこにはどうせもうあの森を抜けないから別にどっちでもいい",
                "という単純な思いしかなかった"),
            mako.talk("そうですね。",
                "$gmapが合っているとするとこの先に集落がありますよ。",
                "$st_town3という名前の村みたいですけど",
                "寄ってみますか？"),
            h.deal("示された地図を見ながら$Sは眉根を寄せて考え込む。",
                "距離的には村に立ち寄ると$st_town2に日が落ちるまでに到着するのが難しくなりそうだ"),
            yusha.talk("この$st_town3を二人は知ってるの？"),
            mako.talk("いいえ"),
            sol.talk("$meも聞いたことがないな。", "新しく出来た村ってこともないだろうが"),
            h.think("$Sは旅立つ前にこっそりと$phoneで調べてみた『冒険の心得』について思い出す。",
                "そこには確か『町の住民の話によく耳を傾けること』という項目があった。",
                "人々の何気ない話の中に重要な旅のヒントが隠されているらしい。",
                "そもそも旅にヒントが必要なのかどうかもよく分からないが",
                "ここはその心得というものに従うことにした"),
            yusha.talk("よし。", "それじゃあ$st_town3に寄ってみて",
                "日が暮れそうならそこで宿を取ろう"),
            h.deal("二人とも$Sの決断に反論はないらしく",
                "それぞれ頷くと彼に続いて歩き出した"),
            h.think("$Sは二人には黙っていたが",
                "実は可能なら野営をしたくなかった。",
                "テントや寝袋があったとしても夜といえば虫に悩まされるし",
                "何より雨や嵐になったらどうするんだ。",
                "やはり雨風を凌ぎ", "体調を整えておく為にも宿の利用は大事だろう"),
            h.think("それに外泊という響きに何ともいえない冒険感を唆られるのだ。",
                "$Sもまだ十六の少年。", "魔王退治よりもやりたいことが沢山ある年頃なのであった"),
            w.tag.symbol("◆"),
            h.deal("だがそんな彼らの後をこっそりと付いて歩く一つの影があった"),
            h.look("その人物は耳が隠れる程度の金髪を揺らしながらニヤリと笑う。",
                    "特徴的な八重歯が光り", "彼女の切れ長の瞳が楽しげに歪んだ"),
            h.deal("彼女は首に黄色いスカーフを巻きつけた軽装で", "足音もなく", "かつて$st_river1だった場所を渡ったのだった"),
            )

## ep27 scenes
def sc_vila(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    return w.scene("村にやってきた",
            h.be(w.stage.town3, w.day.awake4),
            h.look("粗末な木の柵とアーチを前に",
                "$Sである少年は慎重にその一歩を踏み出した"),
            yusha.talk("はじめての", "村なう！",
                "$st_town3なう！"),
            h.deal("彼は自分に$phoneを向けて",
                "最近覚えた$i_selphyという技を繰り返す"),
            sol.talk("自分の間抜け面を$phoneに載っけて何が面白いんだか"),
            h.deal("村なう", "村人なう", "村幼女なう――"),
            h.look("などと一人で楽しそうに盛り上がる$Sを見て",
                "赤髪の長身の男$solは溜息をつきながら両掌を見せる"),
            mako.talk("いいじゃないですか。",
                "$taroもこの冒険を楽しまれているってことですし。",
                "$meは$taroさえ良ければ", "魔王退治とかよりもこうやって観光旅行するだけで満足ですよ"),
            h.look("そう言ってはしゃぐ$Sを嬉しそうに見つめるのは",
                "小柄なピンクのおかっぱ頭の少女$n_makoである。",
                "彼女も自分の$phoneを彼に向けながら",
                "こっそりとその様子を画像に収めていた"),
            sol.talk("あのよぉ",
                "一度訊いてみたかったんだけど",
                "お嬢ってあいつのどこが気に入ったんだ？"),
            mako.talk("え……"),
            sol.talk("いやだってどう見たってアレがイケメンだとは思わんだろう！？"),
            h.deal("$Sはクワを担いだおじさんを捕まえて何か大声で話しかけている。",
                "おじさんは困惑しているが", "よく分からないままに$Sと横並びになると$i_selphyされていた"),
            mako.talk("べ、別に$taroがイケメンだったから惚れたとか",
                "そういうんじゃありません。",
                "あの方は", "あなたなんかには分からないとても大切なものを心に持っているんです"),
            sol.talk("アレが？", "ホントに？"),
            h.deal("ついに普通に自分を$i_selphyするだけでは満足できなくなったようで",
                "舌を鼻につけたり", "顎を歪めてみたりと",
                "変な顔をして$i_selphyし始めたので",
                "見かねた$solは駆けていって思い切り右拳を叩き込んだ"),
            yusha.talk("何すんだよ！", "いきなり殴ったら痛いだろ？"),
            sol.talk("もう気が済んだろ？",
                "いい加減", "魔王やモンスターについて訊いて回るぞ。",
                "それに川のことも気になる"),
            h.deal("脳天を押さえながら$solを睨む$Sは「わかったよ」と答えると",
                "仕方なく$phoneを肩から下げたズタ袋に仕舞い",
                "先に歩き出した$solについていく"),
            h.move("その後に$n_makoも続いたが",
                "何か気配を感じて振り返った"),
            h.look("けれど村の入り口のアーチがあるだけで",
                "誰もいない。",
                "空は雲が多く浮かんでいたが", "まだこれから太陽が高くなるところだった"),
            )

def sc_strangerumor(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    man = w.vilaman1
    return w.scene("妙な噂話",
            man.talk("あんたら何言ってんだ？"),
            h.deal("$Sたちは共用井戸の近くで木工細工の露店を出していた男に魔王や魔王軍について訊いていた"),
            yusha.talk("知らないんですか？",
                "今この世界が魔王とその軍勢によって恐怖で支配されようとしているんですよ？"),
            h.deal("彼は自分が$Sであることは隠しつつも今の世界情勢について簡単に説明したのだが",
                "男は「魔王って何だ？」と", "どうも要領を得ない"),
            sol.talk("いくら街道から外れた村だからって流石に魔王知らないとかないだろ？"),
            h.deal("自称山奥生まれの$solがその長身で迫るが",
                "露店の男の方は肩を怒らせて「知らねえよ」と不機嫌になるだけだ"),
            mako.talk("他の人たちにも訊いてみましょうよ"),
            h.deal("放っておくと$solが手を出し兼ねないと感じたのか",
                "$n_makoが間に入って収めると",
                "三人は手分けして「魔王」について知る村人を探した"),
            h.think("魔王", "という言葉を耳にしたことがない。",
                "そんな人間がこの世界に存在するとは思わなかったのだが",
                "手当たり次第に「魔王知ってますか？」「魔王恐いですよね？」「魔王来たらどうします？」等と尋ねて回ったが",
                "誰もが、"),
            man.talk("魔王？", "そんな名前の人は知らないねえ"),
            h.deal("という反応を返した"),
            h.deal("村の北外れの墓地の前に集まった三人はそれぞれの成果を報告し合ったが、"),
            sol.talk("魔王しらねえってよ"),
            mako.talk("$me、こんな場所初めてです"),
            yusha.talk("モンスターすら見たことないって言われたよ……"),
            h.deal("三人揃って大きな溜息を零した"),
            sol.talk("ひょっとして魔王ってそんな有名じゃないんじゃないのか？"),
            yusha.talk("そんなことないだろ？",
                "だってあの日", "空が真っ黒になって稲光が何本も落ちたあの時さ",
                "みんな魔王の声を聞いたんだろ？",
                "これから世界は魔王とその配下のものになるってさ。",
                "うちの母さんなんかその日から十日も寝込んでたくらいなんだぞ？",
                "それがまるで夢だったみたいに魔王なんて知らないなんて",
                "どう考えてもおかしいだろ？"),
            h.think("$Sは今でも夢に見るその光景を思い出していた"),
            h.think("それは世界中の都市で同時に発生したと言われている。",
                "その後各国が何度も会議を重ね", "調査や研究をし",
                "何とか魔王軍と渡り合っているのが現状だと", "$Sたちには伝えられていた"),
            sol.talk("$meもそれは聞いたよ。",
                "だからこそこうして山を降りて騎士団に入ろうと思ったんだ。",
                "まあ、良い仕事がなかったてのもあるけど"),
            mako.talk("$meだって同じですよ。",
                "それにほら", "コレを見て下さいよ"),
            h.deal("$n_makoは二人に自分の$phoneを見せた。",
                "そこには彼女の「魔王を知らない人ハケーン」という呟きに対して驚きや嘲笑の反応が羅列されていた"),
            mako.talk("ね？", "この通りですから", "たぶんこの村の人たちがちょっとおかしいだけなんだと思いますよ"),
            h.look("彼女の$phoneの上ではどんどんとコメントが流れていく。",
                "それをじっと見ながら$Sは何か違和感を覚えていた"),
            mako.talk("ねえ$taro。",
                "こんな村のことは放っておいて", "水などの補給をしたらさっさと$st_town2に向かいませんか？",
                "そうしないと日が暮れるまでに間に合いませんよ？"),
            sol.talk("そうだぞ$yusha。", "世界は広いんだ。",
                    "中には一つくらい魔王のことを知らない村だってあるだろってことよ"),
            h.look("二人の意見に曖昧な頷きを返しながら",
                    "$Sは今一度この村を眺めやる"),
            h.look("道も整備されてない地道で",
                    "木や布を組み合わせて作った簡素な家が多い。",
                    "着ているものは袖口の縫製すらしてなくて",
                    "中には素足で歩いている人もいる。",
                    "自分が今まで暮らしてきた$st_homeregion城下町の様子とは何もかもが違って見えた"),
            h.look("ただ違うのはそれだけではなく",
                    "村の人々の表情がどことなく明るいのだ。",
                    "魔王を知らない", "ということがひょっとするとその明るさの原因なのかも知れない"),
            h.think("そんなことを思いついて",
                    "$Sは二人に言った"),
            yusha.talk("ちょっとこの村のことを調べてみたくなった"),
            sol.talk("ハァ！？"),
            mako.talk("何言ってるんですか$taro！？"),
            h.deal("驚いた二人を「まあまあ」と手で制して$Sは自分の$phoneを見る"),
            yusha.talk("旅の心得……気になったらとことん調べるべし。",
                    "という訳で", "なーんか気になるんだわ", "ここ"),
            h.look("二人はそれぞれに懐疑的な目を$Sへと向けたが、"),
            sol.talk("ま、別にここに一泊したからって魔王退治できない訳でもないしな"),
            mako.talk("$meは$taroについていくだけですから"),
            h.deal("それぞれに承諾してくれた"),
            yusha.talk("よーし。", "それじゃあまずは今夜の宿を確保しよう"),
            h.deal("笑顔でそう言った$Sに「仕方ないなあ」という苦笑を二人は浮かべたのだった"),
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

def ep24(w: wd.World):
    return (w.chaptertitle(TITLE[3]),
            sc_gooutmonsters2(w),
            )

def ep25(w: wd.World):
    return (w.chaptertitle(TITLE[4]),
            sc_churchagain4(w),
            sc_avoidgoblin(w),
            )

def ep26(w: wd.World):
    return (w.chaptertitle(TITLE[5]),
            sc_vanishriver(w),
            sc_gogonmap(w),
            )

def ep27(w: wd.World):
    return (w.chaptertitle(TITLE[6]),
            sc_vila(w),
            sc_strangerumor(w),
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
            ep24(w),
            ep25(w),
            ep26(w),
            ep27(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

