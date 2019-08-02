# -*- coding: utf-8 -*-
"""Chapter 01-02: The pants.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.sagepants import config as cnf


# scenes
def sc_Iampants(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("俺はパンツだった！？",
            hero.be(w.stage.prison, w.day.firstmeet),
            hero.look().d("見下ろした薄く輝く水面には",
                "一枚の幼女向けパンツを手にして立つ",
                "グラマラスな女性が映し出されていた。",
                "彼女はその肢体を大量の自身の紫色をした頭髪によって覆い隠している為",
                "乳頭や下腹部は見えないものの",
                "それでも布地面積の少ない水着を着ているようなものなので",
                "$meからしてみれば目のやり場に困るな",
                "という印象だ"),
            hero.think().d("いや",
                "そんな冷静に彼女について語っている場合ではない"),
            hero.talk().t("どうして$meはパンツなんだ！？"),
            hero.look().d("思わず考えていることが声になったが",
                "パンツの前面に付いている犬のイラストは微動だにしない。",
                "一体どこから声が出ているのだ"),
            ery.talk().t("声が出ているように聞こえるだけで",
                "実際には声など出ておらぬ"),
            hero.hear().d("女は溜息混じりにそう言った"),
            hero.think().d("しかしそもそもその声が聞こえるということはパンツである$meにも何かしらの聴覚は備わっているのだろう"),
            hero.think().d("パンツの聴覚って何だ？",
                "又布が震えるのか？"),
            hero.think().d("考えれば考えるほど頭が痛くなってくる。",
                "しかも現在その痛くなる頭すら持ち合わせていないのだ。",
                "何故なら$meはパンツだから"),
            ery.ask().t("何をしょぼくれておる？",
                "折角こうして$meと対話できるように視覚と聴覚を与えてやったというのに",
                "不満なのか？"),
            hero.talk().t("あんたが見えるようにしてくれたのか？"),
            hero.look().d("彼女の形の良い顎がコクリ", "と一つ頷いて見せる"),
            hero.think().d("ああ、なんだ。",
                "これは夢か"),
            hero.think().d("そう納得することを何故一番最初に思いつかなかったのか",
                "$meは自分の勘の悪さを嘆いた"),
            hero.think().d("そもそも人間が目覚めたらパンツになっていたというのは",
                "夢以外の何物でもないじゃないか。",
                "それなら目の前に裸の女がいても不思議じゃないし",
                "パンツである$meが彼女と話したりしていても誰も笑わない"),
            hero.talk().t("なあ。", "ちょっと確認したいことがあるから",
                "ひとつ$meの頬を抓ってみてくれないか？"),
            ery.ask().t("お主の頬とはどこのことだ？"),
            hero.look().d("彼女は$meを持ったまま怪訝な表情になってそう尋ねる"),
            hero.think().d("言われてみればその通りだ。",
                "パンツの頬とはどこだろう？",
                "そもそもパンツに頬というか", "顔という概念はあるのだろうか"),
            hero.think().d("もし今ここに別れた彼女がいてくれたなら教えてもらえたかも知れない"),
            hero.remember().emphasis("$herword3"),
            hero.think().d("そんなことを言っていたことを不意に思い出し",
                "ますます$meはここがただの夢の中なのだと実感した"),
            hero.talk().t("頬はよく分からないから",
                "そうだな。",
                "代わりに踏みつけてくれないか？"),
            ery.talk().t("ほお……"),
            hero.look().d("そう提案した$meを彼女はまじまじと見つめる。",
                    "悪戯っぽく赤い舌を覗かせて「そうかそうか」と舌舐めずりまでする"),
            hero.think().d("それを目にした瞬間背筋を悪寒が登っていった気になったが",
                    "パンツに背筋なんてものはなかった"),
            hero.talk().t("え……"),
            hero.deal().d("唐突に視界が上を向く"),
            hero.look().d("$meはそのまま暗い天井を見上げながらゆっくり落ちていくと",
                    "ぴたりと地面に張り付いた……おそらくそうだろう。",
                    "視界が動かなくなり",
                    "彼女が見下ろしているのが分かったからだ"),
            ery.talk().t("お主はそういう趣味の持ち主だったとはな……"),
            hero.talk().t("な、何か勘違いしてないか？"),
            ery.talk().t("では遠慮なく……"),
            hero.think().d("彼女には$meの言葉は届いていないようだった"),
            hero.look().d("すっと視界に入り込んできた女性の右足の裏は白く発光していて",
                    "ああ、人間の足の裏というのは意外と綺麗なものなのだな",
                    "という$meの素朴な感想を引っ張り出す"),
            hero.look().d("形の良い縦長の楕円の踵部分が仄かに赤らみ",
                    "少し窪んだ土踏まずを経由して上半分のつるりと目立つ母趾までの緩やかな曲線が心地よい。",
                    "その上に生えた五本の柔らかい茸のような指はしゃぶりつきたくなるような膨らみになっていて",
                    "それがどんどん大きくなる"),
            hero.look().d("いや", "迫ってくる"),
            hero.look().d("そう気づいた時には視界が暗くなり",
                    "何も分からなくなった"),
            ery.talk().t("どうだ？",
                    "お望み通りにしてやったが……"),
            hero.talk().t("何も分からん"),
            hero.think().d("踏まれている",
                    "ということだけは理解したが",
                    "痛みも苦悶も喜びも何もなかった。",
                    "ただ彼女のささやかな笑い声と何度か上下する足の裏だけを感じ取ることができた"),
            ery.talk().t("それはそうだろう。",
                    "お主に与えたのは視覚と聴覚のみで",
                    "痛覚や触覚までは持ち得ていないのでな"),
            hero.talk().t("それなら$meはどうやってこれが夢か現実かを見分ければいいんだ？"),
            hero.hear().d("そう尋ねた$meを",
                    "彼女は盛大に笑う"),
            hero.ask().t("何がおかしい？"),
            ery.talk().t("まだ己のことがよく理解出来ていないようだと思ってな"),
            hero.look().d("彼女はそう言うと",
                    "パンツである$meを持ち上げて座る。",
                    "自分の目線まで引っ張り上げると",
                    "言い聞かせるようにして「教えてやるが」と前置きした"),
            ery.talk().t("お主は$meが次元に穴を開けて何とか手繰り寄せることが出来た唯一の物なのだ。",
                    "それが意志を持っていたというのは驚きだが",
                    "退屈凌ぎに気まぐれな神が遣わした存在かも知れぬな。",
                    "しかし五百年も世間に顔見世をしていないと$meを知らぬ存在もいるということか"),
            hero.look().d("彼女は小さく溜息をついたが",
                    "$meはそれよりも頭の悪い作家が考えた不出来な映画かアニメーションの設定を聞かされたような気分で",
                    "次元だ何だという話に嘆息したくなった"),
            hero.talk().t("じゃあ訊くが",
                    "今の話からすると",
                    "あんたが$meをパンツにしたと考えて良いってことだな？"),
            ery.ask("パンツとは何だ").t("$meはお主を呼び寄せただけでそれ以外は何もしておらぬが……その前に一つお主に尋ねたいことがある。",
                "先程から何度も言っている”パンツ”とは一体何なのだ？"),
            )

def sc_whatpants(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("パンツとは何だ？",
            hero.explain("パンツ説明"),
            hero.know(w.pants),
            hero.think().d("パンツとは何なのか"),
            hero.think().d("それを$meは即座に「下着のことだ」とは言えなかった。",
                "何故なら三年前に別れた彼女の遺言にも似た最後の言葉が、"),
            hero.hear().emphasis("$i_herword002"),
            hero.think().d("だったからだ"),
            ery.ask().t("どうした？",
                "何か答えるのに不都合でもあるのか？"),
            hero.talk().t("あんたはパンツを身に着けていない。",
                "それに加えて裸のようだ。",
                "だからひょっとしたら下着を含めた衣類を身に着けるという文化がないのかも知れない。",
                "そういう前提で話させてもらうが",
                "いいか？"),
            hero.look().d("彼女はその言葉に眉を顰めていたが",
                "ゆっくりと縦に首を振ったのを確認すると",
                "$meは滔々とパンツについて語り始めた"),
            hero.talk().t("パンツとは股間を含めた下腹部の一部を覆う着衣の一種だ。",
                "着衣",
                "つまり服を着ることで様々な恩恵を受けることができる。",
                "中でも下着と呼ばれるものは肌着とも呼ばれ",
                "皮膚の上に直接身に着けるように設計されている"),
            hero.look().d("最初は首を傾げ気味だった彼女も",
                "$meが仕事の時のような語り口になったからか",
                "集中して聞き入っているように見えた"),
            hero.talk().t("人間というのは思っている以上に日々汚れ",
                "またその常在菌と呼ばれる微生物は皮膚の上で老廃物となり蓄積する。",
                "そういう体表上の汚れ", "あるいは汗のような分泌物を下着は吸収し",
                "それを付け替えることで人間は己の体を清潔に保つという手段を手に入れたんだ"),
            hero.look().d("長い髪で覆い隠されていたが",
                "彼女は自分の股間を確かめるように見下ろしつつそこをもぞもぞとさせた"),
            hero.talk().t("その肌着の内で主に股の部分を中心に覆うようになっているものがパンツだ。",
                "あんたがさっきした",
                "その",
                "おしっこのように",
                "人は食べたもの飲んだものを排出する。",
                "そこはとても不衛生となる。",
                "だからこそ普段パンツで覆い",
                "生活することで",
                "自分を", "そして周りを汚染せずに済むという訳だ"),
            hero.think().d("もっと言えばデザインやオシャレといった精神性の問題もあるが",
                "目の前の女にそういった説明をしても混乱を招くだけだろうと思って敢えて省いた"),
            hero.talk().t("パンツが何か", "分かったか？"),
            ery.talk().t("そうだな……つまりだ。",
                "パンツとは身に着けるものであり",
                "$meは今裸だ。",
                "本来であれば$sagerobeという法衣を身に着けておったのだが",
                "事情があって今", "$meの手元にはないのだ"),
            hero.look().d("彼女は$meの端を両手で持ったままにっこりと笑みを向ける"),
            hero.talk().t("わ、分かってくれたなら良かったよ"),
            hero.feel().d("ぞわり", "という妙な悪寒に$meの警戒心が顔を覗かせた"),
            hero.look().d("何だろう。",
                    "彼女は$meの両端を持ったまま立ち上がると",
                    "その紫の髪で胸元から下までを覆い隠しているのが改めてよく見えた。",
                    "その片方の足が", "不意に持ち上がる"),
            hero.look().d("右足だ"),
            hero.look().d("続いて少し背を曲げるようにして屈み込むと",
                    "$meの視界はぐんぐんと下降していき",
                    "ほど良い二つの丘から",
                    "肉付きのよい腹部",
                    "形の良い臍を経て",
                    "何もないつるりとした彼女の下腹と",
                    "その先に存在するであろう女性の排泄器官までが見えてしまう"),
            hero.look().d("そう思った瞬間だった"),
            ery.ask().t("ところでお前には前と後ろがあるのか？"),
            hero.talk().t("パンツの前後ろのことだったら",
                    "確かに存在する。",
                    "犬のイラストが付いている方が前だ"),
            hero.think().d("そう答えながらも$meは何を言っているのだろう",
                    "という意識がどうしても脳裏から離れてくれない。",
                    "そればかりか",
                    "彼女の質問からはどう考えても",
                    "ある結果しか導かれないではないか"),
            ery.talk().t("そうか。",
                    "ならばこういうことか"),
            hero.look().d("刹那",
                    "$meの視界は横回りで百八十度振り回され",
                    "この薄暗い空間の壁へと向けられる"),
            hero.feel().d("それに続いて自分のお腹が内部から広げられたような",
                    "何とも胸苦しさを覚える感覚が湧き上がり",
                    "もそもそと何かが動く気配を背中側に強烈に感じさせられた"),
            hero.talk().t("あぅ！？"),
            hero.feel().d("何かが",
                    "$meの右半身を貫いていった"),
            hero.think().d("痛みを伴った衝撃ではないが",
                    "何と表現したものだろう。",
                    "ムズムズとするような", "痛痒感とでも呼べばいいのだろうか。",
                    "それがずっと右半分に張り付いている"),
            hero.feel().d("けれどそれはすぐ残りの左半分にもやってきた"),
            hero.talk().t("ひゃう！"),
            ery.talk().t("妙な声を上げるでない"),
            hero.talk().t("け、けどな。",
                    "あんた一体何をしたんだ？"),
            hero.look().d("一瞬潰れたように歪んだ視界は",
                    "今は明瞭だった。",
                    "少しは目も慣れてきたのだろう。",
                    "壁は岩肌で",
                    "視界の切れ端に鉄の棒のようなものが見える"),
            ery.talk().t("ほお……これは", "なかなかに"),
            hero.feel().d("彼女の手が",
                    "$meに触れる。",
                    "それは分かる。",
                    "けれどその内側にあるものは一体何だ"),
            hero.think().d("考えろ。",
                    "今どういう状況なんだ"),
            ery.talk().t("何をごちゃごちゃと言っておる。",
                    "お主はパンツ。",
                    "そして$meは外見上は人間の姿をしておる。",
                    "ならば自ずと答えは導かれよう"),
            hero.talk().t("嘘、だろ……"),
            hero.hear().d("彼女は声を殺して笑う"),
            hero.look().d("確かに少し考えれば分かることだった。",
                    "さっき彼女に持たれていた時よりも随分と視界が低い。",
                    "それは彼女の顔の高さより低い位置だということだ。",
                    "それに目の前には部屋の様子が広がっていることから",
                    "彼女の方を見ていないということになる"),
            hero.think().d("自明", "というやつだ"),
            hero.think().d("そうだ。",
                    "つまり$meは彼女に……"),
            hero.talk().t("履かれているのか！？"),
            ery.talk().t("お主が言ったではないか。",
                    "パンツは履くものだと"),
            hero.think().d("そう認識した瞬間",
                    "自分の内側に女性のアレやソレやコレが密着しているのだということに気づいて",
                    "$meは思考に急ブレーキを掛けようとした"),
            hero.deal(ery, w.i.equip),
            ery.deal("身に着ける", hero),
            ery.deal(hero, "装着"),
            hero.feel("衝撃"),
            hero.remember("彼女の格言"),
            )

def sc_herstatus(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("彼女の状況",
            ery.talk().t("な、何だこれは……"),
            hero.hear().d("$meを身に着けている彼女が声を上げ",
                "急に蹲った"),
            hero.think().d("もちろん本当に蹲ったのかどうかは分からないから$meの推測だが",
                "大きく陰になり視界が暗がりになって地面が近づいたことと",
                "何より彼女の張りの良い太腿が眼下からやや上方へと移動したから",
                "おそらくそうなのだろう"),
            hero.ask().t("大丈夫か？"),
            hero.hear().d("その問いかけに彼女は答えない"),
            hero.look().d("それよりも光っていた皮膚が明滅し",
                "小刻みに震えているように見える"),
            hero.ask().t("なあ、本当に……"),
            ery.talk().t("うる、さい……"),
            hero.hear().d("くぐもった声だった"),
            ery.talk().t("お主",
                "一体何を……なにをしたんだ？"),
            hero.think().d("ん？"),
            hero.feel().d("違和感だった"),
            ery.talk().t("力が……$Iの力が！"),
            hero.think().d("何か呻いているが",
                "それよりもずっと",
                "彼女の声の変化に気を取られていた"),
            hero.ask().t("今あんたに何かあったら$meはただのパンツだからとても困るんだが。",
                "大丈夫じゃないなら医者を呼ぶなり何なりしてもらった方が良いんじゃないか？"),
            ery.talk().t("何を訳の分からんことを言っておる！",
                "$Iは七日間で世界を滅ぼすと言われた大賢者様だぞ！",
                "多少のことがあったところで……"),
            hero.hear().d("何だよ？"),
            hero.hear().d("そう問い返したいと思ったところで",
                "彼女の言葉が途切れる"),
            hero.ask().t("何だ？",
                "大丈夫か？",
                "なあ？"),
            hero.hear().d("返事がない"),
            hero.look().d("それに体表の妙な明滅も終わった"),
            hero.think().d("$meはパンツのままでこの状況を何とかする術はないだろうかと必死に思案したが",
                "ない。",
                "どう頑張ったところでパンツはパンツだ。",
                "今$meを装着している彼女の涙を拭ってあげられる訳じゃない。",
                "涙を拭うなら",
                "それは彼女自身にしか出来ない"),
            hero.remember().d("それに思い至ると",
                "急に元彼女から「$herword004」と言われたことを思い出した"),
            hero.talk().t("なあ本当に"),
            ery.talk().t("……だいじょうぶだ"),
            hero.hear().t("それは明らかに今までの彼女の声ではなかった"),
            ery.talk().t("$Iが大丈夫といったらだいじょうぶなの！"),
            hero.think().d("話し方も先程までの威厳に満ちた物言いではなく",
                "どこか子供じみた",
                "それこそ駄々をこねているみたいに感じる"),
            hero.talk().t("分かったけど……やっぱあんた変だぞ？",
                    "それとも自覚してないのか？"),
            ery.talk().t("変とか言うなぁ！",
                    "$Iがだいじょうぶと言ったらだいじょうぶなの！"),
            hero.talk().t("なあ",
                    "立ち上がって$meにもう一度姿を見せてくれないか？",
                    "頼むよ"),
            hero.think().d("どうしても確認したかった。",
                    "声の変化と",
                    "それが聴こえてくる場所の近さ",
                    "それに暗がりで見えている彼女の二つの腿の質感に",
                    "長さ。",
                    "それは$meの予想が間違っていなければ",
                    "彼女のある変化を示していた"),
            ery.talk().t("な、何故そんなことを頼むんだ？"),
            hero.talk().t("なあ大賢者様。",
                    "もう一度自分がパンツだってところを確認しておきたいんだ。",
                    "頼むよ"),
            ery.talk().t("そうまで言うなら……仕方ないな"),
            hero.think().d("明らかに今までの彼女とは違っていたが",
                    "何とか承諾してくれたようだ"),
            hero.look().d("視界が徐々に上向き",
                    "そこに水面を捉えることができるようになる"),
            ery.talk().t("少しだけだからな"),
            hero.think().d("何故そんなことを彼女が口にしたのかは",
                    "水面に映った$meと",
                    "$meを履く女性の姿を目にすることで理解した"),
            hero.talk().t("嘘……だろ"),
            hero.think().d("想定はしていた。",
                    "けれど",
                    "実際に目にしたそれは$meの予想を遥かに超えていて",
                    "パンツに後頭部はないが",
                    "それをガツンと金属バットで殴られたかのような衝撃だった"),
            hero.talk().t("幼女に", "なってる！？"),
            hero.look().d("$meを先程まで履いていたあのグラマラスな女性の姿は消え",
                    "水面に映っていたのは",
                    "身長百三十に満たないと思えるぷっくりほっぺで目元を泣きそうに赤くした",
                    "紫髪の女の子だった"),
            hero.deal("状況を理解したい"),
            hero.ask(ery, "色々"),
            ery.explain("閉じ込められたこと等"),
            ery.talk("大賢者"),
            ery.deal("パンツ履こうとする"),
            )

def sc_named_taro(w: wd.World):
    hero, ery = w.hero, w.ery
    return w.scene("名前はタロウ",
            ery.deal(hero, "タロウ"),
            hero.ask("彼女の名前"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("冒頭"),
            sc_Iampants(w),
            )

def ep_main(w: wd.World):
    return (w.chaptertitle("パンツ装着"),
            sc_whatpants(w),
            sc_herstatus(w),
            sc_named_taro(w),
            )

# outline
def baseinfo(w: wd.World):
    return [
            ("chapter 1-02", story(w), w.hero, w.ery),
            ]

def outline(w: wd.World):
    return [
            ("chapter 1-02", story(w),
                w.hero.deal("状況を理解したい"),
                w.hero.know(w.pants),
                w.hero.ask(w.ery, "色々"),
                w.ery.deal(w.hero, "装着"),
                True),
            ]

# main
def story(w: wd.World):
    return (w.maintitle("ニ枚目：美女とパンツ"),
            ep_intro(w),
            ep_main(w),
            )

def main(): # pragma: no cover
    from src.sagepants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

