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
        # chapter 1
        ("truckdriver", "トラック運転手", 35, "male", "運送配達員", "me:俺"),
        ("tencho", "店長", 44, "male", "中華屋店長", "me:オレ"),
        # chapter 4
        ("minako", "水辺水菜子", 28, "female", "幽霊", "me:ワタシ"),
        # chapter 5
        ("ghostjk", "幽霊JK", 17, "female", "幽霊", "me:ワタシ"),
        # chapter 6
        ("beniko", "紅沢紅子", 35, "female", "幽霊", "me:私"),
        ("mia", "青井未青", 22, "female", "幽霊", "me:みぃ"),
        ("kii", "黄川田黄衣", 17, "female", "幽霊", "me:アタイ"),
        # chapter 7
        ("machiko", "田村真千子", 35, "female", "退魔師", "me:私"),
        )


STAGES = (
        ("city13", "十三王子市"),
        ("apart", "畠中のアパート"),
        ("office", "退魔師事務所"),
        ("chineseshop", "中華飯店"),
        # chapter 1,2
        ("street", "通り"),
        ("ghosthome", "幽霊屋敷"),
        # chapter 4,5
        ("ghostschool", "幽霊廃校"),
        # chapter 6,7
        ("ghosthospital", "幽霊病院"),
        # chapter 8
        ("ghosttonnel", "幽霊トンネル"),
        ("ghostworld", "幽霊世界"),
        ("murakohome", "邑子の実家"),
        )


DAYS = (
        ("meet", "出会いの日"),
        # chapter 4
        ("meet2", "出会いの日２"),
        # chapter 6
        ("meet3", "出会いの日３"),
        # chapter 8
        ("meet4", "出会いの日４"),
        )


ITEMS = (
        ("wallet", "財布"),
        # chapter 1
        ("GAnovel", "GA文庫"),
        ("truck", "トラック"),
        )


INFOS = (
        ("ghost", "幽霊"),
        ("goheaven", "成仏"),
        ("beauty", "美少女"),
        ("job", "仕事"),
        ("suicide", "自殺"),
        ("despair", "絶望"),
        ("deadzenzo", "善蔵の死"),
        ("firejob", "仕事を首になる"),
        ("kiss", "キス"),
        ("makelove", "恋愛"),
        ("akebi_reason", "山女の事情"),
        ("akebi_death", "山女の死因"),
        ("ghostbuster", "退魔師"),
        ("ability", "善蔵の能力"),
        ("ghost_real", "幽霊の本当の姿"),
        ("crisis", "危機"),
        # chapter 1
        ("hittruck", "トラックに轢かれる"),
        ("gosteady", "付き合う"),
        ("akebi_history", "山女の恋愛履歴"),
        ("shojo", "処女"),
        ("nohuman", "人間離れ"),
        # chapter 2
        ("lostlife", "生命力を奪われる"),
        ("betogether", "一緒に居る"),
        ("gotodeath", "やがて死ぬ"),
        # chapter 3
        ("poor", "貧乏"),
        ("salary", "給料"),
        # chapter 4
        ("rumor_ghostschool", "幽霊廃校の噂"),
        # chapter5
        ("minako_reason", "水菜子の事情"),
        ("minako_death", "水菜子の死因"),
        ("minako_dream", "水菜子の夢"),
        # chapter 6
        ("badhealth", "体調不良"),
        ("ghospital_info", "幽霊病院の噂"),
        ("beniko_reason", "紅子の事情"),
        ("mia_reason", "未青の事情"),
        ("kii_reason", "黄衣の事情"),
        # chapter 7
        ("propose", "プロポーズ"),
        # chapter 8
        ("murako_dead", "邑子の死"),
        ("firstlove", "初恋"),
        ("machiko_reason", "真千子の事情"),
        # chapter 9
        ("murako_reason", "邑子の事情"),
        ("murako_ghost", "邑子が幽霊"),
        ("zenzo_ghost", "善蔵が幽霊"),
        )


FLAGS = (
        ("case_suicide", "連続自殺事件"),
        ("secret_hospital", "病院の秘密"),
        ("secret_world", "世界の秘密"),
        ("secret_cap", "柊の秘密"), # 実は死神
        ("secret_murako", "邑子の秘密"), # 実は幽霊
        ("case_murako", "邑子の事件"),
        ("secret_zenzo", "善蔵の秘密"), # 邑子の恩人だった
        )

