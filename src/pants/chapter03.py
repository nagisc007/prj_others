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
        "パンツとエプロン",# NOTE: 村編突入
        "パンツが下着でエプロンが服で",
        "パンツの思考",
        "パンツは特別な着衣",# NOTE: 村長と会う
        "パンツが立ったよ",
        "パンツの洗濯日和",# NOTE: パンツ脱げて、エリィ復活作戦
        "パンツ復活",
        "激突パンツとストッキング",
        "パンツ覚醒",
        "パンツの人権",
        ]

# scenes
## ep23 scenes
def sc_mysister(w: wd.World):
    h = hero = w.hero
    ery, dran, lily, mirei = w.ery, w.dran, w.lily, w.mirei
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
                    "体とパンツが細くて尖った葉の束を押し広げながら落ちていく"),
            hero.talk("痛っ！！"),
            h.deal("それはかなり強い衝撃とそこから来る全身に広がる痛みだった。",
                    "やはり$eryの髪の毛の影響で以前よりもはっきりと感覚が存在しているらしい。",
                    "こんな時ばかりは痛覚だけでも無かったらと思わずにはいられないが",
                    "どうやらそうも言っていられない"),
            hero.talk("$eryさん？"),
            h.deal("いくら待っても彼女が立ち上がる様子がない"),
            hero.talk("$eryさん！", "……$ery？", "なあ、どうしたんだ？",
                    "まさかくたばってしまった訳じゃないよな？"),
            h.deal("返事もない。",
                    "それに動いている時には$meの内側に確かに彼女の存在感があったが",
                    "今は石にでも触れているような心地だ。",
                    "そもそもこんなに彼女の肌は冷たかっただろうか"),
            hero.talk("……打ちどころが悪かったのか？",
                    "それとも$meの声が聞こえなくなったのか？"),
            h.think("彼女は完全に沈黙していた"),
            h.deal("動くこともないし", "聴覚に集中してみたが呼吸音もないんじゃないだろうか。",
                    "ただ元から彼女が呼吸をしていたかどうか覚えがなかった。",
                    "見た目が人間に似ているからといって心臓や肺を持っていたり脳があると考える方が間違っているかも知れない"),
            h.think("ここは$meが生きていた世界とは違うんだ"),
            h.think("何度もそう言い聞かせないとなかなか染み付いた常識というものは拭い去れそうになかった"),
            hero.talk("よし。", "まずは状況を確認しよう。",
                    "できることとできないことをはっきりさせ",
                    "タスクリストにして一つずつ地道にこなす。",
                    "そうやって今まで何度も窮地を抜けてきたじゃないか"),
            h.think("わざわざ自分に言いきかせるように声に出すと",
                    "パンツとしてできることを考えた"),
            h.look("上", "即ち今$meが見ているのは葉の鋭いタイプの樹木が沢山ある森の",
                    "そいつらの葉で覆われた天だ。",
                    "葉の隙間から辛うじて空が見えたが", "白と水色を混ぜたような色合いだった"),
            h.deal("つまり今$eryは仰向けで地面か地面に近い場所に倒れているということだ。",
                    "$meから頭部は見えない。", "胸部も見えない。",
                    "負傷しているのかどうかも確認はできない"),
            h.think("前に彼女が視覚の分離という芸当を$meに試してくれたが",
                    "そんな技がパンツにできるとは思えない"),
            h.think("彼女は動くこともなく", "返事すらしない。",
                    "意識があるが答えられないというのではなく",
                    "完全に意識を失っていると考えた方が良いだろう"),
            h.think("パンツである$meにできることは思考すること",
                    "見ること", "聞くこと", "感じること",
                    "そして話すことだ"),
            hero.talk("おい！", "誰かいるか？", "もしこの声が聞こえるなら返事をしてくれ！"),
            h.think("そういえば$n_dranはどうしたのだろう。",
                    "$eryがやったような妙な指笛を吹かなければ来てくれないのだろうか。",
                    "もしそうなら指のない$meには不可能だ"),
            h.think("あの$lilyという$eryの妹だという女性は追いかけてこないのだろうか。",
                    "彼女を憎んでいるとはいえ", "ここから更に状況が悪化するとも考えづらい。",
                    "少なくとも話し合うことができれば交渉することも可能だろう"),
            hero.talk("なあ？", "誰もいないのか？", "おい！"),
            h.hear("$meの声が響くだけだ。",
                    "このまま$eryが目覚めず",
                    "誰も付近を通りかからなかったら",
                    "$meは彼女と共にここで朽ちていくのだろうか"),
            h.think("それは世界から見れば死に等しい。",
                    "誰にも知られず",
                    "外界に影響も与えず",
                    "世界から忘れ去られた存在としてそのうちに空気や地面と同化する"),
            h.think("そんなことを考えて", "パンツながらに寒さを感じた"),
            hero.talk("$meはここにいるぞ！", "まだ生きてる！",
                    "パンツになったけど", "まだ生きているんだ！"),
            h.hear("その声すら虚しく響いたけれど",
                    "木霊が返ってくるようにして",
                    "ガサリ、と足音が聞こえた"),
            hero.talk("誰だ？"),
            mirei.talk("誰か……いるんですか？"),
            h.hear("それはか細い女性の声だった"),
            )

