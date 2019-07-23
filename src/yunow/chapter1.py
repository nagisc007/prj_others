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
        "勇者なう",
        "教会なう",
        "登録なう",
        "捨て猫なう",
        ]

# scenes
def sc_Iamyusha(w: wd.World):
    yusha = w.yusha
    return w.scene("俺は勇者だ",
            yusha.be(w.stage.castle1gate, w.day.callyusha),
            yusha.deal("勇者なう"),
            yusha.deal("黒光りする石版の上で指を滑らせると",
                "自分の呟いた言葉がそのまま表示され",
                "文字の川に流れていった"),
            yusha.talk("おお", "すげえ"),
            yusha.look("思わず声を上げてその石版を見た短い茶髪頭の少年は",
                "苦笑を浮かべる門番たちの視線に気づいて慌てて歩き出す"),
            yusha.move("堀の上に渡された丸太を組んだ橋は気をつけて歩かないと滑って転びそうだが",
                "彼は支給された真新しい革のブーツを履いてご機嫌で進んでいく。",
                "仕立ててが良いらしく",
                "このまま走っても大丈夫なくらい靴底が安定している。",
                "流石”勇者の靴”だ"),
            yusha.talk("いやあ",
                "しかし$meが勇者かあ"),
            yusha.look("一見すると彼はごく普通の十六歳の鼻水垂らした少年に見えるのだが",
                "この度$n_kingより直々に勇者の称号を冠され",
                "魔王退治を依頼された英雄の卵であった"),
            yusha.look("彼が手にしている$phoneと呼ばれる漆黒の石版は",
                "同じ石版を持つ者に対して呟いた文字を流すことができるという特性がある"),
            yusha.talk("お？", "$meって早速話題になってね？"),
            yusha.look("次々と流れてくる”勇者”という文字の洪水に",
                "彼の表情筋は緩み",
                "空の雲行きが怪しくなっていることにも気づかないでいた"),
            )

def sc_strangetown(w: wd.World):
    yusha = w.yusha
    return w.scene("町の様子がおかしいぜ",
            yusha.be(w.stage.hometown),
            w.tag.symbol("◆"),
            yusha.ask("ん？"),
            yusha.look("彼がそれを感じ取ったのは",
                "$st_castle1を出てその城下町の中央広場までやってきた時だった"),
            yusha.talk("あれ？", "さっきまでここって露店いっぱい並んでたはずじゃ"),
            yusha.look("右肩から提げたズタ袋をまさぐり王様から貰った支度金の硬貨の感触を楽しもうとした彼は",
                "立ち止まってぐるりと周囲を見る"),
            yusha.look("広場の真ん中にある五メートルほどの建国記念碑の周りを花壇が囲み",
                "その外側に円形に並ぶようにしてマーケットが広がっていた。",
                "それが今朝のことだ。",
                "彼は眉を顰めた母親にわざわざ王直々の呼び出しだと叩き起こされ", "不機嫌さを抱えてここを通ったのだが",
                "その時には客も集まり", "賑やかな有様だった"),
            yusha.feel("生温かい風を感じて背後を振り返る"),
            yusha.look("そこには彼が持つのより一回り小さな$phoneを持つ老人が立っていて",
                "それを彼に向けて小声で何か呟く"),
            yusha.talk("おい"),
            yusha.look("一瞬の眩しさを感じて顔の前に手をやったが",
                "視界が戻るとその老人の姿は既に小さくなってしまっていた"),
            yusha.talk("何なんだよ……"),
            yusha.move("$Sは舌打ちをし", "とりあえずと酒場の方に歩き出す。",
                "流石に魔王退治の旅に一人で出かける訳にもいかない。",
                "傭兵か", "あるいは仲間でも見繕おうという算段だ"),
            )

