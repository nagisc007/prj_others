# -*- coding: utf-8 -*-
"""Story: Lost her book
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.lostbook import config as cnf
THM = cnf.THEMES


# chapters
def ch1(w: wd.World):
    return (w.chaptertitle("本屋が消える町"),
            # NOTE: 本屋が消えることを知る
            # NOTE: 彼と本屋と彼女の本の関係提示
            # NOTE: 旧校舎の別館になった図書館の謎提示
            )

def ch2(w: wd.World):
    return (w.chaptertitle("彼女の本を救出する"),
            # NOTE: 彼女の本を買い占める為にバイトする夏休み
            # NOTE: 最初の給料を握り締めて向かう、が消える本屋
            # NOTE: 彼女に会える、が、失恋
            )

def ch3(w: wd.World):
    return (w.chaptertitle("現実の物語"),
            # NOTE: 彼女の物語と図書館の謎について
            # NOTE: 彼女が本を書いた理由と、エピローグ
            )

# test data
def story_baseinfo(w: wd.World):
    return [
            ]

def story_outline(w: wd.World):
    return [
            ]

# main
def world():
    w = wd.World("Lost her book")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("彼女の本が消える町"),
            ch1(w),
            ch2(w),
            ch3(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

