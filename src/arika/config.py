# -*- coding: utf-8 -*-
"""Config: The whereabouts
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("mio", "夏草,美緒", 17, "female", "学生", "me:わたし"),
        # sub
        # family
        ("mam", "夏草,母", 42, "female", "パート", "me:私"),
        ("dad", "夏草,父", 43, "male", "会社員", "me:僕"),
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

