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
            h.look("――会社帰りに寄るから映画でも見に行こう"),
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
                "勉強よりもバスケをしていたいという彼は"),
            # TODO
            h.deal("母親が食べていたのと同じ天ぷらを皿に移した時に声が"),
            # NOTE: 父の描写
            # NOTE: 弟の描写
            # NOTE: 家族の中の自分
            mam.talk("あれ？　あんたそれ食べたっけ？"),
            h.deal("どうやら$Sはオクラを食べられないらしい"),
            # NOTE: 朝食、知らない家族、知らない自分、高校生？　二学期
            )

def sc_myschool(w: wd.World):
    h = mio = w.mio
    asano = w.asano
    return w.scene("わたしの学校",
            h.be(w.stage.street1),
            h.deal("通学路を歩く。",
                "スマホで場所は調べた。",
                "周りを歩く同じ制服姿に安堵する"),
            h.deal("SNSを見て、そこにも自分を見つける"),
            h.deal("LINEで友達から連絡。返すと後ろから走ってきて、腕を掴まれる"),
            asano.talk("おーはよ、$mio"),
            # NOTE: くだけた自分、麻乃とのおしゃべり、楽しい？
            h.be(w.stage.school),
            h.deal("三階建ての校舎。グラウンドで朝練する子たち。その一人が何故か睨みつけていく"),
            # NOTE: 学校の自分
            h.be(w.stage.classroom),
            h.deal("席を当然間違えて座るって注意された"),
            h.deal("覚えのない顔ばかりで落ち着かない。ただ$asanoが同じクラスでよかった"),
            h.deal("そして授業が始まる"),
            # NOTE: 登校、知らない道、学校、教室も知らず、友達に声かけられ
            )

def sc_myfriend(w: wd.World):
    h = mio = w.mio
    asano, ochi = w.asano, w.ochi
    return w.scene("わたしのともだち",
            h.be(w.stage.classroom),
            h.deal("休み時間になり、文庫本を開く。それはいつかの自分が読みかけだったものみたいで、前半十数ページで止まったまま。何か思い出せるだろうかと読みふける"),
            # NOTE: 本の内容少し
            h.deal("見ると廊下側で$Sを睨んでいる女子生徒がいた。",
                "立ち上がったがチャイムが鳴り、先生が入ってくる。",
                "あれは確か今朝走っていた部活の生徒で自分を睨んだ子だ"),
            # NOTE: 友達の前の自分
            h.deal("放課後、やっと解放された。",
                "でも$Sはどこにも見つけられない。ふわふわとしたまま一日を過ごした"),
            asano.talk("どっか寄ってく？"),
            mio.talk("ううん。今日は"),
            asano.talk("ああ。またアイツ？　いい加減にしといた方がいいわよ"),
            h.deal("彼と付き合い始めてから雰囲気が変わった、と$asanoに言われた。",
                "自覚ないどころか、何も覚えていないのだ。それは本当に$Sなのだろうか"),
            # NOTE: 友人、自分をよく知る、いつもと違う、雰囲気変わったって
            )

def sc_herboyfriend(w: wd.World):
    h = mio = w.mio
    haru = w.haru
    return w.scene("わたしの彼氏",
            h.be(w.stage.street1),
            h.deal("LINEで待ち合わせ場所を指定され、そこで待っていると車が停まる"),
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
            sc_myfriend(w),
            sc_herboyfriend(w),
            )

def ep_notme(w: wd.World):
    return (w.chaptertitle("わたしで無いわたし"),
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

