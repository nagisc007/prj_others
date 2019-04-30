# -*- coding: utf-8 -*-
"""Story: yubijo.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from . import config as cnf

# episodes


# main
def world():
    w = wd.World("yubijo project")
    w.set_db(cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS,
            cnf.ITEMS,
            cnf.INFOS,
            cnf.FLAGS,
            )
    return w


def story(w: wd.World):
    return (w.maintitle("幽霊が美少女なら問題ないよね？"),
            w.zenzo.hear(w.i.firejob, w.stage.chineseshop, w.day.meet),
            w.zenzo.look(w.wallet, w.i.poor),
            w.zenzo.know(w.i.despair),
            w.zenzo.remember(w.GAnovel),
            w.zenzo.do(w.i.suicide),
            w.zenzo.look(w.truck),
            w.zenzo.do(w.i.hittruck),
            w.zenzo.do("rescue", w.akebi),
            w.zenzo.know(w.akebi, w.i.deadzenzo),
            w.zenzo.do("rescue", w.murako),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

