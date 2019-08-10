# -*- coding: utf-8 -*-
"""Story: The zebra-bra
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.zebra import config as cnf
THM = cnf.THEMES


# scenes
def sc_mybra(w: wd.World):
    h = emi = w.emi
    yumi = w.yumi
    return w.scene("私の下着",
            w.tag.comment("笑美の一人称"),
            h.be(w.stage.myroom, w.day.current),
            h.deal("シャツを頭から脱ぐと", "日焼けしていない肌がじっとりと汗ばんでいて最後の部分で首に張り付いてそのまま$meを締め上げようとした"),
            h.think("このまま十六で人生を終えたら何も無かった$meのそれに最後だけ突飛な彩りが添えられるかも知れないけれど",
                "死因がシャツが脱げなくて窒息というのはできれば回避しないなあ",
                "という思いで襟首に指を入れて一緒に巻き付いていた髪の毛を追い出した"),
            h.look("そろそろ髪を切らないといけないかな", "という肩に掛かった暑そうな黒髪を",
                "姿見を通して確認するとついでに自分の貧相な胸元から下半身までも視界に入ってしまい",
                "溜息が二つほど溢れた"),
            yumi.talk("$emiはスポブラでもまだ大丈夫そう"),
            h.think("この前のマラソン大会の後で$n_yumiから言われたことを思い出し",
                "更に憂鬱感が増す"),
            h.think("いくつの時にスポーツブラを卒業したんだったっけ"),
            h.deal("背中に腕を回してホックを外しながら", "自分の胸の歴史を掘り起こそうと記憶の海を探ったけれど",
                "中学の時に誰かが言っているのを聞いて試しに母親のブラを着けてみたのがそれかな",
                "という", "何とも味わい深い思い出に当たったことで", "$meはその捜索を打ち切った"),
            emi.talk("ああもう……厭になる"),
            h.deal("上半身裸のままでベッドに倒れ込むと",
                "毛布の表面のつるりとした部分が$meの温度を少しだけ奪って", "気持ちいい"),
            h.deal("そのまま枕に手を伸ばして", "胸元に抱き寄せる"),
            h.feel("何か特別な訳でもないのに", "少しだけドキドキがして胸の先が痛い。", "でも少しだけそれが良い"),
            h.think("女の子っぽい", "って何だろう。",
                "髪を伸ばすことだろうか。",
                "オシャレに気を遣うことだろうか。",
                "それとも胸が大きいことだろうか"),
            h.look("初めて自分の部屋を与えられた日からほとんど変わっていない", "モノの少ない殺風景"),
            h.look("これを女子の部屋とあの人は認めてくれるだろうか。",
                "ベッドに本棚", "小学校からずっと使っている勉強机。",
                "テレビもパソコンもなく",
                "本棚には僅かばかりの漫画と文庫本", "後は捨てられないままの教科書と参考書たち。",
                "スマートフォンと過去だけが今の$meの情報源で",
                "$yumiから貰ったファッション誌はどう見ても$meとは体型が違いすぎる別の世界の女の人が",
                "服という装備を得て輝いていた"),
            h.look("ただそんな$meの部屋で異彩を放っている柄がある"),
            h.think("ゼブラ"),
            h.look("白と黒の縞模様はそのままなら単なるボーダーで済ませられるのに",
                "ハンガーから垂れ下がった袖の長いそのシャツに刻まれた白黒柄は",
                "単なる縞模様じゃなく稲妻が走ったみたいにけばけばしく描かれていて",
                "もうそれを目にした瞬間に「ゼブラ」って言いたくなるくらいの",
                "ゼブラ柄だった"),
            h.think("けれど$meは知っている"),
            h.think("その大嫌いなゼブラ柄のシャツのタグには",
                "あの人の名前が刻まれていることを"),
            h.think("白か黒かみたいな世界から$meを助け出してくれたあの人の"),
            )

def sc_myfavorite(w: wd.World):
    h = emi = w.emi
    return w.scene("みんな同じ？",
            h.be(w.stage.classroom),
            h.feel("十月も終わるというのに", "冬服のセーラーだと黒に近い紺色だからか",
                "じっとりと汗が滲んでくる"),
            h.look("ニ学期の席替えで教室の真ん中あたりに移ってしまった居心地の悪さは何日経ってもそのままで",
                "背中にも腕にも頬にも誰かの視線を感じて",
                "$meという存在がクラスの人たちに晒されている", "という思いだ"),
            h.look("学校に行けばみんな同じ服を使っている"),
            h.think("そのことに対してみんなは何も思わないのかも知れないけれど",
                "同じ服で同じ机で",
                "黒板にチョークでガリガリと数式を書いている先生も$meたちを名前ではなく「一番前の列の人これ問いて」と",
                "割り当てられた番号を扱っているみたいに言う"),
            h.think("たぶん誰もが高校生というブランド商品なんだろう"),
            h.think("けれどその中で$meだけはアウトレット品にすらなれなくて",
                "半端品で売り物にすらならないからあげるよ", "と言われてしまうような",
                "そんな出来損ない感を覚えている"),
            h.think("誰も口にはしないけれど", "みんな同じではないんだ"),
            h.look("事実",
                "同じ制服姿なのに目に映るそれは違って見えている。",
                "輝いている子、暗い子、スタイルのいい子。",
                "身長も体重も体型も違えば",
                "髪の長さや顔の輪郭", "眉毛の濃さや目の大きさ",
                "鼻だって口だって", "もっと言えば肌の色や質感だって全然違う"),
            h.think("それをこっそりと「羨ましい」という言葉に託して自分とは違う人間だと訴えようとしているけれど",
                "$meはただただ自分が惨めになるだけだと思って", "誰にも言わない。",
                "自分の中の奥深くに沈めてしまって", "何とか日常を送っている"),
            w.teacher.talk("$ln_emi"),
            emi.talk("は、はい"),
            w.teacher.talk("今話したことで何か分からなかったところはあるか？"),
            h.look("立ち上がった拍子に椅子が心をざわつかせる音で後ろに行くと",
                "全員の視線が$meだけに集められてしまって", "正解の言葉なんて分からないまま「分かりません」と「すみません」を繰り返した"),
            w.teacher.talk("いいから座れ。", "このように二次関数をグラフで表した時には……"),
            h.hear("くすくす", "という笑い声が聴こえた気がしたけれど",
                "本当はそんなものがないことを$meは知っている。", "単なる幻聴だ"),
            h.look("椅子に座った$meはノートを隠すようにして俯くと",
                "そこにしてしまった落書きを見つめて", "聞こえないように溜息を落とす"),
            h.look("漫画調の可愛らしい馬が笑っていたけれど",
                "そこに縞模様を描き込む。",
                "白と黒のストライプを貼り付けたみたいにすれば良い訳ではなくて",
                "首と胴体とお尻の方で方向を変えたり", "縞の厚みを調整したりしないといけない"),
            h.think("シマウマの縞は敵から身を守る為のカモフラージュだから"),
            )

def sc_firstmeet(w: wd.World):
    h = emi = w.emi
    ken = w.ken
    return w.scene("彼との出会い",
            # NOTE: ちょっと回想
            h.think("$meがそのシマウマと出会ったのは",
                "今年の五月", "長い連休が終わった後の久しぶりの学校が始まった日だった"),
            h.deal("その日$meは久しぶりに学校に行かなかった"),
            h.think("初めて不登校をしたのは小学校の四年生の時で",
                "元から男子にあまり外見のことをよく言われていないことは自覚していたけれど",
                "でも面と向かってどうこう言ってくる人はいなくて",
                "だから何となく安心していたのだと思う"),
            h.think("それがある日突然",
                "隣のクラスの全然知らない男子から「お前ちょっときもいよな」って言われて",
                "心が真っ白になった"),
            h.think("人を傷つけるのなんて簡単で",
                "何も思っていないような顔をして", "安心していたところに背後からそっと言葉のナイフを突き刺すだけでいい。",
                "そのナイフは本人が口にはしないけれど普段からちょっと気にして隠すようなものなら",
                "それはただの罵倒のナイフよりもずっと効果的だ"),
            h.think("その言葉がどれだけ乙女心を傷つけたのかも知らない彼は",
                "知らないうちに逃げるように転校してしまったけれど",
                "その傷だけは未だに心に残っている"),
            h.move("とにかく久しぶりに不登校したい病が発症した$meはあの日",
                "少し山の方に歩いて", "$st_templeというお寺の敷地内にある竹林に入った"),
            h.look("そこを抜けた先に丸太のベンチがある。",
                "小さい頃は両親に連れられてよく筍堀りをさせてもらったりしたけれど",
                "住職さんが体調を崩してからはそういったこともなくなった"),
            h.look("当時はまだ綺麗に整備されていて",
                "小さな$meが気にせずに丸太のベンチに横になれた"),
            h.look("何も考えずにぼんやりと空を見上げて",
                "時々抜ける風が笹の葉を揺らすのを聞きながら眠りに落ちる"),
            h.think("どうせならこのまま降ってくる笹にでも埋もれてしまって世界から見えなくなればいいのに",
                "なんて考えていたことを思い出す"),
            ken.ask("みーつけ"),
            h.look("男の人の声がして",
                "ぞわっと肌が粟立った"),
            h.look("更にそこに現れたのはシマウマだったから二度びっくりした"),
            h.look("よく見ればそれはＴシャツに大きくシマウマの写真をプリントしたものだったのだけれど",
                "その時は一瞬だけ本物のシマウマが現れたのかと思った。",
                "更に『$i_Ilove』なんて書いてあるから動物を愛護する系の人かとも思ったが",
                "英語だとシマウマはシマウマじゃないだろうと気づいて",
                "何だかおかしくなって",
                "その人の日焼けしたように見える明るい笑顔も相まって",
                "$meは思い切り吹き出した"),
            ken.talk("あれ？", "なんかおかしかった？"),
            h.look("妙なシマウマのＴシャツにデニムの膝丈のパンツ", "それにサンダルという出で立ちと",
                "珈琲色をした肌から", "最近この町にも増えている外国人旅行者かと思ったのだけれど",
                "彼が話した日本語に外国語訛りがなく",
                "何より『$i_Ilove』はやっぱり地元の人間だろうという結論に$meの中で決着した"),
            emi.talk("何か用ですか", "シマウマさん？"),
            ken.ask("あれ？", "やっぱり君もシマウマ好き？"),
            h.look("何がやっぱりなのか分からないけれど",
                "彼は笑顔のまま近づいてくると", "$meの隣の丸太に腰を下ろした"),
            h.look("近くで見ると胸元の大きなシマウマの目がじっと$meを見つめていて",
                    "シマウマそのものはちょっと可愛らしいとすら思える。",
                    "ただ服としてそれが人の体に張り付いていると", "どうにも気持ち悪さが増す"),
            emi.talk("あの……何でシマウマなんですか？"),
            h.think("誰なのかとか何の目的なのかとか",
                    "そんなことよりもずっとそっちの方が気になって",
                    "$meは思わず訊いてしまった。",
                    "たぶんその質問をした時には既に",
                    "彼のことが気になり始めていたのだと思う"),
            ken.talk("何故シマウマかって？"),
            h.think("彼は得意げに高い鼻を指で掻くと",
                    "こう答えてくれた"),
            ken.talk("だってこんな奇妙な配色", "世界中でもシマウマかパンダくらいなもんだろ？"),
            h.think("その言葉を聞けて$meは思ったんだ。"),
            h.think("ああ", "$meがずっと欲しかった言葉って", "きっとこれだったんだ", "って"),
            )

def sc_presentbra(w: wd.World):
    h = emi = w.emi
    ken, murata, mam = w.ken, w.murata, w.mamken
    return w.scene("彼の家へ",
            h.be(w.stage.hisshop),
            h.deal("彼は$n_kenと言って母親がインドネシアの方の人で", "所謂ハーフらしかった"),
            h.think("歩いて十分くらいの県営住宅に住んでいて", "父親は彼が五歳の時に出ていったきりだそうだ"),
            h.move("$meは小春日和の日曜の午後", "その彼のアパートに向かっていた"),
            h.look("歩き慣れた住宅街の路地が", "今日は少しだけ明るく見える。",
                "塀の上に出た紅葉や銀杏の中には色を変え始めているものもあったから", "それで景色が変わって見えるのかも知れない"),
            h.think("そう言えば出会って半年か"),
            h.think("いつの間にか家に遊びに行くような仲になっていた。",
                "特別何かがあった訳じゃないけれど", "一緒にいて話していると元気になれる。",
                "そういう$meにはない明るさを彼は持っていて",
                "学校で厭なことがあっても彼と会うとすぐに忘れることができた"),
            h.think("ただ一点だけ",
                "どうしても受け入れられないことがあったのだけれど"),
            h.look("三階建てのアパートが近づいてくると",
                "その前で黒白のストライプシャツを着たお爺さんと彼が", "大きな声で笑いながら話していた"),
            ken.talk("おお！", "emi！"),
            h.look("彼は$meを見つけるなり大きな手振りで早く来いと促す"),
            emi.talk("あの", "こんにちは"),
            murata.talk("なに？", "この子が$ln_ken君の彼女なの？"),
            h.look("彼女", "という響きが頬の温度を熱くしたが",
                "$meはすぐに「違います」と訂正して", "にたりとするお爺さんを見た"),
            murata.talk("あらぁ", "そうなの？",
                "お似合いだと思うんだけどなぁ。", "彼女", "素直そうだし"),
            h.look("何故かお爺さんは$meの胸元を見ながら言うと",
                "「じゃあまた道の駅で」と手を振って行ってしまった"),
            ken.talk("$ln_murataさんは$meが商品を置かせてもらっている道の駅でお世話になってる人なんだ。",
                "$i_brandnameのシャツも気に入ってくれててね"),
            h.look("$meは遠ざかる$ln_murataさんのシャツがしっかりとゼブラ柄なことを確認して",
                "心の中で溜息をつく"),
            emi.talk("それで", "今日は用事って何なんですか？"),
            h.look("特別日焼けしている訳ではないのに",
                "彼のゼブラシャツから出た逞しい首筋はこんがりと珈琲色だ。",
                "それなのに彼の目と歯は真っ白で",
                "そのコントラストが$meには眩しい。",
                "眩しくて", "もっと見たくなる"),
            ken.talk("うーん", "とりあえず家に上がってよ。",
                "コレを食べながら話そう"),
            h.look("そう笑った彼の手には", "ビニール袋に入った幾つかの丸いものがあった"),
            )

def sc_presentbra2(w: wd.World):
    h = emi = w.emi
    ken, murata, mam = w.ken, w.murata, w.mamken
    return w.scene("プレゼント",
            mam.talk("あら$emi。", "いらっしゃいな"),
            h.look("部屋に入ると奥から洗濯物のゼブラパンツを持った彼の母親が出てきて",
                "彼によく似た珈琲色の肌をゼブラのシャツから覗かせながら笑いかけてくれた"),
            emi.talk("どうも$kmam"),
            h.look("恰幅がよくて胸のボリュームも凄い。",
                "彼に似た目元が犬のそれみたいで可愛らしいのだが",
                "少しだけ苦手だった"),
            mam.ask("それで今日はプロポーズするの？"),
            ken.talk("何言ってるんだよ母さん。", "$emiにはちょっと頼み事があって来てもらっただけ。",
                "嫁に来て欲しいのは分かるけど", "いつもいつもそんなこと言ってたら迷惑でしょ？",
                "ねえ$emi"),
            h.deal(""),
            h.look("一画だけ間借りさせてもらっているそうだ。地元野菜の並びにゼブラ服があるのは奇妙だったが、これが意外と売れているらしい"),
            ken.talk("ありがとう。こっち持ってきて"),
            h.deal("$meは休日には仕事を少し手伝ったりした。当然アルバイト代なんてない。でも一緒にいる時間が貴重だ"),
            h.think("同じ学校の男子には感じない何かがある。それを知りたかった"),
            # TODO: てらいなくゼブラを着るおじさんおばさん、自分はどうも苦手、理由が不明
            )

def sc_disliked(w: wd.World):
    h = emi = w.emi
    return w.scene("嫌いなものたち",
            h.be(w.stage.dyning),
            # TODO: 食事風景、嫌いなものばかり、大人になると増えていく？
            )

def sc_lookingmind(w: wd.World):
    h = emi = w.emi
    return w.scene("気持ちが行方不明",
            h.be(w.stage.myroom),
            h.deal("部屋に戻った$me"),
            h.look("もらった$zebrabraを見て悩ましい"),
            h.deal("一応着けてみる"),
            h.look("姿見で見る"),
            h.think("まるでコスプレのお姉さんみたいだ"),
            h.think("でもちょっとだけ、自分じゃない自分が鏡の向こうにいる気がした"),
            h.think("その$meが笑った気がした"),
            )

def sc_model(w: wd.World):
    h = emi = w.emi
    ken, mam = w.ken, w.mamken
    return w.scene("写真モデルになってって",
            h.be(w.stage.kenapart),
            h.look("久しぶりに$kenの家。狭いアパートに母親と二人暮らし"),
            mam.talk("いつも悪いわね。手伝ってもらって"),
            mam.talk("なんかもううちの子みたいね。結婚する？"),
            h.think("相手の母親から結婚という言葉が出るのはどうなんだ"),
            emi.talk("そういうのじゃ、ないんで"),
            ken.talk("こんなおっさん困るだけだよ。ねえ"),
            ken.talk("それよりちょっと頼みがあるんだ"),
            h.deal("今度下着もHPに載せたいけど、顔とか出さないモデルをしてもらえないかと"),
            ken.talk("$emiスタイルいいし、絶対にしてほしいんだ"),
            h.deal("顔は写さないから。こんなことは君にしか頼めない"),
            h.think("$meは考えさせてくださいと言って一旦自宅に戻った"),
            )

def sc_whyme(w: wd.World):
    h = emi = w.emi
    return w.scene("私の意味",
            h.be(w.stage.myroom),
            h.look("下着を試着した自分を眺めて"),
            h.think("顔は写らない。でも撮影時は見られる。下着姿だ"),
            h.think("何も分かっていない。お腹の肉だって、腕だって、何もかも気になる"),
            h.think("ひょっとして好きだと分かっていて頼んでいるのだろうか。断れないから"),
            h.think("この時点で自分の中に「断る」という選択肢がないって気づいた"),
            )

def sc_takephoto(w: wd.World):
    h = emi = w.emi
    ken, masa = w.ken, w.masa
    return w.scene("写真撮影",
            h.be(w.stage.studio),
            h.deal("撮影日。緊張してやってきたが、まだ着替えていない"),
            ken.talk("今日とってくれる$n_masa。気軽に$masaって呼んでやって"),
            masa.talk("どうも宜しく"),
            h.deal("握手をすると自分の手が冷や汗だらけと気づく"),
            h.deal("彼はそれを拭っていた"),
            h.look("$meが着替えるいくつかの種類の下着が並んでいた"),
            ken.talk("後でプレゼントするよ"),
            h.think("そう言ってくれたけれどこれを自分が履くと思うと、それを晒すと思うと、どうしても無理だ"),
            h.move("下着になった"),
            h.move("でも撮影に耐えられず、逃げ出した。上着だけはおって"),
            )

def sc_confession(w: wd.World):
    h = emi = w.emi
    ken = w.ken
    return w.scene("私の告白",
            h.be(w.stage.myroom),
            h.deal("電話に向かって話す"),
            # NOTE: 自分がゼブラ嫌いだったこと、ただ好きだから付き合っただけなこと
            # NOTE: $kenは自分を認めてくれていたと思いこんでいた。でもそれだけ。好きとかはない。
            h.think("$meが黒ならあの人は白。一生混ざり合うことなく、人生のしまもようになっただけ"),
            h.deal("下着を捨てた。明日、新しいのを買いに行こう。ゼブラ柄じゃないやつを"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("思春期と下着について"),
            sc_mybra(w),
            )

def ep_mylover(w: wd.World):
    return (w.chaptertitle("大好きな人"),
            sc_myfavorite(w),
            sc_firstmeet(w),
            sc_presentbra(w),
            sc_presentbra2(w),
            sc_disliked(w),
            sc_lookingmind(w),
            # NOTE: 好きな人との関係、ブラを貰う、困惑
            )

def ep_underwear(w: wd.World):
    return (w.chaptertitle("大嫌いな下着"),
            sc_model(w),
            sc_whyme(w),
            sc_takephoto(w),
            sc_confession(w),
            # NOTE: モデルに写真撮影させてほしいと頼まれ、困惑
            )

def ep_mymind(w: wd.World):
    return (w.chaptertitle("私の気持ち"),
            # NOTE: 本音を打ち明ける
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story", story(w), w.emi, w.ken),
            ]

def story_outline(w: wd.World):
    return [
            ]

# main
def world():
    w = wd.World("The zebra-bra project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("ぜぶらぶら"),
            ep_intro(w),
            ep_mylover(w),
            ep_underwear(w),
            ep_mymind(w),
            # base
            w.emi.be(w.stage.hometown, w.day.getzebra),
            w.emi.think(w.ken, w.info("小さい頃からずっと好き")),
            w.emi.deal(w.info("下着をプレゼントされる")),
            w.emi.think(w.info("嫌いなゼブラ柄で付けるか迷う")),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