## ep24 scenes
def sc_meetgirl(w: wd.World):
    h = hero = w.hero
    ery, dran, lily, mirei = w.ery, w.dran, w.lily, w.mirei
    return w.scene("女性に出会った",
            h.be(w.stage.left_prison, w.day.outprison),
            mirei.talk("そちらですか？"),
            h.hear("やや怯えを含んだ女性の声が",
                "ガサゴソという葉を踏み締める音を伴って近づいてくる"),
            h.think("訳も分からないものに恐怖心を覚える", "というのは実に人間らしい反応だ。",
                "だから$meはその女性の危険度が低いだろうと推測を立てて更に声を出した"),
            hero.talk("声が聞こえたんだな？",
                "こっちだ。", "人が倒れてているんだ"),
            h.think("うまく伝わるだろうか"),
            h.hear("その声の主は茂みを掻き分けながら注意深く歩いているようで",
                "落ち葉を踏むのとは別の音が間に挟まる"),
            mirei.talk("あ！"),
            h.look("どうやら$eryの体が視界に入ったらしい"),
            h.hear("すぐに慌ただしい足音になり",
                "$meの視界にもその姿を現した"),
            mirei.talk("大丈夫ですか？"),
            h.look("茂みを抜けて姿を見せたのは", "人間の女性だった。",
                "身長は百六十ないくらいだろうか。",
                "短い茶髪で栗色の大きな瞳が目を引く。",
                "ただ$meがこの世界で見た生き物は今まで全て裸体だった。",
                "骨や毛皮", "硬化した皮膚などを裸と呼ぶものかどうかは分からないが",
                "ただ一人の例外を除いて裸体だったのだ"),
            h.look("けれど現れた女性は首から膝の上までを一枚の布で隠している。",
                "その布の下や後側がどうなっているかは見えないが",
                "少なくとも上半身から下半身の大切な部分は隠されていた。",
                "布製のエプロンといった見た目だ"),
            mirei.talk("あの", "どうされましたか？"),
            h.look("彼女の目は当然パンツである$meではなく$eryの方に向いている。",
                "反応がないことに不安そうな表情になり",
                "彼女はしゃがみ込んで$eryを揺すった"),
            mirei.talk("大丈夫なんですか？", "聞こえますか？"),
            h.think("彼女を頼るしかない。",
                "$eryは揺すられても目覚めそうにないし",
                "やはり$meが交渉するしかないだろう"),
            hero.talk("すまないが……"),
            mirei.talk("あの", "分かりますか？"),
            h.deal("彼女は声がしたのに気づいて",
                "$eryの体に手をやっている"),
            mirei.talk("どうされました？"),
            h.deal("けれど話しかけているのはやはり$eryの方だ。",
                "その声は彼女の顔へと向いている"),
            hero.talk("そっちじゃない。", "今この女は意識を失っているんだ"),
            mirei.talk("え？", "けど声が……"),
            hero.talk("こっちだ。", "もっと下の方をよく見てくれ"),
            mirei.talk("下？"),
            h.think("その不安そうな声に", "$meには彼女の戸惑いが手に取るように分かった。",
                "$meだって同じ状況に置かれたら全く同じ反応を示しただろう"),
            hero.talk("もっと下", "足の方を見てくれ"),
            mirei.talk("足……ですか？"),
            h.look("明らかに気味悪がって眉を寄せている彼女の顔が",
                    "漸く$meの視界に入った"),
            hero.talk("やあ"),
            mirei.talk("キャアァァァ！！！"),
            h.deal("彼女は今までで一番大きな声を出してその右手で$meを平手打ちした"),
            h.think("女性に叩かれるという経験はこれで二度目だ。",
                    "一度目は人間だった時、元彼女に。", "そしてパンツになってからの今が二度目だった"),
            h.think("一度体験済みとはいえ",
                    "肉体の痛みと同時に精神的な痛みがあって",
                    "一瞬何が起こったのか分からなくなるのは一緒だった"),
            hero.talk("驚かせてすまない。",
                    "$meは彼女に履かれているパンツなんだ。",
                    "パンツ", "分かるか？"),
            mirei.talk("ぱ、ぱんつ", "さん？"),
            h.deal("彼女は立ち上がって自分の胸の前に手をやり", "防御姿勢を取りながら$meに恐れの目を向ける"),
            hero.talk("ああ、そうだ。",
                    "パンツだ。",
                    "彼女の下腹部を覆うこれのことだ"),
            mirei.talk("しゃべれる、ん、ですか？"),
            h.deal("ああ", "と頷きを返した後で", "$meは無理矢理に右側の目を瞑って見せる。",
                    "ウインクというにはあまりに不格好だったろうが",
                    "それでも元彼女の時はこれで上手く笑ってくれた"),
            h.look("だが人生そう簡単に同じ手は通用しないものらしい"),
            mirei.talk("何ですか……？"),
            h.think("彼女の警戒心を高めただけのようで",
                    "$meの努力は逆効果になったようだ"),
            hero.talk("いきなりパンツに話しかけられてあんたも困っているだろうが",
                    "こっちも履いている彼女が気を失ったままでとても困っている。",
                    "危害は加えないしパンツである$meにはそんな真似できないから安心して欲しい",
                    "と言っても難しいかも知れないが",
                    "何とか助けてはくれないだろうか？"),
            h.look("できる限り落ち着いた声で話しかけてみた。",
                    "彼女はまだ$meを見下ろしたままだが",
                    "その視線が何度か$meと$eryを行き来してから「そうですね」と再び屈み込んでくれる"),
            mirei.talk("ぱんつ、という生き物は初めてなのでよく分かりませんが",
                    "こちらの$i_humansの方があなたのご主人様なのですね？"),
            hero.talk("あ、ああ。", "そうだ"),
            h.think("おそらく$eryは否定するだろうが", "この場を収める為には嘘も方便というものだろう"),
            mirei.talk("そうですか。",
                    "それはお困りですよね。",
                    "ぱんつ、さん？", "はお一人で動けないんですか？"),
            hero.talk("パンツですから"),
            h.look("即答したが彼女の方はよく分からなかったようだ"),
            hero.talk("無理を言ってすまないが",
                    "彼女の体をどこか安全なところまで運んでやってくれないだろうか？",
                    "このままだといつか日も暮れて夜になるだろうし",
                    "そうなったら野生動物に襲われる心配も出てくる。",
                    "何より冷えるだろう。", "そうなると体力も奪われる"),
            h.look("そこまで喋ってから$meは彼女が口を半開きにして何度も瞬いてることに気づいた"),
            hero.talk("すまない。", "いつも説明を始めると長いと言われてしまうんだ。",
                    "話のよく分からなかったところは忘れてくれていい。",
                    "とにかく彼女をここから運んで欲しい。", "それを頼めないだろうか？"),
            mirei.talk("え、ええ。", "分かりました"),
            h.look("それでも彼女はしっかり頷くと",
                    "$eryの頭側に回って彼女の体を起こしてくれた"),
            h.deal("長座位にすると今度は前側に回り",
                    "屈み込んで$eryの両腕を自分の肩へと載せた"),
            hero.talk("あ……"),
            h.look("前に回って背中側が露になると", "どうやら裸エプロン宜しく前掛けの他には何も身につけていないことが判明した。",
                    "今$meの視界には屈み込んだ彼女の背骨がくっきりと見える綺麗な背中と",
                    "それに続く裸の臀部が広がっている"),
            mirei.talk("背負いますからもしぱんつさんが苦しくなったら言って下さいね"),
            h.deal("そう断り", "彼女は$eryの体を引きつける。",
                    "$meの前面はちょうど彼女の腰の辺りに押し付けられた"),
            h.look("再び視界は薄暗くなったが",
                    "それよりも見た目よりも筋肉質できゅっと引き締まった彼女の臀部と",
                    "$meを履いている$eryの下腹部とに挟まれているという状況に",
                    "何とも言い難い感情が湧き上がっていた"),
            mirei.talk("$meの村まで少しありますけど", "我慢して下さいね。", "行きますよ？"),
            h.deal("彼女はそう言ってから立ち上がり", "$eryを背負うと",
                    "森の中を歩き出した"),
            h.think("こんな時", "$eryのように視界を分離させたり相手の視界を借りたりできれば",
                    "ディスカバリー的な森林映像を見られたのかも知れない"),
            h.look("だが現実は女性の腰とそこから続く上臀部が左右に揺れ動く様を", "じっと見続けるしかなかった"),
            )

