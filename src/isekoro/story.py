# -*- coding: utf-8 -*-
"""Story: re_isekai_sunami
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.isekoro import config as cnf
THM = cnf.THEMES


# scenes
def sc_vanish(w: wd.World):
    h, kasagi = w.hiiragi, w.kasagi
    return w.scene("また異世界が消えた",
            # NOTE: 実は女性作者である（修正）
            h.be(w.stage.apart, w.day.current),
            h.hear("どこか遠くでシャッター音が響いたような気がして",
                "$meは意識を取り戻す"),
            h.look("また異世界が消えた"),
            h.deal("手に取ったスマートフォンのモニタには",
                "すぐに同じフレーズで何十という呟きが流れる"),
            h.talk("どうしてなんだ……なあ", "$sunami"),
            w.combine(
            h.think("それを見て$meは思わず声を漏らしていたが、"),
            h.deal("ほどなく$n_kasagiという$meの担当編集の名前が表示され",
                "目覚まし時計のようなコール音が鳴り始めた"),
            ),
            h.talk("何ですか", "$kasagi"),
            kasagi.talk("ツイート見たか？"),
            h.talk("ええ"),
            h.look("そう答えつつ",
                "ノートパソコンの画面に映っていた原稿を一旦閉じてブラウザを表示する。",
                "国内の主要なニュースサイトでは特に扱われていないが",
                "一部",
                "特にライトノベルやアニメーション関連のニュースを載せているサイトでは",
                "最近よく見るワードが踊っていた"),
            kasagi.talk("またなんだろうな……$isekoro"),
            h.hear("$isekoroと嘆息のように言った後に苦い思いの詰まった紫煙を吐き出したと感じられたが",
                "今は彼の愚痴に付き合っている余裕はない"),
            h.talk("もう少しなんです。",
                "$meが何とかします"),
            kasagi.talk("まだそんなこと言ってるのか？",
                "喩え異世界が全て消えてしまったとしても$meたちには何一つ関係ない。",
                "それどころか寧ろお前は嬉しいくらいなんじゃないのか？",
                "散々異世界ものを書かされて",
                "ずっと自分が書きたいものを封印し続けた$n_hiiragiにとってはな"),
            h.think("どの口が言う。",
                "そんな思いを心の中で握り潰し",
                "こう言って電話を終えた"),
            h.talk("あと一歩で$isekoroを追い詰められるんですよ。",
                "奴は$meの小説の中を移動している。",
                "だからこそ$meが何とかして",
                "彼女を殺してみせます……全ての異世界が殺される前に"),
            )

def sc_gotomyworld(w: wd.World):
    h = w.hiiragi
    return w.scene("私の異世界に",
            h.deal("$kasagiとの電話を終えるとスマートフォンの画面には再び滝のような$isekoroに関するツイートが流れ始める"),
            h.deal("$meは一旦テーブルの上にそれを置いて",
                "汗を掻いているペットボトルのソーダ水を手に取った。",
                "一口飲み込むと刺激が胃袋まで落ちていき",
                "生きている実感を与えてくれる"),
            h.deal("それからビタミン剤をひと掴みして口に放り込むと",
                "改めてノートパソコンに向かう。",
                "マウスを操作して呼び出したのは",
                "未発表原稿だ"),
            h.look("タイトルは『$isekoro』。",
                "ただ彼女を捕まえて殺す為だけに書いている",
                "永遠に発表されることのない原稿だった"),
            h.look("画面には$n_sunamiという名前だけが表示されている"),
            h.explain("$meが書いた『$mybook』の主人公だったカメラ好きの女子高生だ。",
                "大好きな祖父から貰った旧いライカを使い",
                "世界を切り取る能力を持ってしまったことから",
                "様々な騒動に巻き込まれていく。",
                "プロットの時点では$kasagiの受けも良かったが",
                "いざ本になると主人公が地味で魅力に乏しいと言われ",
                "眼鏡をした外見もイラストでのインパクトに欠けるとけなされた"),
            h.think("中身についての評価ならどんなものだって甘んじて受けるが",
                "表紙や挿絵の話ならイラスト屋さんの方に言ってくれと",
                "この時ばかりは$kasagiに愚痴った"),
            h.look("少し目を離すと",
                "原稿の中から$n_sunamiの文字が消えていた。",
                "またどこかの異世界に潜り込んだのだ"),
            h.talk("もうお前が行ける異世界なんて",
                "そんなに残ってないだろ。",
                "分かっているんだ。",
                "お前が最後に向かう場所は"),
            h.deal("ぶつぶつとぼやきながら",
                "キーボードを叩く。",
                "画面に文字がどんどん打ち込まれ",
                "変換され",
                "それが世界を紡いでいく。",
                "ただこの感覚が味わいたくて作家を目指したようなものだ"),
            h.think("それでも",
                "と疑問符が浮上する"),
            h.look().emphasis("踏みしめた土くれから申し訳程度に伸びていた草が",
                "ゆらゆらと落ちてきた白い結晶に触れると途端に生気を失って倒れた"),
            h.think("画面に表示されたその文章に",
                "誰かの心に響く力はあるだろうか。",
                "いつだって自身と不安の狭間で",
                "それでも”$meは面白いはずだ”という無謀な確信というドラッグを呑み込んでは",
                "半ば無理矢理に物語を綴ってきた"),
            h.look("モニタの文字が", "僅かに薄くなる"),
            h.think("この物語世界は既に力を失いつつあるのだ"),
            h.think("誰にも読まれない",
                "楽しまれない物語は",
                "存在しないのと同じ"),
            h.remember("$meはかつて作中で", "そう", "彼女に言わせた"),
            h.think("あとで$kasagiから主人公は作者の代弁者じゃないと怒られたが",
                    "なら一体$meは何の為に書いているというのだろう"),
            h.deal("世界を支える為に",
                    "どんどん文章を書いていく"),
            h.hear("カタカタと心地よいリズムが脳を刺激して",
                    "次々と言葉が目の前に浮かび上がる"),
            h.talk("よし", "これでいける……はずだ"),
            h.deal("ターン",
                    "と勢いよくリターンキィを叩くと",
                    "世界が確定していく"),
            h.look("モニタには既に原稿ではなく",
                    "この$isekoroの世界が映り込んでいた"),
            )

def sc_deadworld(w: wd.World):
    h = w.hiiragi
    return w.scene("死にゆく異世界",
            h.feel("頬に痛いくらいの冷気を感じて周囲を見回すと",
                "そこは床にシミの付いたアパートの六畳間ではなかった"),
            h.look("アスファルトも敷かれていない砂利道だ"),
            h.look("そこにジーンズと七部丈のシャツという軽装で立ち",
                "露出した腕先を撫でた風に思わず自分を抱きかかえる"),
            h.look("振り返れば遥か下に崩れた学校とグラウンドが小さく見えた"),
            h.think("間違いなくここは『$mybook』の世界だ"),
            h.think("主人公だった$n_sunamiはカメラで世界を切り取る能力を使って事件を解決していたが",
                "自分の力がただ世界を好きなように破壊しているだけだと理解して",
                "大嫌いだった学校を壊す。",
                "その先は彼女が封印してしまった自分の本当の初恋の記憶と向き合う話だったが",
                "未完のまま永遠に発表する機会を失われてしまった"),
            h.look("持ち物を確認するとやはりスマートフォン以外には何もない"),
            h.look("空を見上げれば次々と小さなゴミのような雪が落ちてくる。",
                "それらは野道に降り積もり",
                "脇の草花を萎れさせていく"),
            h.look("世界を終わらせる雪だ"),
            h.think("異世界が終わる前には",
                "こんな雪が降るらしい"),
            h.think("そんな話を誰から聞いたのか思い出せないまま",
                "$meは丘の頂上を目指して歩き出した"),
            h.hear("と",
                "どこか遠くで雷のようなシャッター音が響く"),
            h.think("またどこかの異世界が殺されたのだ"),
            h.think("けれどそれが聞こえたということは",
                "彼女が確かにこの近くにいる", "ということでもある"),
            h.look("シミの付いたスニーカーの上で",
                "雪が解けずに付着する。",
                "それを蹴り飛ばすように爪先を振り上げても",
                "離れたりはせずに表皮のように固まり",
                "$meの足取りを重くした"),
            h.think("それはまるで彼女が意志を持って降らせた足止めの雪のようだ"),
            h.think("ずっと考えていた"),
            h.think("何故彼女が『$isekoro』になったのか。",
                "何故ほかの異世界を殺す必要があったのか"),
            h.think("$meにはただ一つを除き",
                "その理由を想像することはできない"),
            h.think("だからもし彼女がただその為だけに$isekoroをしているとすれば",
                "作者である$meが止めてやる必要がある。",
                "いや", "意地でも止めなければならない"),
            h.look("吐く息が白く染まる"),
            h.look("見上げても空は見えず",
                "ただ白い空間から次々と雪が舞い落ちてくるだけだ。",
                "見ているうちにもその勢いはどんどん酷くなり",
                "$meの心までも凍えさせようとしていた"),
            h.think("けど",
                "まだ倒れる訳にはいかない"),
            h.behav("足を上げる。",
                "彼女は絶対にこの先にいると信じて",
                "前に進む"),
            h.think("ただそれだけが",
                    "今の$meの物語だった"),
            )

def sc_facetoface(w: wd.World):
    h, sunami = w.hiiragi, w.sunami
    return w.scene("対峙",
            w.hiiragi.come(w.stage.cherryhill, w.day.current),
            h.talk("やはりここにいたんだな"),
            h.look("女性の小さな手にもすっぽりと収まるコンパクトな一眼レフを構えた彼女が",
                "降りしきる雪にも構わずに眼下に広がる桜の森を捉えている"),
            h.look("そこは$meの作品に登場する",
                "永遠に花を咲かせ続ける千年桜だけが植えられた不思議な森だ。",
                "けれども今はその大半が雪によって覆われていてピンクの絨毯とはとても言えない"),
            sunami.ask("待っていたのよ", "あなたが来ると思って"),
            h.look("彼女はシャッターを切らずに顔だけをこちらに向ける"),
            h.look("髪の上の雪を払い",
                "眼鏡を調整するように書け直して$meを見る。",
                "一度は作中で襟首のところまで短くした黒髪が",
                "今は耳も隠れるくらいに伸びて肩まで掛かっていた"),
            h.look("彼女は軽装の自分とは異なり",
                "ちゃんと温かそうな白のフェイクファー付きのロングコートを羽織って",
                "何も言わずにただ眼鏡の奥の瞳を細め",
                "白く変化する吐息を漏らす"),
            h.talk("もう止めるんだ。",
                "そんなことをして何になるって言うんだ？",
                "全ての異世界を殺したところで",
                "次から次にまた新しい異世界は生まれ",
                "異世界ものによって多くの作品が淘汰されるんだよ"),
            sunami.talk("あなたは何も分かっていない"),
            h.hear("強い口調と揺るぎない目が$meに投げつけられる"),
            h.talk("分かっていないのは君の方だ"),
            h.think("彼女は自分が本当は何者で",
                "何のために生まれたのか理解していない。",
                "今目の前でカメラを構えるその行為がただの暴走だということすら",
                "知らないでいる"),
            h.think("だから$meは作者として",
                "彼女に対する責任を果たさなければならない"),
            h.talk("そのカメラで自分が何をしようとしているのか",
                "分かっているのか？",
                "そのカメラの意味を",
                "理解しているのか？"),
            h.look("何を今更", "と瞳を大きくして", "彼女は微笑を返すだけだ"),
            h.talk("それは君の祖父が大事にしていたただの旧いライカじゃない。",
                "世界を切り取ってそれを人々の記憶から消し去ってしまう特別なカメラでもない"),
            h.look("彼女の瞳が", "僅かに震えたのが分かった"),
            h.talk("君のそれは……異世界を殺すカメラだ"),
            h.look("その事実を突きつけたが", "彼女は特に驚いた様子もなく$meを見返している"),
            sunami.ask("それが？"),
            h.talk("シャッターを切れば一つ異世界が消える。",
                "誰かが粉骨砕身して必死に書いた異世界が",
                "君の戯れに押したボタン一つで消し去ってしまうんだよ"),
            h.look("彼女はそれに対しても小首を傾げる"),
            h.talk("その力で君はこの世界そのものを消し去ろうとしている。",
                "けどそれは",
                "$meの創作物である君自身も消し去るということなんだ。",
                "$isekoroは",
                "君自身を殺すことでもあるんだよ！"),
            h.look("そう言い放った$meに向ける彼女の視線は",
                "全く色を変えることがなかった"),
            h.think("やはり作中の人物というのは", "実在の人間のような感情や考えは持ち得ない。",
                "ただ作者が創造した人形でしかないということなのだろう"),
            h.talk("何を言っても君は理解し得ないだろう。",
                    "だからもう",
                    "これで終わりにしよう"),
            h.look("そう言ってスマートフォンを向ける"),
            h.deal("自分が創造した物語を", "閉じるのだ。",
                    "”了”の字を刻むことで",
                    "それがどんなに渦中にあろうと",
                    "俺達の戦いはこれからだろうと",
                    "物語として全く体をなしていなかったとしても",
                    "強制的に終わることができる"),
            h.think("ただこれで終わるという",
                    "作者の強い意志だけが",
                    "終止符を打つことができるのだ"),
            h.look("そう決意した$meに",
                    "彼女はカメラを向けた"),
            h.think("――どうなっても構わない"),
            h.look("その目には感情が見えず",
                    "すっとレンズをこちらに向けると",
                    "彼女は右の人差し指をシャッターボタンにゆっくりと置いた"),
            h.think("――これで全て終わり"),
            h.deal("そんな素っ気なさで",
                    "シャッターを切――"),
            )

def sc_truth(w: wd.World):
    h, sunami = w.hiiragi, w.sunami
    return w.scene("真実",
            w.tag.symbol("※"),
            h.think("シャッターを？"),
            sunami.look("｜あなた《・・・》は$meにスマートフォンを向けたまま",
                "固まっていた"),
            sunami.ask("思い出した？",
                "$isekoroは$meじゃないの",
                "あなたよ"),
            sunami.look("シャッターを切れないでいるあなたはスマートフォンを持つ手を震わせながら",
                "$meを見る瞳を大きくする"),
            h.talk("嘘だ"),
            sunami.hear("もう一度大きく「嘘」とあなたは言った"),
            sunami.talk("嘘じゃないわ。",
                "だって$meはあなたが創ったあなたの分身なのよ。",
                "誰よりもあなたのことを理解しているの"),
            sunami.look("あはたは驚いた様子で口を動かすと何かを呟く"),
            sunami.talk("$meはあなたが最後に自分の作品世界を殺そうとここにやってくることを知っていた。",
                "だからここでずっと待っていたのよ。",
                "あなたは自分で$meをここに追い詰めた", "と思い込んでいたみたいだけれどね"),
            h.talk("何バカなことを言っているの！",
                "どうして$meが自分で自分の世界を殺さなきゃならない？",
                "そもそも自分が$isekoroって何？",
                "そんなことをして誰が得をするというんだ！"),
            sunami.talk("あなたは絶望したのよ。",
                "いくら書いても報われない自分の作品。",
                "巷には次々と生まれてはそれなりに売れていく異世界もの。",
                "自分がどんなに必死になって命を削るような思いをして誰かの心に届くようなものをと",
                "考えて書いて何とか作品にしたその一冊が",
                "異世界というだけで売れていく他の作品たちの海に沈んでいく。",
                "その現実に絶望したのよ"),
            sunami.look("あなたの唇が小さく震えた"),
            sunami.talk("だから全ての異世界を殺して",
                "最後に自分の世界も殺して終わろうとした"),
            sunami.look("おわる", "という形をあなたの唇が作る"),
            sunami.talk("終わるというのはつまり",
                "自分の作家人生を終えることでもある。",
                "あなたにとって作家というのは命そのものだった。",
                "つまりはこれがどういうことなのか",
                "説明するまでもないわ"),
            h.talk("嘘だ嘘だ！",
                "何度も今まで命の尊さを書いてきた$meが",
                "そんな$meが",
                "自らの手で全てを断とうなんて",
                "そんなこと有り得ない！"),
            sunami.look("左手を額に当てて前髪を掻き上げたあなたは",
                "何度も「嘘だ」と繰り返す。",
                "それでも思い当たることが幾つもあったようで",
                "視線が定まらなかった目がすっと$meに戻された"),
            h.talk("でも$meはそのカメラを持っていない。",
                "異世界を殺すカメラは君の手にある。",
                "つまりは君こそが$isekoroだってことだ。",
                "そうだろう？"),
            sunami.deal("カシャリ",
                    "と鈍い音をさせてカメラが動作する"),
            sunami.look("フラッシュは焚いていないけれど",
                    "あなたは目を瞑り",
                    "スマートフォンを顔の前にやって怯んだ"),
            h.talk("……え？"),
            sunami.look("けれど何も起こらなかったことに気づいてゆっくり目を開けると",
                    "$meを見て顔色を変化させた"),
            h.talk("嘘だ"),
            sunami.deal("$meはもう一度シャッターを切る"),
            h.talk("嘘だ！"),
            sunami.deal("もう一度"),
            h.talk("そのカメラは異世界を殺す。",
                    "消し去る。",
                    "だから撮られたら$meは消えて無くなってしまう。",
                    "そうじゃないと設定がおかしい！"),
            sunami.deal("$meはもう一度だけシャッターを切ると",
                    "カメラを下ろしてあなたに視線を投げた"),
            sunami.talk("これはただの祖父の遺品のライカよ。",
                    "思い出を残しておく為にフィルムに焼き付けることしかできない",
                    "ただのカメラ。",
                    "本当の$isekoroのカメラはね……あなたの手にあるスマートフォンの方"),
            sunami.look("あなたは自分の手にあるそれを見て",
                    "手を震わせる"),
            sunami.look("それから徐にそのレンズを自身へと向けると",
                    "シャッターを切ろうとした"),
            sunami.talk("やめなさい"),
            h.talk("$meが", "自分で……消した。",
                    "そうなのか"),
            sunami.look("$meを見たあなたに",
                    "確かに頷く"),
            h.talk("$meが$isekoroなのか？",
                    "本当に？"),
            sunami.look("その問いに再度コクリ", "と顎を動かすと",
                    "あなたはスマートフォンを落としてそのまま地面にへたり込むように座った"),
            h.talk("にく", "かった……から？"),
            sunami.look("その目線はもう$meには向けられない。",
                    "空を見上げ",
                    "落ちてくる塵のような雪を見つめ",
                    "それに助けを求めるように両手を上げて再度声を出す"),
            h.talk("違う！",
                    "憎んだ訳じゃない。",
                    "羨ましかった。",
                    "異世界というだけで$meのものよりもずっと人に読まれ",
                    "楽しまれ",
                    "売れることが！"),
            sunami.look("自由になった両手で顔を覆うと",
                    "あなたは更に続けた"),
            h.talk("同じように",
                    "いや",
                    "それ以上にもっとがんばったのに",
                    "どうして$meの作品だけいつも打ち切りで",
                    "内容は良かったんだよって言ってくれる癖に",
                    "物語は殺したままで",
                    "それならいっそ異世界全てを殺してしまえばいいんだって",
                    "そう考えたんだ"),
            sunami.talk("分かってる"),
            h.talk("分かってない！",
                    "だって$meは……$isekoroなんだ。",
                    "みんなの大切な異世界を殺しまくったヤツなんだ"),
            sunami.talk("それも分かってる。",
                    "だって$meはあなただから"),
            sunami.look("その言葉で",
                    "あなたはようやく$meが泣いていることに気づいた"),
            h.ask("なんで？"),
            sunami.talk("あなたが一番殺したかったのは自分の世界だって",
                    "自分自身だったって",
                    "分かっているから"),
            h.talk("$n_sunami……いや",
                    "$meの主人公"),
            sunami.deal("$meは口元に微笑みを作り",
                    "手にしたライカを胸の前にやってあなたに見せる"),
            sunami.talk("これはあなたが$meに与えてくれた",
                    "現実のあなたが高校時代に祖父から貰ったという大切なライカ。",
                    "あなたはこれで沢山の現実を切り取り",
                    "それを物語にしてきたわ。",
                    "$meが生きたのはその中の僅かな時間だけれど",
                    "それでも嬉しかった。",
                    "色々なものを見て",
                    "人と出会って",
                    "泣いて笑って",
                    "苦しんで……それでも最後にはあなたはいつも微笑みをくれた"),
            sunami.look("あなたの瞳からも",
                    "一筋の涙が流れた"),
            sunami.talk("だから$meはあなたに大切なものをね",
                    "返さないといけないんだ"),
            h.talk("返す？",
                    "$meは何も"),
            sunami.deal("首を横に振る。",
                    "それにあなたは不思議そうな表情を浮かべたけれど",
                    "確かに貰ったことは$me自身が一番よく分かっていた"),
            sunami.talk("$meはあなたに夢をもらった。",
                    "それによって絶望の淵から立ち上がり",
                    "色々な冒険をすることができた。",
                    "その一つ一つもまた$meにとっては夢で",
                    "とても大切なものになった。",
                    "だからね",
                    "今度は$meがあなたに",
                    "この言葉を返す番なの"),
            sunami.look("あなたは涙を滲ませながら",
                    "ちょっとだけ照れくさそうにすると",
                    "「それは何だい？」と尋ねてくれる"),
            sunami.deal("だから$meは一番の笑顔になってから",
                    "こう言った"),
            sunami.talk("あなたの夢はまだ", "生きている"),
            sunami.deal("シャッターを切る"),
            sunami.look("今度はフラッシュを焚いて"),
            sunami.look("すると降っていた雪の全てが光へと変わり",
                    "辺り一面が弾け飛ぶようにして",
                    "空へと全てが打ち上がった"),
            sunami.look("舞い上がった光の粒は桜色の花びらとなり",
                    "風に紛れて流れていく"),
            sunami.look("$meはそれを見上げてカメラを構えると",
                    "最後のシャッターを切った"),
            sunami.deal("この物語を終わらせる為の",
                    "そしてあなたの物語を始める為の",
                    "シャッターを"),
            )

def sc_awake(w: wd.World):
    h, sunami = w.hiiragi, w.sunami
    return w.scene("そして目覚めた",
            w.tag.symbol("※"),
            h.feel("最初に感じたのは",
                "頬の冷たさだった"),
            h.deal("触れてみるとそれは何かの雫のようで",
                "けれど見上げたアパートの六畳間の天井には",
                "そんなシミ一つ見つけられない"),
            h.talk("$me", "一体……？"),
            h.look("自分が仰向けに倒れていたことに気づいて上体を起こすと",
                "その手元には色とりどりの錠剤が転がっている"),
            h.talk("え……"),
            h.look("ノートパソコンのモニタは黒いままで",
                "テレビは音量が絞られたままずっと通販番組を流している"),
            h.think("あ……"),
            h.look("テーブルの上に置いていたスマートフォンが鳴った。",
                "メールだ"),
            h.look("何通も編集の$kasagiから原稿の確認が入っていた"),
            h.think("$meは何をしていたのだろう。",
                "何をしようとしていたのだろう"),
            h.look("振り返って見た本棚では",
                "綺麗に並んでいた$me", "$n_hiiragi名義の文庫本の中で",
                "『$mybook』だけが綺麗に倒れていた"),
            h.look("$meが$kasagiに返信をしようと思って画面をタッチしようとしたところで",
                "再び着信がある。",
                "差出人の宛名のない",
                "件名も空っぽのメールだ"),
            h.look("それにはただ『ありがとう』とだけ書き込まれており",
                "添付された画像を開くと画面いっぱいに見覚えのある女性の写真が広がった"),
            h.look("耳の下で切り揃えられた髪と縁のしっかりした眼鏡を掛けたまま",
                "祖父から貰った大切な旧いライカを構えようとして驚いているセーラー服姿の少女だ"),
            h.think("十数年ぶりに目にしたかつての自分の姿に",
                "$meは声を我慢できずに泣いてしまった"),
            )

# episodes
def ep_intro(w: wd.World):
    return (w.chaptertitle("異世界を殺すモノ"),
            sc_vanish(w),
            )

def ep_lastisekai(w: wd.World):
    return (w.chaptertitle("最後の異世界に"),
            sc_gotomyworld(w),
            sc_deadworld(w),
            sc_facetoface(w),
                w.hiiragi.think(w.i.stop_isekoro),
                w.hiiragi.know(w.i.isekoro),
                w.hiiragi.go(w.stage.cherryhill),
            )

def ep_isekaikoroshi(w: wd.World):
    return (w.chaptertitle("異世界殺し"),
            sc_truth(w),
            sc_awake(w),
                w.hiiragi.know(w.sunami, w.i.truth),
            )

# outline
def story_baseinfo(w: wd.World):
    return [
            ("story", story(w), w.hiiragi, w.sunami),
            ]

def story_outline(w: wd.World):
    return [
            ("story", story(w),
                w.hiiragi.think(w.i.stop_isekoro),
                w.hiiragi.know(w.i.isekoro),
                w.hiiragi.go(w.stage.cherryhill),
                w.hiiragi.know(w.i.truth),
                True),
            ]

# main
def world():
    w = wd.World("Re_isekai_sunami")
    w.set_db(cnf.CHARAS,
            cnf.STAGES,
            cnf.DAYS,
            cnf.ITEMS,
            cnf.INFOS,
            cnf.FLAGS,
            )
    return w

def story(w: wd.World):
    return (w.maintitle("Re:異世界殺し"),
            ep_intro(w),
            ep_lastisekai(w),
            ep_isekaikoroshi(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

