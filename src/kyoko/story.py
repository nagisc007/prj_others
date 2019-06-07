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
            kyoko.look("青すぎる空"),
            w.kyoko.do("wait", w.hiiragi),
            w.hiiragi.go("仕事に出た"),
            w.kyoko.be("部屋で一人"),
            kyoko.feel("孤独"),
            w.kyoko.deal("宅配が届く"),
            )

def sc_delivered(w: wd.World):
    kyoko, hiiragi, deliverman = w.kyoko, w.hiiragi, w.deliverman
    return w.scene("宅配便",
            kyoko.be(w.stage.apart, w.day.current),
            kyoko.feel("宅配に怯える"),
            kyoko.deal("宅配応対"),
            kyoko.think("居留守"),
            deliverman.talk("柊の名"),
            kyoko.talk("ちょっと待って"),
            w.tag.comment("今日子外見とか服装の記述"),
            kyoko.deal("外見と服装確認"),
            kyoko.go("玄関"),
            kyoko.have(w.hisfambox),
            w.kyoko.look(w.hisfambox),
            kyoko.deal("開ける", "破って"),
            kyoko.look(w.hiiragi, w.famphoto),
            kyoko.think(w.i.hisgone),
            kyoko.feel("自分が泣いている"),
            )

def sc_thinkfamily(w: wd.World):
    kyoko, hiiragi = w.kyoko, w.hiiragi
    return w.scene("彼の家族",
            kyoko.be(w.stage.apart, w.day.current),
            kyoko.remember("彼の実家の話"),
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