## ep25 scenes
def sc_gotovila(w: wd.World):
    h = hero = w.hero
    ery, dran, lily, mirei = w.ery, w.dran, w.lily, w.mirei
    return w.scene("村へ向かう道",
            h.be(w.stage.forest1, w.day.outprison),
            h.think("$meは森の中を運ばれているんだよな"),
            h.look("自分の前では勤勉な彼女の臀部の筋肉がしっかりと動いている様をずっと見せられていた"),
            mirei.talk("何か言われましたか？"),
            hero.talk("いや、大丈夫だ。",
                "それよりあんたも重かったら途中で休んでもらって構わないからな"),
            h.think("パンツでなく人の姿形をしていたなら", "小柄な女性二人くらい何とかがんばって運ぶことができたろう。",
                "それが一人は気を失い", "それをもう一人の女性に背負わせている状態というのは",
                "己の無力さを痛感すると共に何とも情けない"),
            h.deal("体感で背負われ始めてから既に十分から十五分は経っている。",
                "だが彼女は特に息を乱すでもなく森を歩き続け", "時折$meの様子を伺うように声を掛けてくれていた"),
            hero.talk("村", "と言ったが", "あんたの他にも誰か暮らしているということだな？"),
            mirei.talk("そうですよ。",
                "村長様含めて三十人程度でしょうか"),
            h.think("この世界の人口のほどがよく分からないから何とも言えないが",
                "それでも今までに見た集団というのは$st_prisonに巣を作っていた$i_antsの群れしかないので",
                "人間が三十人といえば結構な規模に思える"),
            hero.talk("突然こんなことを訊いて失礼かも知れないが",
                "あんたらはその", "パンツのことは知らないんだよな？"),
            mirei.talk("はい。", "見るのも聞くのも初めてです。",
                "$pantsはどちらの方なんですか？"),
            h.think("どちら", "と尋ねられても$meには日本あるいは東京と答えるしかなかったが",
                "それを話したところで混乱させるだけだろう。",
                "だから「よく分からないんだ」と答えておいた"),
            hero.talk("そういえばあんたのその前掛け。",
                "$meの知っているものではエプロンと呼んでいたものに似ているんだが",
                "みんなそれを身に着けているのか？"),
            h.deal("今まですんなりと答えてくれていたのに",
                "何故かその質問に彼女は答えない。",
                "黙り込み", "先を急ぐように早足になった"),
            hero.talk("何か悪いことを訊いてしまったのか？",
                "$meもこちらに来てまだ日も浅いのでどうもこの世界の礼儀というものがよく分からなくてな。",
                "失礼があったことは謝る。", "すまなかった"),
            mirei.talk("違うんです"),
            h.deal("彼女はそう言うと「はぁ」と小さく息をついてから歩く速度を緩め",
                "事情を話してくれた"),
            mirei.talk("実はこの前掛け", "$meが発案して作ったものなんです"),
            hero.talk("それじゃあ以前は？"),
            mirei.talk("当然何も身につけていませんでした。",
                "$pantsの言葉では全裸と呼ぶのでしょうか？",
                "とにかく何もなく", "常に全てを露出した状態のままでした"),
            h.think("それを聞いてこの世界にはパンツどころか基本的な衣類すら存在しないんじゃないかと思えてきた。",
                "そうすると今$meは", "この世界に服というものが誕生する瞬間に立ち会っているのかも知れない。",
                "人類が最初に身に着けたのがアダムとイブの局部を隠す葉っぱだったかどうかは知らないが",
                "体毛の大半を失った人間が厳しい条件下でも生き抜く為に発明したという服は",
                "少なくともこの世界ではまだそこまで必要とは考えられていないということだろう"),
            mirei.talk("でも$meたちにとってはそれが当たり前の状態で",
                "誰も疑問なんて持たなかったんです"),
            hero.talk("それはそうだろう。",
                "$meもここに来るまで当たり前のように下着や服を着るものだと思っていたからな"),
            mirei.talk("したぎ？", "ふく？"),
            h.deal("やはりその単語も存在しないようだ。",
                    "$meは自分のようなパンツが下着で",
                    "彼女が付けている前掛けのようなものが服だ", "とざっくりとした説明をしておいた"),
            mirei.talk("$pantsの世界ではもっと沢山の服というものがあるのですね。",
                    "いつか$meも$pantsの世界に行くことができるでしょうか？"),
            hero.talk("それは……どうだろうな"),
            h.think("パンツである自分と常識の通用しないこの世界に慣れることに必死で",
                    "自分が人間として三十年ほど生きたあの世界に帰ろうと",
                    "何故今まで一度も考えなかったのだろう"),
            h.think("やはりあのトラックが向かってきた瞬間に$meの精神は一度死んでしまったのかも知れない"),
            h.think("それともパンツではなく人間の姿をしていたなら",
                    "一縷の望みを託して再び元の世界に戻って人生の続きを楽しむことを考えたろうか"),
            h.think("分からない"),
            h.think("いつの間にか自分がパンツ以外の姿をしていることを想像できなくなっていた。",
                    "手足がないことに慣れ",
                    "$eryに履かれることを当たり前と思い",
                    "常に股間の位置から世界を見上げることが日常になりつつあった"),
            mirei.talk("遠いんですか？"),
            hero.talk("そうだな。", "簡単には行くことはできない。",
                    "元大賢者とやらの力を以ってしてもな"),
            mirei.talk("え……"),
            hero.talk("どうした？"),
            h.deal("彼女の歩みが突然止まる"),
            mirei.talk("今", "なんて言われました？"),
            hero.talk("元大賢者とやら……？"),
            h.deal("$meがそう口にすると彼女は何も答えずに立ち止まり",
                    "その背中から$eryを下ろす"),
            hero.talk("どうしたんだ？"),
            h.look("降ろされた$meの視界は地面に近づき",
                    "足を曲げて座らされた$eryの股間から",
                    "彼女の肩を持ってこっちを真剣な表情で見つめる栗色の瞳を真正面に捉えた"),
            mirei.talk("もしかして$pantsのご主人様って", "あの大賢者様なんですか？"),
            hero.talk("元大賢者だと聞いている"),
            mirei.talk("本当なんですね？"),
            h.deal("$eryの肩を揺すりながら彼女は$meに何度も「本当か？」と尋ねた"),
            h.deal("$meが$st_prisonの奥深くに五百年閉じ込められていたことと",
                    "そこから出てきて知らない女に崖から落とされたことを話すと",
                    "女は驚きを隠せず口を押さえて大きく首を振った"),
            mirei.talk("それじゃあ伝説は本当だったんですね！",
                    "信じられない……"),
            hero.talk("伝説って何のことだ？",
                    "そもそもあんたは大賢者が恐くないのか？", "世界を破壊しようとしたんだろ？"),
            h.look("その質問に彼女は首をぶるぶると左右に振る"),
            mirei.talk("$meが知っている伝承では",
                    "大賢者$ln_ery・$fn_ery様が五百年前にお隠れになられてからこの世界はおかしくなり始めたというものです"),
            h.think("そもそも$meの知識の範囲ではおかしいことだらけのこの世界が”おかしくなった”と言われても",
                    "何の実感も湧かなかった。",
                    "それとも五百年も経てば色々と話が捻じ曲げられるという", "よくある話だろうか"),
            mirei.talk("実は$meがこのエプロン？　ですか", "それを考案しなければならなかったのも",
                    "世界の大異変に関連しているんです"),
            hero.talk("$meにはさっぱり事情が分からないが",
                    "今この世界は", "おかしいのか？"),
            h.deal("彼女は栗色の目を閉じて大きく頷くと",
                    "再び$eryを背負った"),
            mirei.talk("ぜひ村で長に会って下さい。",
                    "そして大賢者様に$meたちの村を助けていただきたいのです"),
            h.deal("彼女は真剣な声でそう言うなり",
                    "一気に落ち葉を蹴って駆け出した"),
            )

