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
        "mamazonなう",
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

# episodes
def ep6(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_mystalker(w),
            sc_threaten(w),
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
            )

def main(): # pragma: no cover
    from src.yunow.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

