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
        )


STAGES = (
        ("city13", "十三王子市"),
        ("apart", "畠中のアパート"),
        ("office", "退魔師事務所"),
        ("chineseshop", "中華飯店"),
        )


DAYS = (
        ("meet", "出会いの日"),
        )


ITEMS = (
        ("wallet", "財布"),
        ("GAnovel", "GA文庫"),
        ("truck", "トラック"),
        )


INFOS = (
        ("suicide", "自殺"),
        ("despair", "絶望"),
        ("deadzenzo", "善蔵の死"),
        ("hittruck", "トラックに轢かれる"),
        ("firejob", "仕事を首になる"),
        ("poor", "貧乏"),
        )


FLAGS = (
        )