## ep26 scenes
def sc_arrivevila(w: wd.World):
    h = hero = w.hero
    ery, dran, lily, mirei = w.ery, w.dran, w.lily, w.mirei
    zones = w.zones
    return w.scene("エプロンの村",
            h.be(w.stage.town1),
            h.explain("森で出会った彼女に背負われてやってきたのは",
                "村と言っても$meが想像していたような木で組んで建てた民家が幾つか集まっている",
                "というものではなく", "地面にテントのように三角形をした大きな屋根だけが並んでいた。",
                "その屋根も文化財に指定されるような茅葺きといったものではなく",
                "石だろうか", "何か硬質な四角が並べられている"),
            mirei.talk("確認してくるので", "こちらで少しお待ち下さい"),
            h.deal("そう言って彼女は$eryを背から下ろして地面に寝かせると",
                "足早に手前の三角屋根の中へと入っていった"),
            h.look("置き去りにされた$meが見ていたのは", "空だった"),
            h.think("パンツの視界。",
                "自分で動くことすらできない", "誰かの助けを得られないと何もできない",
                "$eryの不思議な力のお陰でこうして見たり喋ったりできているが",
                "それが無ければただ思考するだけの存在だったろう"),
            h.think("いや。", "そもそもパンツは思考するのか？"),
            h.think("手足がない", "頭がない", "動かせない",
                "ということがこれほど思考や感情に影響を与えるものだとは思わなかった。",
                "$meはどこに行っても変わらずに$meのままだ",
                "と元彼女に言ってしまったことを今は後悔している"),
            h.think("パンツになったら", "それはもう$meではなくパンツの思考だろう"),
            h.look("見上げた空の青さが目に染みる",
                "というのはこんな気分のことなんだろうな", "と物思いに耽っていたところに",
                "彼女が小走りで戻ってくる"),
            mirei.talk("頼み込んだら数日なら置いて下さるそうです。",
                "ただ$meの家で悪いんですけど"),
            hero.talk("事情はよく分からないが", "今は助かるよ。",
                "たぶん少し休めば彼女も目を覚ますだろう"),
            h.think("それは$meの楽観的な希望でもあった。",
                "けれど元大賢者であり", "$st_prisonの中では$i_antsの大群を相手にあれだけの立ち回りをした彼女だ。",
                "そう簡単にくたばることはないだろう"),
            mirei.talk("$meたちの家は少し離れているんです"),
            h.deal("そう断ってから彼女は再び$eryを背負うと",
                "沢山立つ三角屋根の間を縫って歩いて行った"),
            )

