# -*- coding: utf-8 -*-
"""Config: The whereabouts
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("mio", "夏草,美緒", 17, "female", "学生", "me:わたし:S:わたし:asano:右輪さん:asachi:麻乃さん:inaba:稲葉さん:haru:春彦さん"),
        # sub
        ("haru", "稲葉,春彦", 25, "male", "会社員", "me:俺:mio:美緒ちゃん"),
        ("asano", "右輪,麻乃", 17, "female", "学生", "me:うち:mio:美緒っち"),
        ("ochi", "越智,侑李", 17, "female", "学生", "me:私:mio:美緒"),
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
        ("current", "現在", 9,1, 2019),
        ("first", "最初に気づいた日", 9,1,2019),
        # sub
        )

ITEMS = (
        # main
        # sub
        )

INFOS = (
        # main
        )


FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

