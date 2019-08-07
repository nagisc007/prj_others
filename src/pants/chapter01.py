# -*- coding: utf-8 -*-
"""Story: chapter 1 ''
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.pants import config as cnf
THM = cnf.THEMES

# titles
TITLE = [
        # prologue
        "プロローグ",
        # chapter1
        # NOTE: １話あたり2000から3000字程度、増えたら前後編
        "パンツのない無",# NOTE:目覚めるまで
        "アイ・アム・パンツ",# NOTE: 転生？自分がパンツと知る
        "部屋とパンツとオレ",# NOTE: エリィのこと、呼び出された？パンツとは何ぞ？
        "パンツは履くもの",# NOTE: パンツ履かれる
        "知性のあるパンツ", ## NOTE: 小さくなった
        "黙れパンツ",# NOTE: 事情説明、ここは牢屋で巨大迷路
        "パンツの名は",# NOTE: 名前の話
        ]

# scenes
def sc_hardday(w: wd.World):
    h = hero = w.hero
    robber = w.robber
    return w.scene("ハードな一日",
            h.be(w.stage.train, w.day.deadman),
            h.think("最後に君にパンツを履かせてから", "もう三年になるのか"),
            h.look("と、スマートフォンに着信したメールの日付を見て唐突に思い出す"),
            h.think("八月二日がパンツの日だと知ったのは",
                "今朝のテレビ番組のおちゃらけたアナウンサー同士のやり取りの中でのことだ"),
            w.sufferer1.talk("……やめて……ださ……"),
            h.look("いつもと変わらぬ速度で満員の電車はカーブに差し掛かり",
                "強烈なＧで背中側に引っ張られる。",
                "それを感じながらも$meは上司から送られてきた『辞めないで下さい』という懇願の内容に一通り目を通していた"),
            h.think("果たしてブラックだったろうか。",
                "仕事内容に特に不満はなかったし",
                "入社して六年", "それなりに仕事はしてきた。",
                "ただこのまま上から流れてきた指示通りにプログラムという小さな部品を作り続けていて",
                "果たして自分の人生には何が残るのだろうか",
                "そんな疑問を抱いてしまったことからは目を逸らせない"),
            w.sufferer1.talk("……お願い……やめて……"),
            hero.look().d("ドア付近に立つ鞄を肩から下げた髪の短い女性だった。",
                "自分よりも少し若いくらいだろう。",
                "ノースリーブに短いスカートから出た脚が$meの立ち位置からも見えたが",
                "その彼女がもぞもぞと体を動かして移動しようとしている"),
            hero.look("けれど周囲に立つ他の客に阻まれ",
                "そこから逃げ出せないでいるようだ"),
            hero.look().d("その彼女の右手側",
                "一人の別の女性を挟んだ先に",
                "暗灰色の帽子をしたマスク姿の男性が",
                "競馬新聞を持っていない方の左手をすっと",
                "彼女のスカートに差し入れたのが見えた"),
            hero.think().d("痴漢",
                "という言葉が真っ先に浮かんで",
                "$meはそっと体を捩りながらそっち足を進める"),
            hero.think().emphasis("$i_herword001"),
            hero.think("そう言っていつも憤っていた元彼女は",
                "満員電車のない土地で元気にしているだろうか"),
            hero.look().d("男の手はその女性の臀部をまさぐっているのか",
                "スカートがややまくれ上がり気味になって小さく動いている"),
            hero.look().d("女性の顔は見えない。",
                "じっと我慢しているのかも知れないと考えると",
                "さっさとその苦悶から解放してあげたかった"),
            hero.think().d("もうすぐでその男の手を掴める"),
            hero.look().d("そう思った刹那", "男の手が彼女のスカートから引き抜かれた"),
            hero.look().d("$meはその手が掴んでいたものを目にして思わず心の中で唸ってしまう"),
            hero.look("彼の手には四つの紐がだらりと垂れ下がる",
                "女性ものの布地面積の少ない白の下着が", "握られていたのだ。",
                "彼はそれをスマートフォンでも仕舞うかのような動作で",
                "自分のジャケットの内側へと差し入れる"),
            hero.deal().d("だがそれが完全に彼のものとなる前に",
                "$meの右手がそこから下着ごと引きずり出した"),
            hero.talk().t("この男",
                "痴漢だ"),
            hero.look().d("振り返ったマスクの男は",
                "やたらと血走った目を$meに向けたが",
                "観念したのか",
                "藻掻くことも否定することもせず",
                "ただ大人しくその下着を女性に差し出し",
                "こう言った"),
            robber.talk("あんたには似合わないパンツだ。",
                    "だから$meが供養してやろうとしたんだよ"),
            hero.hear().d("喉に下着を詰め込んだような",
                    "潰れた声だった"),
            hero.deal("$meの右拳が思い切りそいつの頬に叩きつけられると",
                    "車内から控えめに拍手が起こる"),
            hero.look().d("けれど下着を返してもらった彼女は俯いたままで",
                    "電車が停車してドアが開くと一目散にそこから逃げ出して行ってしまった"),
            )

def sc_gotoheaven(w: wd.World):
    h = hero = w.hero
    robber = w.robber
    return w.scene("そして天国へ",
            hero.move(w.stage.sta_home).d("目的の駅ではなかったが",
                "一旦犯罪者を駅員に引き渡そうと思い", "ホームに降り立った"),
            hero.talk().t("おい"),
            hero.deal().d("しかし大人しくしていた痴漢男は$meの右手からするりと身を捻って抜け出すと",
                "そのまま車両の進行方向と反対側へと駆け出した"),
            hero.talk().t("待て！",
                "すみません！",
                "そいつ痴漢なんです！"),
            hero.think().d("僅かな油断だった"),
            hero.move().d("とにかく$meも後追いで駆け出したが",
                "人の多いホームではなかなか全速力で走ることもままならない"),
            hero.look().d("だがその痴漢男の方はこういった状況に慣れているのか",
                "上手く人を躱しながら駆け抜けていくと",
                "車両が切れたところで線路へと飛び降りる。",
                "そのまま駅を出ていこうという気だろう"),
            hero.think().d("逃がすかよ"),
            hero.move().d("$meも後追いで飛び降りると",
                "心臓がどんどん熱くなるのも構わずに思い切り足を蹴る"),
            hero.think().d("もう少し。",
                "あと三メートル……"),
            hero.think().d("届かないか"),
            hero.look().d("踏切の遮断器が上がり",
                "男は道路側へと曲がる"),
            hero.think().d("逃げられる"),
            hero.think().d("そう思った時だった"),
            hero.look().d("$meの目の前を横っ飛びで痴漢男の体が吹き飛んでいく"),
            hero.look().d("続いてトラックの厳ついフロントが頭を覗かせたが",
                "そいつは真っ直ぐに進むことを拒否し",
                "運悪く",
                "$meの方へと向きを変えて",
                "正面からそのまま$meの意識を刈り取っていった"),
            hero.do("dead").d("そう。",
                "$meはちっぽけな正義感を振り回した挙句",
                "この世界を去ったのだ"),
            )
## ep2 scenes
def sc_awaking(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("目覚めたらどこ？",
            h.be(w.stage.prison, w.day.transfer1),
            hero.think("確か最初にどこかの宗教の神とやらは『光あれ』と言ったのだったか"),
            hero.think("$meがそんなことを一番に思い出したのは",
                "何も神頼みがしたいとかそういう超常的な現象に縋りたいとかといったことではなく",
                "ただ目の前が果てしなく闇だったからだ"),
            hero.think("そもそも人というのは死んでもその意識というのはずっと消えないものなのだろうか"),
            h.think("生憎と$meは宗教やオカルトの趣味も教養もなく",
                "死んだらそれで終わり", "全部が綺麗サッパリと無くなってしまうものだろう",
                "くらいに考えている。",
                "だから死んでも尚", "何かしらを考えてそのままよく分からない場所を彷徨い続けるなんてことがあれば",
                "喩えこの世ならぬ美女の花園であったとしても", "そこを地獄と呼ぶだろう"),
            hero.think("記憶の限りなら",
                "$meはトラックによって容赦なく轢き殺されたはずだ"),
            hero.think("ひょっとすると人間というものは意外と丈夫に出来ているそうだから",
                "今こうして$meが思考している間にも手術やら何やらが行われて",
                "生死の境目から助け出されようとしているところなのかも知れない"),
            hero.think("もしそうなら",
                "早く目覚めることよりも", "とにかく無事に息を吹き返させてくれることを望む"),
            hero.feel("だがしかし",
                "仮にそういった状態にあるのなら",
                "こんなにも意識がはっきりとしているだろうか"),
            hero.think("実に不可思議な感覚だ"),
            hero.think("それは$meが知る数少ない言葉から敢えて選ぶとすれば”無”。",
                "そう。",
                "一切が存在せず",
                "光だ闇だ",
                "男だ女だと騒ぐ必要もない",
                "完全な無の世界"),
            h.think("パンツのない無", "だ"),
            h.think("そんな言葉が浮かんだのは元彼女に言われたつまらない言葉を思い出してしまったからだ"),
            h.think().emphasis("$i_herword006"),
            h.think("パンツすら生まれない闇がどこまでも広がっているように感じられた"),
            hero.feel("感じる？"),
            hero.think("仮に死んでしまっていたならば何も感じることなどないだろう。",
                "そうだ。",
                "手を動かそうとも",
                "足を動かそうとも",
                "そんな感覚はどこにもなくて当然なのだ"),
            hero.be("ただ",
                "何だろう"),
            hero.think("それは圧倒的な違和感だった"),
            hero.think("何かの超常的な存在感が",
                "$meの心の一番奥底に眠るある感情をまさぐっていた"),
            ery.talk("ほお。",
                "そなた",
                "意識があるのか"),
            hero.think("声",
                "という代物ではなかった。",
                "低く",
                "地面を揺るがすような振動を持っていたが",
                "それでもおそらくは女性のそれだと分かる"),
            hero.think("ここがどこなのか",
                "それこそ天国だか地獄だか生死の境なのか知らないが",
                "そんな宙ぶらりんの$meに道案内でもしてくれる可愛らしい女性でもいるのか。",
                "それならさっさとその姿を見せて",
                "一瞬だけでいい",
                "一体今$meがどうなっているのかちゃんと認識させてくれ"),
            hero.hear("だがそんなことを考えた$meに浴びせかけられたのは",
                "自分の体ごと震わすような圧倒的な高笑いだった"),
            ery.talk("何だ。",
                "お主はせっかく現れたというのにもう$meに消してもらいたいというのか？",
                "二百年ほど掛けてようやく呼び出せたというのに",
                "そう簡単に消えてもらう訳にはいかんなあ"),
            hero.think("何なのだろう", "この女。",
                "いやそれ以前に$meの言葉が通じているなら",
                "ずっと気になっていたことを質問してみるのが先だ"),
            hero.ask("なあ。",
                "あんたは$meの言葉が分かるようだから是非一つ確認したいことがあるんだが"),
            ery.ask("何だ？"),
            hero.ask("今の$me。",
                    "一体どうなっているんだ？",
                    "何も見えないし",
                    "ここは暗闇なのか？",
                    "それに体を動かそうにも何の感触もない。",
                    "自分で自分のことがさっぱり分からないんだよ"),
            hero.hear("今度は噛み殺した笑いだった"),
            hero.ask("さっきからあんた何をそんな笑ってるんだ？",
                    "$meってそんな奇妙な格好させられてるのか？"),
            hero.think("会社の新入社員歓迎会で上司の命令で当時流行っていたアニメの女子のコスプレをさせられたことを思い出し",
                    "有り得ないほど短い丈のスカートからガーターベルト付きの真っ黒なストッキングの脚を見せてしまったあの恥辱が",
                    "何十回と脳裏を過って行った"),
            ery.ask("お主",
                    "自分が何者であるか",
                    "全く分かっておらぬ", "ということか？"),
            hero.reply("分かるも分からぬもないさ。",
                    "何も見えない感じない",
                    "そもそも口すらないみたいなのにどうして$meしゃべれてるんだ？"),
            hero.hear("小さな溜息だった"),
            ery.talk("わかった"),
            hero.think("続いてそう呟くと", "彼女の気配が途切れる"),
            hero.think("何だ？"),
            hero.think("トンネルを抜け出た時に感じるような",
                    "不思議な間だった"),
            w.combine(
            hero.look("続いて目の前に強烈な光を感じ、"),
            hero.feel("それが何かの感触となって$meに襲いかかる。",
                    "その次の瞬間",
                    "今まで失われていた感覚が一気に戻ってしまったかのような激しい熱と痛みが全身を包み込んだ"),
            ),
            hero.ask("あ、あんた",
                    "一体$meに何したんだ！？"),
            hero.think("熱いのが全身に広がると",
                    "今度はそれが一気に冷却されたみたいに意識を落とし穴に投げ込まれた勢いで",
                    "$meは目を覚ました"),
            hero.do("そう。",
                    "目を",
                    "覚ますことが出来た",
                    "のだ"),
            )

def sc_Iampants(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("転生したらパンツだった",
            h.look("眩しい"),
            h.feel("最初に感じたのは懐かしい瞼の感覚だった"),
            hero.talk("何が起こったんだ……"),
            hero.look("続いてうすぼんやりとした光の輪のようなものが見えた"),
            hero.look("それが徐々に人の形を成していき",
                "胡座で座っている人間の女性のシルエットとして浮かび上がる"),
            hero.look("はじめ彼女は白い肌に白い服を着ているのだ",
                "と思ったのだが",
                "どうやらそうではない。",
                "自ら発光していた"),
            hero.look("顔は髪にその輪郭部分が覆われてしまっているが",
                "相当な小顔と見て良いだろう。",
                "きりっとした黄金色の瞳に",
                "すっと通った鼻筋",
                "赤紫の形の良い唇が目立つ"),
            hero.look("けれど何よりも奇異と感じさせたのは",
                "足元まで伸びる毛量の多い髪だ。",
                "色は部分的にピンクにも見える紫で",
                "頭から顔の隣を降りて",
                "二つの滝のようになって胸元を通り抜け",
                "臍のあたりで交差するように広がり",
                "それがひざ掛け然として彼女の脚を覆っていた"),
            hero.think("それを目にして浮かんだのは『髪ブラ』というワードだった"),
            hero.look("ただ目の前のそれはブラなどという部分的な名称には収まりきらない",
                "正に髪のドレスと言ってしまって良いだろう。",
                "それくらいしっかりと彼女の下半身を覆い尽くしている"),
            hero.think("おそらくその髪のドレスの下は裸体なのだが",
                "劣情を微塵も感じさせないほどの高貴さと美麗さが漂っていた"),
            ery.ask("$meの姿を見ても驚かぬとはな",
                "お主", "さてはただの阿呆だな？"),
            hero.look("小さな口がきゅっと曲がり",
                "楽しそうな笑い声と共に尖った小さな犬歯が見えた"),
            hero.talk("あんたが痴女でない限りは",
                "そういう格好でいる女性を$meはまともには見られないよ。",
                "とにかく服でも何でもいいから着てくれ"),
            hero.think("いつもなら理性も吹っ飛びそうなほどの下腹部の猛りを感じるだろうが",
                "どういう訳か目の前の裸女からはそんな劣情は一切感じない。",
                "寧ろ彼女を神々しいとさえ感じる。",
                "ミロのビーナスを前にして一心不乱にその曲線をスケッチブックに写し取る作業でもしているかのようだ"),
            hero.look("しかし目の前に座る女性",
                "一向に服を着ようとしない。",
                "これが本物の痴女というやつか",
                "と思いそうになったが",
                "もしかすると別の可能性があることに$meは気づいた"),
            hero.ask("ひょっとしてあんた",
                "服を持っていないのか？"),
            hero.look("だが彼女は目元を細めて眉間に皺を寄せただけだ"),
            hero.ask("$meが死んだか死んでいないかは一旦置いておくが",
                "今まであんたのことを天国に連れて行く天使的な",
                "あるいは地獄に連れていく鬼的な何かかと思っていたんだが",
                "そうだよな",
                "あんたも訳が分からないまま今ここで目を覚ましたばかりということだって有り得るし",
                "そう考えるのが自然だった。",
                "とすると何だ。",
                "$meも今素っ裸だったりするのか？"),
            hero.look("そう思うと急に羞恥心が湧き上がってきて",
                    "$meは慌てて自分の体を確認しようとした"),
            hero.think("ん？"),
            hero.behav("$meは自分の体を確認しようとした"),
            hero.think("あれ？"),
            hero.behav("$meは自分の体を……"),
            ery.ask("何を", "しておるのだ？"),
            hero.talk("いやな",
                    "どういう訳か自分の体が見れないんだ。",
                    "そもそも見えるようになったのに手も足も動かないし",
                    "顔も動かせないみたいだし……。",
                    "すまないが",
                    "今の$meってその",
                    "何も着ていない状態だったりするのか？"),
            hero.hear("その言葉に",
                    "彼女は再び大きな声を上げて笑った"),
            hero.talk("だから何がおかしいんだ？",
                    "こっちはこれでも相当困っているんだぞ。",
                    "いや$meだけじゃない。",
                    "あんただってそうだろう？"),
            ery.talk("まあ確かに困っておるが……"),
            hero.talk("だろう？",
                    "だったらここはお互いに協力してだな",
                    "この不毛な状況を何とか打開するというのが",
                    "同じ人間としての使命じゃないだろうか"),
            hero.hear("しかし彼女は喉の奥を鳴らして笑いを呑み込むと",
                    "一際声を低くしてこう告げた"),
            ery.talk("人間？",
                    "$meが人間だと言うのか？",
                    "そもそもお主だってとても人には見えぬぞ"),
            hero.think("ずっと最初から違和感があった"),
            hero.ask("何……だって？"),
            hero.think("目覚める前",
                    "痴漢男を追いかけていて向かってきたトラックに轢き殺されたはずの自分の意識が",
                    "ここで蘇った時からずっとだ。",
                    "目が見えないことへの不安や不思議が",
                    "その正体だと思っていた"),
            ery.talk("折角見えるようにしてやったのに",
                    "それだけで不満とはな"),
            hero.think("次には女の声が聴こえてきたことで",
                    "その正体の知れぬ彼女への不信感から来る何かだと思い込んでいた"),
            ery.talk("わかった。",
                    "ではそこに鏡を作るから", "それでよく己の姿を確認するが良かろう"),
            hero.look("彼女はそう言うとおもむろに立ち上がり",
                    "それから背を向けて屈み込んだ"),
            ery.talk("しばし待っておれ"),
            hero.look("何だろう。",
                    "きゅっと締まった剥き出しの女性の臀部が",
                    "二つに割れているのがよく見える"),
            hero.talk("な、何する気だ！？"),
            hero.behav("$meは慌てて目を閉じたが",
                    "彼女は全く気にしていないようで",
                    "何も見ないように",
                    "何も想像しないようにしている$meの聴覚には",
                    "暫くするとチロチロという妙な音が響いてきた"),
            hero.think("それは夏の炎天下から逃げ出した彼女が",
                    "体操着のまま水道の蛇口を捻った時に思ったよりも水量がなく",
                    "線のように細い流れが下のコンクリへと届いて",
                    "ピチピチと跳ねて運動靴の上の白く端が丸まった靴下を履く足へと掛かった",
                    "そんな場面を想起させる音だった"),
            ery.talk("もう目を開けて良いぞ"),
            hero.look("ふぅ", "という彼女の吐息に続いてそう促され",
                    "$meはおずおずと目を", "左側から開ける。",
                    "最初は薄目にして",
                    "彼女が元の位置に再び胡座で座っているようだと確認できてから",
                    "右側の目も開けた"),
            hero.look("彼女と$meの間には", "小さな泉が生まれていた"),
            hero.look("それはおそらく", "いや間違いなく",
                    "彼女から絞り出された体液の一部なのだが",
                    "どういう訳か匂いも何も感じない。",
                    "それどころか淡く光を放ち",
                    "表面が鏡のように周囲の様子を映し込んでいる"),
            hero.look("だから$meは躊躇することなく",
                    "そこに映っている何かの姿を見やった"),
            hero.think("あ……"),
            hero.think("初めて鏡を目にした動物の心境というのは",
                    "こんな感じなのかも知れない"),
            hero.look("そこに映るものが何か",
                    "と問われれば",
                    "$meは自分のなけなしの語彙の中から人間以外のものを引っ張り出してこなければならない"),
            hero.look("少なくとも人ではなかった"),
            hero.look("それどころか",
                    "そいつは手も足もない。",
                    "寧ろ手足があったら恐い"),
            ery.ask("分かったであろう？",
                    "お主は人ではない"),
            hero.look("彼女の言う通り",
                    "本当に人ではなかった"),
            hero.think("それはその他の動物", "いやもっと言えば生物ですらない"),
            hero.look("輪郭を取れば平たい三角形を更に横に引き伸ばしたように見える。",
                    "おそらく$meが立ち上がれていたなら",
                    "それはもっと立派な小さい三角形をした何かに見えただろう"),
            ery.ask("よく見えぬか？",
                    "ならば$meがじっくりと見せてやろう"),
            hero.talk("い、いや",
                    "そこまでしなくても大丈夫だ"),
            ery.talk("何故恥ずかしがるのか分からんが",
                    "全身を見られないというのもつまらない。",
                    "しっかりと自分の目で今一度",
                    "己が何者なのかを確認すると良い"),
            hero.talk("ああぁぁ", "やめろ！", "やめてくれ！",
                    "$meは絶対に見んぞ！",
                    "どうして自分のこんな姿を見なきゃいけないんだ！"),
            hero.deal("だが暴れようにも手足がない"),
            hero.deal("$meの体は立ち上がったその女の手によって軽々と掴まれ",
                    "鏡となった水面に",
                    "ご丁寧にもわざわざしっかりと広げた姿を映し出された"),
            hero.think("そこに映し出されたのは紛れもなく", "パンツだ"),
            hero.look("小学生低学年の児童が履くような",
                    "クマのイラスト付きのパンツだった"),
            hero.look("$meの目はどうやらその正面を見ているクマの目らしく",
                    "くりっとして愛らしいとは思うが",
                    "パンツに張り付いた単なるイラストとなった自分をまじまじと見させられるのはただの拷問ではないか",
                    "と思わなくもない"),
            hero.talk("$meは",
                    "パンツ", "なのか……"),
            h.hear("その言葉を発した$meに", "彼女が喉を鳴らすような嘲笑をしているのが聞こえたのだった"),
            )

## ep4 scenes
def sc_lookingmypants(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("どう見てもパンツ",
            hero.be(w.stage.prison, w.day.firstmeet),
            h.think("本当に$meはパンツ", "なのか……"),
            hero.look("見下ろした薄く輝く水面には",
                "一枚の女児向けパンツを手にして立つ",
                "グラマラスな女性が映し出されていた。",
                "彼女はその肢体を大量の紫色の頭髪によって覆い隠している為",
                "乳頭や下腹部は見えないものの",
                "それでも布地面積の少ない水着を着ているようなものであって",
                "$meからしてみれば目のやり場に困るな",
                "という印象だった"),
            hero.think("いや",
                "そんな冷静に彼女について語っている場合ではない"),
            hero.talk("どうして$meはパンツなんだ！？"),
            hero.look("思わず考えていることが声になったが",
                "パンツの前面に付いているクマのイラストは微動だにしない。",
                "一体どこから声が出ているのだ"),
            ery.talk("声が出ているように聞こえるだけで",
                "実際には声など出ておらぬ"),
            hero.hear("女は溜息混じりにそう言った"),
            hero.think("しかしそもそもその声が聞こえるということはパンツである$meにも何かしらの聴覚は備わっているのだろう"),
            hero.think("パンツの聴覚って何だ？",
                "股布が震えるのか？"),
            hero.think("考えれば考えるほど頭が痛くなってくる。",
                "しかも現在その痛くなる頭すら持ち合わせていないのだ。",
                "何故なら$meはパンツだから"),
            ery.ask("何をしょぼくれておる？",
                "折角こうして$meと対話できるように視覚と聴覚を与えてやったというのに",
                "不満なのか？"),
            hero.talk("あんたが見えるようにしてくれたのか？"),
            hero.look("彼女の形の良い顎がコクリ", "と一つ頷いて見せる"),
            hero.think("ああ、なんだ。",
                "これは夢か"),
            hero.think("その考えで納得を得ることを何故一番最初に思いつかなかったのか",
                "$meは自分の勘の悪さを嘆いた"),
            hero.think("そもそも人間が目覚めたらパンツになっていたというのは",
                "夢以外の何物でもないじゃないか。",
                "カフカを読んだことはないがあれだって実体験ではなく単なる創作だ。",
                "夢であれば目の前に裸の女がいても不思議じゃないし",
                "パンツである$meが彼女と話したりしていても誰も笑わない"),
            hero.talk("なあ。", "ちょっと確認したいことがあるから",
                "ひとつ$meの頬を抓ってみてくれないか？"),
            ery.ask("お主の頬とはどこのことだ？"),
            hero.look("彼女は$meを持ったまま怪訝な表情になってそう尋ねる"),
            hero.think("言われてみればその通りだ。",
                "パンツの頬とはどこだろう？",
                "そもそもパンツに頬というか", "顔という概念はあるのだろうか"),
            hero.think("もし今ここに別れた彼女がいてくれたなら教えてもらえたかも知れない"),
            hero.remember().emphasis("$i_herword003"),
            hero.think("そんなことを言っていたことを不意に思い出し",
                "ますます$meはここがただの夢の中なのだと実感した"),
            hero.talk("頬はよく分からないから",
                "そうだな。",
                "代わりに踏みつけてくれないか？"),
            ery.talk("ほお……"),
            hero.look("そう提案した$meの前面を覗き込むようにして彼女はまじまじと見つめる。",
                    "悪戯っぽく赤い舌を覗かせて「そうかそうか」と舌舐めずりまでする"),
            hero.think("それを目にした瞬間背筋を悪寒が登っていった気になったが",
                    "パンツに背筋なんてものはなかった"),
            hero.talk("え……"),
            hero.deal("唐突に視界が上を向く"),
            hero.look("$meはそのまま暗い天井を見上げながらゆっくり落ちていくと",
                    "ぴたりと地面に張り付いた……おそらくそうだろう。",
                    "視界が動かなくなり",
                    "彼女が見下ろしているのが分かったからだ"),
            ery.talk("お主はそういう趣味の持ち主だったとはな……"),
            hero.talk("な、何か勘違いしてないか？"),
            ery.talk("では遠慮なく……"),
            hero.think("彼女には$meの言葉は届いていないようだった"),
            hero.look("すっと視界に入り込んできた女性の右足の裏は白く発光していて",
                    "ああ、人間の足の裏というのは意外と綺麗なものなのだな",
                    "という$meの素朴な感想を引っ張り出す"),
            hero.look("形の良い縦長の楕円の踵部分が仄かに赤らみ",
                    "少し窪んだ土踏まずを経由して上半分のつるりと目立つ母趾までの緩やかな曲線が心地よい。",
                    "その上に生えた五本の柔らかい茸のような指はしゃぶりつきたくなるような膨らみになっていて",
                    "それがどんどん大きくなる"),
            hero.look("いや", "迫ってくる"),
            hero.look("そう気づいた時には視界が暗くなり",
                    "何も分からなくなった"),
            ery.talk("どうだ？",
                    "お望み通りにしてやったが……"),
            hero.talk("何も分からん"),
            hero.think("踏まれている",
                    "ということだけは理解したが",
                    "痛みも苦悶も喜びも何もなかった。",
                    "ただ彼女のささやかな笑い声と何度か上下する足の裏だけを感じ取ることができた"),
            ery.talk("それはそうだろう。",
                    "お主に与えたのは視覚と聴覚のみで",
                    "痛覚や触覚までは持ち得ていないのでな"),
            hero.talk("それなら$meはどうやってこれが夢か現実かを見分ければいいんだ？"),
            hero.hear("そう尋ねた$meを",
                    "彼女は盛大に笑う"),
            hero.ask("何がおかしい？"),
            ery.talk("まだ己のことがよく理解出来ていないようだと思ってな"),
            hero.look("彼女はそう言うと",
                    "パンツである$meを持ち上げて座る。",
                    "自分の目線まで引っ張り上げると",
                    "言い聞かせるようにして「教えてやるが」と前置きした"),
            ery.talk("お主は$meが次元に穴を開けて何とか手繰り寄せることが出来た唯一の物なのだ。",
                    "それが意志を持っていたというのは驚きだが",
                    "退屈凌ぎに気まぐれな神が遣わした存在かも知れぬな。",
                    "しかし五百年も世間に顔見世をしていないと$meを知らぬ存在もいるということか"),
            hero.look("彼女は小さく溜息をついたが",
                    "$meはそれよりも頭の悪い作家が考えた不出来な映画かアニメーションの設定を聞かされたような気分で",
                    "次元だ何だという話に嘆息したくなった"),
            hero.talk("じゃあ訊くが",
                    "今の話からすると",
                    "あんたが$meをパンツにしたと考えて良いってことだな？"),
            ery.ask("パンツとは何だ").t("$meはお主を呼び寄せただけでそれ以外は何もしておらぬが……その前に一つお主に尋ねたいことがある。",
                "先程から何度も言っている”パンツ”とは一体何なのだ？"),
            h.look("$meにそう尋ねた彼女は", "きりっとした線の眉毛を少しだけ曲げた"),
            )

## ep5 scenes
def sc_whatispants(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("パンツとは何だ？",
            h.think("パンツとは何か", "と問われて咄嗟に答えられる人間がどれくらいいるだろうか"),
            hero.think("少なくとも$meはその問いに対して即座に「下着のことだ」とは言えなかった。",
                "何故なら三年前に別れた彼女の遺言にも似た最後の言葉があり、"),
            hero.hear().emphasis("$i_herword002"),
            hero.think("というものだったからだ"),
            ery.ask("どうした？",
                "何か答えるのに不都合でもあるのか？"),
            h.look("紫の長い髪をブラジャーにしている女性はきりっとした眉を傾けてパンツである$meを見ているが",
                "パンツが下着だと知った上の冗談として尋ねているようには見えない。",
                "おそらくパンツという言葉を知らないのだろうと$meは推測した"),
            hero.talk("あんたはパンツを身に着けていない。",
                "それに加えてどうも裸のようだ。",
                "パンツという単語が存在しないというよりは",
                "ひょっとすると下着を含めた衣類を身に着けるという文化がないのかも知れない。",
                "そういう前提で話させてもらうが",
                "いいか？"),
            hero.look("彼女はその言葉に眉を顰めていたが",
                "ゆっくりと縦に首を振ったのを確認すると",
                "$meは滔々とパンツについて語り始めた"),
            hero.talk("パンツとは股間を含めた下腹部の一部を覆う着衣の一種だ。",
                "着衣",
                "つまり服を着ることで様々な恩恵を受けることができる。",
                "中でも下着と呼ばれるものは肌着とも呼ばれ",
                "皮膚の上に直接身に着けるように設計されている"),
            hero.look("最初は首を傾げ気味だった彼女も",
                "$meが仕事の時のような語り口になったからか",
                "集中して聞き入っているように見えた"),
            hero.talk("人間というのは思っている以上に日々汚れ",
                "またその常在菌と呼ばれる微生物は皮膚の上で老廃物となり蓄積する。",
                "そういう体表上の汚れ", "あるいは汗のような分泌物を下着は吸収し",
                "それを付け替えることで人間は己の体を清潔に保つという手段を手に入れたんだ"),
            hero.look("それを聞いた彼女の視線がその下腹部の方へと降ろされる。",
                "$meが最初に確認している段階ではそこは長い髪で覆い隠されていたが",
                "今は見えない。", "辛うじて臍の辺りまでだ。",
                "彼女は自分の股間を確かめたのだろう。",
                "理解できないというように眉間に皺を作り",
                "改めて$meを見た"),
            hero.talk("その肌着の内で主に股の部分を中心に覆うようになっているものがパンツだ。",
                "あんたがさっきした",
                "その",
                "おしっこのように",
                "人は食べたもの飲んだものを排出する。",
                "そこはとても不衛生となる。",
                "だからこそ普段パンツで覆って生活することで",
                "自分を", "そして周りを汚染せずに済むという訳だ"),
            hero.think("もっと言えばデザインやオシャレといった精神性の問題もあるが",
                "目の前の女にそういった説明をしても混乱を招くだけだろうと思って敢えて省いた"),
            hero.talk("パンツが何か", "分かったか？"),
            ery.talk("そうだな……つまりだ。",
                "パンツとは身に着けるものであり",
                "$meは今裸だ。",
                "本来であれば$sagerobeという法衣を身に着けておったのだが",
                "事情があって今", "$meの手元にはないのだ"),
            hero.look("彼女は$meの端を両手で持ったまま頷くと", "にっこりと笑みを向ける"),
            hero.talk("わ、分かってくれたなら良かったよ"),
            hero.feel("ぞわり", "という妙な悪寒に$meの警戒心が顔を覗かせた"),
            hero.look("何だろう。",
                    "彼女は$meの両端を持ったまま立ち上がると",
                    "その紫の髪で胸元から下までを覆い隠しているのが改めてよく見えた。",
                    "その片方の足が", "不意に持ち上がる"),
            hero.look("右足だ"),
            hero.look("続いて少し背を曲げるようにして屈み込むと",
                    "$meの視界はぐんぐんと下降していき",
                    "ほど良い二つの丘から",
                    "肉付きのよい腹部",
                    "形の良い臍を経て",
                    "何もないつるりとした彼女の下腹と",
                    "その先に存在するであろう女性の排泄器官までが見えてしまう"),
            hero.look("そう思った瞬間だった"),
            ery.ask("ところでお前には前と後ろがあるのか？"),
            hero.talk("パンツの前後ろのことだったら",
                    "確かに存在する。",
                    "クマのイラストが付いている方が前だ"),
            hero.think("そう答えながらも$meは何を言っているのだろう",
                    "という意識がどうしても脳裏から離れてくれない。",
                    "そればかりか",
                    "彼女の質問からはどう考えても",
                    "ある結果しか導かれないではないか"),
            ery.talk("そうか。",
                    "ならばこういうことか"),
            hero.look("刹那",
                    "$meの視界は百八十度振り回され",
                    "この薄暗い空間の壁へと向けられた"),
            hero.feel("それに続いて自分のお腹が内部から広げられたような",
                    "何とも胸苦しさを覚える感覚が湧き上がり",
                    "もそもそと何かが動く気配を背中側に強烈に感じさせられた"),
            hero.talk("あぅ！？"),
            hero.feel("何かが",
                    "$meの右半身を貫いていった"),
            hero.think("痛みを伴った衝撃ではないが",
                    "何と表現したものだろう。",
                    "ムズムズとするような", "痛痒感とでも呼べばいいのだろうか。",
                    "それがずっと右半分に張り付いている"),
            hero.feel("けれどそれはすぐ残りの左半分にもやってきた"),
            hero.talk("ひゃう！"),
            ery.talk("妙な声を上げるでない"),
            hero.talk("け、けどな。",
                    "あんた一体何をしたんだ？"),
            hero.look("一瞬潰れたように歪んだ視界は",
                    "今は明瞭だった。",
                    "少しは目も慣れてきたのだろう。",
                    "壁は岩肌で",
                    "視界の切れ端に鉄の棒のようなものが見える"),
            ery.talk("ほお……これは", "なかなかに"),
            hero.feel("彼女の手が",
                    "$meに触れる。",
                    "それは分かる。",
                    "けれどその内側にあるものは一体何だ"),
            hero.think("考えろ。",
                    "今どういう状況なんだ"),
            ery.talk("何をごちゃごちゃと言っておる。",
                    "お主はパンツ。",
                    "そして$meは外見上は人間の姿をしておる。",
                    "ならば自ずと答えは導かれよう"),
            hero.talk("嘘、だろ……"),
            hero.hear("彼女は声を殺して笑う"),
            hero.look("確かに少し考えれば分かることだった。",
                    "さっき彼女に持たれていた時よりも随分と視界が低い。",
                    "それは彼女の顔の高さより低い位置だということだ。",
                    "それに目の前には部屋の様子が広がっていることから",
                    "彼女の方を見ていないということになる"),
            hero.think("自明", "というやつだ"),
            hero.think("そうだ。",
                    "つまり$meは彼女に……"),
            hero.talk("履かれているのか！？"),
            ery.talk("お主が言ったではないか。",
                    "パンツは履くものだと"),
            hero.think("そう認識した瞬間",
                    "自分の内側に女性のアレやソレやコレが密着しているのだということに気づいて",
                    "$meは思考に急ブレーキを掛けようとした"),
            h.feel("その時だった"),
            ery.talk("お、お主", "謀ったな！"),
            h.hear("彼女が声を荒らげると同時に",
                    "$meの視界は眩い光で塗り尽くされた"),
            )

## ep6 scenes
def sc_littlegirl(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("小さくなったエリィ",
            hero.be(w.stage.prison, w.day.firstmeet),
            h.look("彼女にパンツとして履かれている",
                "と感じる間もなく視界いっぱいに光が広がったが",
                "それが音もなく収まった。",
                "その気づきと共に",
                "$meの聴覚には今まで聞いていた女の声とは違う",
                "もっと甲高い", "それに舌足らずなものが響いてくる"),
            hero.ask("他に誰かいるのか？"),
            h.deal("だが返答はなく", "$meは周囲を確認しようとパンツである己の視界の限界を探った"),
            h.look("天井は暗くてよく見えないが", "あまり高くないようだ。",
                "それに壁も同じような素材に見える。", "岩かそれに似せたものが窓もなくべったりと覆っている。",
                "多少明るい前方には壁の代わりに金属製の棒が幾つも並べられていて",
                "それは鉄格子のようにも思えるが", "あまりはっきりと見えない為に判別は付かない"),
            hero.look("他に確認できるのは足元の鏡のような水面だ。",
                "彼女が作り出したそれには",
                "パンツとなった$meを履いたままその両端を小さな手でぎゅっと握りしめて立っている",
                "足元までの長い紫色の髪を垂らした女が映っていた。",
                "ただそれは先程までのあの女でない。",
                "明らかに幼女と呼んでいいような年齢の小柄な女の子だった"),
            hero.talk("あの……"),
            hero.think("泣きそうなところを必死に我慢している彼女に対して",
                "何を言ったものかと思案してみたが",
                "声を出したところでその目が鋭くなったのを確認して",
                "$meはすぐまた黙り込む"),
            hero.look("先程までの",
                "$meをパンツにしたかも知れない大人びた女が低学年向けパンツを履く姿は",
                "どこかそういう世界観のプレイでもしているように見えて",
                "強烈な違和感が醸し出されていたが",
                "今こうして小さい女の子が$meというパンツを履いている姿として映し出されると",
                "何の抵抗もなく自分がただの児童向けパンツであることを受け入れられそうな気分になる。",
                "それくらい彼女に$meは似合っていた"),
            hero.look("しかし当の本人はそれなりに文句があるようで",
                "口元をぎゅっと結びつけて",
                "何かを必死に堪えている"),
            hero.ask("一つ確認なんだが"),
            ery.ask("何だ"),
            hero.hear("声が不機嫌だ。",
                "ただ先程までのような威圧感がない為か",
                "どこか可愛らしい"),
            hero.ask("今$meが見ているこの女の子は",
                "あんたで間違いないんだな？"),
            ery.talk("ああそうだが……女の子言うな！"),
            hero.deal("眉毛がくっと角度を急にして",
                "彼女の小さな丸い手が$meの目の前に何度も叩きつけられた"),
            hero.feel("しかし痛覚を持たない$meにとって",
                "それはただ単に視界を幼女の拳が覆うという現象に過ぎない"),
            hero.think("これはこれでいくら叩かれても大丈夫というのは良いものかも知れない"),
            hero.think("そんな思いが生まれるくらいパンツ人生に馴染みつつある自分が悲しくなる"),
            hero.ask("失言はすまない。",
                "謝るよ。",
                "ただあんたはどうして小さくなったんだ？",
                "何かしたのか？"),
            hero.look("だが彼女はじっと水面に映る$meを見たまま",
                "何も言わない"),
            hero.talk("ひょっとして……$meの所為なのか？"),
            ery.talk("お主以外に誰が$meをこんな姿にできると思っておるか！",
                    "ええい！", "騙しおってからに！"),
            h.deal("彼女は怒りを顕にして何度も$meであるパンツを叩く。",
                    "だが何度も言おう。", "$meには痛覚がない。",
                    "痛みを伴わない打撃というのは", "モニタの向こう側の出来事のようにまるで他人事にしか思えない"),
            hero.talk("必死になっているところ済まないが",
                    "$meは何もしていないぞ。",
                    "そもそもあんたが喋れるようにしてくれるまで$meは何もできなかったんだ。",
                    "考えることしかできなかった。",
                    "そんな$meにあんたを小さくできると思うか？"),
            ery.talk("そう言われればそうだ。",
                    "それにお主からは全く$i_energyを感じぬ。",
                    "簡単な魔法すら使えぬであろうな"),
            h.think("どうやら話の分かる相手のようで安心した。",
                    "$meはひとまず状況を整理する為に", "互いの身の上についてある程度打ち明けることを提案する"),
            hero.talk("どうだ？", "お互いの情報を共有すれば何か解決の糸口が見えるかも知れない。",
                    "何より困っていたから$meを呼び出した訳だろう？",
                    "まあ$meが現れたことは手違いだったかも知れないけどな"),
            ery.talk("お主……パンツにしては随分と知性があるな。",
                    "よし分かった。",
                    "ではまずお主の話を簡単に聞かせてもらおうか"),
            h.deal("そう言って彼女は$meを履いたまま",
                    "地面に胡座を掻いて座った"),
            )

def sc_prisoner(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("我は囚人である",
            hero.talk().t("ちょっと待て。",
                "$meは何もしてないし",
                "そもそもただのパンツだぞ。",
                "そいつに何が出来るって言うんだ？"),
            hero.think().d("自分の所為と彼女に言われて慌てたが",
                "よくよく考えてみれば$meを履いた大人の女性が幼女になっただけだ。",
                "そのよく分からない現象の責任をパンツである$meに押し付けてもらっても困る"),
            ery.talk().t("力が……出せないのだ"),
            hero.ask().t("力って何の？"),
            ery.talk().t("$i_energyと呼ばれておるものだ。",
                "重い石を手を使わずに持ち上げたり",
                "炎を出したり",
                "水を鏡にしたり",
                "お主にやってやったように物体に視覚や聴覚を与えるなどといったことも可能だ"),
            hero.think().d("手品とは違う",
                "ということだけは分かった"),
            hero.think().d("こんな状況でもなければ$meはあまりそういった迷信じみたことに理解を示さないが",
                "流石に自分がパンツになってしまっていて",
                "そんな$meに目と耳を与えてくれたらしい彼女の言葉を信用しない訳にもいかないだろう"),
            hero.talk().t("それがどうして出せなくなったんだ？"),
            hero.hear().d("彼女は一際大きな溜息を落としてから",
                "小さく首を振ってこう続ける"),
            ery.talk(w.i.destroy_sage.flag()).t("だからお主の所為だと言っておる。",
                "どういう理屈かは分からんが",
                "パンツとやらを履いたら$i_energyが急激に萎んでいき",
                "見事に育ったはずだった$Iの体があの頃の軟弱な自分に戻ってしまった。",
                "世界を破滅に追いやった大賢者様がこんなちんちくりんじゃ", "良い笑いものだぞ"),
            hero.think().d("パンツを履くと力が失われる",
                "という発言に",
                "$meは小さい頃に楽しんだあるＴＶ番組の再放送を思い出した。",
                "あれはパンツではなく金の輪っかだったが",
                "それを付けられた粗忽者の猿男は経典を求めて旅をする僧侶に戒められる度に呪文によりその輪を締められる。",
                "痛みによって力を制御される様は",
                "子供心にも体育会系の肉体派指導ここにあり",
                "と刻み込まれたが",
                "人というのは言葉では何も教えられないのかも知れないという諦めも同時に$meの心の中に植え付けていった"),
            hero.ask().t("それなら$meを脱げばいいんじゃないのか？"),
            hero.think().d("$meを履いて縮んだというなら", "それで問題は解決するはずだ。",
                "もし仮にそれでも元に戻らない場合は",
                "これはもう$meが原因ではないということになる"),
            ery.talk().t("それでもそうだの。",
                "何故そんな簡単なことに思い至らなかったのだろうか……",
                "よし分かった。",
                "脱ぐぞ？"),
            hero.think().d("そんな確認は要らないと思ったが$meは一応「おう」と頷いてやると",
                "彼女は$meの両端を掴み",
                "勢いよくそれを下ろした"),
            ery.talk().t("ん！？"),
            hero.look().d("勢いよくそれを"),
            ery.talk().t("おい！",
                    "お主今度は何をしておるんだ！"),
            hero.talk().t("いや$meは何も。",
                    "そもそも何か出来るならあんたに言われる前にしてるよ"),
            hero.think().d("ただのパンツに無理言わないでくれと思いつつも",
                    "何故彼女はさっさと$meを脱がないのだろうと不思議に感じた"),
            hero.talk().t("どうしたんだ？"),
            ery.talk().t("脱げん"),
            hero.think().d("はあ？",
                    "である"),
            hero.talk().t("パンツが履けたのなら脱ぐことも出来るだろう？",
                    "それとも誰かにしてもらわないとパンツすらまともに脱げないくらい退化してしまったのか？"),
            ery.talk().t("ええいうるさい！",
                    "$Iだってパンツくらい一人でどうとでも出来るわ！",
                    "侮るでないぞ！"),
            hero.look().d("しかし一向に$meの視界は変わらない"),
            hero.feel().d("そればかりか",
                    "触覚がないはずなのに体の内側にピッタリフィット感があった。",
                    "それが存外心地良い。",
                    "これが収まっているという満足感なのだろうか"),
            hero.think().d("パンツの満足感て何だよ……"),
            ery.talk().t("んーんー！",
                    "脱がして！",
                    "パンツ脱がして！"),
            hero.look().d("そんなことを考えている間にも",
                    "彼女を$meを引っ張って無理やり自分の足から引き抜こうとしているが",
                    "どういう訳か皮膚の一部にでもなったのかのように",
                    "パンツは彼女の臀部をしっかり覆ったまま離れようとしない"),
            hero.think().d("仮に$meが人間であったなら",
                    "幼女の下腹部に抱きついたまま殴られても蹴られてもしっかりと抱き締めたままでいるといった感じかも知れないが",
                    "生憎と$meにはそんな趣味はないし",
                    "何より$meはパンツだ。",
                    "彼女を掴む手すら持ち合わせていない"),
            hero.think().d("$meがどうこうして解決する問題とは思えなかった"),
            hero.talk().t("なあ",
                    "もう諦めたらどうだ？",
                    "パンツ", "脱げないんだろ？"),
            ery.talk().t("分かった。",
                    "壊す"),
            hero.think().d("何？"),
            ery.talk().t("いくら$Iの$i_energyが失われたからといっても",
                    "こんな布切れ一枚破壊するのは造作もない"),
            hero.talk().t("おい。",
                    "やめろ。",
                    "パンツは大事なんだぞ？",
                    "$meがいないとお前は一生丸裸で暮らすことになるんだぞ？",
                    "それでもいいのか？"),
            hero.think().d("無茶苦茶な理論だと思ったが", "背に腹は変えられない。",
                    "いや今はパンツだから背も腹も表も裏も変え放題な気がするけれど",
                    "とにかくそんな悠長なことを言っている場合ではない"),
            hero.look().d("彼女のしっかりと握りしめた右手が光を放ち",
                    "その手を開くと",
                    "輝きが一気に広がった"),
            hero.hear().d("一瞬の間の後で",
                    "大きな地響きを聞いた"),
            hero.think().d("耳がツンとするような張り詰めた静寂を感じると",
                    "次第に視界がはっきりとしてくる"),
            hero.look().d("そこには彼女の手が光を放つ前とほぼ同じ空間が広がっていることが確認できた"),
            hero.talk().t("あれ……大丈夫", "なのか？"),
            ery.talk().t("なぜだ……なぜ壊れぬ！"),
            hero.hear().d("彼女の驚きの声も", "幼いままだ"),
            ery.talk().t("なんで壊れてくれないの！",
                    "そうか。",
                    "ひょっとしたら$Iの力そのものが弱っていてお主を破壊できないのか？"),
            hero.look().d("そう言うと今度はその手を鏡にした水面へと向け",
                    "光を放った"),
            hero.feel().d("空間そのものが震える衝撃の後で",
                    "水面は見事に水滴すら残さずに消滅してしまう"),
            ery.talk().t("おかしいな……。",
                    "何故お主は壊れんのだ？"),
            hero.talk().t("$meに聞かれても知らないよ。",
                    "それよりもこんだけ出来るのにそれでも力が無くなったって言うのか？"),
            ery.talk().t("ここが普通の檻なら",
                    "本来の$Iの力であれば全てを塵にまで分解してしまえる。",
                    "しかしここは特別製でな。",
                    "まあ見てみろ"),
            hero.look().d("そう言うと",
                    "彼女は体を鉄格子に向けて$meにはっきりと見えるようにした。",
                    "それから手を翳して一撃",
                    "光の銃を放つ"),
            )

## ep7 scenes
def sc_namedtaro(w: wd.World):
    h = hero = w.hero
    ery = w.ery
    return w.scene("名前は太郎",
            # TODO: 太郎と命名する
            )

# episodes
def ep1(w: wd.World):
    return (w.chaptertitle(TITLE[0]),
            sc_hardday(w),
            sc_gotoheaven(w),
            )

def ep2(w: wd.World):
    return (w.chaptertitle(TITLE[1]),
            sc_awaking(w),
            )

def ep3(w: wd.World):
    return (w.chaptertitle(TITLE[2]),
            sc_Iampants(w),
            )

def ep4(w: wd.World):
    return (w.chaptertitle(TITLE[3]),
            sc_lookingmypants(w),
            )

def ep5(w: wd.World):
    return (w.chaptertitle(TITLE[4]),
            sc_whatispants(w),
            )

def ep6(w: wd.World):
    return (w.chaptertitle(TITLE[5]),
            sc_littlegirl(w),
            )

def ep7(w: wd.World):
    return (w.chaptertitle(TITLE[6]),
            sc_prisoner(w),
            )

def ep8(w: wd.World):
    return (w.chaptertitle(TITLE[7]),
            sc_namedtaro(w),
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ]

def story_outline(w: wd.World):
    return [
            ]

# main
def story(w: wd.World):
    return (w.maintitle(cnf.TITLES["chap01"]),
            ep1(w),
            ep2(w),
            ep3(w),
            ep4(w),
            ep5(w),
            ep6(w),
            ep7(w),
            ep8(w),
            )

def main(): # pragma: no cover
    from src.pants.story import world
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

