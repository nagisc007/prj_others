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
    return w.scene("私の好きなものたち",
            h.be(w.stage.classroom),
            h.feel("十月も終わるというのに", "冬服のセーラーだと黒に近い紺色だからか",
                "じっとりと汗が滲んでくる"),
            h.look("ニ学期の席替えで教室の真ん中あたりに移ってしまった居心地の悪さは何日経ってもそのままで",
                "背中にも腕にも頬にも誰かの視線を感じて",
                ""),# TODO
            h.look("学校に行けばみんな同じ服を使っている。",
                "それなのに目に映るのは違って見える。輝いている子、暗い子、スタイルのいい子。いろいろだ"),
            h.think("服を変えなくても、その人はその人らしいんだと思う。けど$kenはそんなこと言わない。"),
            h.think("小さい頃からハーフで色黒だとバカにされたからか、気づいたら髪を黒くしてみたり、白粉で真っ白にしたり、そんな奇行が目立つ人だった"),
            # TODO: 学校の不満、制服、同じにしようとすることと実態の差への不満
            )

def sc_firstmeet(w: wd.World):
    h = emi = w.emi
    ken = w.ken
    return w.scene("彼との出会い",
            # NOTE: ちょっと回想
            h.think("$meは自分の容姿に自信はなくて、でもそこまで酷いと思ってなかったけど、ある日、突然男子から「お前ちょっときもいよな」って言われて"),
            h.think("その言葉がどれだけ乙女心を傷つけたのかも知らない彼は、逃げるように転校してしまったけれど、あの傷だけは未だに心に残っている"),
            h.think("そんな$meを変えてくれたのが$kenだった"),
            # TODO: 場所考える。ちょっと変わったところがいい
            ken.ask("どうしたの？"),
            h.look("その時の彼の着ていたのが自作のシャツだった。なんか動物愛護団体みたいなものかと思った。アイラブシマウマって書いてあったけれど英語だとシマウマじゃないよなと思ったことを覚えている"),
            h.think("普通ならこういう時は大人の人が$meに驕ってくれるものかと思っていたけれど、結局全額$meが出した"),
            h.think("あとで聞くと、近所の子だと分かったから話しかけてくれたらしい。金を借りるつもりだったのだとか"),
            h.think("それ以来、結構頻繁に一緒に話すようになり、$kenがオリジナルブランドを作っているのだと知った"),
            ken.talk("だってあんな奇妙な配色", "シマウマかパンダくらいなもんだろ？"),
            h.think("その言葉が、$meが欲しかった感情かも知れない"),
            )

def sc_presentbra(w: wd.World):
    h = emi = w.emi
    ken = w.ken
    return w.scene("下着のプレゼント",
            h.be(w.stage.hisshop),
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

