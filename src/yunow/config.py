# -*- coding: utf-8 -*-
"""Config: yusha now
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("yusha", "タロウ", 16, "male", "勇者", "me:俺:S:勇者:yula:ユラ"),
        # sub
        ("maou", "魔王", 36, "male", "魔族の王", "me:我"),
        ("yula", "ユラ", 16, "female", "盗賊", "me:アタシ:yusha:勇者"),
        ("sol", "ソル", 18, "male", "戦士", "me:オレ:yusha:タロ吉"),
        # mob
        ("king", "王様", 58, "male", "王", "me:ワシ"),
        ("barmaster", "酒場の店主", 45, "male", "店主", "me:オレ"),
        ("eada", "イーダ", 44, "female", "ホステス", "me:ウチ"),
        ("priest1", "クレルク", 42, "male", "神父", "me:私"),
        ("mas_soldier", "ライアス", 58, "male", "戦士"),
        )


STAGES = (
        # Area
        ("homeregion", "ジハーン"),
        # Place
        ("hometown", "城下町"),
        ("homefield", "ジハーン近郊"),
        ("castle1", "ジハーン城"),
        ("bar1", "ルイージンの酒場"),
        ("church1", "ジハーンの教会"),
        # Part
        ("castle1gate", "城門"),
        ("townstreet1", "路地"),
        )


DAYS = (
        # main
        ("current", "現在"),
        ("callyusha", "勇者の称号を得た日"),
        ("firstawake", "最初に死に戻りした日"),
        )


ITEMS = (
        # main
        ("phone", "スマフ"),
        ("yumark", "勇者のしるし"),
        # chapter 1
        ("photo", "シャメ"),
        )


INFOS = (
        # main
        ("get_phone", "スマフを手に入れた"),
        ("beat_maou", "魔王退治"),
        ("destroy_peace", "世界平和が脅かされた"),
        ("trouble", "困難"),
        ("yen", "ギール"),
        # chapter 1
        ("god", "ルルミス神"),
        ("reset", "リセエトの儀"),
        ("matching", "賊シィ"),
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
