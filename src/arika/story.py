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
## ep intro scenes
def sc_awaking(w: wd.World):
    h = mio = w.mio
    mam = w.mam
    return w.scene("目覚め",
            h.be(w.stage.myroom, w.day.first),
            h.deal("目の下に何か止まった感触に",
                "$Sは思わず自分を叩く"),
            h.feel("痛みという感覚が広がるよりも早く開いた目が捉えた白い壁紙の天井を見て",
                "$Sは呼吸を止めた"),
            h.think("$Sって", "誰だ？"),
            h.look("部屋だ。", "おそらく$Sの個室だ。",
                "真っ白な壁紙がぐるりと天井から壁までを覆っていて菓子箱の内側みたいと感じたけれど",
                "それを見ても$Sの部屋だという実感はどこにも見つからない"),
            h.deal("$Sという感覚を確かめるように右手を握る。",
                "ズレた掛け布団から曝露していたそれは上手く$Sに馴染んで握られてくれたけれど",
                "綿の軽さに埋まったもう片方はうまく力が入れられない。",
                "体を左側に捻ってから引き抜くと動いたシャツで乳首が擦れた。", "それが微かにむず痒い"),
            mio.talk("ハァ"),
            h.deal("という自分の吐息の音は", "$Sの声なのだろうけれど", "座り心地が悪くて妙にふわふわとして耳に馴染まない"),
            h.deal("それでも体を起こし$Sは改めて部屋を見回す。",
                "緑色のカーテンは日差しを遮っているけれどそれは完全ではなく外の明るさを孕んでいる。",
                "サイドに目の大きな女の子のキャラクターのステッカーが貼られた机の上には大学ノートが開かれたままで",
                "その上をシャーペンと三色ボールペンが転がっていた"),
            h.look("そのノートの手前で", "携帯電話が光っている。", "ワインレッドのフレームをしたそれは小さく震え",
                "息絶えるように止まる"),
            h.deal("$Sは息を詰め", "手を伸ばす。",
                "ひやりとした手応えは特別新しいものではなかったが",
                "指を触れて表示された画面には$Sの知らない名前があった"),
            mio.talk("$ln_haru、$fn_haru？"),
            h.think("その発音が合っているかも怪しいけれど字面からはそうとしか読めない。",
                "ただ口に出して発音してみても記憶に引っかかりを覚えない。",
                "知らないのか", "忘れているのか。", "けれど何かの間違いやスパムの類では無いのだろう"),
            h.deal("指を動かしてそのメッセージを表示させる"),
            h.look("――$i_hismessage1"),
            h.think("ただそれだけの文面なのに", "$Sは頭の中に手を突っ込まれたみたいに酷く混乱した"),
            h.think("あなたは誰だ？", "そして$Sは誰だ？"),
            h.look("黄色に赤い花柄のハーフパンツの下", "露出した肌は張りがあってつるりとしていたけれど膝頭を超えた先",
                "脛の一部で産毛が触れた。",
                "右足の小指の爪だけが赤く色づいていて", "引っ掻くとそれが剥げる"),
            h.deal("$Sはベッドから起き出し", "その足をカーペットに着けた。",
                "その足裏に違和感はない"),
            h.look("顔を上げると壁のハンガーに掛かった制服が目に付いた。",
                "紺色のブレザーに臙脂のタイがだらりと下がり", "スカートも野暮ったい紺色だ"),
            h.hear("と、足音が上がってきた"),
            mam.talk("$mio", "まだ起きてないの？"),
            h.hear("女性の声", "おそらく$meの母親か", "それに近い保護者のものだろう"),
            h.look("アッシュブラウンのスクールバッグが床に倒れていて", "そこから教科書がはみ出している"),
            mam.talk("ねえ$mio？"),
            h.hear("ドアが二度、三度とノックされる"),
            h.look("カーテンを捲って窓の外を見た。",
                "二階だ。", "ベランダもない。", "逃げ出すことはできそうになかった"),
            mam.talk("開けるわよ？"),
            h.look("$Sの返事を待たずにドアが開く。",
                "ゆっくりと開けられたそこから顔を出した皺とシミの多い中年女性を",
                "$Sは知らない。",
                "目が合って眉間に僅かに皺が寄った"),
            mio.talk("あの"),
            h.deal("声が喉に張り付いたみたいになって上手く喋れない"),
            mam.talk("何よ？"),
            h.deal("その不機嫌そうな声にも", "自分の口から絞り出した声にも", "耳覚えがない"),
            h.deal("$Sはじっと見られているのが辛くて俯くと", "目元が熱くなった"),
            mam.talk("あんた",
                    "また学校行きたくないとか言い出すんじゃないでしょうね？",
                "そういうのは中学で卒業してよね。", "そうでなくても色々言われるんだから"),
            h.think("何だそれは。", "$Sは不登校だったの？"),
            h.deal("膝の上に置いた手はじっとりと自分の体温を感じていたのに",
                    "それ以上の実感が$Sには湧き上がらない"),
            mam.talk("ご飯", "食べなさいよ？"),
            h.deal("小さな返事をしたら彼女はドアを閉め", "一階に降りていった"),
            h.deal("$Sは再びベッドに仰向けになり", "天井をぼんやりと見上げる"),
            h.think("目覚めた時に自分がどこにいてどうなっているか分からない。",
                    "そんな経験はよくある。", "けれどこんなにも自分という実感がないというのは",
                    "それこそ記憶喪失にでもなったのかと思えてくる"),
            mio.talk("記憶喪失？", "まさかね……"),
            h.deal("$Sは体を起こし", "慌てて机の上のノートに自分の名前を書いてみる。",
                    "実感のない『$n_mio』が出来上がるとその文字がミミズのように這い出して霧散してしまった。",
                    "だから$Sはもう一度名前を書く。", "二度、三度と", "消えてなくならないように書く"),
            h.deal("けれど何度書いても$n_mioは$Sにはなってくれなかった"),
            mio.talk("$Sは", "どこ？"),
            h.look("壁に掛けられた高校の制服を見やったまま", "情けない声を上げた"),
            )

