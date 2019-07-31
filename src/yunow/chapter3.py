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
        "mamazonなう",# NOTE: 何でもamazon
        "全滅なう",# NOTE: 旅立ち編終了、ラストで死に戻り体験
        ]

# scenes
## ep11 scene
def sc_preparation(w: wd.World):
    h = yusha = w.yusha
    sol, mako, mam = w.sol, w.mako, w.mother
    return w.scene("旅立ちの準備だ",
            h.be(w.stage.myliving, w.day.firstawake2),
            h.look("$yumarkを無事に落札者に発送し終え",
                "$Sは空腹を抱えて自宅へと戻ってきた"),
            sol.talk("それで魔王って奴はどこに住んでるんだよ？"),
            mam.talk("うちの息子がそんなこと知ってる訳ないじゃないの。", "ねえ$makoはどう思う？"),
            mako.talk("魔王城だと思いますよ"),
            h.look("だが中に入って目の前に広がったのは",
                "赤頭の男$solとピンクのおかっぱ頭の$n_mako",
                "それに$Sの母親がテーブルの上に広げた色とりどりのお菓子を囲んで",
                "仲良さそうに談笑する姿だった"),
            yusha.talk("お前ら何してんの？"),
            sol.talk("お前も食えよ。", "$makoさんがくれた菓子めちゃめちゃうめえぞ"),
            mam.talk("あんたお帰り"),
            mako.talk("あ", "$taroおかえりなさい。", "ちゃんと手続きできましたか？"),
            h.look("まるで長年連れ添ったパーティのように見えたが",
                "まだ三人とも昨日顔を合わせただけのただの他人だ。",
                "それも母親は全く関係ない。", "どちらかといえば$Sの方の知り合いである"),
            yusha.talk("だからなんで母さんは馴染んでんの！"),
            mam.talk("お前の友だちなんだから$meの息子や娘みたいなもんじゃない？"),
            yusha.talk("そういう何でも$meのものみたいな考えはやめてくれ……"),
            mam.talk("おい", "ちょっと$yusha……"),
            h.deal("必死に付いてこようとする母親を追い払い",
                "$Sは$solと$n_makoとお菓子と共に",
                "自室に入った"),
            yusha.talk("とりあえず魔王退治をする為には何が必要なのかを",
                "旅立つ前に考えなきゃいけないと思うんだ"),
            sol.talk("なんか伝説の武器とか手に入れて",
                "適当にバーンてやればいいんじゃね？"),
            h.look("真剣に考える気のない$solを放り出し",
                "$Sは自分だけをじっと見つめている少女に相談をする"),
            yusha.talk("なあ$mako。",
                "まずはちゃんとした仲間が必要だと思うんだ。",
                "旅は過酷と聞いているし",
                "何より町の外は強いモンスターがうじゃうじゃしている。",
                "それに立ち向かうには今の$meではどうしても力不足なんじゃないだろうか"),
            mako.talk("うんうん。", "$meもそう思います。",
                "あ", "それよりコレ食べます？"),
            yusha.talk("ありがとう……うん、うまいな。",
                "じゃねえ！", "そもそもこの大量のお菓子は何なんだ？"),
            h.deal("床を叩きつけると", "お菓子を盛った木の大皿が跳ねてそこから宝石のような色とりどりのクッキーが落下した"),
            mako.talk("ああ、もう。",
                "もったいないなあ"),
            h.deal("少し唇を尖らせて彼女は落ちたお菓子を拾う"),
            mako.talk("$meの朝ご飯。", "折角だから$taroと一緒に食べようと思ってね。",
                "足りなかったら言ってね。",
                "いくらでも持ってこさせるから"),
            yusha.ask("流石にご飯にお菓子はないだろ……てか",
                    "今何て言った？", "持ってこさせる？"),
            mako.talk("うん、", "知らない？", "コレ"),
            h.look("$n_makoは彼女の$phoneを見せた。",
                "そこには$st_amazonと表示され",
                "お菓子みたいな食べ物だけでなく",
                "服や家具", "他に武器や防具なんてものまでが価格と共に映っていた"),
            yusha.talk("コレ……何？"),
            mako.talk("$st_amazonよ。",
                "例えば飲み物が欲しいなあって思うでしょ？",
                "で、ここからタピオカミルクティー選ぶでしょ？",
                "当日配送選ぶでしょ？",
                "はい終わり"),
            h.deal("$Sも$solも彼女が何をしているのかさっぱり分からないまま「お、おう」と頷く"),
            h.deal("しかし彼女が中央にピンクの甘いゼリーの乗ったクッキーを一つ食べ終えたところで",
                "玄関先で声がした"),
            mam.talk("ねえ$yusha。", "こんなものが届いたんだけど？"),
            h.look("母親が持ってきたのは小さな紙の箱だった。",
                "中身はガラスのコップを満たす",
                "何か小さな粒状の黒いものがころころと入っているのが分かる不思議な薄茶色の液体で",
                "$n_makoはそれを取り出すとストローを差して美味しそうに飲み始める"),
            mako.talk("最近これ流行ってるんだってね……美味しい"),
            h.deal("彼女は笑顔を見せると、"),
            mako.ask("$taroも飲む？"),
            h.deal("とそのストローを向けた"),
            )

