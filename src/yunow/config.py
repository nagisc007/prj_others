# -*- coding: utf-8 -*-
"""Config: yusha now
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("yusha", "タロウ", 16, "male", "勇者", "me:俺:S:勇者:yula:ユラ:mako:マコ:sol:ソル"),
        # sub
        ("maou", "魔王", 36, "male", "魔族の王", "me:我"),
        ("yula", "ユラ", 16, "female", "盗賊", "me:アタシ:yusha:勇者"),
        ("sol", "ソル", 18, "male", "戦士", "me:オレ:yusha:タロ吉"),
        ("mako", "魔子", 16, "female", "魔法使い", "me:僕:yusha:勇者様:taro:タロウ様"),
        ("mother", "母", 36, "female", "内職", "me:あたし:yusha:タロウ"),
        ("maneko", "マネ子", 99, "female", "魔王軍参謀", "me:私:maou:魔王様:full:オモイマネー・ノミコ"),
        ("goken", "ゴーケン", 99, "male", "陸戦大将", "me:儂"),
        # mob
        ("king", "王様", 58, "male", "王", "me:ワシ"),
        ("barmaster", "酒場の店主", 45, "male", "店主", "me:オレ"),
        ("eada", "イーダ", 44, "female", "ホステス", "me:ウチ"),
        ("priest1", "クレルク", 42, "male", "神父", "me:私"),
        ("mas_soldier", "ライアス", 58, "male", "戦士"),
        ("minion", "魔王の部下", 99, "male", "魔王の部下", "me:オレ:mane:軍参謀"),
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
        ("myhome", "勇者の家"),
        ("mainbank", "ドツボ銀行"),
        ("maocastle", "魔王城"),
        ("freema", "モウカリ"),
        # Part
        ("castle1gate", "城門"),
        ("townstreet1", "路地"),
        ("bedroom", "勇者の寝室"),
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
        ("scshot", "スクシヨ"),
        ("doga", "ドーガ"),
        )


INFOS = (
        # main
        ("get_phone", "スマフを手に入れた"),
        ("beat_maou", "魔王退治"),
        ("destroy_peace", "世界平和が脅かされた"),
        ("trouble", "困難"),
        ("yen", "ギール"),
        ("ggr", "ゴゴる"),
        # chapter 1
        ("god", "ルルミス神"),
        ("reset", "リセエトの儀"),
        ("matching", "賊シィ"),
        # games
        ("game1", "勇者ブルーファンタジィ"),
        ("game2", "勇者グランオーダー"),
        ("game3", "パズル勇者ドラゴン"),
        ("darkgame", "黒ガチャと勇者ウィズ"),
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
