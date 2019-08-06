# -*- coding: utf-8 -*-
"""Config: The zebra-bra
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("emi", "槙坂,笑美", 15, "female", "高校生", "me:わたし:ken:ケン"),
        ("ken", "陣野,ケン", 21, "male", "アパレル経営", "me:オレ"),
        # sub
        # family
        ("mamken", "ケンのママ", 42, "female", "パート", "me:私"),
        # mob
        )

STAGES = (
        # Area
        ("Chiba", "千葉県"),
        ("hometown", "袖ケ浦市"),
        # Place
        ("myhome", "槙坂家"),
        ("kenapart", "ケンのアパート"),
        # Part
        ("living", "リビング"),
        ("dyning", "食堂"),
        )

DAYS = (
        # main
        ("current", "現在"),
        ("getzebra", "ゼブラブラ入手日"),
        # sub
        )

ITEMS = (
        # main
        ("zebrabra", "ゼブラブラ"),
        # sub
        )

INFOS = (
        # main
        ("brandname", "KenKen"),
        )


FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