def sc_mamazon(w: wd.World):
    h = yusha = w.yusha
    sol, mako, mam, daima = w.sol, w.mako, w.mother, w.daimaou
    return w.scene("mamazonは何でも揃う",
            yusha.talk("いやそれは要らない"),
            h.look("即座に断った$Sを驚きの表情で彼女は見つめたが",
                "もう一度ストローを咥えるとジュルジュルと音をさせながら液体を啜った"),
            mako.talk("美味しいのに。",
                "とにかくね$st_amazonなら何でも揃えられるのよ。",
                "何だったらこれで旅に必要なものも全部揃えてしまえばいいのに"),
            sol.talk("いくらそのゾマホンてのが凄いって言ったって何でも揃うってこたぁねえだろ？",
                "それじゃあ……畑を耕すクワは？"),# NOTE:何か簡単なもの
            h.deal("普通なら注文してから良いものなら納品まで一月かかるものもあるというのに",
                "すぐにそれは届けられた。", "それも現代の名工と呼ばれる$n_muramasaが仕上げたものだ"),
            sol.talk("嘘だろ……"),
            h.look("$solは確かに刻まれた$n_muramasaの紋に言葉を失っていた"),
            yusha.talk("じゃあ……これならどうだ？"),# NOTE:ちょっと無理め
            h.deal("$Sは常々欲しいと思っていた等身大$n_idolの抱き枕を注文したが",
                "オークションにもなかなか出回らないという逸品だ。",
                "しかしそれもすぐに届いた"),
            yusha.talk("それじゃあ"),
            h.deal("$Sと$solは次々と無理難題をふっかけてみたが",
                "それらは悉く届けられ",
                "やがて$Sの自室には収まりきらなくなり",
                "家の前に巨大な精霊像や荷馬車",
                "最新式のテントまでが揃えられてしまった"),
            sol.talk("なあ……もうこれで魔王退治すればいいんじゃね？"),
            h.look("その光景に$solは呆れてそう言ったが、"),
            mako.talk("魔王退治までは流石に……あ"),
            h.look("どうやら$n_makoはそれを見つけてしまったらしい"),
            mako.talk("ねえ。",
                "これちょっと見てよ……"),
            h.look("言われて二人は彼女の$phoneを覗き込む。",
                "そこには『魔王退治』と書かれていた"),
            yusha.talk("コレって注文したら本当に魔王退治してくれるのか？"),
            h.look("$Sは嬉々として$n_makoに尋ねたが",
                "流石の彼女も首を捻った"),
            sol.talk("まあものは試しだ。", "注文してみようぜ"),
            h.deal("$solの無駄に前向きな姿勢に背中を押され",
                "戸惑う彼女に変わって$Sは『注文』を押したのだった"),
            )