def sc_herhouse(w: wd.World):
    h = hero = w.hero
    ery, dran, lily, mirei = w.ery, w.dran, w.lily, w.mirei
    zones, mam = w.zones, w.mam_mirei
    return w.scene("彼女の家にて",
            h.be(w.stage.mirei_house),
            h.deal("三角屋根の中は", "二メートルほど地面を掘って造られた大きな部屋になっていた"),
            mirei.talk("粗末な家ですみません"),
            h.deal("彼女はそう言って一段高くなったベッド代わりに使ってそうな場所に$eryを寝かせる"),
            mam.talk("$mirei", "帰ってきたのかい？"),
            h.hear("声がしたのは仕切りの壁で区切られた奥からだった"),
            mirei.talk("母さん", "森で気を失っている人を助けたの"),
            mam.talk("あらまあ。", "他にもお前みたいな人がいたのね？"),
            h.look("奥から出てきた女性は目が不自由なのか",
                "壁伝いで歩いてきて", "その手を彼女が掴んでこちらに誘導した"),
            mam.talk("$mirei", "こちらの方は大丈夫なの？"),
            h.deal("彼女が母さんと呼んだ女性は自分の手で$eryのお腹の辺りに触れながらそう尋ねると",
                "膝を突いて屈み込み", "全体をじっくりと確かめるように撫でていく。",
                "上半身を終えると当然$meの方にも女の手がやってきたが",
                "その感触はややざらついて", "水仕事なのか手仕事なのか",
                "日々何かしらの作業に従事している職人のものと感じた"),
            mam.talk("この股のところにあるものは$mireiが作ったものかい？"),
            mirei.talk("$meじゃないの。",
                "その方は$pantsと言って", "どこか遠くからこちらにいらしたみたい"),
            h.deal("彼女にそう紹介されたが", "やはりその母親も「ぱんつ」という言葉を発音し辛そうに繰り返す"),
            h.think("少し慣れてきたが", "誰もがパンツという言葉や存在を知らないというのは",
                "自分のこれまで人間として生きてきた常識を丸ごと否定されているようで何とも心細い"),
            mirei.talk("$meはこれから村長さまを呼んで来なくちゃいけないから",
                "お母さん", "それまでこの方たちのことをお願いします"),
            mam.talk("ああ。", "大丈夫だからいってらっしゃい。",
                "長さまに失礼のないようにね"),
            mirei.talk("分かってる。", "余計なことを言わないようにすればいいんでしょ。",
                "すぐ戻ってくるから"),
            h.deal("彼女はそう言うと$meを見てから小さく手を振り", "家を出て行ってしまう"),
            h.think("これで最低でも風雨は防げるようになったと安堵した$meの視界を",
                "彼女の母親の掌が何度も往復する"),
            hero.talk("そんなに珍しいのか？"),
            h.think("彼女と同じように母親も前掛けを着けていたが", "確かに$meの素材よりはしっかりしてそうだ"),
            h.think("そういえば$meはどんな素材で出来ているのだろう。",
                "勝手に合成繊維だと思い込んでいたが", "どうもこの世界にそんなものがあるとは思えない。",
                "無難なところで綿だろうか。", "綿花", "あるいは綿のような実を付ける植物はありそうだが"),
            mam.talk("あら", "お目覚めになったの？"),
            h.think("$meは声を発してしまってから黙ったままでいた方が良かったことに気づく"),
            hero.talk("驚かせてしまったらすみません。",
                "$meは今あなたが触っているパンツなんです"),
            mam.talk("え？", "ぱんつ……さん？"),
            h.deal("結局ついニ十分ほど前に彼女とやったやり取りを繰り返し",
                "簡単に$meがパンツであり", "見たり喋ったりできることを理解してもらった"),
            mam.talk("それじゃあ", "あなたは元大賢者さんのパンツさんなんですね？"),
            hero.talk("まあ", "そういうことになりますかね"),
            h.deal("大賢者という言葉を出すのを躊躇ったが",
                "説明を簡略化する為に使ってしまった。",
                "それでも彼女はその名に驚いた様子もなく",
                "$meがパンツということも受け入れてくれた"),
            mam.talk("$meは小さい頃からずっとこの村から出たことがなくて",
                    "あの子が$meの娘になってくれるまで知らないことばかりだったんです。",
                    "それで大賢者さんはどうして亡くなっているのですか？"),
            hero.talk("え？"),
            h.think("聞き間違いでなければ", "今彼女は$eryを”亡くなっている”と言った"),
            mam.talk("だってこの方", "全然$i_energyを感じませんもの"),
            hero.talk("そうなのか？", "あんたは触れればそれが分かるのか？"),
            h.think("$mireiと呼んでいた彼女の娘の方はそういったことが全然分からないと言っていた"),
            mam.talk("はい。",
                    "$meはこの$st_town1村の元巫女ですから"),
            h.deal("そこに足音が複数響き",
                    "数名が家に入ってきたのが分かった"),
            mirei.talk("お母さん……"),
            h.hear("彼女の声に続いて聞こえたのは",
                    "嗄れた老女のそれだった"),
            zones.talk("それで元大賢者というのは……その小娘かい？"),
            )

