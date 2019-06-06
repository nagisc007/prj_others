# -*- coding: utf-8 -*-
"""Config: yubijo.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("kyoko", "明日川,今日子", 27, "female", "無職", "me:わたし"),
        ("hiiragi", "柊,秋雄", 30, "male", "会社員", "me:僕"),
        # sub
        # family
        ("himam", "柊,母", 58, "female", "農家"),
        ("hidad", "柊,父", 59, "male", "役所"),
        # mob
        ("deliverman", "宅配,届男", 32, "male", "宅配", "me:オレ"),
        )

STAGES = (
        # Area
        # Place
        ("apart", "アパート"),
        # Part
        ("living", "リビング"),
        ("kitchen", "キッチン"),
        ("bathroom", "浴室"),
        ("toilet", "トイレ"),
        )

DAYS = (
        # main
        ("current", "現在"),
        # sub
        )

ITEMS = (
        # main
        ("hisfambox", "彼の実家からのダンボール"),
        ("famphoto", "家族写真"),
        # sub
        ("coat", "春物のコート"),
        )

INFOS = (
        # main
        ("myreason", "彼にとって自分が何なのか"), # NOTE: main theme
        ("departing", "別離の不安"),
        ("anxiety", "言いようのない不安"),
        ("sink", "溶ける"),
        # sub
        ("hisgone", "いつか彼が実家に帰る"),
        ("break_anxiety", "不安を破壊する"),
        )


FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        "existence": "存在",
        }