def sc_theend(w: wd.World):
    yusha, bar = w.yusha, w.barmaster
    return w.scene("そして終わりは突然に",
            yusha.go(w.stage.homefield),
            w.tag.symbol("◆"),
            yusha.talk("何すんだ！"),
            yusha.deal("$Sの胸倉を掴んで店の外へと押し出して追い出した大男は",
                "$st_bar1の店主だった。",
                "その巨躯で睨みを利かせ", "手を叩きながら太い声を唸らせる"),
            bar.talk("あんた勇者だろ？",
                "それを全世界に向けて呟いたことの意味", "理解してんのか？"),
            yusha.look("何をそんなに怒っているんだろう",
                "という表情しか彼は返せない"),
            bar.talk("今がどんなご時世か考えろってんだよ"),
            yusha.look("そう吐き捨てると大男は店内に戻っていき",
                "ドアを閉める前に看板を『ＣＬＯＳＥＤ』に変えた"),
            yusha.talk("ハァ！？",
                "$meが何したってんだよ", "ったくう"),
            yusha.move("意味も分からないまま彼は立ち上がる"),
            yusha.move("とりあえず別の酒場を当たろうと思ったが",
                "どこも開いていない"),
            yusha.talk("何が起こってんだよ……"),
            yusha.feel("そうぼやいて$phoneを取り出した彼の頭に",
                "粘性の強い液体が滴った"),
            yusha.talk("ん？"),
            yusha.look("見上げるとそこには鳥の頭をした人型のモンスターが翼を広げて浮かび",
                "その手にした剣を振り上げている"),
            yusha.talk("あん！？"),
            yusha.look("鼻から紫の煙を吐き出したそいつは",
                "どう考えても今の彼では太刀打ちできそうにない"),
            yusha.talk("何でだよ！"),
            yusha.move("$Sは慌てて頭を下げ", "その低い姿勢から一気に駆け出す"),
            yusha.look("彼の頭のあった場所を鋭い刃が抜けていったが",
                "間一髪で助かったようだ"),
            yusha.look("しかしその前方には巨大なハンマーを持った豚面をした筋肉質の獣人や",
                "ガイコツ兵士", "真っ白なお面を被って髑髏の杖を手にした奴らといった",
                "この近隣では見たことのないモンスターが大挙していた"),
            yusha.talk("ど", "どういうことだよ！？"),
            yusha.look("立ち止まった彼の視線の先で",
                "紫色の顔をした細長い頭の男が笑いながら",
                "その手にした$phoneを見せた"),
            yusha.look("彼も慌てて自身の$phoneを見たが",
                "そこにはもの凄い勢いで、"),
            yusha.look().emphasis("勇者特定なう"),
            yusha.look("彼がいる場所", "その背格好",
                "本名に幼少期の出来事",
                "全然知らない架空の元恋人の話までが文字の渦となって流れていた"),
            yusha.talk("何……だよ", "これは"),
            yusha.look("逃げ場を失った彼は叫びながらそのモンスターの群れへと突っ込んでいく"),
            yusha.think("彼は知らなかったのだ。",
                "魔王たちもまた",
                "$phoneを手に",
                "日夜活動を行っていることを"),
            yusha.look().emphasis("勇者ボコボコなう"),
            yusha.look("その呟きは",
                    "画像付きで瞬く間に世界に広められたのであった"),
            )