## ep27 scenes
def sc_meetreader(w: wd.World):
    h = hero = w.hero
    ery, dran, lily, mirei = w.ery, w.dran, w.lily, w.mirei
    zones, mam = w.zones, w.mam_mirei
    return w.scene("長に出会う",
            h.be(w.stage.mirei_house, w.day.meetmirei),
            h.look("$mireiに連れられて家に入ってきたのは",
                "灰色の髪の毛で体の前面を覆った老女だった。",
                "$meの視界では下腹部まで覆われているように見えたが",
                "それがどこまで続いているかまでは見られない"),
            mam.talk("あら", "村長さま"),
            h.deal("その声に$mireiの母親は顔を入り口の方へと向けたが",
                "長の方は何も反応せず", "そのまま$eryの前まで歩いてきて",
                "傍で屈んでいた母親は邪魔にならないようにと後ろに下がった"),
            zones.talk("ふむ"),
            h.look("長の老女は$eryを見て小さく唸ると",
                "後ろを振り返って入り口に立つ$mireiに尋ねる"),
            mirei.talk("何でしょうか"),
            zones.talk("何の能力もないお前に何故この少女ごときが大賢者だと分かるのかねえ？",
                "それとも……"),
            h.look("眉毛のほとんどないその皺塗れの目を一瞬彼女の母親の方へと向けたが",
                "$mireiはすぐにそれを否定する"),
            mirei.talk("お母さんじゃありません。", "$meが大賢者さまの従者である$pantsから直接聞きました"),
            zones.talk("ぱん、つ……さん？"),
            h.think("何度となく繰り返された光景だったが",
                "すんなりとパンツと発音できる人間はいないのだろうか"),
            hero.talk("パンツ", "だよ。", "婆さん"),
            h.deal("声を上げたところで最初は気づかれないだろうと高を括っていた。",
                "けれど村の長というだけあってか", "その視線はすぐに$meを捉える"),
            zones.talk("お前は……$i_humansではないな。", "何者だ？"),
            h.look("長は二歩ほど後ずさると",
                "$meに向かって右の掌を向けた。", "彼女も$eryと同じように不思議な力を扱えるのだろうか"),
            hero.talk("$meはパンツだ。",
                "パンツがどういうものかを理解してもらうのが難しいというのはよく分かっている。",
                "それでも何かしら理解できるように説明するなら",
                "そこの彼女", "$mireiさんが身につけている前掛けのような",
                "衣類の一種ということになる"),
            h.deal("ちらりと$mireiを見やってから", "長は$meに顰め面を向けた"),
            zones.talk("そういうことかい……。",
                "あんたらはこの$bad_maekakeを着けさせる為にこんな元大賢者だという偽物を準備して",
                "$meを謀《たばか》ろうというんだね？"),
            mirei.talk("そんな！", "長さま。", "それは違います。",
                "この方は$meとは何も関係ありませんし",
                "こちらの女性は本当にあの大賢者さまなのです"),
            h.look("$mireiは傍まで駆け寄ってくると", "真剣な眼差しで村長を見た"),
            zones.talk("寄るでないよ。",
                "お前のような不浄の者と話してやっているだけでも有り難いと思いなさい"),
            mirei.talk("す、すみません。", "けど$meは"),
            h.look("彼女は一度目を下に向けて唇を噛んだ。",
                "それを見て", "事情はよく分からないが少なくとも$meは$mireiの側に付くべきだと感じた"),
            hero.talk("婆さん。",
                "あんたはこの$eryを見てすぐに元大賢者ではないと言ったが",
                "その根拠は何だ？"),
            zones.talk("パンツ、とやら。",
                "お前がどういう素性の者かは知らん。",
                "だがその程度の$i_energyでは何も分からんし",
                "$meが説明したところで信じられんだろう"),
            h.think("やはり$eryたちと同じく$i_energyを見る力があるのだと", "今の発言で確信できた"),
            hero.talk("確かに$meには大した$i_energyがない。",
                    "けれどパンツというのはあんたらのような生き物じゃない。",
                    "パンツは特別な着衣なんだ。",
                    "もし本当に彼女が元大賢者ではないというなら$meを脱がせてみればいい。",
                    "でもどうなっても知らないぞ？",
                    "何故ならこの元大賢者は$meによってその$i_energyを抑え込まれているんだからな"),
            h.feel("誰もが息を呑んだのが分かった"),
            zones.talk("$i_energyを", "抑える……それは神具", "あるいは魔具と呼ばれるものではないか。",
                    "パンツ", "お前が", "そうなのか？"),
            h.look("皺でだぶついた長の目が大きく開かれる"),
            h.think("$meにはその神具とか魔具というものが分からなかったが",
                    "相手が恐れを抱いているならそれを利用しない手はない"),
            hero.talk("どうしたんだ？",
                    "脱がさないのか？"),
            zones.talk("わ、$meがお前のような$bad_maekakeに触れられる訳がなかろう？"),
            h.deal("そう言うと長は後ずさり",
                    "さっきは寄るのも嫌だと言った$mireiの手を引いて$eryの方へと歩かせる"),
            zones.talk("$fn_mirei", "お前がやるんだよ。",
                    "もしお前らが共謀して$meに何か仕掛けようとしているなら",
                    "お前の母親ごと二度とこの村にいられないようにしてやるからね"),
            mirei.talk("そんな……！"),
            h.look("彼女の視線が何度も$meと母親", "長の間を往復する"),
            hero.talk("大丈夫だ。", "心配ない"),
            h.deal("$meの予想が正しいなら誰の手によっても$eryから$meを脱がすことはできないはずだ。",
                    "そもそもあれだけ彼女が試して一度も脱ぐことができなかったのだから",
                    "それを何の力もなさそうな$mireiがやったところで無理だろう。",
                    "脱がす以外の方法というと",
                    "$i_antsとの戦いの中で起こったように", "物理的な損傷に加えて彼女自身の$i_energyの暴走のような内側からの力が不可欠だろう"),
            h.think("それとも$eryが気を失っているように見える今なら",
                    "すんなりと脱がすことができるのだろうか").omit(),
            mirei.talk("分かりました。",
                    "やってみます"),
            h.deal("彼女は決意を固め", "$meの両脇に手を掛ける。",
                    "それから一度確かめるように母親を見て頷くと",
                    "腰のところからズラし始めた"),
            h.feel("何度やってもズレることすらなかったそれが",
                    "腰骨のところから捲れ", "巻き取られていくように裏地に返る"),
            h.think("これなら脱げる"),
            h.think("そういう予感だったが", "半分くらいまで折れたところで動かなくなった"),
            zones.talk("どうしたんだい？"),
            h.deal("長が苛立った声を上げる"),
            mirei.talk("おかしいな……何か", "ここから先が脱げないんです"),
            h.look("既に$meの視界はひしゃげてまともに機能していなかったが",
                    "それでもパンツである自分が半分くらいまで体を曲げられていることは分かった。",
                    "人間でいえば前屈をしているようなものだ。",
                    "$meが人間であった頃は爪先を指で掴むなんて真似はできなかったけれど",
                    "パンツの今なら可能なんだろうか。",
                    "少なくとも今の$meは容易に百八十度くらいは体を折り曲げられる"),
            mirei.talk("$pants", "何かしている訳じゃありませんよね？"),
            hero.talk("ああ。",
                    "$meには喋ることしかできないよ。",
                    "あとは今ある痛みを我慢することくらいだ"),
            mirei.talk("え？", "痛いんですか？", "ごめんなさい！"),
            h.deal("彼女が驚いて手を離すと", "その反動か$eryの体が転がり落ちる"),
            zones.talk("ひぃ！？"),
            h.hear("長の枯れた悲鳴が聞こえたが", "自分の体が回転している感覚しかなく",
                    "視界がほぼ潰れて見えないから一体どうなっているのか分からない"),
            zones.talk("く", "来るな！"),
            h.hear("強烈な拒絶に続いて聞こえたのはバタバタと逃げ出す足音だ"),
            mirei.talk("大丈夫ですか？"),
            h.hear("近づいてきた方の足音は$mireiだろう。",
                    "$meは「大丈夫だと思う」と答えておいたが",
                    "本当に無事かどうかは分からなかった"),
            hero.talk("すまないが", "$meを元に戻してくれないか。",
                    "何も見えないんだ"),
            mirei.talk("あ、はい。", "分かりました"),
            h.deal("そう答えた彼女の手が$meに触れる"),
            h.deal("だが彼女の手は$meを腰の方に引き上げるのではなく",
                    "するりと", "$eryの下半身から引き抜いてしまった"),
            h.look("視界が戻った$meの目には",
                    "にっこりと笑う$mireiの綺麗な栗色の瞳が見えていた"),
            )

