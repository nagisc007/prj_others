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
    return w.scene("勇者チューバーでいこう",
            )

def sc_(w: wd.World):
    h = yusha = w.yusha
    sol, mako = w.sol, w.mako
    return w.scene("",
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
            ep14(w),
            ep15(w),
            ep16(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