## ep2 scenes
def sc_awakechurch(w: wd.World):
    yusha, yula = w.yusha, w.yula
    h = yusha
    return w.scene("教会で目覚めた",
            yusha.be(w.stage.church1, w.day.firstawake),
            yula.deal("目覚めなさい……若者よ"),
            yusha.hear("愛らしい女性の声が聞こえる"),
            yusha.think("まさか……女神様！？"),
            yusha.look("そう思って目を開けるとそこは城下町の教会だった"),
            yusha.look("$Sは床に寝かされ",
                "胸の上で手を組んでいるところに",
                "ぼたぼたと何やら液体を落とされている"),
            yula.talk("ひゃあ").omit(),
            yusha.talk("あんた$meに何してんの？"),
            yusha.look("水の入った瓶を傾けていたのは彼が見たこともない女だった。",
                "耳が隠れる程度のふんわりとした金髪に",
                "驚いて開いた口の八重歯が光る。",
                "小ぶりな目はぱちくりと何度も瞬きをしたが",
                "その手の瓶からはどぼどぼと液体が溢れ続け",
                "遂には中身が空っぽになってしまった"),
            yula.talk("あ……"),
            yusha.talk("いや",
                "『あ』じゃねえし！"),
            yusha.behav("がっと勢いよく起き上がると",
                "立ち上がりその女の細いが筋肉質な手を掴んだ"),
            yusha.talk("これ何なんだよ？",
                "てか", "あんた誰よ？", "$n_priest1神父は？"),
            yusha.look("よく見れば首から十字架を下げ",
                "紺色に染めたローブを纏っている"),
            yula.talk("えーっと",
                "$n_priest1さんは今休暇で旅に出掛けられてて"),
            yusha.look("そう言った彼女は慌てて宣誓台の上から黒い板状のものを手に取ると",
                "「ほら」とそれに指で触れてから", "$Sに見せる"),
            h.look("教会なう"),
            h.look("その言葉と一緒に色鮮やかなステンドグラスの前でピースサインをしている$n_priest1が",
                "絵ではなく実際に見たままの姿で映っている"),
            yusha.ask("これって$phoneだろ？",
                "呟きが遠隔地で見える以外にもこんなことできたのかよ！"),
            yula.talk("知らなかったの？",
                "ほら", "もっと色々なところで映ってるわよ"),
            h.look("そう言って見せられた$photoというものには",
                "世界各地の教会と一緒に映る$n_priest1の姿をいくつも確認することができた"),
            yusha.talk("すげえ……"),
            h.deal("彼は自分の胸元がびっしょびしょに濡れていることも忘れ",
                "しばらく色々な$photoが見られることに感心していたが",
                "ふと我に返り",
                "今一度自分の手元の$phoneと彼女を見比べた"),
            yusha.talk("これって$meの$phoneじゃね？",
                "てか$me",
                "勇者なうって呟いて魔物の集団に襲われたのに何でこんなとこにいるんだ？"),
            yula.talk("ゆ、勇者……？"),
            yusha.talk("あ、いや", "ユ・シャという名前なんだよ。",
                "ところであんた", "やっぱ誰よ？"),
            h.look("じろじろと$Sに見られ",
                    "彼女はコホンと咳払いをすると",
                    "胸の前で手を組んでこう答えた"),
            yula.talk("$meは$n_priest1の代理の者です。",
                    "あなたは教会の前で行き倒れていた旅人なので",
                    "魂を呼び戻す$i_resetを行っていたのです"),
            yusha.talk("ハァ？"),
            yula.talk("$i_godにより清められた聖水を垂らすことで",
                    "御霊を呼び戻しておりました"),
            h.think("そんなこともやってたかも知れない",
                    "というおぼろげな記憶に適当に相槌を打ち",
                    "彼は彼女の手を取って握手をした"),
            yusha.talk("まあいいや。",
                    "とにかく$meは生き返ったって訳だな？"),
            yula.talk("行き倒れていただけだと思いますが……助けた$meへの謝礼は大丈夫ですよ"),
            yusha.talk("ああ、そうか。",
                    "少しは寄付しといた方がいいよな"),
            h.look("彼女の足元に自分のズタ袋を見つけ",
                    "彼はその中に手を突っ込む"),
            yusha.talk("確か王様から貰った支度金が……"),
            )

