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
        "代行なう",# NOTE: 代行業を依頼
        "全滅なう",# NOTE: 旅立ち編終了、ラストで死に戻り体験
        ]

# scenes
## ep11 scene
def sc_preparation(w: wd.World):
    h = yusha = w.yusha
    sol, mako, mam = w.sol, w.mako, w.mother
    return w.scene("旅立ちの準備だ",
            h.be(w.stage.myliving, w.day.firstawake2),
            h.look("$yumarkを無事に落札者に発送を終え",
                "$Sは空腹を抱えて自宅へと戻ってきた"),
            sol.talk("それで魔王って奴はどこに住んでるんだよ？"),
            mam.talk("うちの息子がそんなこと知ってる訳ないじゃないの。", "ねえ$makoはどう思う？"),
            mako.talk("魔王城だと思いますよ"),
            h.look("だが中に入って目の前に広がったのは",
                "赤頭の男$solとピンクのおかっぱの少女$n_mako",
                "それに$Sの母親がテーブルの上に広げた色とりどりのお菓子を囲んで",
                "仲良さそうに談笑する姿だった"),
            yusha.talk("お前ら何してんの？"),
            sol.talk("お前も食えよ。", "$makoさんがくれた菓子めちゃめちゃうめえぞ"),
            mam.talk("あんたお帰り"),
            mako.talk("あ", "$taroおかえりなさい。", "ちゃんと手続きできましたか？"),
            h.look("まるで長年連れ添ったパーティのように見えたが",
                "まだ三人とも昨日顔を合わせただけのただの他人だ。",
                "それも母親は全く関係ない。", "どちらかといえば$Sの知り合いである"),
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
                "$Sは自分だけをじっと見つめている少女$n_makoに相談をする"),
            yusha.talk("まずはちゃんとした仲間が必要だ。",
                "旅は過酷と聞いているし",
                "何より町の外は強いモンスターがうじゃうじゃしている。",
                "それに立ち向かうには今の$meではどうしても力不足だと思うんだ"),
            mako.talk("うんうん。", "$meもそう思います。",
                "あ", "それよりコレ食べます？"),
            yusha.talk("ありがとう……うん、うまいな。",
                "じゃねえ！", "そもそもこの大量のお菓子は何なんだ？"),
            h.deal("床を叩きつけると", "お菓子を持った木の大皿が跳ねてそこから宝石のような色とりどりのクッキーが落下した"),
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

# episodes
def ep11(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_preparation(w),
            sc_mamazon(w),
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
            ep11(w),
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