## ep25 scenes
def sc_takeoffpants(w: wd.World):
    h = hero = w.hero
    ery, dran, lily, mirei = w.ery, w.dran, w.lily, w.mirei
    zones, mam = w.zones, w.mam_mirei
    return w.scene("パンツが脱げた",
            h.be(w.stage.mirei_house, w.day.meetmirei),
            h.look("$mireiはパンツである$meを広げて持ちながら笑いかけていた"),
            hero.talk("どういうことだ？", "さっきは脱がせられないって言ってなかったか？"),
            h.deal("$meは自分の体が$eryの腰のところで引っかかってそれ以上脱げなくなった時に痛みも感じたというのに",
                "何故こんなにもすんなりとパンツを脱がすことができたのだろう"),
            mirei.talk("すみません。",
                "先程は嘘をついていたんです"),
            h.think("つまり脱げないフリをしたということか"),
            hero.talk("じゃあいつでも脱がせたということか？"),
            mirei.talk("え？", "$pantsて本当は脱げなかったりするんですか"),
            h.think("どうなのだろう。",
                "前とは少し状況が異なるから簡単に比較することはできないが",
                "一番最初の時には脱げなかった。",
                "ぴったりと彼女の皮膚に張り付き", "$eryの力を使っても破壊することすら敵わなかった"),
            h.think("そう。", "ちらりと捲ることすらできなかったのだ。",
                "それがどういう理屈なのだろう"),
            h.deal("$meは幾つか可能性を考えてみたが",
                "どれも勝手な推測の域を出ないものばかりだった"),
            mam.talk("$mireiや。", "その女の子は大丈夫なのかね？"),
            mirei.talk("あ、そうだった。",
                "ごめんなさい。", "ちょっとだけここで休んでて下さい"),
            h.deal("母親に言われて$eryを見た彼女はそう断ってから$meを布の掛けられたテーブルの上に置くと",
                "転がったままになった$eryを抱き起こす"),
            mirei.talk("あ……"),
            h.deal("彼女を抱き起こしながら顔をこちらに向けた$mireiが",
                "何かに気づいたようで声を発した"),
            hero.talk("どうかしたのか？"),
            mirei.talk("$pants", "一人で立てるんですか"),
            h.think("え……"),
            h.look("そう言われて$meは慌てて自分の姿勢を確認する"),
            hero.talk("どうなってるんだよ……"),
            h.think("人間であった頃の$meに言ったらきっと笑って首を横に振られるだろうが",
                "これがこの世界での現実だというなら受け入れるしかない"),
            h.deal("パンツが", "立っていた"),
            h.deal("厳密に言えば自立している。",
                "生活とか意味ではなく", "股裾の部分を軽く広げ",
                "クロッチ", "所謂股布の部分をテーブルの上に突いて自重を支えているのだ。",
                "腰側も広がっているみたいだったが", "流石にそこまでは鏡がないと確認できない"),
            h.think("$meは意識することなく", "自然とテーブルの上で立っていた"),
            hero.talk("……そうか。",
                "$meって一人で立つことができたのか"),
            h.deal("思わず声に出して呟いてしまったが",
                "それを見て$mireiは目をぱちくりとさせている"),
            h.deal("彼女にこの感動をすぐ言葉にして説明しても良かったのだが",
                "それよりも$meにはまず確かめなければならないことが残っていた"),
            h.deal("右側の股裾を縮めてみる。", "少し窄《すぼ》めることはできた"),
            h.deal("続いて左側だ。", "これでもできる。",
                "それなら次だ"),
            h.deal("パンツが立った。", "それなら次に試すことは決まっている。",
                "歩くということだ。", "移動するということだ"),
            h.think("自立移動ができるようになれば", "$meは今までのように$eryに履かれているだけのパンツではなくなる。",
                    "少しは何かの役に立つこともできるかも知れない"),
            hero.talk("んんんん！！！！"),
            h.deal("足も爪先もない中で",
                    "$meは精一杯に歩くことをイメージしてみた"),
            hero.talk("んんん……動か", "ない！"),
            h.deal("だが所詮はパンツだ。",
                    "立ち上がることはできても歩くことなど不可能だった。",
                    "左右に少し体を捻ることは可能だったが",
                    "全体を跳躍させてでも前に進むような芸当はできなかった"),
            hero.talk("いや", "それでも屈伸や腹這いならば……"),
            h.deal("$meは歯を食いしばり",
                    "前後に体を折って何とか前に進めないかとやってみたが",
                    "同じ場所でへこへことお辞儀をするように曲げられただけだ"),
            h.deal("次に顔面から倒れ込み", "前部を下に付けた状態ならと考えたが",
                    "それも徒労に終わった。",
                    "もぞもぞとするだけで前進する為には腕で言えば懸垂運動の時のように引き付ける動作が必要となる。",
                    "しかしパンツにはそんな力など備わっていなかったのだ"),
            h.deal("それでも一頻り色々と試してみた。",
                    "立つことができたのだから何か方法があるだろう", "という楽観だ。", "だが、"),
            hero.talk("無理だ……"),
            h.deal("項垂れた$meを見て彼女は「気が済みましたか？」と優しい表情を向けた"),
            hero.talk("ところで長の方はどうするつもりなんだ？",
                    "見たところあまり良好な関係という訳ではなさそうだったが"),
            h.look("$mireiが$eryの体を土を削り出したベッドに寝かせている間に",
                    "彼女の母親は少し休むと言って奥の部屋に引っ込んでしまった。",
                    "$meの聞き間違いでないなら", "確か母親のことを”元巫女”と言っていたはずだ"),
            mirei.talk("お見苦しいところをお見せしましたね。",
                    "色々と事情があって", "またお話ししますが",
                    "それよりも大賢者さまはこれで宜しいでしょうか？"),
            hero.talk("ああ。", "しばらくすれば目を覚ますんじゃないだろうか。",
                    "それから少し水で顔や体を拭ってやってくれると助かる"),
            h.look("仰向けに寝かされた彼女の小さな体を見たが",
                    "大量の紫の髪の毛で覆われた胸元とそれをまとめて置かれた下腹部を除いて",
                    "露出して見える部分には擦り傷や泥が付着しているのが分かった"),
            mirei.talk("分かりました。",
                    "$pantsはどうされますか？"),
            hero.talk("どう", "とは？"),
            mirei.talk("お食事とか", "それとも休まれますか？"),
            h.think("こちらの世界に来てから疲労感があったのは", "あの犬もどきの牙で風穴を開けられ",
                    "$i_energyが漏れ出ていた時くらいなもので",
                    "後は眠らずとも平気だった"),
            h.think("ただ$eryもそれは同じで",
                    "$st_prisonを歩いている時も特に疲れたり眠ろうとしたりした素振りはなかったし",
                    "食事や何かを飲むといったことすらしなかった"),
            h.think("だからこの世界ではそれが当たり前なのかと思っていたが"),
            hero.talk("あんたは食事や睡眠が必要なのか？"),
            mirei.talk("そうですね。",
                    "一部の特殊な方を除けば", "$meたちは僅かばかりの$i_energyを得る為に食べたり休んだりといった行為が必要となります"),
            h.think("その件については$meの世界の常識が当てはまりそうで安心したが",
                    "それは同時に$meにある願望を呼び起こさせた"),
            hero.talk("つまり……この世界にも食べ物はあるんだな？",
                    "うどんやパスタはないかもしれんが", "小麦粉を捏ねて焼いたり",
                    "スープで煮込んだり", "そういった料理があるということだな！？"),
            h.deal("$meはこの喜びを全身を左右に揺さぶることで表現した。",
                    "これが今の$meにできる最大限の喜びの表現法だったが",
                    "彼女はそれを見て口元に手を当てながら笑ってくれた"),
            mirei.talk("それじゃあ、$pantsも何か食べられますか？"),
            )

