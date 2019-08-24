# -*- coding: utf-8 -*-
"""Config: sage pants project
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')


CHARAS = (
        # main
        ("hero", "パンツ,太郎", 30, "male", "パンツ", "me:オレ:I:太郎:ery:エリィ:lily:リリィ:dran:ヴァヴァルさん:mirei:ミレィ"),
        ("ery", "ステラ,エリザベート", 99, "female", "賢者", "me:我:my:私:I:わし:hero:タロウ:ery:エリィ:lily:リリィ"),
        ("lily", "ステラ,リリィ", 20, "female", "魔道士", "me:あたし:ery:お姉ちゃん"),
        ("mirei", "澤森,ミレィ", 18, "female", "村人", "me:私:pants:パンツさん"),
        # sub
        ("robber", "パンティ,三郎", 42, "male", "パンツ", "me:ワシ"),
        ("rey", "ワムザ,レイ", 30, "female", "大賢者", "me:私"),
        ("pery", "ルナ,ペリィ", 27, "female", "公安特別部隊長", "me:ワタシ"),
        ("reiko", "沢森,麗子", 30, "female", "役場職員", "me:私"),
        ("dran", "ヴァヴァル", 99, "female", "ドラゴン", "me:私:ery:エリィ:hero:タロちゃん"),
        # chapter 1-1
        ("sufferer1", "痴漢被害者", 27, "female", "会社員"),
        # chapter 2
        ("gater1", "番人1", 28, "female", "番兵"),
        ("gater2", "番人2", 30, "female", "番兵"),
        ("kerberos1", "ケル", 99, "male", "番犬"),
        ("kerberos2", "ベロス", 99, "male", "番犬"),
        ("avy", "アヴィ", 22, "female", "番人", "me:アタシ"),
        ("empu1", "エンプ", 99, "male", "巨大猿"),
        ("antboss", "アルカラ", 34, "female", "蟻族", "me:アタイ"),
        # chapter 3
        ("zones", "シルバ,ゾネス", 56, "female", "長", "me:儂:yurka:ユルカ"),# NOTE: シルバ（羅）森の意
        ("mam_mirei", "ユルカ", 54, "female", "村人", "me:私:mirei:ミレィ"),
        )

STAGES = (
        # Team
        ("org_adomin", "世界管理協会"),
        # Area
        ("lemurian", "エル・レム・リアン"),
        # Place
        ("island_prison", "監獄島"),
        ("prison", "監獄迷宮"),
        ("station", "駅"),
        ("forest1", "大森林"),
        ("herhome", "エリィの家"),
        ("udon", "饂飩おくやま"),
        # Part
        ("train", "列車内"),
        ("sta_home", "駅のホーム"),
        ## chapter1
        ("out_prison", "監獄の外"),
        ## chapter2
        ("prison1", "監獄迷宮最下層"),
        ("pri_nest", "迷宮の巣"),
        ## chapter3
        ("left_prison", "迷宮跡地"),
        ("town1", "ベグリ"),# NOTE: ベリグリ（三愛）
        ("mirei_house", "ミレィの家"),
        ("river1", "ベグリ付近の小川"),
        )

DAYS = (
        # main
        ("deadman", "死んだ日", 8,2, 2019),# パンツの日
        ("firstmeet", "最初の遭遇日"),
        ("transfer1", "転生した日"),
        ("current", "現在"),
        ("outprison", "脱獄した日"),
        ("meetmirei", "ミレィと出会った日"),
        # sub
        ("departher", "彼女と別れた日", 6,6, 2016),# NOTE: 三年前
        )

ITEMS = (
        # main
        ("pants", "パンツ"),
        ("sagerobe", "聖紫法衣"),# Yomi: せいしほうい
        # sub
        ("udon_fav1", "冷やしとり天うどん"),
        # chapter 3
        ("bad_maekake", "悪心の衣"),
        )

INFOS = (
        # main
        ("transfer", "転生"),
        ("pants_life", "パンツの人生"),
        ("myvalue", "己の価値"),
        ("anotherworld", "異世界"),
        ("equip", "装着"),
        ("energy", "エナ"),
        ("metal", "魔鋼"),
        # sub
        ("coope", "協力"),
        # chapter 1
        ("pervert", "痴漢"),
        ("rescue_her", "被害女性を助ける"),
        ("catch_pervert", "痴漢逮捕"),
        ("dead_truck", "トラック事故死"),
        ("knowledge_world", "この世界についての知識"),
        ("myfuture", "自分の未来"),
        # chapter 1-3
        ("destroy_sage", "世界を滅ぼす大賢者"),
        ("her_status", "彼女の状況"),
        ("this_world", "この世界のこと"),
        ("mean_taro", "勤勉な者"),
        ("realname", "真名"),
        # chapter 1-4
        ("mystatus", "己の状況"),
        # chapter 2
        ("ery_home", "エリィの家の場所"),
        ("language1", "レム語"),
        ("ants", "蟻族"),
        ("dragons", "龍族"),
        ("humans", "人族"),
        # her phrase
        ("herword001", "パンツは知らない他人に触らせる為のものじゃないのよ"),
        ("herword002", "パンツというのは人類が最初に身に着けた服そのものであって決して下着なんて呼んでいい代物じゃないの"),
        ("herword003", "下着は隠されたもう一つの顔みたいなものなのよ"),
        ("herword004", "あなたが私の為にできることなんか本質的には何もないのよ"),
        ("herword005", "一番最悪な人種は人が楽しんでいるところにわざわざ水を差すような発言をする輩よ"),
        ("herword006", "もし世界が闇のままだったとしたらパンツだって生まれてなかったのかも知れないのよ？"),
        ("herword007", "気持ちがどうにかなりそうになった時はね私のパンツの柄を思い出してみればいい。きっとそれがあなたを助けてくれるわ"),
        )

FLAGS = (
        )

THEMES = {
        }

MOTIFS = {
        }

TITLES = {
        "chap01": "転生したらパンツだった件！",
        "chap02": "監獄にパンツを求めるのは間違っているだろうか！",
        "chap03": "パンツ・アウト・オフライン！",
        "chap04": "とあるパンツの禁則目録！",
        "chap05": "ノーパンツ・ノーライフ！",
        "chap06": "俺のパンツがこんなに可愛いわけがない！",
        "chap07": "オーバーパンツ",
        "chap08": "Re:パンツから始める異世界生活！",
        "chap09": "この素晴らしいパンツに祝福を！",
        "chap10": "大賢者さまのパンツ！",
        }