def sc_nomonery(w: wd.World):
    yusha, yula = w.yusha, w.yula
    h = yusha
    return w.scene("一文無し",
            h.think("彼は何度も手を突っ込み",
                "最終的には袋の中身を全部引っ張り出してみてから",
                "思い切り天井を見上げた"),
            yusha.talk("……ない"),
            yula.talk("だから謝礼はいいですと申しましたでしょう？"),
            yusha.talk("そうか。",
                "あのモンスターたち", "$meから有り金巻き上げやがったのか！"),
            h.move("$Sはズタ袋に広げたものを仕舞うと",
                "立ち上がって一度彼女を振り返る"),
            yusha.talk("そういえばまだあんたの名前を聞いてなかったな"),
            yula.talk("$meですか？",
                "$n_yulaです"),
            yusha.talk("$yulaさんよ。",
                "絶対にあんたにこの礼はするから。",
                "魔王倒した報奨金でな！"),
            h.move("彼はそう言い放つと",
                "教会を駆け出ていく"),
            h.look("その背を見送る彼女は彼が振り返らないのを良いことに",
                "堪えきれない笑みを漏らした"),
            h.deal("もし$Sに彼女を疑う慎重さがあったなら",
                "$phoneを使って真実を知ることができただろう"),
            h.think("女盗賊$n_yulaに注意しろ", "という$photo付きの警告文が大量に文字の川を流れていくのを"),
            yula.talk("あれのどこか勇者よ。",
                "$phoneで神父不在は分かってたけど",
                "相手が馬鹿なお陰でこっちは大儲けですわ。", "アッハハハハ！"),
            h.feel("責任者不在の教会に",
                "女の高笑いが響き渡った"),
            )

## ep3 scenes
def sc_baragain(w: wd.World):
    yusha, bar, eada = w.yusha, w.barmaster, w.eada
    h = yusha
    return w.scene("酒場再び",
            h.come(w.stage.bar1, w.day.firstawake),
            h.move("無一文になった",
                "という事実から目を逸らすようにして",
                "$Sである若者は左手で黒い鉱石の板を持って歩いていた"),
            h.explain("$phoneと呼ばれる不思議な道具で",
                "同じ板を持つ者同士", "離れた場所であっても連絡を取り合えたり",
                "書き込んでおいた文章などを読むことが可能なのだ"),
            yusha.talk("しかし世の中魔王の所為で大不況に逆戻りしてんなあ……お？",
                "簡単に稼げる仕事あります連絡を", "だって。",
                "こんなもんまで流れてくるとは", "$phone", "有能だな"),
            h.move("むふふ", "と笑みを垂れ流しながら彼が向かっているのは",
                "酒場通りだった"),
            h.look("やや日も落ちて", "歩く影も長くなる"),
            h.look("彼を追い抜いていく屈強な男たちの足取りや笑い声は軽く",
                "それに客引きの賑やかな声が重なって響いていた"),
            yusha.talk("あ……そういやさっき"),
            h.look("$Sが入ろうと立ち止まったのは看板に『$st_bar1』とある木造りの二階建てだ。",
                "店の前には酒樽が並び",
                "ランタンが灯された店内から賑やかな女の声が聞こえてくる"),
            yusha.talk("いやいや。", "$meが勇者って呟いたのは消えてたから大丈夫なはずだ"),
            h.move("彼は大きく息を吸い込んで気持ちを整えると",
                "酒場のドアを潜る"),
            eada.talk("いらっしゃい"),
            h.look("初めて入る酒場で彼の目に飛び込んできたのは",
                "カウンターの上に乳を載せた（ように見える）女性だった。",
                "露出度の高い網のように編まれた襟首の黒ブラウスは",
                "化粧の濃い彼女の妖艶さを際立たせていた"),
            eada.talk("坊やはいくつ？",
                "成人してないとお断りなの"),
            yusha.talk("十六だけど", "べ、別に酒飲みに来た訳じゃねえし"),
            h.look("店内を見回すとテーブル席が幾つも並び", "まだ早い時間帯にも関わらずその半分程度が既に埋まっている"),
            eada.ask("人探し？"),
            yusha.talk("ちょっと仲間というか", "手練れな傭兵たちをニ、三見繕ってもらえないですかね？"),
            h.look("カウンターに無理やり身を乗り出して得意げに尋ねた彼を",
                "呆れた目でその女性店主は見返した"),
            yusha.talk("あ、いやその",
                "旅に出るつもりなんで", "同行してくれる経験者とかいると嬉しいなと思って……"),
            eada.talk("なら最初からそう言いなよ。",
                "ねえ"),
            h.look("女性が振り返って店の奥を見ると",
                "ちょうど階段を図体のでかい男が降りてくる"),
            yusha.talk("あ……"),
            h.look("彼はかつて”勇者なう”と呟いたことを叱りつけて店から追い出した巨漢だ"),
            bar.talk("なんだ？",
                "ガキは家帰ってミルクでも飲んでな"),
            h.look("相変わらずの強面で", "声だけで$Sはちびりそうになる"),
            eada.talk("それが旅のお仲間さんを探してるんだって。",
                "あんたの知り合いでも紹介してやんなよ"),
            bar.talk("はぁ？", "ガキのお遊びに付き合ってくれる奴なんざいねえよ。",
                "そもそも旅って何すんだよ？"),
            h.look("男の問いかけに待ってましたとばかりに$Sは胸を張る"),
            yusha.talk("魔王退治だ"),
            bar.talk("は？"),
            yusha.talk("この世界を大不況にしている魔王を退治して平和を取り戻すんだよ。",
                    "何か文句あるか？"),
            h.look("魔王？", "お前が？", "という明らかに嘲笑の視線を感じ取ると",
                    "$Sはズタ袋の中に仕舞ってある王様から貰った$yumarkを取り出して",
                    "自分が正真正銘の勇者であることを突きつけてやろうかと思ったが",
                    "自分が勇者と呟いた時にボコボコにされたことを思い出し",
                    "あっさりとその考えを捨てた"),
            yusha.talk("笑われても本気なんだよ。",
                    "それに何も$me一人でどうにかしようって訳じゃないんだ。",
                    "何人も強力な仲間がいれば",
                    "魔王の一人や二人", "何とかできるかも知れないだろ？"),
            )

