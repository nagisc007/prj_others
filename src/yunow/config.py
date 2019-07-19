# -*- coding: utf-8 -*-
"""Config: yusha now
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("yusha", "勇者", 16, "male", "勇者", "me:俺"),
        # sub
        ("maou", "魔王", 36, "male", "魔族の王", "me:我"),
        # mob
        ("king", "王様", 58, "male", "王", "me:ワシ"),
        )


STAGES = (
        # Area
        ("homeregion", "ジハーン"),
        # Place
        ("hometown", "城下町"),
        ("homefield", "ジハーン近郊"),
        # Part
        ("castle1gate", "城門"),
        )


DAYS = (
        # main
        ("current", "現在"),
        ("callyusha", "勇者の称号を得た日"),
        )


ITEMS = (
        # main
        ("phone", "スマフ"),
        # chapter 1
        )


INFOS = (
        # main
        ("get_phone", "スマフを手に入れた"),
        ("beat_maou", "魔王退治"),
        ("destroy_peace", "世界平和が脅かされた"),
        ("trouble", "困難"),
        # chapter 1
        )


FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

TITLE = {
        "chap1": "第一章　旅立ち",
        }