## ep12 scenes
def sc_defeatmaou(w: wd.World):
    h = yusha = w.yusha
    sol, mako, mam, daima = w.sol, w.mako, w.mother, w.daimaou
    return w.scene("魔王退治",
            h.be(w.stage.bedroom, w.day.firstawake2),
            h.look("今", "$Sたちの目の前には『魔王退治』と表示された$phoneがある"),
            h.explain("$phoneとは不思議な鉱石で出来た板で",
                "それを持っていれば遠隔地であっても文章や画像のやり取りが可能という魔法の道具なのだが",
                "更にそれを使って様々な注文ができる$st_amazonというサービスがあり",
                "$Sとその愉快な仲間二人は",
                "そこに表示された『注文』に掛けられた彼の指をじっと凝視していた"),
            yusha.talk("コレって注文したら本当に魔王退治してくれるのか？"),
            h.think("内心では流石にそれは無理だろう", "と$Sである少年は思っていたのだが",
                "赤髪の長身男性$solは彼の肩に手を置いて", "こう言った"),
            sol.talk("まあものは試しだ。", "注文してみようぜ"),
            mako.talk("ちょっとやめときなさいよ。", "流石に魔王退治を注文するなんてどうかしてる"),
            h.look("苦言を呈したのはピンクのおかっぱ頭の少女、$n_makoだ。",
                "元々は彼女が$st_amazonを紹介してくれたのだが",
                "魔王退治注文はどうも気に入らないらしい"),
            yusha.talk("これで魔王退治できたら儲けもんだし",
                "まあ注文するだけ注文してみようぜ"),
            h.deal("楽観的な$solに賛同した$Sは", "そこに記された金額や注意事項を一切確認することなく",
                "実に無責任な指の動きで『注文』を押した"),
            mako.talk("……そもそも魔王退治なんてされたら困るんですけど"),
            h.look("あーあ", "という溜息を漏らした$n_makoは「何も起こんねえな」と笑う男性二人を横目に",
                "何故かつまらなさそうだ"),
            h.be("しばらく待ってみたが何も起こらない"),
            h.think("いや", "妙な地響きを感じた"),
            yusha.talk("な、何が起こってるんだ？"),
            h.look("その時、空が光った"),
            )

def sc_daimaou(w: wd.World):
    h = yusha = w.yusha
    sol, mako, mam, daima = w.sol, w.mako, w.mother, w.daimaou
    return w.scene("大魔王",
            mako.talk("なんか、変よ"),
            h.look("今までに見せたことのない神妙な顔つきになる"),
            mam.talk("なんか外が騒がしいわねえ"),
            h.move("みんなで外に出てみる"),
            h.look("街中の人間が家の外に出て何やら騒いでいる"),
            h.look("中央広場は人混みになっていた"),
            h.look("札が立てられ", "人が殺到している"),
            sol.talk("何だって？"),
            h.look("$solは目がよかった"),
            sol.talk("いや、なんか『魔王が退治されて平和が戻った』とか書いてあんだよ"),
            mako.talk("え？"),
            h.hear("その声をあげたのは$n_makoだった"),
            mako.talk("退治とか、そんなの有り得ないのに……"),
            yusha.talk("まあホントに退治されたんなら", "ありがたいじゃないか。",
                "魔王退治の旅に出なくても済むし"),
            h.deal("喜ぶ町の人々の顔"),
            h.look("何故か悲しそうな$n_makoの顔"),
            yusha.talk("そんなに$meと旅したかったなら", "これから平和になった世界を旅すればいいじゃないか"),
            h.deal("そう声を掛けるが", "表情は変わらない"),
            h.look("と、空が急に暗くなる"),
            h.look("黒雲に覆われたかと思えばそこが裂けるようになって",
                "真っ赤に燃えていた。",
                "その天の炎が柱となって城に突き刺さる"),
            h.look("誰もが悲鳴を上げた"),
            yusha.talk("何だありゃ……"),
            h.look("城は半壊し", "燃えていた"),
            h.hear("そこに声が響き渡る"),
            daima.talk("魔王は倒された。",
                "その代わりに今後は$meが世界を恐怖に震え上がらせてやろう。",
                "我が名は大魔王。",
                "世界に絶望と混沌をもたらす最凶の闇"),
            h.explain("その日", "世界は闇に覆われた"),
            yusha.talk("まじかよ……$st_amazonすげえな"),
            sol.talk("感心するとこソコかよ！"),
            )

# episodes
def ep11(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_preparation(w),
            sc_mamazon(w),
            )

def ep12(w: wd.World):
    return (w.chaptertitle(TITLE[1]),
            sc_defeatmaou(w),
            sc_daimaou(w),
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
            #ep11(w),
            ep12(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