def sc_entryapply(w: wd.World):
    yusha, bar, eada = w.yusha, w.barmaster, w.eada
    h = yusha
    return w.scene("登録しました",
            h.look("その真剣な眼差しに気圧されたのか、"),
            eada.talk("それじゃあ"),
            h.look("と女性店主の方が彼の$phoneを貸すように言った"),
            eada.talk("うーんとね",
                "最近これ持ってる人多いでしょ。",
                "だから……あった"),
            h.look("彼女がいくつか操作すると",
                "盤面には『$i_matching』という文字が浮かび上がり",
                "”登録してね”のピンクのフレーズからハートが吹き出していた"),
            yusha.ask("これ……何ですか？"),
            eada.talk("知らない？", "マッチングアプリって呼ばれてるもので",
                "探したい人同士をうまく結びつけてくれるものなのよ。",
                "まずここを押して"),
            h.look("彼女が$Sの左側に顔を寄せて手に触れると",
                "ふわりと甘い香りが漂った"),
            yusha.talk("えっと", "これですね"),
            eada.talk("そうそう。",
                "名前と年齢", "あと希望する相手の職業や特徴を記入していって"),
            yusha.talk("名前は……$n_yushaでいいか"),
            h.explain("それは彼のアカウント名だった"),
            yusha.ask("あのこれ", "月額とか書いてあるんですけど",
                "金かかるんですか？"),
            eada.talk("大丈夫よ。",
                "ほらここ。", "今ならキャンペーン中で初回登録無料に翌月月額無料ってあるじゃない"),
            yusha.talk("無料か。", "それなら……よしっと"),
            h.look("登録なう。",
                "そう表示されて可愛らしい女性がお辞儀をする姿が映り",
                "どうやら登録作業は無事に終えられたようだった"),
            yusha.talk("これで後はどうするんですか？"),
            eada.talk("希望する相手を色々な条件で探せるから",
                "相手を見つけたらとりあえずイイネすればいいのよ"),
            h.look("さっぱり分からない。",
                "という顔をした$Sから$phoneを取ると",
                "彼女は適当に選んで出てきた相手の顔の横にあるハートを押した"),
            eada.talk("これでいいわよ"),
            yusha.talk("いいね？"),
            h.look("そう言いながら彼女に人差し指を差し出した$Sに対して",
                "微笑を浮かべたまま彼女はこう答えた"),
            eada.talk("あなたが十八で成人してからね"),
            h.look("大人のウインクをされて上機嫌で$Sは店を出て行ったが",
                "その背を見て", "大男は呟いた"),
            bar.talk("登録したままになって延々と金を毟り取られるヤツが多いと聞くが",
                "あのガキ大丈夫なのかよ"),
            eada.talk("あら", "社会勉強ってやつよ？"),
            h.look("男は今一度", "店の$phoneでさっきのアプリを確認する。",
                "そこは月額一万｜Ｇ《$i_yen》と書かれていた"),
            bar.talk("これ高っ！"),
            )

