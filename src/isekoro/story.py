# -*- coding: utf-8 -*-
"""Story: re_isekai_sunami
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.isekoro import config as cnf
THM = cnf.THEMES


# scenes
def sc_vanish(w: wd.World):
    h, kasagi = w.hiiragi, w.kasagi
    return w.scene("また異世界が消えた",
            # NOTE: 実は女性作者である（修正）
            h.be(w.stage.apart, w.day.current),
            h.look("また異世界が消えた"),
            h.deal("手に取ったスマートフォンのモニタには",
                "すぐに同じフレーズで何十という呟きが流れる"),
            h.talk("どうしてなんだ……なあ", "$sunami"),
            w.combine(
            h.think("それを見て$meは思わず声を漏らしていたが、"),
            h.deal("ほどなく$n_kasagiという$meの担当編集の名前が表示され",
                "目覚まし時計のようなコール音が鳴り始めた"),
            ),
            h.talk("何ですか", "$kasagi"),
            kasagi.talk("ツイート見たか？"),
            h.talk("ええ"),
            h.look("そう答えつつ",
                "ノートパソコンの画面に映っていた原稿を一旦閉じてブラウザを表示する。",
                "国内の主要なニュースサイトでは特に扱われていないが",
                "一部",
                "特にライトノベルやアニメーション関連のニュースを載せているサイトでは",
                "最近よく見るワードが踊っていた"),
            kasagi.talk("またなんだろうな……$isekoro"),
            h.hear("$isekoroと嘆息のように言った後に苦い思いの詰まった紫煙を吐き出したように感じられたが",
                "今は彼の愚痴に付き合っている余裕はない"),
            h.talk("もう少しなんです。",
                "$meが何とかします"),
            kasagi.talk("まだそんなこと言ってるのか？",
                "喩え異世界が全て消えてしまったとしても$meたちには何一つ関係ない。",
                "それどころか寧ろお前は嬉しいくらいなんじゃないのか？",
                "散々異世界ものを書かされて",
                "ずっと自分が書きたいものを封印し続けた$n_hiiragiにとってはな"),
            h.think("どの口が言う。",
                "そんな思いを心の中で握り潰し",
                "こう言って電話を終えた"),
            h.talk("あと一歩で$isekoroを追い詰められるんですよ。",
                "奴は$meの小説の中を移動している。",
                "だからこそ$meが何とかして",
                "彼女を殺してみせます……全ての異世界が殺される前に"),
            )

def sc_gotomyworld(w: wd.World):
    h = w.hiiragi
    return w.scene("私の異世界に",
            h.deal("$kasagiとの電話を終えるとスマートフォンの画面には再び滝のような$isekoroに関するツイートが流れ始める"),
            h.deal("$meは一旦テーブルの上にそれを置いて",
                "汗を掻いているペットボトルのソーダ水を手に取った。",
                "一口飲み込むと刺激が胃袋まで落ちていき",
                "生きている実感を与えてくれる"),
            h.deal("それからビタミン剤をひと掴みして口に放り込むと",
                "改めてノートパソコンに向かう。",
                "マウスを操作して呼び出したのは",
                "未発表原稿だ"),
            h.look("タイトルは『$isekoro』。",
                "ただ彼女を捕まえて殺す為だけに書いている",
                "永遠に発表されることのない原稿だった"),
            h.look("画面には$n_sunamiという名前だけが表示されている"),
            h.explain("$meが書いた『$mybook』の主人公だったカメラ好きの女子高生だ。",
                "大好きな祖父から貰った旧いライカを使い",
                "世界を切り取る能力を持ってしまったことから",
                "様々な騒動に巻き込まれていく。",
                "プロットの時点では$kasagiの受けも良かったが",
                "いざ本になると主人公が地味で魅力に乏しいと言われ",
                "眼鏡をした外見もイラストでのインパクトに欠けるとけなされた"),
            h.think("中身についての評価ならどんなものだって甘んじて受けるが",
                "表紙や挿絵の話ならイラスト屋さんの方に言ってくれと",
                "この時ばかりは$kasagiに愚痴った"),
            h.look("少し目を離すと",
                "原稿の中から$n_sunamiの文字が消えていた。",
                "またどこかの異世界に潜り込んだのだ"),
            h.talk("もうお前が行ける異世界なんて",
                "そんなに残ってないだろ。",
                "分かっているんだ。",
                "お前が最後に向かう場所は"),
            h.deal("ぶつぶつとぼやきながら",
                "キーボードを叩く。",
                "画面に文字がどんどん打ち込まれ",
                "変換され",
                "それが世界を紡いでいく。",
                "ただこの感覚が味わいたくて作家を目指したようなものだ"),
            h.think("それでも",
                "と疑問符が浮上する"),
            h.look().emphasis("踏みしめた土くれから申し訳程度に伸びていた草が",
                "ゆらゆらと落ちてきた白い結晶に触れると途端に生気を失って倒れた"),
            h.think("画面に表示されたその文章に",
                "誰かの心に響く力はあるだろうか。",
                "いつだって自身と不安の狭間で",
                "それでも”$meは面白いはずだ”という無謀な確信というドラッグを呑み込んでは",
                "半ば無理矢理に物語を綴ってきた"),
            h.look("モニタの文字が", "僅かに薄くなる"),
            h.think("この物語世界は既に力を失いつつあるのだ"),
            h.think("誰にも読まれない",
                "楽しまれない物語は",
                "存在しないのと同じ"),
            h.remember("$meはかつて作中で", "そう", "彼女に言わせた"),
            h.think("あとで$kasagiから主人公は作者の代弁者じゃないと怒られたが",
                    "なら一体$meは何の為に書いているというのだろう"),
            h.deal("世界を支える為に",
                    "次々と文章を書いていく"),
            h.hear("カタカタと心地よいリズムが脳を刺激して",
                    "次々と言葉が目の前に浮かび上がる"),
            h.talk("よし", "これでいける……はずだ"),
            h.deal("ターン",
                    "と勢いよくリターンキィを叩くと",
                    "世界が確定していく"),
            h.look("モニタには既に原稿ではなく",
                    "この$isekoroの世界が映り込んでいた"),
            )

def sc_deadworld(w: wd.World):
    h = w.hiiragi
    return w.scene("死にゆく異世界",
            h.feel("頬に痛いくらいの冷気を感じて周囲を見回すと",
                "そこは床にシミの付いたアパートの六畳間ではなかった"),
            h.look("アスファルトも敷かれていない砂利道だ"),
            h.look("そこにジーンズと七部丈のシャツという軽装で立ち",
                "露出した腕先を撫でた風に思わず自分を抱きかかえる"),
            h.look("振り返れば遥か下に崩れた学校とグラウンドが小さく見えた"),
            h.think("間違いなくここは『$mybook』の世界だ"),
            h.think("主人公だった$n_sunamiはカメラで世界を切り取る能力を使って事件を解決していたが",
                "自分の力がただ世界を好きなように破壊しているだけだと理解して",
                "大嫌いだった学校を壊す。",
                "その先は彼女が封印してしまった自分の本当の初恋の記憶と向き合う話だったが",
                "未完のまま永遠に発表する機会を失われてしまった"),
            h.look("持ち物を確認するとやはりスマートフォン以外には何もない"),
            h.look("空を見上げれば次々と小さなゴミのような雪が落ちてくる。",
                "それらは野道に降り積もり",
                "脇の草花を萎れさせていく"),
            h.look("世界を終わらせる雪だ"),
            h.think("異世界が終わる前には",
                "こんな雪が降るらしい"),
            h.think("そんな話を誰から聞いたのか思い出せないまま",
                "$meは丘の頂上を目指して歩き出した"),
            h.hear("と",
                "どこか遠くで雷のようなシャッター音が響く"),
            h.think("またどこかの異世界が殺されたのだ"),
            h.think("けれどそれが聞こえたということは",
                "彼女が確かにこの近くにいる", "ということでもある"),
            h.look("シミの付いたスニーカーの上で",
                "雪が解けずに付着する。",
                "それを蹴り飛ばすように爪先を振り上げても",
                "離れたりはせずに表皮のように固まり",
                "$meの足取りを重くした"),
            h.think("それはまるで彼女が意志を持って降らせた足止めの雪のようだ"),
            h.think("ずっと考えていた"),
            h.think("何故彼女が『$isekoro』になったのか。",
                "何故ほかの異世界を殺す必要があったのか"),
            h.think("$meにはただ一つを除き",
                "その理由を想像することはできない"),
            h.think("だからもし彼女がただその為だけに$isekoroをしているとすれば",
                "作者である$meが止めてやる必要がある。",
                "いや", "意地でも止めなければならない"),
            h.look("吐く息が白く染まる"),
            h.look("見上げても空は見えず",
                "ただ白い空間から次々と雪が舞い落ちてくるだけだ。",
                "見ているうちにもその勢いはどんどん酷くなり",
                "$meの心までも凍えさせようとしていた"),
            h.think("けど",
                "まだ倒れる訳にはいかない"),
            h.behav("足を上げる。",
                "彼女は絶対にこの先にいると信じて",
                "前に進む"),
            h.think("ただそれだけが",
                    "今の$meの物語だった"),# TODO
            )

def sc_facetoface(w: wd.World):
    h = w.hiiragi
    return w.scene("対峙",
            w.hiiragi.come(w.stage.cherryhill, w.day.current),
            # TODO: 丘でやっと追いつく、そこにいると思った
            )

def sc_confession(w: wd.World):
    h = w.hiiragi
    return w.scene("告白",
            # TODO: 彼女に真実を告げる、彼女の告白
            )

def sc_truth(w: wd.World):
    h = w.hiiragi
    return w.scene("真実",
            # TODO: 真実の曝露、実は犯人は柊
            )

def sc_awake(w: wd.World):
    h = w.hiiragi
    return w.scene("そして目覚めた",
            # TODO: 夢オチ？　パソコンに残された言葉
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("異世界を殺すモノ"),
            sc_vanish(w),
            )

def ep_lastisekai(w: wd.World):
    return (w.chaptertitle("最後の異世界に"),
            sc_gotomyworld(w),
            sc_deadworld(w),
            sc_facetoface(w),
                w.hiiragi.think(w.i.stop_isekoro),
                w.hiiragi.know(w.i.isekoro),
                w.hiiragi.go(w.stage.cherryhill),
            )

def ep_isekaikoroshi(w: wd.World):
    return (w.chaptertitle("異世界殺し"),
            sc_confession(w),
            sc_truth(w),
            sc_awake(w),
                w.hiiragi.know(w.sunami, w.i.truth),
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story", story(w), w.hiiragi, w.sunami),
            ]

def story_outline(w: wd.World):
    return [
            ("story", story(w),
                w.hiiragi.think(w.i.stop_isekoro),
                w.hiiragi.know(w.i.isekoro),
                w.hiiragi.go(w.stage.cherryhill),
                w.hiiragi.know(w.i.truth),
                True),
            ]

# main
def world():
    w = wd.World("Re_isekai_sunami")
    w.set_db(cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS,
            cnf.ITEMS,
            cnf.INFOS,
            cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("Re:異世界殺し"),
            ep_intro(w),
            ep_lastisekai(w),
            ep_isekaikoroshi(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