## ep29 scenes
def sc_eatingpants(w: wd.World):
    h = hero = w.hero
    ery, dran, lily, mirei = w.ery, w.dran, w.lily, w.mirei
    zones, mam = w.zones, w.mam_mirei
    return w.scene("パンツで食べよう",
            h.be(w.stage.mirei_house, w.day.meetmirei),
            h.think("特に空腹は感じていなかった"),
            h.think("それでも$meはパンツになったことで長らくご無沙汰だった「食べる」という",
                "実に生き物らしい行為の懐かしさを思い出しながら",
                "$mireiが用意してくれるという食事を待っていた"),
            mirei.talk("食べるものといっても大したものが出せなくて申し訳ないんですけど"),
            h.look("苦笑を浮かべながら彼女が持ってきたのは", "浅い平皿に入ったスープだった。",
                "器は粘土を捏ねて焼いたもののようで綺麗な円状にはなっていない。",
                "スープも薄っすらと黄色み掛かっているだけでシチューやカレーのような濃厚さはなく",
                "大粒の赤茶げた豆が幾つか沈んでいるだけだ"),
            h.feel("それでも$meは自分の目の前に置かれたそれを見て",
                "小刻みに体が震えていた"),
            h.think("確かに僅かに豆が入っただけのスープというのは粗末な食事かも知れない。",
                "けれどもう食べられないと思っていた者の前に芳しい湯気と共に提供されたら",
                "胃袋がなくても胃が泣くというものだ"),
            hero.talk("あれ……？"),
            h.feel("違和感だった"),
            h.deal("自分がかつて人間だった時のように初手で思い切りその料理の香りを楽しもうとしたのだが",
                "眼鏡をしていれば曇るほどの湯気が立っているのに",
                "無臭だった"),
            mam.talk("さあ", "いただこうかねえ。", "いつも悪いね", "$mirei"),
            mirei.talk("何言ってるのよ", "お母さん。",
                "今の$meがあるのはお母さんのお陰なんだよ？",
                "$meだってあの日", "お母さんが助けてくれてこうして温かいスープを飲ませてもらってなかったら",
                "この世界から消えていたかも知れない"),
            h.look("同じテーブルに就いた$mireiとその母親は",
                "それぞれに木を輪切りにしただけの椅子に座り", "$meと同じスープを前に木彫りのスプーンを手にしている"),
            mirei.talk("あの", "$pantsはご自分で食べられるんですか？"),
            h.deal("手と呼ばれる部分に相当するものが存在しない$meは当然スプーンなど持てない"),
            hero.talk("口を付けて飲むので", "たぶん大丈夫でしょう"),
            h.think("そもそも$meの気がかりはもっと違う部分に対してのものだ"),
            mirei.talk("そうですか。", "もし無理そうでしたら言って下さい。",
                "これでも看病は慣れていますから"),
            h.deal("悪意のない笑顔が$meに向けられる"),
            h.deal("$meはそれに「ああ」と素っ気なく頷くと",
                "自分の口", "つまりパンツにプリントされたクマのイラストの口の部分を",
                "身を乗り出すようにして平皿に寄せる"),
            h.feel("スープ面に近づけば近づくほどその違和感は確信へと変わったが",
                "それでもまだ$meはその確信を信じたくない気持ちを貫こうとしていた"),
            mirei.talk("どうですか？"),
            h.look("彼女は$meの口がスープ面に到達したのを見て", "不安そうに声を掛ける"),
            hero.talk("やっぱり無理みたいだ……"),
            )

def sc_washpants(w: wd.World):
    h = hero = w.hero
    ery, dran, lily, mirei = w.ery, w.dran, w.lily, w.mirei
    zones, mam = w.zones, w.mam_mirei
    return w.scene("パンツを洗おう",
            # NOTE: 食べられず汚して、初洗濯体験
            )

# episodes
def ep23(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_mysister(w),
            )

def ep24(w: wd.World):
    return (w.chaptertitle(TITLE[1]),
            sc_meetgirl(w),
            )

def ep25(w: wd.World):
    return (w.chaptertitle(TITLE[2]),
            sc_gotovila(w),
            )

def ep26(w: wd.World):
    return (w.chaptertitle(TITLE[3]),
            sc_arrivevila(w),
            sc_herhouse(w),
            )

def ep27(w: wd.World):
    return (w.chaptertitle(TITLE[4]),
            sc_meetreader(w),
            )

def ep28(w: wd.World):
    return (w.chaptertitle(TITLE[5]),
            sc_takeoffpants(w),
            )

def ep29(w: wd.World):
    return (w.chaptertitle(TITLE[6]),
            sc_eatingpants(w),
            sc_washpants(w),
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
            ep24(w),
            ep25(w),
            ep26(w),
            ep27(w),
            ep28(w),
            ep29(w),
            )

def main(): # pragma: no cover
    from src.pants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

