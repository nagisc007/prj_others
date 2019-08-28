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
        ("sol", "ソル", 18, "male", "戦士", "me:オレ:yusha:タロ吉:mako:マコ"),
        ("mako", "魔子", 16, "female", "魔法使い", "me:僕:yusha:勇者様:taro:タロウ様:sol:ソル"),
        # sub
        ("maou", "魔王", 36, "female", "魔族の王", "me:我"),
        ("daimaou", "大魔王", 99, "male", "魔族の王", "me:我"),
        ("yula", "ユラ", 25, "female", "盗賊", "me:アタシ:yusha:勇者:taro:タロウ"),
        ("mother", "母", 36, "female", "内職", "me:あたし:yusha:タロウ:mako:マコちゃん:sol:ソル君"),
        ("maneko", "マネ子", 99, "female", "魔王軍参謀", "me:私:maou:魔王様:full:オモイマネー・ノミコ"),
        ("goken", "ゴーケン", 99, "male", "陸戦大将", "me:儂"),
        # mob
        ("king", "王様", 58, "male", "王", "me:ワシ"),
        ("barmaster", "酒場の店主", 45, "male", "店主", "me:オレ"),
        ("eada", "イーダ", 44, "female", "ホステス", "me:ウチ"),
        ("priest1", "クレルク", 42, "male", "神父", "me:私:yusha:タロウ君"),
        ("mas_soldier", "ライアス", 58, "male", "戦士"),
        ("minion", "魔王の部下", 99, "male", "魔王の部下", "me:オレ:mane:軍参謀"),
        ("muramasa", "ムラサメ", 58, "male", "刀鍛冶", "me:ワシ"),
        ("idol", "ユカリン", 40, "female", "アイドル"),
        ("gatekeeper", "門番", 28, "male", "兵士", "me:私"),
        ("vilaman1", "村の男性", 45, "male", "村人", "me:私:my:俺"),
        ("uru", "ウル", 68, "female", "宿屋の主人", "me:ワシ"),
        ("town3head", "村長", 70, "male", "村長", "me:わし"),
        # monster
        ("slime", "スライム", 99, "male", "モンスター", "me:ボク"),
        ("goblin", "ゴブリン", 99, "male", "モンスター", "me:ワイ"),
        ("gobrou", "ゴブロウ", 99, "male", "ゴブリン", "me:オレ:suke:ゴブスケ"),
        ("gobsuke", "ゴブスケ", 99, "male", "ゴブリン", "me:ワイ:rou:ゴブロウ"),
        ("gobshu", "ゴブ主任", 99, "male", "ゴブリン", "me:ワシ"),
        ("hobgoblin", "ホブゴブリン", 99, "male", "モンスター", "me:ワシ"),
        )


STAGES = (
        # Area
        ("homeregion", "ジハーン"),
        ("region2", "ローレア"),
        # Place
        ("homemount", "アルチハン山脈"),
        ("hometown", "城下町"),
        ("homefield", "ジハーン近郊"),
        ("castle1", "ジハーン城"),
        ("bar1", "ルイージンの酒場"),
        ("church1", "ジハーンの教会"),
        ("myhome", "勇者の家"),
        ("mainbank", "ドツボ銀行"),
        ("maocastle", "魔王城"),
        ("freema", "モウカリ"),
        ("amazon", "mamazon"),
        ("town2", "クレーベ"),
        ("town3", "ナズム"),
        ("forest1", "クレーベ周辺の森"),
        ("river1", "ポム川"),
        ("lake2", "クレーベ湖"),
        ("near_town3", "ナズム近郊"),
        ("goblinnest", "ゴブリンの巣"),
        ("gobdom", "ジハーン北汚水製造施設"),
        # Part
        ("castle1gate", "城門"),
        ("townstreet1", "路地"),
        ("bedroom", "勇者の寝室"),
        ("myliving", "勇者の家のリビング"),
        # chapter4
        ("valley1", "ゴブリン渓谷"),
        )


DAYS = (
        # main
        ("current", "現在"),
        ("callyusha", "勇者の称号を得た日"),
        ("firstawake", "最初に死に戻りした日"),
        ("firstawake2", "死に戻り１の翌日"),
        ("awake2", "二回目死に戻り日"),
        ("buying", "旅の買い物日"),
        ("firstfield", "初めて町の外に出た日"),
        ("awake3", "三回目死に戻り日"),
        # chapter 3
        ("awake4", "4回目死に戻り日"),
        ("awake5", "5回目死に戻り日"),
        )


ITEMS = (
        # main
        ("phone", "スマフ"),
        ("yumark", "勇者のしるし"),
        # chapter 1
        ("photo", "シャメ"),
        ("scshot", "スクシヨ"),
        ("doga", "ドーガ"),
        ("game", "ゲエム"),
        # chapter 2
        ("yutuber", "勇チューバー"),
        ("drag_mentos", "メンタス"),
        ("healdrink", "薬草ジュース"),
        ("otokudotcom", "爆買いドットコム"),
        ("shortsword", "ショートソード"),
        ("karebasho", "今ソコなう"),
        ("gmap", "ゴーゴンマップ"),
        ("smacache", "スマフ決済"),
        ("wikipedia", "生キペディア"),
        # chapter3
        ("drink1", "ドクトルペップ"),
        ("na_drink1", "ドクペ"),
        ("mapsoft", "マップアプリ"),
        ("ale", "エールビア"),
        # chapter4
        ("townlog", "町歩くログ"),
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
        # chapter 2
        ("mentosgeyser", "メンタスゲイザー"),
        ("selphy", "セルフィン"),
        ("message", "メッセ"),
        ("makoword001", "何でもはできませんよ。アプリがあるだけ"),
        # chapter 3
        ("boshu1", "ジハーン北汚水製造工場作業員募集のお知らせ"),
        )


FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

TITLE = {
        "chap1": "第一章　旅立ち編",
        "chap2": "第二章　冒険初心者編",
        "chap3": "第三章　ゴブリン討伐編",
        "chap4": "第四章　さよなら故郷編",
        "chap5": "第五章　新大陸ローレア編",
        }
