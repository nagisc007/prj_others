# -*- coding: utf-8 -*-
"""Config: yubijo.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("hiiragi", "柊,桜介", 30, "male", "カメラマン", "me:私:sunami:砂美:kasagi:笠木さん"),
        ("sunami", "桜葉,砂美", 27, "female", "殺人鬼", "me:わたし"),
        # sub
        ("kasagi", "笠木,慎吾", 39, "male", "編集者", "me:俺"),
        )


STAGES = (
        # Area
        ("Tokyo", "東京"),
        # Place
        ("apart", "アパート"),
        ("cherryhill", "幻桜の丘"),
        # Part
        ("living", "リビング"),
        )


DAYS = (
        # main
        ("current", "現在"),
        )


ITEMS = (
        ("camera", "一眼レフ"),
        )


INFOS = (
        ("isekoro", "異世界殺し"),
        ("stop_isekoro", "異世界殺しを止めたい"),
        ("truth", "異世界殺しの真実"),
        )


FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

