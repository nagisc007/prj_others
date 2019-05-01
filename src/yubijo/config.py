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
        # chapter4
        ("minako", "水辺水菜子", 28, "female", "幽霊", "me:ワタシ"),
        )


STAGES = (
        ("city13", "十三王子市"),
        ("apart", "畠中のアパート"),
        ("office", "退魔師事務所"),
        ("chineseshop", "中華飯店"),
        ("ghosthome", "幽霊屋敷"),
        ("ghostschool", "幽霊廃校"),
        ("ghosthospital", "幽霊病院"),
        )


DAYS = (
        ("meet", "出会いの日"),
        ("meet2", "出会いの日２"),
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
        )


FLAGS = (
        )

