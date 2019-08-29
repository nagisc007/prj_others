# -*- coding: utf-8 -*-
"""Story: chapter 4 'Goodbye home'
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
        "進路どっちなう",
        "Re: 村なう",
        "Re: 宿屋なう",
        "遺跡なう",
        "ゴブリンいないなう",
        "洞窟なう",# NOTE:洞窟内で
        "野営なう",# NOTE:野宿編１から
        ]

# scenes
## ep40 scenes
def sc_restart(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    return w.scene("リスタート",
            h.be(w.stage.homefield, w.day.awake5),
            h.look("城下町を出た$Sと愉快な仲間たちは街道沿いに北の$st_town2の町を目指していた"),
            yusha.talk("澄み渡る風なう！"),
            h.deal("元気に何もない草原に向かって$phoneを向けているのは短い黒髪に太眉が特徴的な$Sである少年だ。",
                "彼は$phoneと呼ばれる不思議な道具で見た景色を画像に収めつつ",
                "呟きを投稿するのが日課になっていた"),
            sol.talk("おい$yusha。",
                "風なんて画像にできないだろ？", "そもそも”なうなう”うるせえんだよ"),
            h.deal("その$Sに文句を垂れるのは赤髪で長身の戦士$sol。",
                "背中に大きな両手剣を背負い", "右肩には食料や簡易の寝袋の入った大きな袋を担いでいる"),
            mako.talk("いいんですよ$taroは。", "こうやって旅を楽しむことも魔王退治に大事なことなんだと……$meは思いますよ！"),
            h.deal("ピンクのおかっぱ頭の少女、$n_makoは", "被った尖り帽子を揺らしながら$Sに近づくと",
                "その手を握ろうとする。", "だが$Sはすっとそれを躱すと",
                "遠くの大きな岩に向けて$phoneで「岩なう」と呟いた"),
            yula.talk("それにしてもまだ夏は遠いのにやけに日差しがきついわね。",
                "もっと多めに日焼け止め塗っておくべきだったわ"),
            h.deal("三人の後について歩く金髪の女性は", "自称大盗賊の$yulaだ。",
                "口を開けるとよく尖った八重歯が目立つ。",
                "先程から空を見上げながらハーフパンツから出た脚やベストの上着から露出した腕を気にしている。",
                "肌は白く", "$Sの見立てではスタイルが良さそうに見える"),
            yusha.talk("痛っ！", "急に何すんだよ$mako"),
            mako.talk("何でもないですぅ！", "ふんだ！"),
            h.deal("$yulaをちらりと見やった$Sの脛を$n_makoが手にした杖で殴って離れる。",
                "$Sに対してあかんべえと舌を出すが", "彼は自分が彼女に対して変なことをしたつもりはなかった"),
            h.deal("そんな四人でところどころに立て看板の設置された街道を歩いていく"),
            h.look("かつては毎日行商人や旅の人間の往来で賑わっていたというが",
                "今や気軽に出歩いている冒険者すら見かけなくなってしまった"),
            yusha.talk("お！", "$n_slimeなう！"),
            h.look("と、$Sが遠くの草陰から伸びて出てきた緑色をした粘性のあるモンスター、$n_slimeを発見して喜んで$phoneを向けた"),
            yusha.talk("おい$sol", "あれ$n_slimeだよな？"),
            sol.talk("そうだけど襲ってこないんだからさっさと素通りするぞ？",
                "相手にしても何もいいことなんかないからな。", "無駄に苦戦して", "最悪命を落とすだけだ"),
            h.deal("自分の腰につけた$shortswordに手を掛けていた$Sだったが",
                "$solの態度は素っ気なく", "立ち止まった彼の肩を掴んで先に歩かせる"),
            yusha.talk("そういやなんか前に殺されたことあるんだった……忘れてたわ。", "ハハハ"),
            sol.talk("あん？", "$yusha", "お前$n_slimeとやったことあんの？",
                "一度でも戦ったことあるんだったら尚更やめとけよ。",
                "あんなのはそれこそ遠くから魔法使いに炎で焼き払ってもらうくらいの方が良いんだよ。",
                "なまじ力自慢の戦士が武器片手に向かった日にゃ", "丸ごと呑み込まれて何日も掛けて体内で溶かされて骨になっちまうからな"),
            h.think("$Sは前も$n_slimeのことで$solに注意されたことを思い出したが",
                "やはり$solの方は何も覚えていないようだ"),
            yula.talk("それよりこの先どうするの？", "$gmapで見てるけど",
                "湖畔脇を抜けるか", "橋を渡って一端西に出るかの二択よ"),
            yusha.talk("ちょっと見せて"),
            h.deal("そう言って$yulaの$phoneを覗き込もうとしたのだが、"),
            yula.talk("嫌よ。", "自分ので見なさいよ"),
            h.deal("彼女に拒否され", "$Sは仕方なく自分の$phoneで$gmapを使って近隣の地図を見てみる。",
                "そこにはこれまでに$Sが見たような森もなく", "蛇行した川もない。",
                "何故か谷が表示され", "そこに橋が渡されている。",
                "橋の先には$st_town3村が表示されていたが", "また同じ村なのだろうか"),
            yusha.talk("ちょっと$sol", "紙の地図の方を出してみてよ"),
            h.deal("もしやと思って$phoneの方ではない地図を確認すると",
                    "そちらも同じように森は描かれていない。", "ただ村の北側に遺跡跡という表記が消えそうになっているのが見つかった"),
            yusha.think("コレってあの$n_goblinダムのことだろうかと$Sは考える"),
            sol.talk("で", "どうすんだ？", "特に用がないなら湖畔の脇を抜けて$st_town2に行けばいいと思うけどよ？"),
            yusha.talk("橋を渡ろう"),
            sol.talk("は？"),
            h.deal("顔を歪めて$Sを見た$solにもう一度「橋だ」と言う"),
            sol.talk("あのよ$yusha。", "$meの話聞いてたか？",
                    "この湖畔脇のルートの方が$st_town2に近いっつってんだよ？"),
            yusha.talk("分かってる"),
            sol.talk("だったら"),
            yusha.talk("橋を渡ろう"),
            h.deal("そう言って一人頷いた$Sに$solは右の拳を握り締めながら目の前に突き出した"),
            sol.talk("他人の話！"),
            yusha.talk("ちょっと確かめたいことがあるんだ"),
            h.deal("だが真面目な顔で$Sがそう言い返すものだから", "目の前に突き出した拳を$solは軽く広げてから「なら仕方ねえ」と退けた"),
            yula.talk("それじゃあいいのね？", "橋を渡る方で？"),
            yusha.talk("うん。", "それで頼む"),
            h.look("確認するように尋ねた$yulaに笑顔で答え西に進路を取った$Sを", "$n_makoは不思議な表情で見ながらその後に続いた"),
            )

## ep41 scenes
def sc_bridge(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    return w.scene("橋きたー",
            h.be(w.stage.homefield, w.day.awake5),
            yusha.talk("ほんとに橋だ……"),
            h.look("石と丸太を組み合わせて造られた巨大な橋が", "裂けた大地を繋いでいた。",
                "$Sの記憶では確か川の干上がっていた跡があった場所だが", "今は覗き込むと底がよく見えないほど深い谷になってしまっている"),
            sol.talk("マジかよ！", "$meが$st_homeregion目指してる時にはこんなもん見た記憶がねえぞ……"),
            h.deal("赤髪の長身の戦士$solはちょっと顔を出して谷を覗き込んでは", "目元を覆って首を振っていた"),
            mako.talk("何やってるんですかー？", "$taroさっさと行きましょうよ"),
            h.deal("その巨大な橋を前に躊躇している二人の男性を尻目に",
                "ピンクのおかっぱ頭に尖り帽子を乗せた少女$n_makoは既に真ん中あたりまで橋を渡ってしまっている。",
                "声を掛けながら手を振るが", "特にびくびくした様子もない"),
            yula.talk("いつまでも見てないで", "ほら", "さっさと渡る。", "時は金なりよ"),
            h.deal("橋の支柱にしがみついて動こうとしない赤頭のお尻を叩き",
                "すらりとした金髪の女性が通り過ぎて行く。",
                "自称大盗賊の$yulaだ。",
                "彼女の足取りも軽快なもので", "落ちるという恐怖からは程遠い"),
            yusha.talk("まあ……大丈夫だろ。", "ほら$sol。", "行くぞ。",
                "みんなで渡れば恐くないって"),
            sol.talk("ヤダよ！", "てかみんなで渡ったら余計に落ちる確率上がるだろうが！"),
            h.deal("一人だけ嫌がる$solを無理矢理に引っ張り", "$Sである少年も女性陣二人に続く"),
            h.look("足元を丸太が何本も真っ直ぐ対岸まで伸びている。",
                "切れ目はなく", "どこで調達したのかも分からないようなしっかりとした木だ。",
                "その上にタイル状になった薄い石が並んでいる。",
                "隙間は粘土で埋めてあるようだったが", "$Sは城下町の建物では見かけたことのない技術だな", "と少し感心した"),
            h.look("谷はちょうど元川が流れていた場所に沿って続いていたが", "見える範囲に別の橋が架けられているようなことはない"),
            h.deal("$gmapではしっかりとこの橋が描かれ", "谷に沿って少し北側に歩くと$st_town3村の表記があった"),
            sol.talk("……たくよ", "$meは高いところと暗い場所は苦手なんだよ"),
            h.think("何とか橋を渡り切った$solがそうぼやいたが",
                "恐いものなら何でも駄目なんじゃないかと$Sが思ったことは心の中に仕舞っておいた"),
            )

def sc_re_vila(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    man = w.vilaman1
    return w.scene("村再び",
            h.deal("右手に谷を見ながら道のない平原を北へと進む。",
                "ほどなくして$st_town3村らしきものが見えてきたのだが",
                "$Sの記憶にあったあの木の柵で覆われた何世代か昔の村の趣《おもむき》とは打って変わって",
                "村の入り口には賑やかなアーチが掲げられていた"),
            yusha.talk("$st_town3村へようこそ……こんなのあったっけ"),
            sol.talk("ん？", "何だ$yusha。", "お前城下町から一歩も外に出たことないとか言ってなかったっけ？"),
            h.deal("色鮮やかな花で飾られた門柱とその上のアーチを眺めて声を漏らした$Sに",
                "$solが疑問を投げかけたが「ああ、いやいや。ほら$phoneで見たことあったから」と誤魔化しておいた"),
            mako.talk("なんか$townlogだと生スライム料理が特産だって書いてますよ", "$taro"),
            h.deal("既にアーチを潜って中に入っている$n_makoは手にした$phoneを見ながらそう声を掛けて笑っているが",
                "その言葉を耳にした$solと$yulaは揃って「生スライム。うぇ」と顔を歪める"),
            man.talk("おお", "あんたら旅の人か。", "最近めっきり減っちまったがここは$st_valley1のお陰か割と安全地帯だ。",
                "安心して楽しんでいってくれよな"),
            yusha.talk("え？", "あの谷って$n_goblinの名前がついてるの？"),
            h.deal("ああそうさ。", "と村の男は逞しい顎髭を撫でながら頷く"),
            man.talk("何でも祖父さんたちから聞いたところだと",
                "昔はここらに大量の$n_goblinの巣があったんだって。",
                "中には川を堰き止めてそこに巨大な巣を作ったって話もあったな。",
                "ところがある日", "名も知らぬ冒険者がそいつらをみんな破壊してくれたんだがよ……どうもその時に使った魔法だか何だかの所為で",
                "この大きな地割れができてそれが$st_valley1になったって", "$myなんかは聞いてる"),
            h.deal("その話を$S以外は「ふーん」と適当に聞き流していたが",
                "彼だけは必死に自分の$phoneに書き込んでいた"),
            h.think("特に地図にあった遺跡について男に質問し", "それがかつて$n_goblinの巣の一つだったんじゃないかと云われていることまで聞き出した"),
            mako.talk("$taro？"),
            yusha.talk("おう$mako。", "今行くよ……どうもありがとうございました"),
            h.deal("$Sは男に頭を下げ", "小走りで三人に追いつく"),
            h.look("$st_town3の町並みは以前とすっかり変わっていた"),
            h.look("メインストリートは整備され", "脇には看板を掲げた木造りや煉瓦造りの店が並ぶ。",
                "それはまるで$st_homeregion城下町の一画と言っても差し支えない"),
            sol.talk("お", "なんか美味そうなもん焼いてるな"),
            h.deal("$solが反応したのは店先に石で作った簡易の竈《かまど》を用意し",
                "その上で鉄のフライパンを熱して粉を練ったものを平たく伸ばして焼いている", "香ばしい匂いのする食べ物だった。",
                "焼き上がったそれで何かを巻いて食べるらしい"),
            man.talk("お？", "そっちの赤い兄ちゃん。", "食ってくか？",
                "$slimegalette"),
            sol.talk("また$n_slimeかよ。", "いいよ$n_slimeは……"),
            yusha.talk("あ、じゃあ$me一つください"),
            sol.talk("おい$yushaマジかよ。", "$n_slimeだけはやめとけって"),
            h.deal("何故か必死に$solは止める"),
            yusha.talk("何で？", "美味そうじゃん"),
            h.deal("しかし$Sは忠告を聞かず",
                "茶色く色づいて焼けた熱々のそれを受け取る。",
                "中に包んであるのは焼いた$n_slimeということだが", "どう見ても黒光りしたナメクジのようなものだ。",
                "それが僅かに蠢く"),
            yula.talk("ちょっと$taro。", "なんであんたそんなもん買ってんのよ！"),
            h.deal("他の店を見ていた$yulaは$Sの手にそれがあることに気づき", "あからさまに表情が歪む"),
            yusha.talk("いや", "美味そうだと思って……熱っ！"),
            h.deal("齧り付いた$Sの口から黒くて粘性の強い何かがどろりと出ていたが",
                "それは落ちていかずにずっと顎の当たりでウニョウニョと奇妙な屈伸を繰り返している"),
            yula.talk("こっち見ないで！", "さっさと口の中に仕舞いなさいよ、もう！"),
            h.deal("$yulaは顔を背けたままさっさと歩いて行ってしまう"),
            yusha.talk("美味いのになあ……じゅる"),
            h.deal("吸い込むと一瞬唇に張り付いたが", "$Sはそれを強引に指で押し込んだ"),
            mako.talk("美味しいですね、$taro"),
            h.deal("隣にやってきた$n_makoも$Sと同じように$slimegaletteを食べながら", "笑顔でそう言う"),
            h.look("$Sは彼女の口の端から伸びてウニョウニョしている焼き$n_slimeを気にしつつ",
                    "ひとまず宿を見つけようと歩き出した"),
            )

## ep42 scenes
def sc_inn(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    return w.scene("村の宿",
            h.be(w.stage.town3, w.day.awake5),
            h.deal("$st_town3村に宿は三つも見つかった"),
            h.deal("$Sが$n_makoに教わって$phoneで調べてみると",
                "どうやら最近都市部ではなく郊外の町村に宿を建てて回っている$st_apahotelグループというのがあって",
                "二つはその系列だった"),
            yusha.talk("これが……宿？"),
            h.look("総大理石造りに見える三階建ての四角い建物だった。",
                "$Sは年老いた夫婦が二人で切り盛りしているような小さな民宿を想像していたが",
                "入り口には制服姿のスタッフがいて道行く人に挨拶をしている"),
            sol.talk("最近はこういうのがボコボコ建ってくれてるお陰で",
                "どこ行ってもそうそう宿には困らねえんだ。", "$meみたいな貧乏冒険者にゃちと高いがな"),
            h.deal("赤い短髪の後頭部を掻き毟りながら$solがそう言うと",
                "「そう？」という興味無さそうな視線を向けて$yulaが先に入っていく"),
            mako.talk("あ、$meここの会員アプリ持ってるんで少しお安く泊まれますよ。",
                "二人部屋二つで$meと$taroが一緒でいいですよね？"),
            yusha.talk("え？", "四人一緒じゃないの？"),
            h.deal("腕組みをしたまま建物を見上げる$solを無視して$n_makoが$Sに尋ねたが",
                "$Sの方はどうも男女分けて泊まるという考えはなかったらしい"),
            mako.talk("えー！？", "それじゃあこの何も考えてないバカ男と一緒の部屋なんですか！"),
            sol.talk("んあ？"),
            h.deal("その何も考えていない長身の男は二人を見る。",
                "$Sは「みんな一緒が楽しいんじゃん」と言うが",
                "どうにも$n_makoの方は部屋を分けたいようだ"),
            yula.talk("何やってんの？", "もうチェックイン済ませたわよ？"),
            h.deal("しかしそんな三人とは打って変わって淡々と事務処理をした$yulaにより",
                "女性二人", "男性二人という部屋分けして手続きを済ませられてしまった"),
            w.tag.symbol("◆"),
            h.deal("部屋は二階で", "階段を上がるとまるでお城の中のような絨毯が敷かれた通路が伸びていて",
                "$Sたちは案内された一番突き当りの", "通路を挟んで対面の部屋にそれぞれ入った"),
            sol.talk("んでよー$yusha", "宿取ったっつーことはやっぱり地図にあった遺跡に行くつもりなのか？"),
            h.deal("部屋は簡易の木製ベッドが二つあるだけの質素な造りだったが",
                "それでも石の床に直に横になるよりはマシだ。",
                "$Sはズタ袋を肩から下ろして壁際に置くと薄い布団の置かれたベッドに腰を下ろしてみた。",
                "自分の家のそれより上等に思える"),
            sol.talk("$yushaはさ", "旅に出ておいて今更なんだけど",
                "本気で魔王退治とかするつもりなのか？"),
            yusha.talk("ん？", "急にどうしたんだ？",
                "ひょっとしてアレか$sol君よ。",
                "今更になって怖気づいたってことかな？"),
            sol.talk("ちげーよ！",
                "お前は王様から$yumark渡されて勇者認定されたってだけで魔王退治とか騒いでるけど",
                "$meたちは魔王がどこにいるかも分からず",
                "付き添いに屈強な兵士とかも借りられず",
                "船や馬車も準備してもらえず",
                "何つーかほら", "裸で野外に放り出されたみてえなもんだろ？",
                "そんな状況でも魔王退治しますとか", "どうなんだろうなって急に思ってさ"),
            h.deal("突然真面目なことを語り出した$solに",
                "$Sは当惑の表情を向ける"),
            yusha.talk("いやいや。",
                "$solだって魔王退治したら賞金いっぱい出るし",
                "何も知らないっぽい$meだけじゃ不安だから付いてってやろうって",
                "そう言ってたじゃんか"),
            sol.talk("まあそれはそうなんだけどさ",
                    "城下町を出て一日目だってのに",
                    "もう何日も旅をしたような気分になってんだよ。",
                    "何だろうな"),
            h.think(""),
            # NOTE: 宿は新しかった
            )

def sc_ruins(w: wd.World):
    h = yusha = w.yusha
    sol, mako, yula = w.sol, w.mako, w.yula
    return w.scene("遺跡なう",
            # NOTE: 遺跡でゴブリンダムの痕跡、何があったんだ？　壊れたスマフ（最新型）
            )

# episodes
def ep40(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_restart(w),
            )

def ep41(w: wd.World):
    return (w.chaptertitle(TITLE[1]),
            sc_bridge(w),
            sc_re_vila(w),
            )

def ep42(w: wd.World):
    return (w.chaptertitle(TITLE[2]),
            sc_inn(w),
            sc_ruins(w),
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
    return (w.maintitle(cnf.TITLE["chap4"]),
            ep40(w),
            ep41(w),
            ep42(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

