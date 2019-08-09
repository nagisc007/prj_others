# -*- coding: utf-8 -*-
"""Config: The zebra-bra
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("emi", "槙坂,笑美", 16, "female", "高校生", "me:わたし:S:わたし:ken:ケンさんi:yumi:遊美"),
        ("ken", "陣野,ケン", 21, "male", "アパレル経営", "me:オレ:emi:エミちゃん:masa:マサ"),
        # sub
        ("masa", "鈴村,マサト", 27, "male", "カメラマン", "me:俺"),
        ("yumi", "武田,遊美", 16, "female", "高校生", "me:あたし:emi:エミ"),
        # family
        ("mamken", "ケンのママ", 42, "female", "パート", "me:私i:ken:ケン:emi:笑美ちゃん"),
        # mob
        ("teacher", "先生", 50, "male", "高校教師", "me:私"),
        )

STAGES = (
        # Area
        ("Chiba", "千葉県"),
        ("hometown", "袖ケ浦市"),
        # Place
        ("myhome", "槙坂家"),
        ("kenapart", "ケンのアパート"),
        ("hisshop", "ケンの店"),
        # Part
        ("myroom", "笑美の部屋"),
        ("living", "リビング"),
        ("dyning", "食堂"),
        ("classroom", "教室"),
        ("studio", "撮影スタジオ"),
        )

DAYS = (
        # main
        ("marason", "マラソン大会", 10,25, 2019),
        ("current", "現在", 10,28, 2019),
        ("getzebra", "ゼブラブラ入手日"),
        ("camera", "撮影日"),
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

