# -*- coding: utf-8 -*-
"""Config: yubijo.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        ("zenzo", "畠中善蔵", 20, "male", "退魔師", "me:オレ", "幽霊が美少女に見える男"),
        ("akebi", "山野井山女", 17, "female", "幽霊", "me:わたし", "自殺した女子高生"),
        ("murako", "田村邑子", 33, "female", "退魔師", "me:私"),
        ("cap", "柊聖文", 56, "male", "所長", "me:僕:zenzo:善ちゃん:murako:ムラムラちゃん"),
        # chapter 4
        ("minako", "水辺水菜子", 28, "female", "幽霊", "me:ワタシ"),
        # chapter 6
        ("beniko", "紅沢紅子", 35, "female", "幽霊", "me:私"),
        ("mia", "青井未青", 22, "female", "幽霊", "me:みぃ"),
        ("kii", "黄川田黄衣", 17, "female", "幽霊", "me:アタイ"),
        )


STAGES = (
        ("city13", "十三王子市"),
        ("apart", "畠中のアパート"),
        ("office", "退魔師事務所"),
        ("chineseshop", "中華飯店"),
        # chapter 1,2
        ("ghosthome", "幽霊屋敷"),
        # chapter 4,5
        ("ghostschool", "幽霊廃校"),
        # chapter 6,7
        ("ghosthospital", "幽霊病院"),
        # chapter 8
        ("ghosttonnel", "幽霊トンネル"),
        ("ghostworld", "幽霊世界"),
        )


DAYS = (
        ("meet", "出会いの日"),
        # chapter 4
        ("meet2", "出会いの日２"),
        # chapter 6
        ("meet3", "出会いの日３"),
        )


ITEMS = (
        ("wallet", "財布"),
        ("GAnovel", "GA文庫"),
        ("truck", "トラック"),
        )


INFOS = (
        ("ghost", "幽霊"),
        ("goheaven", "成仏"),
        ("beauty", "美少女"),
        ("job", "仕事"),
        ("salary", "給料"),
        ("suicide", "自殺"),
        ("despair", "絶望"),
        ("deadzenzo", "善蔵の死"),
        ("hittruck", "トラックに轢かれる"),
        ("firejob", "仕事を首になる"),
        ("poor", "貧乏"),
        ("kiss", "キス"),
        ("makelove", "恋愛"),
        ("akebi_reason", "山女の事情"),
        ("akebi_death", "山女の死因"),
        ("ghostbuster", "退魔師"),
        ("ability", "善蔵の能力"),
        ("ghost_real", "幽霊の本当の姿"),
        ("crisis", "危機"),
        # chapter5
        ("minako_reason", "水菜子の事情"),
        ("minako_death", "水菜子の死因"),
        ("minako_dream", "水菜子の夢"),
        # chapter 6
        ("ghospital_info", "幽霊病院の噂"),
        ("beniko_reason", "紅子の事情"),
        ("mia_reason", "未青の事情"),
        ("kii_reason", "黄衣の事情"),
        )


FLAGS = (
        )

