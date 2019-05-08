# -*- coding: utf-8 -*-
"""Story: yubijo chapter01.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd


# episodes
def ep_avant(w: wd.World):
    z = w.zenzo
    lunchtime = w.day.meet.elapsed(hour=12)
    lunchafter = lunchtime.elapsed(hour=2)
    scenes = [
            w.tag.comment("善蔵（他）の一人称が原則"),
            w.scene("男むさい職場",
                z.be(w.stage.chineseshop, lunchtime),
                z.look("店内"),
                z.look("満席", w.i.moreusual.flag()),
                z.do("皿を割る"),
                z.do(w.tencho, "angry"),
                ),
            w.scene("バイトクビだってよ",
                z.talk(w.tencho, "疲れてるか？"),
                w.tencho.talk(w.i.rumor_ghostdead),
                z.know(w.tencho, w.i.rumor_ghostdead),
                z.have(w.i.salary, w.tencho),
                w.tencho.talk(w.i.allupbusiness.flag(), "お前が来てから"),
                z.talk(w.tencho, w.i.firejob),
                z.know(w.i.firejob),
                ),
            w.scene("そうだ異世界に行こう",
                z.look(w.stage.city13),
                w.stage.city13.explain("都心から離れた町"),
                z.go(w.stage.street),
                z.look(w.truck),
                z.think("近所に工場が多い"),
                z.go(w.stage.bookstore),
                z.have(w.GAnovel),
                z.look(w.GAnovel, w.i.beauty),
                z.think("付き合いたい"),
                z.think(w.i.zenzolove),
                z.remember(w.GAnovel, "異世界もの"),
                z.be(w.i.despair),
                z.think(w.i.suicide, "異世界に行ける"),
                ),
            w.scene("トラックバイバイ",
            w.zenzo.do(w.i.suicide, "$want"),
            w.zenzo.do(w.i.hittruck, w.i.suicide),
            w.truckdriver.look(w.zenzo),
                ),
            ]
    return [w.chaptertitle("そうだ異世界に行こう"),
            *scenes,
            ]


def ep_meetbijo(w: wd.World):
    z = w.zenzo
    return [w.chaptertitle("美女に出会った"),
            w.zenzo.look(w.akebi, "美女"),
            w.zenzo.look(w.stage.ghosthome, w.day.meet),
            w.zenzo.meet(w.akebi),
            w.akebi.talk(w.zenzo, "家の前で寝ていた"),
            w.zenzo.ask(w.akebi, "彼女のこと"),
            w.akebi.do(w.zenzo, "ベッドに浮かべて運ぶ"),
            w.zenzo.think(w.akebi, "能力者"),
            w.zenzo.do(w.akebi, "love", "$want"),
            w.akebi.reply(w.zenzo, "照れる"),
            w.zenzo.ask(w.akebi, "彼氏"),
            w.akebi.reply(w.zenzo, "no"),
            w.akebi.talk(w.zenzo, w.i.akebi_history),
            w.zenzo.know(w.akebi, w.i.shojo),
            w.zenzo.talk(w.akebi, w.i.gosteady),
            w.zenzo.do(w.akebi, w.i.gosteady, "yes"),
            # TODO:
            z.know(w.i.moreusual.deflag(), w.i.allupbusiness.deflag()),
            ]


def ep_bijoghost(w: wd.World):
    return [w.chaptertitle("幽霊が美女なら問題ないよね"),
            w.zenzo.be(w.stage.ghosthome, w.day.meet),
            w.zenzo.be(w.akebi, w.i.gosteady),
            w.zenzo.ask(w.akebi, "本当に？"),
            w.akebi.reply("yes"),
            w.zenzo.feel("happy"),
            w.zenzo.do(w.akebi, w.i.kiss, "$want"),
            w.zenzo.know(w.akebi, "色々なこと"),
            w.zenzo.think(w.akebi, w.i.nohuman.flag()),
            w.zenzo.ask(w.akebi, w.i.ghost),
            w.akebi.reply(w.zenzo, "yes", w.i.nohuman.deflag()),
            w.zenzo.know(w.akebi, w.i.ghost),
            ]


# main
def story(w: wd.World):
    return (w.maintitle("第一話　無職が自殺しても問題ないよね？"),
            ep_avant(w),
            ep_meetbijo(w),
            ep_bijoghost(w),
            )


def main(): # pragma: no cover
    from . import story as mainstory
    w = mainstory.world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

