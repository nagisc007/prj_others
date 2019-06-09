# -*- coding: utf-8 -*-
"""Story: the kyoko-san
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.kyoko import config as cnf


# scenes
def sc_gotojob(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("仕事に出掛けてしまった",
            kyoko.think().d("$hiiragiの「いってきます」が恐くなったのは",
                "いつからだろう"),
            w.kyoko.be(w.stage.apart, w.day.current, w.hiiragi),
            hiiragi.ask().t("$kyoko？"),
            kyoko.hear().d("彼は$meの名を呼んで", "朝七時五分の苦笑を浮かべる"),
            hiiragi.talk().t("$kyoko", "手"),
            kyoko.talk().t("あ", "ごめんなさい"),
            kyoko.behav(hiiragi, "手を離さない").d("口ではそう言ったけれど",
                "握っている彼の右手を離してしまったらもう二度とその優しさが戻ってこないんじゃないかと思うと",
                "そんなに簡単に解放してあげる訳にはいかない"),
            kyoko.ask("いつ帰ってくる").t("今日は何時頃？"),
            hiiragi.reply(kyoko).t("そうだね……"),
            kyoko.look().d("右斜め三十度くらいを見て", "思案する。",
                "その時に右の眉だけ下がって唇がキスできそうな具合に尖るのが心地良い"),
            kyoko.think().d("けれどそこに自分の唇を乗せようとすると彼は怒るので",
                "$meは必死に我慢する"),
            kyoko.think().d("$hiiragiとの同棲はいつも", "$meの我慢と彼の妥協によって成り立っていた"),
            hiiragi.talk().t("残業がなかったら六時までには帰ってくるよ"),
            kyoko.talk().t("そっか。",
                "じゃあ今日は", "豚汁にしようかな"),
            hiiragi.talk().t("それなら秋刀魚でも一緒に買ってくるよ"),
            kyoko.behav().d("$hiiragiは絶対に嫌と言わない。",
                "好き嫌いはないのだと", "出会って間もない頃に教えてくれたけれど",
                "それが本当なのかどうかは未だによく分からない。",
                "そもそも$meじゃなくいつも彼が台所に立つのだから",
                "彼の嫌いなものは並べないだろう。",
                "今まで奇跡的に$meの食べたいものの中に彼の大嫌いがなかっただけ",
                "という可能性が有力だと思っている"),
            hiiragi.talk().t("じゃあ"),
            kyoko.think("不安").d("あ……"),
            kyoko.look().d("驚くほど前置きなく$meの手は解かれて",
                "世界の全てがスローモーションになったみたいに彼の体が反転する。",
                "紺の背広の大きな背中が向けられて", "アパートの重いスチールドアは閉まろうとする"),
            kyoko.think().d("待って"),
            kyoko.deal().d("という声が掛けられないまま$meは自分の自由にされてしまった右手を虚空に置いて",
                "右足をサンダルに通そうとした"),
            kyoko.deal().d("耳が痛くなるような大きな音を立ててドアは閉まり",
                "$meのオリーブ色のペディキュアが禿げた右足を嫌ったサンダルは転がって寝そべった"),
            kyoko.look().d("それを見て力なく座り込むと",
                "ドアに開いた覗き窓の小さな穴だけが希望の光みたいに明るくて",
                "でも$meは立ち上がってそこから希望を覗く気力もない"),
            kyoko.look("青すぎる空").d("今日の天気予報は夜までずっと快晴だと言っていたから",
                "$meは外に出たら消滅してしまうだろう。",
                "まだ夏が遠いのに",
                "どうして世界はこんなにも光に満ちているのだろう"),
            kyoko.think().d("$meの心にはあの日からずっと",
                "分厚い雷雲が掛かったままだというのに"),
            w.kyoko.do("wait", w.hiiragi),
            w.hiiragi.go("仕事に出た"),
            w.kyoko.be("部屋で一人").d("このまま座り込んでいても$hiiragiは帰ってきてはくれない。",
                    "そんなため息と共に立ち上がろうとした時だった"),
            kyoko.feel("孤独"),
            w.kyoko.deal("宅配が届く").d("無機質なインタフォンが鳴らされた"),
            )

def sc_delivered(w: wd.World):
    kyoko, hiiragi, deliverman = w.kyoko, w.hiiragi, w.deliverman
    return w.scene("宅配便",
            kyoko.be(w.stage.apart, w.day.current),
            kyoko.behav().d("その音に",
                "思わず自分の胸の前に腕を被せる。",
                "それからゆっくりとキャミソールのＵの字になった空間に視線を入れ",
                "ブラの存在がないことを確認した"),
            kyoko.feel("宅配に怯える").d("そんな$meのことなんて無視して二度、三度と続けて鳴らされるが",
                "反応がないことに苛立ったのだろう。",
                "今度はドアを拳でノックして「すみません。宅配便ですけど」と", "いがらっぽい声を響かせた"),
            kyoko.think().d("どうしよう"),
            kyoko.feel().d("大したものはないけれど",
                "それでもノーブラ女が朝から男を送り出したままの格好で何気なく宅配を受け取りに出るなんて",
                "$hiiragiは何て言うだろう"),
            kyoko.think().d("何でも許してくれそうな優しげな顔をしているのに",
                "彼は意外とマナーや身なりといったことに煩い"),
            kyoko.think().d("だからきっとこのままドアを開けてしまったらとても悲しむし",
                "それを知った時点で「別れよう」と言い出すかも知れない"),
            kyoko.talk().t("ちょっとだけ", "待ってもらえませんか……"),
            kyoko.think().d("小さくて震えた声だったと思う。",
                "でもそれが聞こえたのか",
                "「早くして下さいよ」という返事があって",
                "$meは一つ吐息を落として立ち上がると",
                "上着を取りにリビングに戻った"),
            kyoko.deal("宅配応対"),
            kyoko.think("居留守"),
            deliverman.talk("柊の名"),
            kyoko.talk("ちょっと待って"),
            w.tag.comment("今日子外見とか服装の記述"),
            kyoko.look().d("我が家と呼ぶと$hiiragiが笑顔で「君の家じゃない」と指摘するのだけれど",
                "それでも$meにとってはもうここ以外に家と呼ぶべき場所がなくて",
                "だからこそ愛着も執着もそれなりに湧こうと言うのに",
                "彼は出会った当初からそういった点で非常にドライな一面を$meに見せてくれている"),
            kyoko.look().d("そんな我が家の八畳ほどのリビングには目立つ場所に姿見が置かれていて",
                "今そこには$meと$hiiragiの春物コートが映っている。",
                "つまり「何を着ればいいだろう」という$meのエクスキューズに一つの光明を与えてくれたのが",
                "段違い平行棒のような移動式のハンガーラックからぶら下がる彼のお気に入りのクリーム色のそれだった"),
            kyoko.look().d("襟の切り方だろうか。",
                "腰のところでボタンを合わせると", "彼なら膝くらいまでしかない丈のものが$meの膝下までを覆ってしまう。",
                "それでも相手が透視能力でも持っていない限りは", "ノーブラの防御力の低い胸元から視線を逸らせるだろう"),
            kyoko.deal("外見と服装確認").d("たぶんこれで大丈夫",
                "という自信を", "$meはいつも$hiiragiから貰っている。",
                "そういう安心感が仄かに残る彼の体臭からも滲んでいるような気がした"),
            kyoko.go("玄関").d("玄関口まで戻ると",
                "「はぁい」とわざとらしく声を出してから鍵を開ける"),
            kyoko.look().d("緑の帽子を被った男性はため息がちに「お届け物です」と言うと",
                "両手でしっかりと抱えていた段ボール箱を足元に置いた。",
                "宛名書きには$hiiragiの名前があって", "差出人の名字も同じなことを見つけると",
                "冷たい安堵が訪れる"),
            kyoko.have(w.hisfambox).d("サインをして", "彼をさっさと追い返す"),
            kyoko.think().d("何も言われなかったからこの格好は大丈夫だったということだろう"),
            kyoko.look().d("それにしてもと",
                    "$meは視線を足元の段ボール箱に向ける"),
            kyoko.think().d("重そう"),
            kyoko.deal().d("それでもこのままにしておく訳にもいかないので",
                    "何とか手を伸ばして持ち上げようとする。",
                    "箸より重いものだって余裕で持ち上げられるけれど",
                    "非労働者の細腕だと準備運動なしではどこかの筋を痛めてしまいそうな筋肉の張りを感じる"),
            kyoko.talk().t("……無理"),
            kyoko.look().d("一体何を詰め込んだらみかん箱くらいのものがこんなにも動かざること山の如しになるのか。",
                    "ひょっとして$hiiragiが屈んで中に丸まっていて",
                    "何かの記念日のサプライズ的演出をするのだろうか。",
                    "そんな無駄な妄想をしても", "中から彼は出てこない"),
            kyoko.deal().d("$meは「$hiiragi力をおらに分けてくれ」と呟いて袖まくりをすると",
                    "思い切りガニ股になってそれを引っ張り上げる"),
            kyoko.behav().d("妙な声が出た気がしたけれど",
                    "ここには$hiiragiがいないし",
                    "いたらそれこそ彼が$meの代わりに軽々とこれを部屋まで運んでくれたはずだ"),
            kyoko.talk().t("人生って残酷ね"),
            w.kyoko.look(w.hisfambox).d("腕の痛みを感じながら何とかテーブルの傍まで移動させた段ボール箱は",
                    "$meに感謝の一言もないまま鎮座している"),
            kyoko.think().d("さて", "お前をどうしてやろうか"),
            kyoko.think().d("とりあえず開けないとどうしようもないことは分かっていたけれど",
                    "彼のご家族からの送り物だということで",
                    "否応なく$meの心は防衛体制を取ってしまうのだ"),
            kyoko.deal("開ける", "破って").d("段ボール箱は真ん中の合わせの部分がぴっちりとガムテープで貼り付けられているだけでなく",
                    "四隅まで綺麗に隙きなく貼られている。",
                    "そういった仕事の丁寧さに$hiiragiみを感じて",
                    "だからこそ手を差し込んで破いてやりたくなる"),
            kyoko.deal().d("けれど$meの手は貧弱だ。",
                    "おまけに一週間前の禿げているオリーブ色のネイルをした右の人差し指の一部が引っかかって",
                    "少しヒビが入った。",
                    "もうその事実だけで泣きたくなる"),
            kyoko.behav().d("$meは$hiiragiのコートの袖を思い切り伸ばして",
                    "それで一度自分を抱き締める。", "彼の匂いがほんのり慰めてくれるけれど",
                    "顔を上げた時に部屋の中の空虚の多さを実感させるだけで",
                    "マッチポンプで$meの寂しさを増長させてしまう"),
            kyoko.think().d("$n_kyokoは寂しい生き物です"),
            kyoko.remember().d("昨夜そう言って彼に真剣な表情で首を振られたことを思い出したが",
                    "不意に顔を覗かせる$meの本性の一部を知らない顔はできない"),
            kyoko.deal().d("カッターナイフは見つからなかったから",
                    "百円ショップで買ったボールペンを突き刺して", "彼の家族の手による梱包を解体する。",
                    "音が心地よく引き裂いてくれる。",
                    "いいぞ、もっとやれ。",
                    "そんな風に$meを応援してくれる"),
            kyoko.deal().d("だから楽しくなって", "どんどんプス",
                    "と突き刺しては引き裂いてを繰り返す"),
            kyoko.look().d("でも楽しい時は一瞬で",
                    "すぐに段ボール箱は口を半開きにして中身を確かめろと無言で$meを睨みつけてくる"),
            kyoko.look(w.hiiragi, w.famphoto).d("その薄っすら開いた隙間から",
                    "何も印刷されていない封筒が見えた"),
            kyoko.deal().d("そっと取り出してみると",
                    "中に複数枚の硬いものが入っていると分かって",
                    "$meの気分は容易に地の底まで沈み込んだ"),
            kyoko.think().d("それなら見なければいい。",
                    "彼が帰ってくるまで部屋の隅に押しやって",
                    "彼の下着ででも覆い隠しておけばいいんだ"),
            kyoko.think().d("それが分かっていても",
                    "どうしようもなく$meの手は簡単に折られただけの封筒の口を開け",
                    "中の写真を取り出した"),
            kyoko.think(w.i.hisgone).d("後ろに写る空が",
                    "きっと",
                    "$meには眩しすぎるのがいけないのだ"),
            kyoko.feel("自分が泣いている").d("いつの間にか自分の頬を伝うものに気づいて",
                    "$meはその場に足をハの字に広げたまま",
                    "自分を見失った"),
            )

def sc_thinkfamily(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("彼の家族",
            kyoko.be(w.stage.apart, w.day.current),
            kyoko.remember("彼の実家の話").d("$hiiragiにはちゃんとした実家がある。",
                "それは彼が$meと違う人間で",
                "比較的まともな人生を歩んできた側に所属しているということでもある"),
            kyoko.think().d("でも彼は$meがそれを口にすることを酷く嫌う"),
            kyoko.think("彼は長男"),
            kyoko.think("幸せな家族"),
            kyoko.think("子供好き"),
            kyoko.think("自分とかけ離れている"),
            hiiragi.talk("いつかは帰らなきゃ"),
            w.kyoko.think(w.i.departing),
            kyoko.think("自分のことを話してない"),
            kyoko.think("どうすればいい？"),
            kyoko.do("涙"),
            )

def sc_herproblem(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("彼女の悩み",
            w.tag.comment("ここから今日子幻想劇場突入"),
            kyoko.be(w.stage.apart, w.day.current),
            w.kyoko.think(w.i.myreason),
            kyoko.remember("彼に拾われた時"),
            kyoko.think("絶望から救ってくれた"),
            kyoko.think("誰かがいないと立てない"),
            kyoko.think("あのまま溶けていた"),
            kyoko.think("世間の雨は酸性雨"),
            kyoko.have("雨の飴玉"),
            w.kyoko.talk().d("私の存在"),
            kyoko.think("少しだけ他人と違う"),
            kyoko.feel(w.i.anxiety),
            kyoko.think(w.i.break_anxiety),
            kyoko.look("彼のコート"),
            kyoko.have(w.coat),
            kyoko.feel("彼の臭い"),
            kyoko.look("コートが女の形になる"),
            )

def sc_breaker(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("破壊衝動",
            kyoko.be(w.stage.apart, w.day.current),
            kyoko.feel("コート女を怖れ"),
            kyoko.look("彼が別の女と楽しげに"),
            kyoko.think("醜い嫉妬だ"),
            kyoko.look("女の笑み"),
            kyoko.think("いつも羨ましい"),
            kyoko.deal("女を沈める"),
            kyoko.talk(hiiragi, "なんでいないの"),
            kyoko.look("次々知らない女になる"),
            kyoko.deal("次々沈める"),
            kyoko.do("暴れる"),
            kyoko.do("break"),
            kyoko.do("部屋を空っぽ"),
            )

def sc_sink(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("沈む世界",
            kyoko.be(w.stage.apart, w.day.current),
            kyoko.look("沈めても沈めても消えない"),
            kyoko.look("不安が形になる"),
            kyoko.look("空虚"),
            kyoko.look("不安と彼がキスをする"),
            kyoko.feel("ぷつ"),
            kyoko.think("別れ"),
            kyoko.do(w.i.sink),
            kyoko.deal("床に沈む"),
            kyoko.look("夕方の西日"),
            )

def sc_hishand(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("彼の手",
            kyoko.be(w.stage.apart, w.day.current),
            kyoko.look("心の澱の世界"),
            kyoko.look("沢山の気持ちの死骸"),
            kyoko.deal("自分ゾンビが抱きしめにくる"),
            kyoko.look("夕焼けが遠のく"),
            kyoko.hear("彼の声"),
            kyoko.talk("答えたい"),
            kyoko.hear("ゾンビの囁き"),
            kyoko.think("このまま？"),
            kyoko.deal("もがく"),
            w.kyoko.meet(w.hiiragi),
            kyoko.deal("彼の手"),
            kyoko.deal("救われる"),
            kyoko.ask(hiiragi, "いつか帰るの？"),
            hiiragi.reply("お盆に墓参りに", "一緒にくる？"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("彼との安寧"),
            sc_gotojob(w),
            )

def ep_box(w: wd.World):
    return (w.chaptertitle("贈り物"),
            sc_delivered(w),
            sc_thinkfamily(w),
            )

def ep_breakmemory(w: wd.World):
    return (w.chaptertitle("思い出を壊す"),
            sc_herproblem(w),
            sc_breaker(w),
            )

def ep_hersinks(w: wd.World):
    return (w.chaptertitle("彼女は沈む"),
            sc_sink(w),
            sc_hishand(w),
            )

# outline
def episode_basics(w: wd.World):
    return [
            ("ep1", ep_intro(w), w.kyoko, w.hiiragi),
            ("ep2", ep_box(w), w.kyoko, w.hiiragi),
            ("ep3", ep_breakmemory(w), w.kyoko, w.hiiragi),
            ("ep4", ep_hersinks(w), w.kyoko, w.hiiragi),
            ]

def episode_outlines(w: wd.World):
    return [
            ("ep1", ep_intro(w),
                w.kyoko.do("wait", w.hiiragi),
                w.hiiragi.go("仕事に出た"),
                w.kyoko.be("部屋で一人"),
                w.kyoko.deal("宅配が届く"),
                True),
            ("ep2", ep_box(w),
                w.kyoko.think(w.i.hisgone),
                w.kyoko.have(w.hisfambox),
                w.kyoko.think("どうすればいい？"),
                w.kyoko.do("涙"),
                True),
            ("ep3", ep_breakmemory(w),
                w.kyoko.think(w.i.break_anxiety),
                w.kyoko.feel(w.i.anxiety),
                w.kyoko.do("break"),
                w.kyoko.do("部屋を空っぽ"),
                True),
            ("ep4", ep_hersinks(w),
                w.kyoko.think("別れ"),
                w.kyoko.look("空虚"),
                w.kyoko.do(w.i.sink),
                w.kyoko.meet(w.hiiragi),
                True),
            ]

# main
def world():
    w = wd.World("The kyoko-san project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("今日子さんの夕沈み"),
            ep_intro(w),
            ep_box(w),
            ep_breakmemory(w),
            ep_hersinks(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

