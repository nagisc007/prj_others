# -*- coding: utf-8 -*-
"""Story: chapter 1 'Depature'
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
        "実況なう",
        "診断なう",# NOTE: 診断メーカーからの乗っ取りツイート
        "魔王なう",# NOTE: 魔王とは？　恨み
        "無料なう",# NOTE: 重課金の罠
        "mamazonなう",# NOTE: 何でもamazon
        ]

# scenes
## ep6 scenes
def sc_mystalker(w: wd.World):
    h = yusha = w.yusha
    sol, mam, mako = w.sol, w.mother, w.mako
    return w.scene("勇者のストーカー",
            h.be(w.stage.myhome, w.day.firstawake),
            mako.talk("$taroのこと特定しました"),
            h.think("何……だと！？"),
            h.look("$Sである少年は",
                "自宅の玄関前に立つどう考えても彼より五歳程度は若いだろうと思われるピンクのおかっぱ娘の笑みに",
                "戦慄していた"),
            yusha.talk("あの……どうして$meの名前を？"),
            h.look("右側の膝が小刻みに震え始めたのを強引に手で押さえ込み",
                "$Sは尋ねる"),
            mako.talk("コレですよ"),
            h.look("愛らしい声と絶えない笑顔で彼女が見せたのは",
                "その小さな手にはやや余る$phoneと呼ばれる鉱石を加工した板状の道具だ。",
                "それには同じものを持つ者同士", "どんなに離れていても文字や映像をやり取りできるという",
                "不思議な能力があった"),
            h.look().emphasis("$n_yusha様のご自宅なう"),
            h.look("そう書かれ",
                "家の玄関のドアと彼女がはにかむ様子が映っていた"),
            yusha.ask("……コレ",
                "何してるの？"),
            mako.talk("実況です"),
            yusha.talk("じっきょう？"),
            mako.talk("はい。", "大好きな$taro実況なうです"),
            h.look("そう答えながら女の子は$phoneに指を置いて「実況なう」と笑った"),
            yusha.talk("とにかく入って！"),
            mako.talk("$taroの住処に入場なう"),
            h.deal("$Sは次々と彼の状況を呟こうとする彼女を家に押し込んで",
                "ドアに鍵を掛けた"),
            mam.ask("その子", "あんたの知り合い？"),
            h.deal("片眉を上げた母親の不機嫌な声に", "$Sは慌てて首を横に振ろうとする。",
                "しかしそれに先んじて彼女が前に出ると",
                "丁寧なお辞儀からの爆弾発言を投げつけた"),
            mako.talk("$taroのお母様ですね？",
                "初めまして。",
                "$meは$n_makoと言いまして",
                "こちらの$yushaの婚約者です"),
            mam.ask("ぼ、僕？",
                "それに婚約って……？", "あんた"),
            yusha.talk("おいおいおい。",
                "いきなり訪ねてきて何勝手なことを言って――"),
            h.look("人生の間違いまで訂正するのかという勢いで割り込んだ$Sだったが",
                "$makoと名乗った少女は彼に向けて$phoneを見せる。",
                "そこには$scshotと呼ばれる",
                "彼が『勇者なう』と呟いた瞬間の$phoneの盛り上がりを捉えた画像が映っていた"),
            yusha.talk("あれ……コレって気づいたら消えてたはずじゃ"),
            h.look("彼女は笑みを浮かべたまま口だけを動かしてこう彼に伝える"),
            mako.behav("――あなたが勇者だって世界中にバラしますよ"),
            )

def sc_threaten(w: wd.World):
    h = yusha = w.yusha
    sol, mam, mako = w.sol, w.mother, w.mako
    return w.scene("脅迫される勇者",
            yusha.talk("あー", "そ、そうなんだよ。",
                "母さん悪い。", "$meってこの子と婚約したんだったわ。",
                "はは", "はははは……"),
            h.look("乾いた笑いを上げる彼の隣に並び",
                "再び「宜しくお願いします」と$n_makoは頭を下げる"),
            mam.talk("あら、そうなの？",
                "でもあなたってまだ子供じゃない？"),
            h.feel("その言葉が出た瞬間", "$n_makoの周辺の空気が凍りつく"),
            yusha.talk("さ、寒っ！"),
            mako.talk("$meは見た目が小さいだけでこれでも既に立派な大人なんです！",
                "どうして人間て見た目だけで物事を判断しちゃうんですかね！"),
            h.look("彼女は母親を睨みつけたまま",
                "右手を壁に向ける。",
                "呪文の詠唱もなしにそこからは鋭い冷気の塊が飛んでいき",
                "それが当たった天井と壁の一部は凍りついてしまった"),
            mako.talk("$me", "これでも上級魔法使いなんです"),
            h.look("得意げにそう言ったが",
                "$Sも母親も大きく目を開いて何度も凍ってしまった我が家の一部を見る"),
            yusha.talk("あ、あの。", "ちょっといいか"),
            mako.talk("$n_makoです"),
            yusha.talk("は？"),
            mako.talk("だから$n_makoって呼んで下さい。", "そうしないとあなたが勇者だってバラ……"),
            yusha.talk("あーあー分かった分かった。",
                "$makoちゃん？"),
            h.look("名前を呼ばれたことがそんなに嬉しかったのか",
                "彼女は俯きがちになって頬を染めてから「何ですか？」と聞いた"),
            yusha.talk("ちょっとあっちで二人だけの話をしないか？"),
            mako.talk("えっ……そんな",
                "急に二人きりだなんて"),
            yusha.talk("いや", "なんかその面倒くさいのいいから"),
            h.deal("もじもじとする彼女の手を掴み",
                "$Sは自分の部屋へと連れて行く"),
            mam.talk("分かってるでしょうけど",
                "$yusha", "あんたはまだ成人してないんだからね！"),
            h.deal("はいはい。", "めんどくせーな。",
                "という気持ちでドアを閉めると",
                "部屋のランタンに火を灯す"),
            h.look("ベッドと物入れの箱が二つ並ぶだけの質素な部屋だったが",
                "$Sは彼女をベッドに座らせると",
                "その両肩に手を置いて話を切り出した"),
            yusha.talk("あの", "$makoさん……いや$mako様"),
            mako.ask("あ、改まって何でしょう？"),
            yusha.ask("どこで$meが勇者だって知ったの！？"),
            h.look("その質問に明らかに落胆した彼女は視線をすっかり暗くなった窓の外に向けつつ",
                "こう答えた"),
            mako.talk("最初からですよ。",
                "言ったでしょう。",
                "$taroが好きなんです。",
                "初めて見つけた時からずっとずっと",
                "$taroだけを想っているんですよ？",
                "ほら"),
            h.look("彼女に見せられたのは$phoneの画面だ。",
                    "そこには$Sが城を出てから『勇者なう』と呟いてその後モンスターたちにボコボコにされたり",
                    "教会や酒場で色々と騙されたり",
                    "迷い猫を助けたりする様子が『実況なう』と書かれながら$photo付きで残されていた"),
            yusha.talk("ほんとに", "ずっと……見てた", "ってこと？"),
            mako.talk("はい！"),
            h.look("元気の良い声に彼は目眩を覚えたが",
                    "その$phoneには他の人間の呟きが全然流れていないことに気づいた"),
            yusha.talk("あのさ……コレって世界に流してないの？"),
            mako.talk("流石に無修正だと色々問題があるんで",
                    "これから編集して", "どうせなら$dogaにしようかなって思って"),
            yusha.talk("$dogaって何？"),
            mako.talk("動く絵みたいなもんです"),
            yusha.talk("やめて"),
            mako.ask("何でですか！？", "折角の二人の愛の記録なのに"),
            h.look("いやいや", "と首を振ったが彼女の方は涙を浮かべて$Sを見ている"),
            yusha.talk("それじゃあどうすればコレを世界に流さないようにしてくれるんだ？"),
            mako.talk("そうですねえ……それじゃあ",
                    "$meを一緒に魔王退治の旅に連れて行って下さい。",
                    "それで手を打ちます"),
            yusha.ask("危険だけど", "それでもいいの？"),
            mako.talk("はい……$yusha"),
            h.look("大きく頷いて", "彼女はこの日一番の笑みを彼に向けたのだった"),
            )

## ep7 scenes
def sc_onthebed(w: wd.World):
    h = yusha = w.yusha
    sol, mam, mako = w.sol, w.mother, w.mako
    return w.scene("ベッドの上で",
            h.be(w.stage.bedroom, w.day.firstawake),
            h.think("今日は色々なことがあった一日だったよなあ"),
            h.look("そんなことを思いながら勇者である少年は自室の天井を見上げていた"),
            sol.talk("いやあしかし悪ぃな。",
                "晩飯食べさせてもらっただけでなく",
                "寝床まで用意してもらって"),
            h.look("シャツに膝丈のパンツ姿で部屋に入ってきた赤髪の大男は",
                "外の水桶で頭まで流してきたのだろう。",
                "すっきりした顔で$Sを見た"),
            sol.talk("ところでお前さ",
                "その便利そうなもん", "どうしたんだ？"),
            h.look("部屋はベッド脇の小棚の上のランタンの灯だけが照らす薄暗さだったが",
                "それでも$Sが手にしている$phoneと呼ばれる薄い石版の存在は彼に分かったようだ。",
                "赤髪の$solはベッドに腰を下ろすと",
                "$Sの後ろからその板を覗き込む"),
            h.look("そこには同じ$phoneを持つ人々が思い思いに書き綴った文章や切り取られた現場の画像が",
                "次々と滝のように流れていた"),
            yusha.talk("王様から支度金と一緒に貰ったんだよ……てかどうしてお前がここにいるんだよ！"),
            sol.talk("いや", "お前のママが泊まってけって言うから"),
            yusha.talk("マジかよ！？",
                "ご近所からケチですぐヒス起こすって有名なのに……お前もしかして",
                "母さんに美人だ何だ言っただろ？",
                "褒めるとすぐのぼせ上がるからな。",
                "全く誰に似たんだか"),
            h.look("仕方ない。",
                "と溜息をつきながら$solに床で寝るように言って毛布を貸してやると",
                "$Sは$phoneに表示されている中から気になる文言を見つけて",
                "それを突《つつ》く"),
            yusha.talk("勇者……診断", "だと！？"),
            h.look("そこには『勇者診断』として誰かの診断結果が適性率の他に強さや知能",
                "正義感といった幾つかの項目で表示されていた"),
            )

def sc_takeovertweet(w: wd.World):
    h = yusha = w.yusha
    sol, mam, mako = w.sol, w.mother, w.mako
    return w.scene("乗っ取りツイート",
            yusha.talk("$Sの$meがやらない訳にはいかないだろう。目指すは適性率百パーセントだ"),
            h.look("診断する",
                "という文字を触ると画面が切り替わり『名前を入れて下さい』と表示された。",
                "彼は一瞬”$S”と入れそうになったが勇者診断で勇者もないだろう。",
                "代わりにアカウント名でもある$n_yushaと入れて『診断』を押す"),
            yusha.ask("あ？",
                "何だコレ"),
            sol.talk("うっせぇなあ。",
                "もう夜なんだからさっさと明かり消して寝ろよ"),
            h.deal("床の上で既に大の字になっていた$solは寝返りを打ってベッドの上の$Sを見やる"),
            yusha.talk("いやさ",
                "これちょっと見てくれよ"),
            sol.talk("んだよ……"),
            h.look("$Sから$phoneを見せられた$solは",
                "そこに表示されている難しい字の並ぶ文章が解読できなかった"),
            yusha.talk("これどういうことだと思う？"),
            sol.talk("$yushaわかんねえの？",
                "だからそれを$meに聞いちゃう？"),
            yusha.talk("いやいや$meだって分かるよ。",
                "ただこの『認証する』ってのを", "どうするべきかと思ってさ"),
            sol.talk("するかしないかっつったら",
                "男たるもの一択だろ？", "するしかねえよ"),
            h.look("やっぱりそうか",
                "と納得し",
                "$Sはそこに表示された認証と書かれた文字を押した"),
            yusha.talk("お", "出た出た。",
                "診断結果早いなって……え"),
            h.look("表示された結果は勇者適性１％という散々なものであった。",
                "強さや知能などの能力は平均的で正義感だけやたらと高い。",
                "ただ運は最悪で", "死因はスライムにぶち殺されると書かれていた"),
            yusha.talk("この診断", "絶対ウソだろ。",
                "適当なこと言いやがって"),
            sol.ask("そういや寝る前に一つ訊いとくんだが"),
            h.deal("眠ろうと思ってランタンの灯を落とした時だった"),
            yusha.ask("何だよ？"),
            h.deal("天井を見上げる$solがそのまま尋ねる"),
            sol.talk("お前ってさ……勇者なのか？"),
            yusha.talk("えっと……その……"),
            h.think("彼はかつて$Sと魔王軍にバレてしまい", "ボコボコにされた経験があった"),
            yusha.talk("頼む", "頼みます！",
                "$sol様神様精霊様！",
                "$meが勇者だってことは黙っておいて！"),
            sol.ask("え？", "それ本気で言ってんの？",
                "自分が勇者だと本気で思ってるの？"),
            yusha.talk("いやだからさ",
                "今日城に呼び出されて王様から$yumark貰ってさ",
                "魔王を退治してくれって頼まれたんだって。",
                "いやホント！", "本気の本気で嘘０％だから！"),
            h.hear("わかったよぉ",
                    "という寝ぼけた声に続いてすぐにイビキが響き始める"),
            yusha.talk("おい？", "$sol？", "寝ちゃったのか？",
                    "……なんだよ。", "ホントに黙っといてくれるんだろうなあ"),
            h.look("不安な気持ちを抱えつつ",
                    "彼も眠りに就こうとした時だった。",
                    "$phoneが明るくなっている"),
            yusha.ask("ん？"),
            h.deal("手にとって見ると",
                    "そこには$Sのアカウントなのに何故か『魔王だよーん』と名前が書かれており",
                    "見ている間に次々と『魔王なう』『世界征服開始なう』などと呟かれていく"),
            yusha.talk("おいおいおい！",
                    "なんで$meが魔王なの？"),
            h.explain("彼は知らなかった。",
                    "『認証』したことで悪さをするあれやこれやが彼のアカウントに魔王を名乗らせてしまったことに"),
            h.look("見ている間にも次々と文句が寄せられ",
                    "あっという間に罵詈雑言に恨みつらみの文字で彼の$phoneは埋め尽くされたのであった"),
            )

## ep8 scene
def sc_maodistress(w: wd.World):
    yusha = w.yusha
    maou = w.maou
    h = mane = w.maneko
    buka = w.minion
    return w.scene("魔王の苦悩",
            h.be(w.stage.maocastle, w.day.firstawake),
            h.explain("勇者が$phoneのアカウントを乗っ取られ「魔王なう」と勝手に呟かれて困っている",
                "その半日ほど前のことである"),
            buka.talk("$mane様", "実は$st_homeregionに集めた手練れの者たちがまだ特別手当てを貰ってないと騒いでおります"),
            h.look("ここは$st_maocastleの執務室。",
                "上から下までピンク色をした服を着込んだ魔王代理を務める参謀の$fullこと$n_manekoは",
                "部下の報告を受けて窓の外に視線を投げていた"),
            buka.talk("それから先日も報告しましたように",
                "各大陸での戦力バランスが歪んでいる所為で",
                "ところによっては遥かに人間たちの方が強いといった事態が発生し",
                "世界制圧計画に破綻が生じつつあります。",
                "早急に戦力バランスの再考と適切な配置をお願いしたく"),
            mane.ask("その件に関しては前も言ったように",
                "強い者と弱い者を同居させるとヤツら弱い者虐めを始めてすぐに軍としての機能を喪失するから", "仕方なく何とかギリギリ指令通りに動けるような編成にしてあるのだ。",
                "これについては現在そうならないよう不満の捌け口となる道具を開発中だ"),
            h.look("全身緑色をした人の体に魚の頭が乗ったような部下のモンスターは",
                "$n_manekoの言葉をさっぱり理解していないようだった"),
            mane.talk("手当ての件は財務部に伝えておく。",
                "それ以外に問題はないな？"),
            h.deal("$n_manekoは後ろで手を組みながら",
                "赤く見える三日月に思いを馳せていた"),
            h.think("人間の女に酷似した容姿をしていたが",
                "$n_manekoは決してその表情を変えない。",
                "内心で「このクソ忙しい時に$maouは一体どこで何しとんのや！」と激怒していても", "である"),
            buka.talk("あの", "それがですね"),
            mane.talk("まだ何かあるのか？"),
            h.look("振り返って部下を見やると", "目線を逸してからこう続けた"),
            buka.talk("我々幹部の$phoneですが", "旧型故に最近固まったまま動かなくなることも増えておりまして。",
                "できましたら最近のＳ８にしていただけるとありがたいなと"),
            mane.ask("よく聞こえなかったんだが"),
            h.look("そう言って$n_manekoは部下にその視線を向ける。",
                "切れ長の瞳の中央が開き", "そこから黄金の眼が射抜くような光を放っていた"),
            buka.talk("あ、いや、その", "まだまだ３Ｇでがんばります！"),
            h.deal("床に突いていた膝が震え始め", "慌ててそれを押さえ込みながらそう答えると",
                "部下は頭を深々と下げたまま部屋を出て行った"),
            mane.talk("はぁ……"),
            h.look("一人になった彼女は特大の溜息をついたが",
                "机の上に積み上げられた報告書の山を見て",
                "思い切り拳を叩きつけた"),
            mane.talk("外出するなら行き先の報告くらいしていけやクソ$maou！"),
            )

def sc_makemao(w: wd.World):
    m = maou = w.maou
    h = mane = w.maneko
    buka = w.minion
    return w.scene("魔王メーカー",
            h.deal("孤独な叫びが部屋を駆け巡り終えると",
                "$n_manekoは椅子に腰を下ろす"),
            h.look("自分の最新型$phoneを取り出し",
                "どこかに$maouの痕跡が見つからないかと盤面を流れていく文字や画像の滝を見やった"),
            h.look("呟かれているのは大半がどうでもいい戯言だ"),
            h.look("魔王しね",
                "魔王のバカ",
                "魔王は一生目が閉じられない呪いにかかれ等",
                "単なる悪口ばかりが目に付く"),
            h.think("いやそもそも最近$maouの悪口しか目にしていない気がする"),
            h.deal("$phoneではそれぞれアカウントと言って",
                "自分の分身のようなものを登録するのだが",
                "流れている文章などを自由に閲覧できる他にも",
                "フォローといって別の者のアカウントを登録しておくと",
                "その者たちの呟きを常に監視することができるようになっていた"),
            mane.talk("そもそも$meが登録してるのって……魔王軍の者たちだけなんだよなあ"),
            h.look("留まることを知らない”魔王”という単語を含んだ罵詈雑言に",
                "軍参謀である$n_manekoは思い切り頭を抱えて机に突っ伏した"),
            w.tag.symbol("◆"),
            m.be("一方その頃", "当の魔王はというと",
                "ある場所で必死に自分の$phoneを見ながら怒りに打ち震えていた"),
            maou.talk("あいつら……後で全員減俸してやるからな"),
            m.look("薄暗い場所で$phoneの板がほんのり光り",
                "それが魔王の表情をそっと照らし出す。",
                "それは皺の多い目口の釣り上がった鬼のような形相とは程遠い",
                "つるりとした目鼻の何とも愛らしいものだったが",
                "彼女は何か必死になって$phoneの上を叩いていた"),
            maou.talk("そもそもどうして$meだけ悪口言われないといけないんだ？",
                "そうよ！", "絶対おかしいって"),
            m.deal("何を思いついたのだろう。",
                "彼女は盤面を掌で撫で", "そこを真っ暗にする"),
            maou.talk("みんな魔王になっちゃえ……"),
            m.deal("続いて意味不明な記号の羅列がそこに表示され始め",
                "暫くするとそれは『魔王診断』と『勇者診断』という二つのアプリとなった"),
            maou.talk("これで……みんな魔王になって悪口言われ邦題だわ。",
                "あっはははは！"),
            m.hear("彼女の高笑いが", "闇にこだましたのであった"),
            )

# episodes
def ep6(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_mystalker(w),
            sc_threaten(w),
            )

def ep7(w: wd.World):
    return (w.chaptertitle(TITLE[1]),
            sc_onthebed(w),
            sc_takeovertweet(w),
            )

def ep8(w: wd.World):
    return (w.chaptertitle(TITLE[2]),
            sc_maodistress(w),
            sc_makemao(w),
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
    return (w.maintitle(cnf.TITLE["chap1"]),
            ep6(w),
            ep7(w),
            ep8(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

