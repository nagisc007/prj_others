# -*- coding: utf-8 -*-
"""Config: The whereabouts
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("mio", "夏草,美緒", 17, "female", "学生", "me:わたし:S:わたし:asano:右輪さん:asachi:麻乃さん:inaba:稲葉さん:haru:春彦さん:yamane:山根さん"),
        # sub
        ("haru", "稲葉,春彦", 25, "male", "会社員", "me:僕:mio:美緒ちゃん"),
        ("asano", "右輪,麻乃", 17, "female", "学生", "me:うち:mio:美緒っち"),
        ("ochi", "越智,侑李", 17, "female", "学生", "me:私:mio:夏草さん"),
        ("yamane", "山根,百合", 17, "female", "学生", "me:私:mio:美緒さん"),
        ("akimoto", "秋本,修二", 17, "male", "学生", "me:僕:mio:夏草さん"),
        # family
        ("mam", "夏草,母", 42, "female", "パート", "me:私:mio:美緒"),
        ("dad", "夏草,父", 43, "male", "会社員", "me:僕:mio:美緒"),
        ("bro", "夏草,正則", 15, "male", "中学生", "me:オレ:mio:姉ちゃん"),
        # mob
        )

STAGES = (
        # Area
        ("Gifu", "岐阜県"),
        ("Tajimi", "多治見市"),
        ("mytown", "万千見市"),# NOTE: まちみ
        # Place
        ("school", "高校"),
        ("myhome", "夏草家"),
        ("famires1", "ファミレス"),
        ("karaoke1", "カラオケ店"),
        ("restaurant1", "レストラン"),
        ("station", "駅前"),
        # Part
        ("myroom", "自室"),
        ("dyning", "食堂"),
        ("living", "リビング"),
        ("kitchen", "キッチン"),
        ("classroom", "教室"),
        ("street1", "通学路"),
        )

DAYS = (
        # main
        ("current", "現在", 10,1, 2019),
        ("first", "最初に気づいた日", 10,2,2019),
        ("second", "二番目の日", 10,3,2019),
        ("datefriend", "幼馴染と会った日", 10,14, 2019),
        # sub
        )

ITEMS = (
        # main
        # sub
        )

INFOS = (
        # main
        ("hismessage1", "会社帰りに寄るから映画でも見に行こう"),
        )


FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