## ep1 scenes
def sc_myfamily(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    return w.scene("わたしの家族",
            h.be(w.stage.dyning),
            h.deal("急な傾斜の階段を一階まで踏み外さないように注意しつつ", "降りる"),
            h.deal("クロゼットの中に突っ込んであったグリーンのジャージのズボンだけ履いて",
                "上は半袖の白シャツのまま", "肩に掛かる髪の毛も癖が強くて盛り上がっている。",
                "そんな格好で出ていくことに抵抗がないといえば嘘になる。",
                "けれど身支度をしっかり整えられるほどの気持ちはなく",
                "知らない顔の家族が並んでいるだろう食堂を覗くのが何より恐ろしい"),
            h.move("玄関を左手に見て", "奥の声がする方に進む"),
            h.look("右手側に大きな磨りガラスが付いた引き戸があり", "そっちで食べているらしいことがその声で分かった"),
            h.deal("見覚えのない家に廊下に部屋の構成。",
                "一歩一歩に目眩を覚えそうになる。",
                "どうして", "と", "$Sはどうなったの", "を頭の中で渦巻かせながらその引き戸に辿り着くと",
                "息を詰めてからそっと開けた"),
            mam.talk("やっと来た"),
            h.look("母親だ。",
                "首周りがゆるゆるになったシャツをだらりと着こなす中肉の中年女性は重そうに腰を上げると",
                "対面にあった空の茶碗を手にしてジャーに歩いていく"),
            dad.talk("おはよう"),
            mio.talk("……うん"),
            h.look("その母親の隣に座る前髪をミリ単位で整えて寝かしつけている男性が",
                "おそらく父親だ。", "母親の三分のニ程度の体の厚みだが血色は良さそうで",
                "味噌汁を持ち上げた時に眼鏡が一瞬曇った。", "それでも構わずに口を近づけて啜る。",
                "ワカメが口から溢れたがそれすらも啜り上げた"),
            h.deal("$Sはひとまず自分のものと思われる席に腰を下ろす"),
            h.deal("隣に座るスポーツ刈りの頭の男子は弟だろうか。", "兄というにはやや目元が幼い。",
                "彼は何も言わずに右側に座った$Sを一瞥すると", "ご飯の上にふりかけで色を付け", "それを掻き込むように食べる"),
            mam.talk("それで$mio。",
                "あんたほんとに大学行くんでしょうね？"),
            h.deal("ご飯が盛られた茶碗を渡しながら母親はそう言い", "続いて味噌汁を装った。",
                "それを$Sの前に置いてから自分の席に座る。",
                "続けて父親が小さく声を挟んだ"),
            dad.talk("$mioがその気になったんだったら",
                "父さんも応援してやりたいと思ってるぞ"),
            h.look("大皿から焼き鮭の切り身を一枚取り", "真ん中に箸を入れる。",
                "目線はずっと脂が黄色く焼けた鮭に注がれていて$Sの方には向けられない"),
            mam.talk("なるべく近いとこにしてもらいたいけど",
                "あんたがどこを選ぶかってことには口出すつもりはないから"),
            h.deal("母親の皿の上には何か長い棒状の天ぷらが置かれていた。",
                "大皿の方にも同じものが載っていたが他にさつま芋やかき揚げがまだ残っている"),
            h.think("$Sは話の着地点がどこに向かおうとしているのか探りつつ",
                "自分の緑色をした箸を手に取る"),
            h.deal("小さく「いただきます」を言ってから", "小皿の青菜の胡麻和えを口に運ぶ。",
                "味はちゃんとする。", "醤油が多くて少し辛い", "と感じる以外は喉を通っても平気だ"),
            h.deal("一つ一つを確かめるように口に運ぶ。",
                "母と父は$Sの大学の話から外れ",
                "弟の高校受験の話をし始める。",
                "勉強よりもバスケをしていたいという彼はスポーツ推薦で勉強しなくてもいいようにしたいとか言い出すが",
                "すぐに母親から「勉強しないとバカになるよ」と決まり文句のような言葉が飛び出して",
                "弟はバツが悪そうにご飯を飲み込んだ"),
            h.think("おそらくこれが$ln_mio家の朝食風景なのだろう"),
            h.think("$Sにはそれが馴染まなくて", "そもそも今日の$Sはまだ$Sを見つけられていなくて",
                    "だから違和感が仕事をしているのは当然なんだと思うけれども",
                    "でも家族は誰一人として$Sが$Sではないかも知れないことには感づかない"),
            h.think("もし中身が宇宙人とか全然別の",
                    "それこそ赤の他人がなりすましていたとしても",
                    "きっと彼らは気づかない"),
            h.think("そんな事実に思い立って", "$Sは自分の胸の内側の空虚を見つけてしまう"),
            h.deal("その空虚を何とかしようと箸を伸ばし母親が食べていたのと同じ天ぷらを皿に移した時だった"),
            mam.talk("あれ？",
                    "あんたオクラ食べたっけ？"),
            h.deal("母親がそう言って$Sに目を向ける"),
            mio.talk("えっと……"),
            h.deal("言葉に詰まった$Sを父親と弟も見た。",
                    "構わず$Sはそのまま箸で真ん中から割ろうとしたけれど上手くオクラが千切れずに衣が剥がれただけになり",
                    "もういいやと丸ごとを口に運んだ。",
                    "シャリっとした食感があって", "口の中に青臭さとざらついた味が広がる。",
                    "あとカニカマが挟まっていた"),
            bro.talk("まだ寝てるだけだろ……ごっさん"),
            h.deal("そう言って弟は席を立つと",
                    "茶碗を重ねて流しに持って行く"),
            h.think("正直特に美味しいとも不味いとも思わず",
                    "ただ少しぬめりのある感覚が喉から胃袋へと落ちていくのを感じながら",
                    "$Sは$Sであることを失敗したのだろうか", "という妙な気持ちが浮かんでいた"),
            mam.talk("オクラ食べれるんだったら今度からお味噌汁にも入れるからね？"),
            h.deal("$Sは「いい」とも「駄目」とも答えずに顎を下げると",
                    "白いご飯を口に押し込んだ"),
            )

def sc_myschool(w: wd.World):
    h = mio = w.mio
    asano = w.asano
    return w.scene("わたしの学校",
            h.be(w.stage.street1),
            h.deal("ブレザーは思っていたよりもずっと$Sの体に馴染んでいた"),
            h.deal("家を出て左手側なのか右手側なのか",
                "それすら思い出せなかったけれど", "目の前を同じ高校の制服姿の男女が楽しげに歩いて行ったので",
                "$Sもその後について右手に歩き出す"),
            h.look("住宅街の路地を抜けると少し大きな通りに出た。",
                "バス停には同じ制服を着た子たちが列を作り", "次のバスを待っているのが見える。",
                "$Sの知り合いがいないか不安になったけれど「行かない」という選択肢もない。",
                "ちらりと何人かが視線を送っただけで特に喋りかけてくる誰かはいなかったのは喜んでいいのか分からないが",
                "それでも同じ制服の人間の中にいると少しだけ安堵感があった"),
            h.think("それは$Sの日常だからだろうか"),
            h.deal("他の一人でいる子がしているように$Sも自分のスマートフォンを取り出すと",
                "特に何を見るでもなく画面に視線を落とす"),
            h.deal("朝届いた覚えのない男性からはそれ以降", "メッセージは届いていない。",
                "既読になったことに安堵したのかそれとも返事なんて待ってないだけか。",
                "$Sはそれを一旦頭の隅に追いやって", "$n_mioの日常を覗き見る"),
            h.deal("スマートフォンの中にはそれほどアプリも入れられてなくて",
                "スケジュール帳や簡易の画像加工もの", "漫画や本や音楽といったものを楽しむそれくらいしか見当たらない。",
                "写真もあまりない。", "それでも知らないスーツ姿の男性と二人で写っているものがいくつかあった"),
            h.think("この眼鏡の男性が$n_haruだろうか。",
                "目鼻が小さくあまり楽しそうにしていない表情からは気難しさが伺える。",
                "清潔感はあるから嫌悪感は抱かない。", "それとも$Sが見慣れているはずだからそう感じるのだろうか"),
            h.deal("バスが来る。",
                "白いボディに赤いラインがよく目立つバスだ"),
            h.deal("低いステップを前の同じ制服姿の子に続いて乗り込むと", "既に車内は八割方埋まっていた。",
                "吊革を掴み", "肩を突き合わせながら車体の揺れに備える。",
                "発車のアナウンスに続いてゆっくりと動き出したが", "その振動を$Sは知っているようだった"),
            h.think("たぶん毎日", "中学も高校も合わせれば千回以上はこうして乗ってきたのだ。",
                "だから頭が覚えてなくても$Sがそれを忘れない。",
                "$Sは$Sを忘れてもバスは$Sを忘れない"),
            h.deal("車窓から見える街並みや車内の混雑した様子を感じているうちに$Sが見つかればいいと思っていたけれど",
                "交差点で停止して", "横断歩道を渡る知らない人たちの中にいつの間にか混ざってしまったみたいに",
                "$Sは$Sを見つけられないまま", "バスは再び発車し", "何度か角を曲がり",
                "高校前で停車した。",
                "ずらずらと降りていく同じ制服の列に並んで", "$Sも降りる"),
            h.think("分からなくても", "考えなくても", "足はその列の流れを追い",
                "挨拶に立つ教師に適当に頭を下げて校門を潜った"),
            w.tag.symbol("◆"),
            h.be(w.stage.school),
            h.deal("下駄箱を前に立ち止まった時だった"),
            asano.talk("おーはよ、$mio"),
            h.deal("背中を叩かれ", "髪色の明るいニキビの目立つ女性から声を掛けられた"),
            mio.talk("おはよ……"),
            h.look("反射的に声を返したけれど表情まではコントロールできず",
                "$Sを見た彼女はきょとんとして「ねえ？」と訝しむ"),
            mio.talk("う、うん"),
            h.deal("それを誤魔化すように背を向け", "$Sは適当に手を伸ばす。",
                "どこに自分の上履きが入っているか分からずその手は行き詰まってしまうけれど",
                "その彼女が$Sの手を導いてくれると、"),
            asano.talk("何やってんの？"),
            h.look("大きな目が$Sを見ている。", "その目の", "黒目の周りのブラウンが綺麗だ", "と思えたからだろう。",
                    "$Sは「ううん」と答えておいて", "自分のものらしい下駄箱を開け", "ゴムの上履きを取り出して履き替える"),
            h.deal("隣でその子も同じように履き替えたけれど踵の部分を凹ませたままそこを直すこともせず",
                    "そのまま廊下へと足を出した"),
            asano.talk("今日からきっちり衣替えとか", "危うくシャツのままで家出るとこだったよ"),
            mio.talk("そうだね"),
            h.deal("反応は合っていない。", "探り探りだ。",
                    "それを特に気にする様子もなく", "彼女は歩き出す。",
                    "上履きの踵がずりずりとリノリウムに擦れて音を立てていたが", "それがいつもの彼女のスタイルなのだと納得して",
                    "$Sも付いていく"),
            h.deal("男子の声も女子の声も賑やかに廊下に反響しているのに",
                    "彼女の声は$Sの耳によく馴染んで聞き取りやすかった"),
            asano.talk("でも来年は受験だからあんま呑気なことも言ってらんないんだろうけど",
                    "自分の人生の舵取りをもうしなきゃなんないなんて", "酷く憂鬱になるっていうか"),
            h.deal("$Sは相槌と愛想笑いだけを返しつつ",
                    "他の生徒たちもちらちらと見やる"),
            h.think("こんなにも沢山の同世代がいるのに",
                    "みんな自分が誰なのかちゃんと分かって生きているのだ"),
            h.move("階段を登る"),
            h.deal("彼女は$Sの中身がどうかなんて気にせず",
                    "自分が喋りたいことをただ並べて", "それに頷きや愛想笑いや肯定の声が返されるのに満足しているだけだ。",
                    "たぶん$Sでなくてもその役割は務まるだろう"),
            h.think("それでも自分が何者なのかを問われない",
                    "というのは案外気楽なものなのだと気づいた"),
            h.deal("二年三組の教室に入ると", "見覚えのない顔ばかりが同じ制服姿でいくつも島を作っていた"),
            asano.talk("おはよー"),
            h.deal("知らない誰かのおはように笑顔になって彼女はその子の席に行ってしまう"),
            h.look("$Sは案内人を失って自分の席を見つけられずに視線を彷徨わせる。",
                    "その目を睨み返す女子生徒がいた。",
                    "教室の窓際の真ん中あたりの席に一人でいる", "花柄のブックカバーを掛けた文庫本を手にした子だ。",
                    "しばらく$Sに視線を向けていたが、"),
            asano.talk("$mio？", "鞄置いてきなよ"),
            mio.talk("う、うん"),
            h.deal("案内人の一声が掛かると途端にその視線を文庫本へと向ける"),
            asano.talk("ねえ$mio？"),
            mio.talk("あ、えっと"),
            asano.talk("そこ"),
            h.deal("彼女に真ん中の前から三番目を差され", "苦笑して机に向かった"),
            h.deal("席に就くと", "腰の辺りが重くなる。",
                    "馴染んでいるというのではなく", "精神的な疲労がどっと押し寄せただけだ。",
                    "でもたぶん考えることなんかなく普通に毎日を過ごしていたら",
                    "こういった余計な気苦労も知らなくて済む"),
            h.look("笑っている子", "適当にじゃれ合ってボクシングの真似事をしている男子",
                    "参考書を開いている勉強組", "黒板の前を陣取ってそこに落書きをしては消している数人",
                    "あとはスマホを片手に一人を守っている個人たち。",
                    "$S以外は誰もが$Sを知っている。",
                    "ちゃんとじゃなくても薄っすらと", "それこそ名前まで覚えて無くても顔かせめて苗字くらいは知っている。",
                    "声や", "普段誰といてどんな声で話して笑って", "泣いたりしたこともあるのだろうか"),
            h.think("$Sは$Sが", "分からない"),
            h.think("どんな顔をしてどんな声でどんな風に笑えばいいのか。",
                    "誰といて誰とはいなくて", "どこに行けばいいのか。",
                    "そんな誰かにとっての当たり前が", "分からない"),
            h.feel("不意に涙が落ちた$Sを見た彼女は「$ln_asano」と呼ばれて自分の席に腰を下ろした"),
            h.look("背の高い男性教師が入ってくると同時に始業のチャイムが鳴り響いた"),
            )

## ep2 scenes
def sc_myfriend(w: wd.World):
    h = mio = w.mio
    asano, ochi = w.asano, w.ochi
    return w.scene("わたしのともだち",
            h.be(w.stage.classroom),
            h.think("放課後", "という言葉の響きが安堵を与えてくれるのは$Sが$Sを見失っていても同じなようだった"),
            h.look("生徒の密度が減った教室には", "鞄に教科書を詰めている$Sと文庫本を開いて読んでいる窓際の席の彼女だけが一人だ。",
                "「行こ」という誰かの声で残っていた集団が出ていくと", "彼女はその本を音を立てて閉じた。",
                "席を立ち", "$Sの方に歩いてくる"),
            ochi.talk("$mio", "無視したでしょ？"),
            h.deal("眼鏡の奥の目は近くで見ると意外としっかり開いていて",
                "睨まれたと感じたのは嘘ではなかったことが彼女の声と共に理解できた。",
                "$Sは鞄を手に", "このまま教室を出て逃げてしまおうかと一瞬考えたが",
                "その言葉に思い当たるものがなかったからもう少しだけ留まることにする"),
            mio.talk("何？"),
            ochi.talk("あの件よ。", "学校には言わないと約束したけれど",
                "$meにはちゃんと連絡してって言ったのに昨日も何も寄越さなかったでしょ？"),
            h.deal("右手を机に突いて$Sに顔を寄せるようにする。",
                "首筋がじっとりと汗ばんでいて", "僅かにそれが臭う。",
                "$Sは立ち上がりかけていたのを止めて椅子に腰を下ろし",
                "鞄を立てて少しだけ彼女と距離を開ける"),
            h.think("彼女と$Sがどういう関係か思い出せない。",
                "それでもそのあの件というものを通して何かしら秘密の共有をしているのは",
                "全く知らない間柄という訳ではないらしい。",
                "けれど今の$Sはそれを知らない"),
            ochi.talk("何よ？",
                "それとも自分は何も間違ったことをしていないと胸を張って言えるの？",
                "中学の頃はそんなじゃなかったのに。", "彼氏ができたらやっぱり変わるのね"),
            h.think("中学の$Sを知っていて",
                "彼氏を知っている。", "それって友達じゃないのだろうか。",
                "だから怒っているの？", "その彼氏って誰だ？"),
            h.deal("頭の中を幾つものハテナが巡って",
                "$Sは言葉を吐き出せずにただ彼女を怯えて見ているだけだ"),
            ochi.talk("どうしてそんな目で見るのよ？",
                "なんで中学の頃と変わっちゃったの？", "変わらないままいようって約束したのに。",
                "あいつらの所為？", "あの$n_asanoらの所為なんでしょ？"),
            mio.talk("あ、あのさ"),
            h.deal("名前を呼びかけて落ち着かせようとするけれど", "$Sは彼女の名前を思い出せない。",
                "いや違う。", "$Sは彼女の名前を知らない"),
            h.look("何も言えないままじっと見返していると", "先に涙を浮かべたのは彼女の方だった"),
            ochi.talk("$mioなんて", "嫌い"),
            h.deal("彼女ははっきりとそう口にして", "自分の鞄を手に教室を出ていく"),
            h.deal("$Sは席から立ち上がり背中に声を掛けようとしたけれど",
                "どんなにがんばってもその言葉は出てこなかった"),
            h.think("一人になった教室で腰を下ろす。",
                "あまりに重くてもうここから動きたくなくなる。",
                "それなのに心は落ち着いてくれない。",
                "ざわざわとして指先まで痺れてしまいそうだ"),
            h.think("このまま目を閉じてひと眠りしたら", "何もかもリセットしたみたいに明るくなっていないだろうか。",
                "今みたいな不安定な$Sじゃなくて",
                "友達と笑って何も気にせずに過ごせる$Sにならないだろうか"),
            h.deal("机に突っ伏して右の頬を付けると感じるひんやりが",
                "こんなでも$Sだと言いたそうだった"),
            h.deal("とスマートフォンが音を鳴らす"),
            h.deal("鞄から出してみると", "あの$n_haruからだった。",
                    "送られてきたメッセージは『来れるならいつもの交差点で待ってる』という簡素なもの"),
            mio.talk("いつものって何？"),
            )

def sc_herboyfriend(w: wd.World):
    h = mio = w.mio
    haru = w.haru
    return w.scene("わたしの彼氏",
            h.be(w.stage.street1),
            h.deal("いつもの交差点", "は駅前にほど近い大通りに面した場所だった"),
            h.deal("場所を適当に書いて送ったらそこは違うと指摘され",
                "正しい場所の地図が送り返された。",
                "マップにピン留めされたところに吹き出しで『忘れないように』と",
                "まるで教師か保護者みたいな文言があって$Sは余計に困惑した"),
            h.look("空はまだ夕焼けを迎えていない"),
            h.look("通りを車が行き来して", "運送業者のトラックがやや黒ずんだガスを吐き出して通り過ぎる。",
                "歩道の上には$Sのような学生らしき姿もあったが",
                "大半は私服かスーツ姿の人間だ。",
                "スマートフォンを片手にきょろきょろと立っている$Sの姿は彼らの目にどう映るだろう"),
            h.think("それが単なる自意識過剰だということは知っている。",
                "けれどそれを気にする$Sなのか気にしない$Sだったのかが分からず",
                "落ち着かないのだ。",
                "例の彼が歩いてくるのか", "それとも車で現れるのか見当が付けられず",
                "意味もなくスマホの画面を適当に触った"),
            mio.talk("あ……"),
            h.deal("不意に画面いっぱいにＳＮＳの忙しない言葉や画像の羅列が広がる。",
                "そこには$n_mioがフォローしたよく知らない人たちの切り取られた日常風景が無秩序に並んでいて",
                "それでも幾つかは$Sの興味を惹いた。",
                "特に自分に向けて可愛い動物の赤ん坊の画像や動画を紹介していたり",
                "アニメのようなイラストを沢山掲載していたり",
                "やたらと「かわいい」や顔文字を並べて絡んでいるよく分からないアカウントたちだ。",
                "彼らは$Sが何も発言していないにもかかわらず",
                "そこに$Sが存在しているかのように振る舞っている"),
            h.think("$Sはどこにもいないと思ったけれど",
                "そこには$Sが確かに生きていた。",
                "過去を遡れば楽しげによく知らない彼らと会話をし",
                "時に学校の愚痴を言い", "友達の悪口を言い",
                "お世辞や愛想を振りまいてはフォロワーからチヤホヤとされている"),
            h.deal("女子高生。", "という単語がプロフィールに載っていて",
                "それが$Sなのだと感じた。",
                "つまり$n_mioではなく", "そういう本名を持った女子高生。",
                "それが$Sの正体なのだ"),
            h.think("そう考えると途端に頬の筋肉が緩んで声が出た"),
            mio.talk("馬鹿みたい"),
            h.deal("今彼氏と待ち合わせ中と書き込むと",
                "餌を投げ入れた鯉の池みたいにわっと湧き立ち",
                "彼氏いたんだ？　どんな相手？", "自分が彼氏だ、いや自分だ等と",
                "よく分からない彼らの自己顕示欲が言葉になって押し寄せる"),
            mio.talk("これが……$me？"),
            h.deal("次々に書き込まれる文字は表情を伴わないからかどこか気持ち悪くて",
                "ゲームで沢山のゾンビに襲われているのを想像してしまう"),
            h.deal("そんな奴らを追い払うようなクラクションで$Sはスマートフォンからやっと目を離した"),
            h.look("$Sの目の前にメタリックブルーのセダンが停まる。",
                "助手席側の窓が開いて", "運転席に座っていたスーツの男性がちらっとこちらを見た。",
                "声を出さずに「乗って」と言ったのが分かって",
                "$Sは周囲の視線を気にしつつも助手席のドアを開けた"),
            haru.talk("どうかした？"),
            mio.talk("う、ううん"),
            h.deal("慌てて乗り込むと",
                    "彼は$Sがシートベルトをするのを確認してからアクセルを踏む。",
                    "車はスムーズに合流して走り出し", "駅前から遠ざかる。",
                    "$Sはどこに行くとも聞けず", "ただ膝の上に緊張気味に手を置いて前を見つめていた"),
            h.look("交差点の信号が赤に変わり", "ゆっくりと前の車両に続いて停車する"),
            h.look("運転席のスーツの男性は何も言わずにバックミラーを何度か確認し",
                    "ラジオを入れる。",
                    "手つきは慣れている。",
                    "$Sのように緊張した様子はなく", "既に何度もこうして出会っていることを感じさせた"),
            h.look("スマートフォンの中に収まっていた写真の印象のまま",
                    "やや気難しそうな眼鏡は沈黙を嫌わないらしく", "何度か窓の外に目線をやり",
                    "その内の数度を$Sに向けた"),
            h.look("その眼鏡の奥の瞳は黒が小さい"),
            mio.talk("青……"),
            h.deal("信号が変わったのを見て声を発すると", "彼はペダルを操作して前の車のコンマ数秒後に発車した"),
            h.deal("だが車はサイドランプを照らすと交差点を抜けた先で左に寄って再び停車。",
                    "それも丁寧に停めたのではないから大きく前後に揺れ", "シートベルトで肩が締まった"),
            haru.talk("君……誰？"),
            h.deal("予想していたよりも軽い声で彼は突然そう問いかけた"),
            mio.talk("どういう、ことですか？"),
            # TODO: だが彼にはわかる。そして打ち明ける
            # NOTE: 彼の描写
            h.deal("スーツ姿の会社員。女子高生を買っているおっさん、という訳ではなさそう。イケメンではないけれど真面目そう。どういう経緯で出会ったんだろう"),
            haru.talk("記憶でも失くした？"),
            h.deal("車を出してからすぐ穏やかな声でそんなことを言う"),
            mio.talk("え？　どうしてですか？"),
            # NOTE: 春彦は何故か分かる。「ここに君がいない」と。
            h.deal("仕方なく事情を話した"),
            haru.talk("病院行く？"),
            # NOTE: 彼氏がやってくる、放課後、初めて自分の本音を告げる
            )

def sc_sleeping(w: wd.World):
    h = mio = w.mio
    return w.scene("眠りにつくか",
            h.be(w.stage.myroom),
            h.deal("ベッドの上で休んでいる。", "制服のまま"),
            h.think("$Sについて考える。$Sは今までどうしていたのだろう"),
            h.think("それは記憶とか思い出とかそんなもので構成されているとすれば、それが消えた途端にゼロになるんだろうか"),
            h.think("自分の病気を疑ったけれど医者に行く勇気はない"),
            h.deal("目を閉じる。眠れば明日になればきっと$Sが$Sに戻っていると信じて"),
            h.deal("と、スマホが鳴った"),
            h.look("迷惑メールだった。ほっとして、けれど眠れず、画面を見つめてしまう"),
            h.deal("自分のアカウントを見つけ、それを覗く。そこには全然違う$Sが広がる"),
            h.deal("それはまるでオタサーの姫。JKというだけでちやほやしてくるフォロワーに媚をうって、かわいいって言われて喜んでいる。これが$S？"),
            h.deal("思い切り投げつけて枕で顔を覆った"),
            # NOTE: 帰ってきて、自室、眠れず、SNSを見つける、知らない自分
            )

def sc_awake2day(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    return w.scene("目覚めたら知らないわたし",
            h.be(w.stage.myroom, w.day.second),
            h.deal("目覚めた時の感覚は昨日と同じだった"),
            h.think("つまり$Sって誰だ"),
            h.look("部屋を観察する。ベッド、本棚、制服、パソコン"),
            # NOTE: パソコンはなかったが置いてある
            h.look("可愛らしい制服。知らない制服"),
            h.deal("スマホが……違う。それが鳴っている"),
            h.deal("見ると家族ＬＩＮＥだった。親からもう起きた？と"),
            h.deal("返事をして食堂に向かうことにする"),
            h.deal("ふと思ってSNSを確認する。そこには昨夜投げ出した$S"),
            # NOTE: 目覚めたらまた知らない部屋、私を見つける作業、SNSには同じ私
            )

def sc_unknownfamily(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    return w.scene("知らない家族",
            h.be(w.stage.dyning),
            h.deal("父と母がいる"),
            h.deal("$Sは一人娘としてとても大切にされているらしい"),
            h.deal("並ぶものはトースト中心に洋風で",
                "コーヒーの香りが満たす"),
            h.deal("飲めるだろうか。不安とともに口をつけると苦味が心地よかった。頭がはっきりとする。ここに$Sはいる、と感じる"),
            # NOTE: 前の家族と違うギャップ、また知らない私、妙に気遣う家族、違う私
            )

def sc_newschool(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    asano, ochi, haru = w.asano, w.ochi, w.haru
    yamane = w.yamane
    return w.scene("違う学校",
            h.be(w.stage.classroom),
            h.deal("違う学校に知らない教室。清潔感漂う校舎"),
            h.deal("隣に座る眼鏡の女性。$n_yamane。どうやらよく一緒にいる友達らしい"),
            h.deal("休み時間になり、彼女は本を開いていた。花柄のブックカバーだったが、内容はライト文芸だ"),
            h.deal("彼女は$Sが普段と違うと指摘する"),
            h.deal("そして彼女からかつて不登校だったと聞く"),
            # NOTE: 違う学校に違うクラス、違う制服、女子校
            )

def sc_samehim(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    asano, ochi, haru = w.asano, w.ochi, w.haru
    return w.scene("同じ彼",
            h.be(w.stage.restaurant1),
            h.deal("彼だけは同じ人"),
            h.deal("違う制服姿の$Sを見ても何も驚かない。彼だけが同じ対応だった"),
            h.deal("ただ距離感が違う。徐々に離れていくそれを感じる"),
            haru.talk("どうかしたかい？"),
            # NOTE: 彼の前だけ同じ私、それが安寧、好きということ、でも彼はそろそろ別れたそう
            )

def sc_alonenight(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    asano, ochi, haru = w.asano, w.ochi, w.haru
    return w.scene("一人の夜",
            h.be(w.stage.myroom),
            h.deal("帰ってきて一人。ベッドの上で考え込む"),
            h.think("昨日の記憶はある。思い出もある。でも$Sが分からない"),
            h.think("$Sはどこにるのだろう。まだ昨日に置き去りなんだろうか。それ以前の$Sはどこだ"),
            h.think("そもそも$Sって何だ"),
            h.look("SNSを見る。そこには$Sがいる。知らない$S。フォロワーにからかわれたり、かわいいと言われる$S"),
            h.look("そこに後ろ姿をアップしてみる。$Sはここにいるんだろうか"),
            h.deal("沢山のいいねが集まり、眠ってしまう"),
            # NOTE: 好きな曲をききながら考え込む、わたしって何、わたしの在り処を知りたい
            )

def sc_everydayme(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    asano, ochi, haru = w.asano, w.ochi, w.haru
    return w.scene("毎日違うわたし",
            h.deal("それからも目覚める度に$Sは$Sを探した。",
                "部屋は同じように見えたが何か常に違和感が支配的だ"),
            h.deal("毎日目覚める度に自分を確認する。部屋を確認する。ちょっとした違いがあったけれど、どれも$Sだった"),
            h.think("$Sって何だろう"),
            h.deal("彼に抱き締められているその時だけが確かな$Sみたいで安心できた。",
                "けれど彼は徐々に距離を取り始めていた"),
            # NOTE: 目覚める度にわたしを探す、その日々の中、彼だけがわたしを安定させてくれていた
            )

def sc_brokenme(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    asano, ochi, haru = w.asano, w.ochi, w.haru
    return w.scene("破壊されるわたし",
            h.deal("目覚めたら彼からメールが入っていた。それも長文だ"),
            h.deal("$Sは自分を確認するよりも早くその文面に目を通した"),
            h.think("概要はこうだ"),
            h.deal("ほんの親切心で町の片隅で拾った$Sとつきあい始め",
                "当初こそ楽しく思ったがそれはただ自分が学生時代に得られなかったものを手にしているというだけのもので",
                "制服を脱いだ$Sには何もときめきがなかったということ"),
            h.deal("その文面を読み終えて",
                "$Sは$Sを見失ったことを理解した"),
            h.deal("ドアが叩かれる。でも反応する気力がない"),
            h.deal("こうして$Sは不登校になった"),
            # NOTE: わたしは壊れた、彼がいなくなった
            )

def sc_lostme(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    asano, ochi, haru = w.asano, w.ochi, w.haru
    return w.scene("わたしはどこにもいない",
            h.deal("学校に行かず、日中はほとんど寝て過ごし、昼過ぎから起き出してSNSに顔を出す。そんな毎日"),
            h.deal("そんな日々を続けていたある日の朝、スマホが鳴った"),
            # NOTE: 自分を見失い、意識も心も漂う
            )

def sc_oldfriend(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    asano, ochi, haru, akimoto = w.asano, w.ochi, w.haru, w.akimoto
    return w.scene("SNSの幼馴染",
            h.deal("SNSで最近フォローがあった、中学時代の友達らしい"),
            h.deal("その彼から連絡。覚えているかと"),
            h.deal("かつてアップした後ろ姿で気づいたらしい"),
            h.deal("小学校からずっと一緒で中学卒業の時には告白まがいの手紙を渡してくれたそうだ。そんなものはどこにも見つからなかった"),
            akimoto.talk("$mioって……今不登校？"),
            h.deal("彼も同じだった"),
            # NOTE: SNSで幼馴染が声をかけてくれる、小さな頃のわたし、
            )

def sc_meetfriend(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    asano, ochi, haru, akimoto = w.asano, w.ochi, w.haru, w.akimoto
    return w.scene("幼馴染との再会",
            h.be(w.stage.station, w.day.datefriend),
            h.deal("駅前で待ち合わせて、出会った"),
            # NOTE: 幼馴染の外見
            h.deal("話しているうちに徐々に$Sが形成される"),
            h.deal("過去と思い出。それが$Sを支えてくれていたんじゃないかと気づく"),
            h.deal("傷跡を抉る旅に出る。昔通っっていた中学や小学校、保育園。児童館"),
            h.deal("それから事故みたいな初キス"),
            h.deal("その翌日、彼が亡くなったことを知った"),
            # NOTE: 再会し、わたしを取り戻す、わたしの在り処の鍵を知る
            )

def sc_findme(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    asano, ochi, haru, akimoto = w.asano, w.ochi, w.haru, w.akimoto
    return w.scene("わたしを見つけた",
            h.deal("$Sはどこにもいなくなった"),
            h.deal("目覚める度に消える$S"),
            h.deal("SNSの中だけが居場所のように思えたのに",
                "アカウントが乗っ取られた。でも誰も気づかない。そのまま$Sとして接する人たち"),
            h.deal("走り出す"),
            h.deal("酷い雨の中"),
            h.deal("車が停まる。彼だった"),
            # NOTE: 色々なところに自分の面影を見つける
            )

def sc_mytruth(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    asano, ochi, haru, akimoto = w.asano, w.ochi, w.haru, w.akimoto
    return w.scene("真実",
            h.deal("彼と話す。最後の会話"),
            h.deal("彼は転勤になる。もう助けてやれないとはっきり言われる"),
            h.deal("自分の在り処は自分で見つけるしかない。どこにもあるし、どこにもない"),
            h.deal("彼は最後のキスをしてくれる。それが必要なら、その相手を探せと言われて"),
            )

def sc_me(w: wd.World):
    h = mio = w.mio
    mam, dad, bro = w.mam, w.dad, w.bro
    asano, ochi, haru, akimoto = w.asano, w.ochi, w.haru, w.akimoto
    return w.scene("わたし",
            h.deal("歩いて帰る"),
            h.deal("沢山の人がいる"),
            h.deal("誰もが自分を分かっているのだろうか"),
            h.deal("$Sは$Sが分からない"),
            h.deal("泣いてる。泣き声が聞こえる"),
            h.deal("それは迷子だった。女の子。彼女を連れて歩く。行く宛てもなく"),
            h.deal("彼女は迷子ではなく、家出娘だった。原因は些細なことだ。でも家には帰りたくない。自分の居場所がないから"),
            h.deal("二人で公園に泊まろうとする。でも母親が迎えに来てしまう。警察に連れて行かれた"),
            h.deal("交番に母が迎えに来る"),
            h.deal("家に帰る。何も言われない"),
            h.deal("玄関に入る前に一言だけ。ごめんお母さん。$Sが見つからなかった"),
            h.deal("わたしなんて外に探しに行くもんじゃないでしょ？　と小突かれる"),
            h.deal("部屋に帰ってくると$Sがいた。$Sが待っていた。姿見に$Sがいた。ずっと気づかなかった。$Sはずっと$Sだ"),
            h.deal("それに気づいてやっと、$Sは$Sを取り戻した"),
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
            )

def ep_notme(w: wd.World):
    return (w.chaptertitle("わたしで無いわたし"),
            sc_myfriend(w),
            sc_herboyfriend(w),
            sc_sleeping(w),
            sc_awake2day(w),
            sc_unknownfamily(w),
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
            sc_mytruth(w),
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