## ep4 scenes
def sc_meetsoldier(w: wd.World):
    h = yusha = w.yusha
    sol = w.sol
    return w.scene("戦士に出会った",
            h.be(w.stage.townstreet1, w.day.firstawake),
            h.look("それぞれの民家に明かりが灯り始める"),
            h.move("レンガ造りの住居が立ち並ぶ路地を",
                "一人の若者が書類の半分ほどのサイズの板を手に",
                "にやにやとして歩いていた"),
            h.explain("彼は$Sと呼ばれる存在なのだが",
                "訳あって素性は隠している（らしい）"),
            h.look("その彼が手にした板は$phoneと呼ばれる不思議な鉱石で出来た魔法の道具で",
                "同じ道具を持つ者同士", "どんなに離れていても文字や映像をやり取りできるというが",
                "文字の洪水がどんどん流れていく中に突然現れた白黒まだらの猫の姿に",
                "思わずそれを指で突いた"),
            yusha.talk("迷子の子猫ちゃんか。", "ミーちゃん……誘拐されたかもって書いてあるじゃねえか。",
                "犯人見つけたらただじゃ置かねえ！"),
            h.explain("$Sは猫好きであった"),
            sol.talk("おいテメェ！",
                "何しやがんだ！"),
            h.look("男の声がして", "慌てて先の脇道に入ると",
                "そこには大きな剣を背負った赤い頭髪の男と",
                "彼から何かを必死に守ろうとして「シャァァ！」と威嚇の声を上げている白黒まだらの猫がいた"),
            yusha.talk("そいつってミーちゃん？"),
            sol.talk("あん？"),
            h.look("男が不機嫌な声で振り返ると",
                "その右頬にある斜めに走った傷跡が民家から漏れる明かりに照らされた。",
                "どう見ても只者ではない。",
                "それどころか", "今まで屈み込んでいたようで立ち上がると",
                "$Sの頭二つ分は背丈があった"),
            yusha.talk("に、睨んだって恐くねーからな！"),
            sol.talk("だからオメェ何なんだよ？"),
            yusha.talk("そのミーちゃんを返せ！"),
            sol.ask("みー？"),
            h.look("太い眉を歪ませただけで十分に威圧的だった"),
            yusha.talk("お前が誘拐した猫のミーちゃんのことだよ！"),
            h.look("猫？", "という視線を男は自分の背後に向ける。",
                "見る度に「シャァァ！」という威嚇をするが",
                "男の方には全く効いていないようだ"),
            h.look("それどころか",
                "彼の$Sに向ける視線が徐々に険しさを増していき",
                "やがて火山の噴火のように怒号に変わった"),
            sol.talk("オメェ", "$meがこいつ誘拐したとか頭スライムみたいなこと言ってんじゃねェ！"),
            )

