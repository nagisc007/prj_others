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
        "Re: 教会なう",# NOTE:再び教会も、世界がループしていると認識
        "旅支度なう・その１",# NOTE: 旅って何が必要？まずは金策だ！
        "勇チューバーなう",# NOTE:yutuberだ
        "旅支度なう・その２",# NOTE: ランキングサイトを使って安く買え？
        "スライムなう",# NOTE:初戦闘、スライムに苦しむ
        "はじめてのおつかいなう",# NOTE:初クエスト
        "洞窟なう",# NOTE:洞窟内で
        "野営なう",# NOTE:野宿編１から
        ]

# scenes
## ep14 scene
def sc_awaking(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    return w.scene("再びの目覚め",
            h.be(w.stage.church1, w.day.awake2),
            h.look("$Sである少年は冷たい床の感触と共に目覚めた"),
            h.think("彼は突如現れた大魔王により派遣された大量のモンスターの群れによって絶命した"),
            h.think("そのはずだった。", "しかし目を開けてみれば自分の手も足も体も",
                "それに頭の方もどうにか無事のようだ"),
            h.look("高い木造の建物の天井には", "見覚えがあった"),
            yula.talk("気が付かれましたか？"),
            h.hear("女性の声だ"),
            h.look("声のした方に顔を向けると", "自分を見下ろすようにして",
                "いつも神父が着ている紺のローブを羽織った女が立っているのが分かった。",
                "耳が隠れる程度のふわりとした金髪と笑みを浮かべた口に微かに見える八重歯が印象的なその女性は",
                "$Sが以前ここで目覚めた時にも神父の代理をしていたという彼女だ。",
                "確か名前は……"),
            yusha.ask("あんた$yulaとか言ったっけ？"),
            yula.talk("え！？", "なぜ$meの名を知っているの？"),
            h.look("一度会ったはずなのに目を大きくして不自然なくらいに彼女は驚いた"),
            yusha.talk("いや", "前にあんたから教わったんだよ。",
                "確か", "$n_priest1神父が旅行中だからって代理をしているんだろ？"),
            h.look("彼女は上半身を起こして笑った$Sを",
                "不思議なものを見るような目で見る"),
            h.look("彼が改めて周囲を確認すると",
                "確かにいつも遊びに来る教会だった。",
                "高い天井", "ところどころに補修の跡が見える板張りの壁",
                "窓に誂えた申し訳程度のステンドグラスが色鮮やかな光を取り込んでいる。",
                "そういえばあれだけのモンスターの進軍を受けながら",
                "大きな穴が空いたりはしていないようだ"),
            yusha.talk("あんたは大魔王の軍勢に襲われなかったのか？"),
            h.look("意味が理解できなかったのか彼女は何も答えず",
                "ただ懐疑的な視線を$Sに向けたままにしている"),
            yusha.talk("そうか。",
                "外に出ずにここに避難していた訳か。",
                "ここなら聖なる力によって建物が守ってくれたのかも知れないな"),
            yula.talk("あなたが何を言っているかよく分からないけど",
                "魔王の軍勢も攻めてきていないし",
                "外に出たって別に死屍累々とかではないし",
                "何よりこの教会にそんな特別な力なんてないわよ。",
                "使われているのだってただの安物の木ばかりだし"),
            h.think("どういうことなんだ。",
                "$Sは自問する"),
            h.think("まさか夢でも見ていたのだろうか"),
            h.deal("そう思って慌てて傍にあった自分のズタ袋の中身を確認する"),
            h.deal("金も$yumarkもない。",
                "ただ辛うじて$phoneだけは無事だった"),
            h.look("$Sはその黒い魔法の板に触れ",
                "状況を確認する"),
            h.explain("$phoneとは不思議な鉱石で造られた道具で",
                "これを持っている者同士ならどんな遠隔地であっても文章や画像のやり取りが可能という優れものだった"),
            yusha.talk("どこにも大魔王が現れたとか……ないな"),
            yula.ask("大魔王？", "魔王じゃなくて？"),
            yusha.talk("いやだからさ", "魔王は$meが退治してその代わりに大魔王が出現したんだ"),
            h.look("彼女は明らかに頭のおかしい人を見る目を$Sに向けていた"),
            yula.talk("とにかく神のご加護を"),
            h.deal("そう言ってさっさと追い返してしまおうとしている"),
            yusha.talk("本当に大魔王を……"),
            yula.talk("そんなものがホントにいるのなら", "もうこの世界って絶望じゃないんですか？"),
            h.look("いい加減にして下さい。",
                    "そんな目できつく睨まれ",
                    "$Sは渋々立ち上がり", "彼女に背を向ける"),
            h.move("だが教会を出ようと歩き出したところで立ち止まり", "$Sは彼女を振り返った"),
            yusha.talk("なああんた。", "もし神官や僧侶のような治癒魔法を習得しているなら一緒に旅をしないか。どうも魔王退治の前にこの世界のことをよく知らなきゃいけないみたいなんだわ"),
            yula.talk("何それ。", "新しいナンパかしら？"),
            h.look("やっと少し表情が柔らかくなった$yulaに「本気だ」と答えると",
                    "彼女は大きく首を横に振ってこう答えた"),
            yula.talk("残念ながら$meにそういった技能はないわ。",
                    "精々がここにいてあなたの悩みごとを聞いてあげられるくらいね。",
                    "ごめんなさい"),
            yusha.talk("そうか。", "まあ……何かあったらまた頼む"),
            h.think("それでも近いうちに再会しそうだという予感を抱きながら",
                "$Sは教会を出た"),
            )

def sc_reunion(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("仲間との再会",
            w.tag.symbol("◆"),
            h.think("教会を出た$Sは","とりあえず仲間だな",
                "と考えたが",
                "酒場に行ってもまともに冒険もしたことない未成年についてきてくれる傭兵はいないことを彼は既に知っている"),
            yusha.talk("こんな$meでも仲間として扱ってくれそうな奴か……"),
            h.think("あ……"),
            h.deal("咄嗟に浮かんだのは赤い頭とピンクの頭だ。",
                "$Sはまず空腹で漂っているであろう赤い方から探しに向かった"),
            yusha.talk("前は確か夕方だったっけ……"),
            h.look("時間帯こそ違うが",
                "レンガ造りの住居が並び", "その家々から賑やかな声が漏れ聞こえる路地にやってくる"),
            h.look("脇道から一匹の白黒まだらの猫が飛び出してきたが",
                "その口には魚の干物を咥えている。", "相変わらず食い意地が張った迷い猫だと思って去っていった方向を見やると",
                "お腹を擦りながらよく目立つ赤髪の長身の男がちょうどこっちに向かって歩いてくる"),
            yusha.talk("よう$sol"),
            sol.talk("あん？", "誰だおめぇ……"),
            h.think("やはり$Sのことは忘れてしまっているらしい。",
                "それとも自分の記憶がおかしいのだろうか"),
            yusha.talk("覚えてないんだな？"),
            sol.talk("知らねえよ。", "だいたいこの町には初めて来たんだ。",
                "畑仕事や大工仕事の手伝いばっかじゃなく", "戦士として城で使ってもらう為にな！"),
            yusha.talk("それは無理じゃないかな。", "ここの騎士団はよそ者に厳しいことで有名だし。",
                "それより飯を食べさせてやるから", "ちょっと相談に乗ってくれないか？"),
            sol.talk("$meがそんな飯ごときで釣られるとでも……"),
            yusha.talk("今晩の寝床と明日の朝食付き"),
            sol.talk("分かった。", "で何だ相談て？"),
            w.tag.symbol("◆"),
            h.deal("$Sは$solを仲間に引き入れると続いてピンク髪の少女を探す"),
            h.think("前は勝手に自宅に訪ねてきたが", "どこに行けば会えるだろうか。",
                "そう思っていた矢先", "彼の$phoneに通知が入った"),
            h.look().emphasis("アカウントがフォローされました"),
            h.explain("アカウントとは彼の$phone上の住所みたいなものだが",
                "どうやら別のアカウントと繋がったらしい"),
            h.look("よく見ると$makoだった。",
                "$n_yusha様が赤い頭の男と歩いているとか",
                "なんかよく分からない実況を呟いていた。",
                "明らかに至近距離にいる"),
            yusha.talk("おい？　いるんだろ？　出てこいよ"),
            h.look("彼が声を掛けると彼女は驚いた様子で物陰から姿を見せる。",
                "ピンクのおかっぱ頭と背の低い幼い顔つき体つきは", "一見すると幼女にも見えた"),
            mako.talk("あの", "フォローせずに見守るつもりだったんですけど",
                "どうしても我慢しきれなくてついフォローしちゃいました。",
                "怒ってますか？"),
            yusha.talk("$meのこと覚えてるのか！？"),
            h.look("彼女は小首を傾げている"),
            yusha.talk("いやだから……"),
            h.deal("彼は小声で彼女に耳打ちをした。",
                "自分が$Sと知っているのかと"),
            mako.talk("ええ。",
                "$taroのことなら何でも知っていますよ。",
                "だって婚約した仲だから……あ、これ言っちゃいけなかった"),
            h.think("なんか不穏な記憶が呼び覚まされそうになったが",
                "その$Sの頭を彼女は思い切り手にした$phoneで殴りつけた"),
            mako.talk("もうやだ$taroったら！"),
            h.think("何故殴られたのか分からないまま",
                "とにかく今一度魔王退治の旅に付き合ってくれるのか尋ねると二つ返事で了承した"),
            h.deal("こうして$Sは頼りない赤頭の戦士と頭のおかしいピンクおかっぱの少女と共に",
                "この世界を知る旅に出る決意をしたのであった"),
            )
## ep15 scenes
def sc_gotoshop(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("質屋に行こう",
            h.be(w.stage.hometown, w.day.awake2),
            h.look("$Sたち一行は城下町の中央広場前へとやってきた。",
                "そこには市が開かれていて",
                "建国のモニュメントの周囲を取り囲むようにして露店がひしめいている"),
            yusha.talk("いざ魔王退治の旅に出ようと言っても何を準備しておけばいいか",
                "全然考えてなかったわ"),
            h.look("$Sである少年は仲間となった赤髪の長身の男$solとピンク髪のおかっぱの少女$n_makoと共に",
                "旅支度の買い物に訪れたのだ"),
            sol.talk("だからよぉ",
                "旅のことなら$meに任せろって。",
                "山奥の田舎町を出てきてもう一年以上職探しの旅を続けてるんだ。",
                "言うなれば旅のエスパーってやつだぜ！"),
            mako.talk("エキスパートだよね", "たぶん"),
            sol.talk("こまけぇこたぁいいんだよ！", "な、$yusha。",
                "とりあえずは食べ物と飲み物と地図だ。", "次の町まで何日かかるのかを知ることが何より重要だかんな！"),
            h.look("にこにこと笑みを浮かべて果物や生鮮品が並ぶ露店に向かう$solの背を見送り",
                "$n_makoは隣にいた$Sの袖を引っ張った"),
            mako.talk("旅に出るのに生物買おうってバカは放っておくとして",
                "$taro", "特に用意していかなくてもすぐに$st_amazonでお取り寄せできますよ？"),
            h.look("そう言って彼女は自分の持っていた$phoneを見せる"),
            h.explain("$phoneとは不思議な鉱石で造られた板状の魔法の道具で",
                "同じものを持つ者同士", "どんなに離れた場所でも文章や画像のやり取りが可能という代物なのだが",
                "それを使って利用できる$st_amazonでは",
                "そこに表示される商品の画像を選んで注文すると即座にそれが届けられるという",
                "魔法使いも顔負けのサービスが提供されていた"),
            yusha.talk("$st_amazon……！？"),
            mako.ask("どうかしたんですか？"),
            h.think("$Sには$st_amazonにまつわる不穏な記憶があった"),
            yusha.talk("い、いや", "$st_amazonは使わないでおこう。",
                "$Sたるものなるべく自力で何とかしたい"),
            h.look("便利なのに", "と漏らした$n_makoを置いて",
                "$Sも露店を覗きに向かう"),
            h.look("魔王とその手下のモンスターたちによって平和が脅かされているというのに",
                "果物や野菜", "魚に家畜の肉", "それらを使った手作りの惣菜と",
                "食べるものは豊富に並べられていた。",
                "少し歩けば向こうでは屋台で焼いた小麦粉で果実のジャムを包んだお菓子を売っていた"),
            yusha.talk("旨そうだな……一つ"),
            h.look("欲しい", "と喉まで出かかったが",
                "三百Ｇ《$i_yen》という価格を見て", "すぐに前を立ち去る"),
            mako.ask("食べないんですか？"),
            h.look("いつの間に後ろにやってきたのだろう。",
                "背中を突いて", "$n_makoが言った"),
            yusha.talk("金が無いんだ"),
            mako.talk("借りればいいじゃないの"),
            yusha.talk("ハァ？",
                "どこに後ろ盾もないただの未成年に大金貸してくれるところがあるんだよ……"),
            mako.talk("じゃあ$meが$taroに貸しますよ。",
                "半永久的に無利子で。",
                "ただ……今すぐ結婚してくれたらっていう条件付きですけど"),
            h.look("$Sは彼女の戯言を無視して金物の店を覗いていた$solに声を掛ける"),
            yusha.talk("おーい$sol", "金持ってないか？"),
            sol.talk("昼飯買う金もねえよ。",
                    "てか", "嬢ちゃんあっちで泣いてるけどいいのかほっといて？"),
            h.look("言われて振り返ると",
                    "道の中央で$n_makoが蹲っている。",
                    "その周りを通行人が取り囲み「誰かこの子のお母さん」と呼びかけている"),
            yusha.talk("行った方がいいと思うか", "なあ$sol？"),
            sol.talk("明らかに何度もちらちらこっち見てるだろ……"),
            yusha.talk("お、おう……"),
            )

def sc_gathermoney(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("動画やろうぜ",
            h.move("$n_makoを連れ出して青空市を離れた$Sたちは",
                    "一旦彼の部屋で今後どうするかの作戦会議を開くことにした"),
            sol.talk("とにかくさ",
                "金ってのは地道に稼ぐしかねえんだよ。",
                "何か仕事探すべ"),
            h.look("ベッドの上にどっかりと腰を下ろした$solは$Sが持ってきた水を一気の飲み干して答える。",
                "そのまま「もう一杯」とばかりにコップを差し出したが",
                "$Sは無視して$n_makoに意見を求めた"),
            mako.talk("まずはお金を稼がないといけないってことですか？",
                "だったら……コレなんてどうです？"),
            h.look("彼女が見せてくれたのは$phoneを使って大金を稼ぐ方法という実に怪しげなものだった"),
            yusha.talk("コレで", "稼げるの？", "ホントに？"),
            h.look("そこに書かれているものを見て",
                "半信半疑なのは$Sだけではなかった"),
            sol.talk("君も商品を紹介して小遣い稼ぎ……だと？"),
            h.look("$solは顔を歪めていたが", "それでも本気にしたのか",
                "そこに表示された幾つかの道具をじっと見つめている"),
            yusha.talk("先に購入しないと紹介できないってさ"),
            sol.talk("何だよ！", "$meに喧嘩売ってんのか！"),
            h.deal("他にもポイントサイトというものに登録してアンケートに答えたり",
                "商品を安く仕入れて$st_freemaなどで転売するなど",
                "いくつか金を稼ぐ方法が書かれていたが",
                "どれもそれなりに元手が必要だったり",
                "すぐお金が手に入るようになっていなかったりと",
                "今の$Sたちにとっては難しいものばかりだ"),
            sol.talk("おい……コレなんか意外とイケるんじゃね？"),
            h.deal("$solが見つけたのは$doga投稿というやつだった"),
            h.explain("$dogaとは動く絵のことだ。",
                "$phoneを使えば見たままを静止画として切り取るだけでなく",
                "それを連続した$dogaにすることも可能だった"),
            yusha.talk("君も$yutuberで大儲けか……これなら$meらでもできそうだな！"),
            mako.talk("そんな簡単に稼げるものじゃないと思うんですけど", "この手のって"),
            sol.talk("いいからいいから。",
                "なんか面白けりゃあ儲かるって書いてあるじゃねえか。",
                "面白いのなら得意だろ？", "なあ"),
            h.look("だが$Sには$solの言葉は耳に入っていなかった。",
                "既に金儲けのことは彼の頭になく",
                "ただ人気者になれるかも知れないというその一点のみが",
                "今の彼の心中で強烈な輝きを放っていたのだ"),
            h.deal("そして部屋は片付けられ",
                "撮影の準備が整えられた"),
            sol.talk("いいか", "最初は『はいどうも』からだ。", "分かったな$yusha？"),
            yusha.talk("はいどうも……だな。", "よし"),
            h.look("ノリノリの$solと$Sを横目に", "撮影係となった$n_makoは不安な様子のまま$phoneをベッドの前に立つ$Sに向けている"),
            sol.talk("よし。",
                "それじゃあ行ってみよか！"),
            h.look("$solの目線を受けて$n_makoは小さく頷いた。", "そして撮影が開始された"),
            yusha.talk("はいどもー！"),
            sol.talk("もっとテンション高く！"),
            yusha.talk("は、はは、はーいどもー！！"),
            )

## ep16 scenes
def sc_yutuber(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("勇チューバーでいこう",
            h.be(w.stage.bedroom, w.day.awake2),
            yusha.talk("はーいどもー！！", "$n_yushaと申しますー！",
                "この度は$dogaというものをしてみんとす", "と題して色々なことにチャレンジしてみたいと思います！"),
            h.look("$Sである少年は", "自室で必死に笑顔を作って大きな身振り手振りを交えて自己紹介をしていた"),
            h.look("その様子を部屋の入口に近い場所に立ち", "赤髪の長身の男$solが腰に手をやって見ている。",
                "更にその隣では黒い板状の$phoneと呼ばれる道具を$Sに向け",
                "その様子を$dogaとして収めているピンクのおかっぱ頭の小柄な少女", "$n_makoがいた"),
            yusha.talk("えーっと……"),
            sol.talk("金儲けしたいからみんな見てくれって言って"),
            h.deal("$solの指示を受け",
                "視線が落ち着かない挙動不審者のままで$Sは続ける"),
            yusha.talk("$meたちは魔王退治の旅に出ようと思ったんだけど",
                "金が全くないってことに気づいたんだ。",
                "だから手っ取り早く稼ぐ方法を探していたら",
                "$yutuberやれば？",
                "って話になって",
                "今こうして$dogaやってる訳。",
                "ど、どうだい？",
                "みんな$meに金を稼がせてくれるかなー？"),
            h.deal("耳に手を当てて声援の一つでも聞こうという身振りを見せるが",
                "その様を撮影していた$n_makoは小さく首を振り",
                "音がしないように溜息をついた"),
            yusha.talk("えーそれではまず",
                "$i_mentosgeyserいきます！"),
            sol.talk("おい段取り！"),
            yusha.talk("え？"),
            sol.talk("普通の$healdrink飲んでまずいつってから",
                "$drag_mentosいれたらどうなるかって前フリ！"),
            h.deal("普段は抜けたところがありいい加減に見えるのに",
                "この時ばかりは何故か$solは必死に$Sに指導していた。",
                "ひょっとすると金が掛かると顔色が変わるタイプなのかも知れない"),
            yusha.talk("え、えと……まずは普通に$healdrink飲みます"),
            h.deal("机の上には濃い緑色の液体が入ったガラス瓶が置かれていた。",
                "$Sがそれを手に取り蓋を開けると", "シュワシュワと炭酸が小さな音を立てる。",
                "その瓶の口をゆっくりと近づけていって一口飲むと",
                "$Sの顔が渋面に変わった"),
            yusha.talk("ゲホッゲホッ……$meって炭酸ダメなんだよ"),
            sol.talk("じゃあ何でコレやろうっつったんだよ……"),
            yusha.talk("いや", "みんな最初はやるもんだって書いてあったし"),
            sol.talk("だから苦手なら最初に言っとけよ！"),
            h.look("$solは我慢し切れずにテーブルまで出ていって",
                "$Sに文句をつけている。",
                "その様に特大の溜息を零した$n_makoは「ねえ」と声を上げて二人の会話を止めた"),
            mako.talk("あとから編集大変になるからさ", "ちょっと$sol", "黙っててくれない？",
                "それに$taroもおどおどせずに台本は読んだんでしょ？",
                "その通りにきちっとやって下さい。",
                "多少言い間違えても後で編集して何とかするから",
                "とにかくやるべきことをきっちりこなして下さいよ。", "いいですか？"),
            yusha.talk("はい……"),
            sol.talk("おう……"),
            h.look("二人ともが小さい声で頷いたところで", "仕切り直される"),
            yusha.talk("えっと", "このように普通に飲むだけだとシュワシュワとした炭酸が楽しめるのですが",
                    "ここにこの$drag_mentosを入れるとどうなるか", "見てみましょう"),
            h.deal("$Sが手にしたのは小さな白い粒状のお菓子だ。",
                    "$drag_mentosという名で売られている少しスパイシィな味わいのキャンディは",
                    "$healdrinkと混ぜると大変危険だとして有名だった"),
            yusha.talk("それじゃあ……入れてみます。", "ど、どど", "どうなるかな？",
                    "ドッキドキですね"),
            sol.talk("……かてぇよ"),
            h.look("つい小声でぼやいてしまう$solを$n_makoは睨みつけると",
                    "$Sが慎重に瓶の口に$drag_mentosを近づける様子を撮影していく"),
            h.look("彼が摘んでいる白い粒を離すと",
                    "それがゆっくりと緑色をした瓶に落ちていき",
                    "その液体の中に沈んでいこうとしたまさにその時だった"),
            yusha.talk("うおぉぉぉ！！！"),
            h.deal("一気に中の液体が緑色の雲にでもなったみたいに細かな泡の柱となって天井まで吹き上がった"),
            yusha.talk("おい！", "これどうすれば止まるんだよ！"),
            h.look("見ている間にも間欠泉のようなそれは天井を濡らし", "部屋中を緑の泡塗れにしてしまう"),
            yusha.talk("それにくっせ！", "$healdrink臭いよ！"),
            )

def sc_nothingmoney(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("儲からない！",
            w.tag.symbol("◆"),
            h.look("あの後で母親に叱られつつも部屋を掃除したり", "大変な目に遭ったが",
                "その甲斐あってか", "何とか最初の$dogaを上げることができた"),
            h.deal("しかし現実とは厳しいものである。",
                "お金を稼ぐどころか", "視聴数は一桁という酷い有様で",
                "$Sたちの$dogaを作る気そのものを根こそぎ刈り取ってしまった"),
            h.think("それでも一度でやめる訳にはいかないと何度か様々な方向から$dogaにチャレンジしてみたのだが",
                "部屋や服が汚れる以外の収穫はなかった"),
            yusha.talk("そうだよ……"),
            h.deal("そしてある日", "$Sは気づいた"),
            yusha.talk("こんなことをしてる場合じゃなーい！",
                "$meたちは魔王退治の旅に出る為の準備をしようとしていたのに",
                "何故こんなことになっているんだ？"),
            h.look("やっと気づいたのか", "という目線を$n_makoは二人の能天気な男子に向けている"),
            sol.talk("いや元々$yushaが言い出したんだろ？", "旅支度する金がないとかって"),
            yusha.talk("でも$yutuberやろうっていうのは$solだろ？"),
            sol.talk("$meは比較的楽に稼げそうなやつを探しててだな……"),
            mako.talk("ああもう！",
                "それじゃあ$meが魔王退治の旅のスポンサーになってあげるから",
                "お金のことはそれで解決してよ！"),
            h.look("取っ組み合いを始めそうな二人の間に割って入った$n_makoにそう言われたが",
                "二人とも「スポンサーって何だ？」という表情で彼女を見ている"),
            mako.talk("あのね。",
                "スポンサーっていうのは君たちがやることに対して興味があるから支援してお金を出してあげようという",
                "お金持ちのことよ"),
            sol.talk("嬢ちゃんそんな金持ちなのか？"),
            mako.talk("金持ちというか……国をどうこうするくらい朝飯前的な？"),
            h.look("今度は奇異な目を男子二人が彼女に向ける番だった"),
            sol.talk("嬢ちゃんも冗談って言うんだな", "ハハハハ"),
            yusha.talk("そんな無理しなくても$meたちで旅費くらい何とかするって。",
                "だからそのスポンサーだなんだってのはやんなくていいよ"),
            mako.talk("ぼ、$meはね", "ホントに……！"),
            h.look("何か言おうとした$n_makoに背を向けて",
                "$Sと$solは二人で肩を寄せ合って「でもどうする。いざ金儲けるっても大変だぞ」などと内緒話を始めていた"),
            mako.talk("……ホントなのに"),
            h.look("一人仲間はずれにされた疎外感の中",
                "$n_makoは自分の$phoneで自宅の一部の画像を呼び出した。",
                "それは薄暗い石造りの地下室の一画を写したもののようだったが",
                "そんな中でも鈍く光る金塊が山となっている様を確認することが出来たのだった"),
            )

## ep17 scenes
def sc_letsbuying(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("さて買い物だ",
            h.be(w.stage.hometown, w.day.buying),
            yusha.talk("今", "帰ったぜ"),
            h.look("自宅の玄関のドアを開けた少年の顔は泥で汚れ",
                "一週間前には貧相に見えた体つきも多少筋肉質になっているようにその少女の目には映った"),
            mako.talk("お勤め", "ご苦労様です。", "$taro"),
            h.look("丁寧に頭を下げた彼女を見て", "$Sである彼は満足そうに頷くと",
                "そのまま膝から崩れて倒れてしまう"),
            mako.talk("$taro？", "大丈夫ですか！？", "$taro！！"),
            sol.talk("ん？　どうした？"),
            h.deal("そこに斧を担いで現れた赤髪の巨漢は倒れた$Sの背を揺する少女を見て",
                "よく分からないまま適当な笑顔を浮かべて小首を傾げた"),
            w.tag.symbol("◆"),
            yusha.talk("ああ……マジで死ぬかと思った"),
            sol.talk("高々一週間程度働き詰めだったからって", "何もぶっ倒れるこたぁねえだろうよ", "$yusha"),
            h.deal("赤髪の男$solに言われながら",
                "$n_makoに濡らした布を額に当ててもらっている$Sは", "信じられない", "という目線を返して答える"),
            yusha.talk("いやいや。", "今まで買い物と遊びに行く以外の外出すらしたことなかった$meが材木運んだり土嚢を積んだりしたんだぞ？",
                "魔王退治よりよっぽど大変だって！"),
            h.think("それは言い過ぎです", "と小声で呟いて",
                "彼女は$Sの顔面に濡れた布を置いて立ち上がる"),
            h.deal("$Sと$solが地道に肉体労働をして何とか一万Ｇを稼ぎ出し",
                "これでやっと旅支度が整えられる", "と三人で安堵していたところだった"),
            h.move("少し落ちついてから軽くご飯を食べると",
                "三人は商店街に足を運んだ"),
            h.look("城下町の商店街は中央から南側の通りに沿って広がっていて",
                "昼前ともなるとやはりかなりの人出がある。",
                "通りに沿って立ち並ぶ様々な看板を掲げる商店からは威勢の良い声が響き",
                "生きているという活気に満ちていた"),
            sol.talk("$yusha。", "ここは旅の先輩として$meが教えといてやる。",
                "地図だけはなるべく最新のものを手に入れるようにするんだ。",
                "もし地図が古くて道や印が間違っているようならとてもまずいことになりかねんからな"),
            h.deal("だが武器屋の店頭に飾られた$Sの身長の倍はある大振りの両手剣を眺めていた彼は",
                "「ふーん」という気のない返事を$solに投げただけで",
                "自分の考えを$n_makoに相談する"),
            yusha.talk("やっぱ野宿用に簡易のテント設備とかも欲しいよな。",
                "あ、でっかいリュックとかもいるのか。",
                "でも$meそんないっぱい荷物持てないよ"),
            mako.talk("別に全部運ばなくても$st_amazonで注文して持って来てもらえばいいんじゃないですか？"),
            sol.talk("いや。テントなんか買っても荷物になるだけだ。",
                "寝たいなら冬場でない限りは丈夫なシートでも敷けばそれで何とかなる"),
            h.deal("二人の間に割って入った$solの物言いに", "$n_makoは驚きの目を向けた"),
            mako.talk("あんたまさか$meに地べたで星空見ながら寝ろっていうの！？"),
            yusha.talk("まあでもそういうのが冒険の醍醐味ってやつじゃないか？"),
            h.look("その意見に「なあ」と納得したよう互いを見てに頷いた$Sと$solを",
                "信じられない", "という顔で$n_makoは見た"),
            mako.talk("いいわよ。",
                "$meだけは最新式の寝袋とテント備えるから"),
            h.move("自分で見るからもういい", "と小さな吐息を漏らし",
                "彼女は一人で行ってしまった"),
            sol.talk("嬢ちゃん何怒ってんだ？"),
            yusha.talk("さあ？"),
            h.look("互いの顔を見合わせる男子二人は",
                    "全く女ってやつはどうしてこう面倒なんだ",
                    "とでも言わんばかりだ"),
            h.look("そんな二人はまずアウトドア用品店を覗いた"),
            h.look("店に入るとまず立派な誂えの簡易テントが目に付く。",
                    "軽い素材で造られた支柱と丈夫に金属繊維を入れて編み込まれた布。",
                    "その組み合わせでの最新型だと十万、十五万Ｇ《$i_yen》という数字が並んでいた"),
            sol.talk("こりゃテントは無理だ。", "全員寝袋だな"),
            h.look("しかし寝袋も五千Ｇ台。",
                    "もう少し安いものもあったが",
                    "$solに言わせると安物はすぐ破れるそうだ"),
            sol.talk("ま、遠足にでも行く程度ならいいんだがな"),
            h.look("他にも野営に必要そうな小型の飯盒や鍋", "登山用のピッケルなどもある"),
            sol.talk("基本的にその時だけ必要なものは都度購入した方がいい"),
            h.look("$solはそう言って手に取った最新式のランタンを棚に戻した"),
            sol.talk("なるべく軽装の方が動きやすい。",
                    "何より沢山荷物があると機動性に欠ける。",
                    "寝込みをモンスターにでも襲われてみろ？",
                    "咄嗟に持って逃げられるだけの荷物にしておかないと大損こくぞ"),
            h.deal("店を出たところで$solは$Sに言い聞かせる"),
            sol.talk("実際旅で一番困るのが盗賊や山賊被害なんだ。",
                    "雪山で買ったばかりの寝袋ごと盗まれた時はマジで死ぬかと思ったぞ"),
            yusha.talk("それはお前がマヌケだっただけじゃないのか？"),
            sol.talk("おめぇは何も知らないなあ。",
                    "モンスターだって盗んでいくんだよ。",
                    "最近じゃ盗難被害の八割はモンスターだっつー話だぞ"),
            yusha.talk("何だって……"),
            h.look("続いて二人で見て回ったのは金物屋だ。", "$solが言うには万能ナイフが大事らしい"),
            sol.talk("戦う武器もそうだが", "旅ってのは色々と自作することになる。",
                    "そうすると万能ナイフ一本あれば簡単な調理までできていいんだよ"),
            yusha.talk("お前って……料理とかできたのか"),
            sol.talk("驚くとこソコかよ！"),
            h.look("だが多機能ナイフは結構高額商品になる。",
                    "武器も欲しかった$Sは「後回しにしようぜ」と購入を回避した"),
            h.deal("他にもロープや小型の鍋",
                    "着火装置などの細々としたものを見て回ったが",
                "一つ一つは少額でも全部揃えるとなると手持ちの資金では足りなそうだったので",
                "二人は一旦帰ってから本当に必要なものを整理することにした"),
            )

def sc_discounting(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("安く揃えようぜ",
            yusha.talk("全然買えないぞ！"),
            sol.talk("結構準備するだけでも金かかるだろ？"),
            h.deal("自宅に戻ってきた$Sと$solは部屋に入ってくつろぎながらも",
                "何も買えなかったことについてうだうだと言っていた"),
            h.move("ちょうどそこに帰ってきたのが$n_makoだ。",
                "彼女の手には小さなピンク色をした袋が握られている"),
            sol.talk("お？　お嬢は買い物してきたんだな"),
            mako.talk("当然でしょ。",
                "あ、でもこれは化粧道具とか",
                "そういった小物で", "別に旅の準備じゃないんだけど"),
            yusha.talk("え……$makoさん？"),
            mako.talk("だって必要になったら$st_amazonで頼めばどこだって配達してもらえるもの。",
                "とりあえず旅行用の服とか日焼けしないようなパラソルとか", "そっちの方が大事でしょ？"),
            h.look("$Sと$solは顔を見合わせて「こいつはダメだ」と心の声をぶつけ合う"),
            mako.ask("それで$taroたちはどうだったんですか？", "目的のものは買えました？"),
            yusha.talk("いやそれがさ……"),
            h.deal("$Sは彼女に事情を説明した"),
            mako.talk("そんなことだろうと思いましたよ……もう"),
            h.look("そう言うと彼女は二人に自分の$phoneを見せる"),
            h.look("そこは$otokudotcomというサービスで",
                "各店舗の価格比較がなされていて一番安い店を選ぶことができるというのだ"),
            sol.talk("おい、ここ安っ！", "嘘だろ？", "$healdrinkまとめ買い一ケースで千Ｇとか特売の時でも見ないぞ"),
            h.look("$solは何度も「おおお！！」と雄叫びを上げて歓喜する"),
            mako.talk("買い物というのは安くても構わないものならこういうとこを利用して揃えるといいのよ。",
                "逆にちゃんと大事にしたいもの",
                "長く使いたいものはしっかりしたお店でお金を出して買うようにした方がいいけどね"),
            sol.talk("この店の万能ナイフ安すぎだろ……ちょっと買ってくる！"),
            h.look("そう言うなり$solは飛び出ていってしまった"),
            yusha.talk("これを参考に揃えてみるよ。", "ありがとうな、$mako"),
            mako.talk("$taro……。",
                "$meはただ$taroのお役に立てればと思っただけで",
                "そんな風に褒めてもらおうとか一ミリも思ってなくて",
                "あ、でも$taroにお褒めの言葉をいただくのは気分が悪くないのでもっと言ってもらってもいいんですよ……あれ？　$taro？"),
            h.deal("恥ずかしそうにもじもじと自分の手を握っていた$n_makoが顔を上げた時には既に", "$Sは部屋を出ていってしまっていた"),
            mako.talk("もう！"),
            h.think("しかし$Sたちは知らなかった。",
                "安物買いの銭失いという格言を大昔の偉人が残してくれていることを"),
            )

# episodes
def ep14(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_awaking(w),
            sc_reunion(w),
            )

def ep15(w: wd.World):
    return (w.chaptertitle(TITLE[1]),
            sc_gotoshop(w),
            sc_gathermoney(w),
            )

def ep16(w: wd.World):
    return (w.chaptertitle(TITLE[2]),
            sc_yutuber(w),
            sc_nothingmoney(w),
            )

def ep17(w: wd.World):
    return (w.chaptertitle(TITLE[3]),
            sc_letsbuying(w),
            sc_discounting(w),
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
            #ep14(w),
            #ep15(w),
            #ep16(w),
            ep17(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