def sc_losecat(w: wd.World):
    h = yusha = w.yusha
    sol = w.sol
    return w.scene("迷い猫",
            h.think("怒りの矛先が明らかに自分に向かった"),
            h.deal("そう感じ取った$Sは自分の方を見ていたミーちゃんに",
                "手で早く逃げろと指示をする"),
            sol.talk("おいテメェ……$meをバカにしてんのか？",
                "腕をフリフリして", "一体何の呪いなんだよ？"),
            yusha.talk("ほほお。", "戦い慣れてそうなのに知らないのかな？",
                "これは伝説の一子相伝の暗殺拳の奥義の技の一つに入れられそうになったくらい",
                "とてもすごく痛いやつなんだ"),
            sol.talk("な、何だよ", "その伝説の奥義ってのは"),
            h.think("あ、こいつバカだ。",
                "明らかに動揺している"),
            h.think("そう感じた$Sは両腕をぶらんぶらんと左右に揺すりながら",
                "一歩", "また一歩と距離を詰めていく"),
            sol.talk("お、おい……やめろ。",
                "それ以上来るんじゃねえ！",
                "$meはこれでも伝説の戦士$n_mas_soldierの息子の兄弟の奥さんの孫なんだぞ！"),
            h.look("男はそう言って背中の剣を抜く。",
                "薄闇の中で刃が民家から漏れた明かりを照らし",
                "不気味に光った"),
            yusha.talk("おいおい！",
                "前途ある丸腰の若者に剣を向けるなんて大人のやっていいことじゃないぞ！"),
            sol.talk("じゃ、じゃあテメェの方こそ", "その妙な動き", "そろそろやめろよ"),
            yusha.talk("お前が剣を仕舞ったらな"),
            h.look("両者ともに引く様子はない"),
            h.deal("だがその二人の間を", "焼き魚を咥えた白黒まだらの猫が駆け抜けていく"),
            sol.talk("$meの晩飯が！"),
            yusha.ask("え？"),
            sol.talk("だからその猫は$meが晩飯に食おうとしてたのを盗んでいきやがったんだよ！",
                "やっとここまで追い詰めたところなのに……くそ！",
                "待てこの野郎！"),
            h.look("男はそう叫んで逃げていった猫の背を追いかける"),
            yusha.talk("あれ？",
                "誘拐されたんじゃなかったのか……"),
            h.look("路地を曲がって消えていった男の背を見送り",
                "$Sは$phoneで先程の情報を再度確認する。",
                "そこには『誘拐されたかも知れません』と書かれているだけで",
                "事件とも何も書かれていない。",
                "それに加えて注意書きに『食べ物を盗みます。盗まれた方すみません』と謝罪文まで書いてあった"),
            sol.talk("おい……"),
            yusha.talk("あ……"),
            h.look("まずいことになった",
                "と思ってさっさとその場から立ち去ろうとしたところに",
                "血相を変えた男が戻ってきて", "$Sの前に立ち塞がる"),
            yusha.talk("なんか、その……大変でしたね。", "はははは"),
            sol.talk("ははは、じゃねえ！",
                "テメェ今晩の$meの飯どうしてくれんだよ？"),
            h.deal("一瞬思案した後で",
                "$Sは躊躇いがちにこう尋ねた"),
            yusha.talk("$meんち来ます？"),
            )

# episodes
def ep1(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_Iamyusha(w),
            sc_strangetown(w),
            sc_theend(w),
            )

def ep2(w: wd.World):
    return (w.chaptertitle(TITLE[1]),
            sc_awakechurch(w),
            sc_nomonery(w),
            )

def ep3(w: wd.World):
    return (w.chaptertitle(TITLE[2]),
            sc_baragain(w),
            sc_entryapply(w),
            )

def ep4(w: wd.World):
    return (w.chaptertitle(TITLE[3]),
            sc_meetsoldier(w),
            sc_losecat(w),
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
                w.yusha.deal(w.i.beat_maou),
                w.yusha.know(w.i.destroy_peace),
                w.yusha.deal(w.phone),
                w.yusha.go(w.i.trouble),
            #ep1(w),
            #ep2(w),
            #ep3(w),
            ep4(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

