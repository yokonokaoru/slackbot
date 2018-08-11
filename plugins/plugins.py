
from slackbot.bot import respond_to # @botnameで反応するデコーダ
from slackbot.bot import listen_to #チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply
import os
import sys
from janome.tokenizer import Tokenizer
import yaml

@listen_to('すごい')
def sugoi_func(message):
    message.reply('ありがとう！あなたの投稿にスタンプ押しますね！')
    message.react('+1')

@default_reply()
def posinega_func(message):
    f = open("/Users/yokonokaoru/Documents/slackbot/yml_file/polarity.yml", "r+")
    polarity = yaml.load(f)

    text = message.body['text']
    t = Tokenizer()
    tokens = t.tokenize(text)
    pol_val = 0
    for token in tokens:
        word = token.surface
        pos = token.part_of_speech.split(',')[0]
        if word in polarity:
            pol_val = pol_val + float(polarity[word])
            message.send(word + ' = ' + polarity[word])
    message.send("TOTAL SCORE =" + str(pol_val))

    if pol_val > 0.2:
        message.reply("```" + 'それは素晴らしいですね！(^^)' + "```")
    elif pol_val < -0.2:
        message.reply("```" + 'それは残念ですね。。。(＞＜)' + "```")
    else:
        message.reply("```" + 'そうなのですね！' + "```")

"""

import os
import sys
from janome.tokenizer import Tokenizer #mecabはc言語で書かれてるので早いが、インストールが少し面倒。janomeはpythonで書かれているので少し遅い。
import yaml
from slackbot.bot import respond_to # @botnameで反応するデコーダ
from slackbot.bot import listen_to #チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply

#logistic_regression



from janome.tokenizer import Tokenizer


def token_generator(text):
    tokenizer = Tokenizer()
    for paragraph in text.split('\n'):
        for sentence in paragraph.split('。'):
            for token in tokenizer.tokenize(sentence):
                if token.part_of_speech.split(',')[0] == '名詞':
                    yield token.surface

doc_list = [
    list(token_generator('春、元美術部で運動音痴の主人公・東島旭（西野七瀬）は、二ツ坂高校に入学する。そこで、1つ上の先輩の宮路真春（白石麻衣）と出会い、その強さと美しさに憧れ、“なぎなた”をはじめる決意をする!入部した薙刀部で同級生の八十村将子（桜井玲香）、紺野さくら（松村沙友理）、2年生の野上えり（伊藤万理華）、大倉文乃（富田望生）と出会い、旭は“なぎなた”を始めたが、“練習は楽な方”、“運動神経はなくても平気”、そんな誘い文句とは真逆で、なぎなたの稽古は過酷そのもの！迎えた夏のインターハイ予選、二ツ坂はダークホース國陵高校に決勝戦で敗れてしまう。なかでも、1年生エース・一堂寧々（生田絵梨花）の強さは圧倒的だった……')),
    list(token_generator('人類初の大規模な宇宙への移住計画のため、滅びゆく地球を旅立った宇宙船コヴェナント号は、コールドスリープ中の2000人の入植者を乗せ、移住先の惑星オリガエ-6を目指していた。その航行の途中、大事故に見舞われたコヴェナント号は女性の歌声が混じった謎の電波をキャッチし、発信元である惑星へと向かう。その神秘的な惑星は、女性乗組員ダニエルズ（ウォーターストン）にとっても、人類の新たな希望の地に思えた。はたしてダニエルズの前に現れた完全な知能を持つアンドロイド（ファスベンダー）は敵か、それとも味方か。そしてエイリアン誕生をめぐる驚愕の真実とは何なのか。')),
    list(token_generator('ワンダーウーマンが生まれたのは、女性だけが暮らすパラダイス島。ダイアナ（ワンダーウーマン）はその島のプリンセスだった。ある日、不時着したアメリカ人パイロットを助けたことから、外の世界で戦争が起きていることを知る。彼女は自身の力で「世界を救いたい」と強く願い、二度と戻れないと知りながら故郷をあとにする……。そんな彼女は、初めての世界で何を見て、何のために戦い、そして、なぜ美女戦士へとなったのか！？')),
    list(token_generator('自由の女神のすぐそばで真っ二つに割れるフェリー。摩天楼の上空で今にも落ちて行きそうなジェット機。NYが大惨事になりかけたその時、現れたヒーローがいる。スパイダーマン。その正体は15歳の高校生ピーター・パーカーだ。憧れのトニー・スターク＝アイアンマンにもらった特製スーツに颯爽と着替え、NYの街を華麗に飛び回り、悪を裁く！…といきたいところだが、理想のヒーローのような姿には少し遠い。ヒーロー気分で街に繰り出しては、ビルの間や住宅街を飛び回るがその姿はまだ初々しい。そんな彼の目標は＜ヒーロー＞として認められること。ある日、大富豪トニー・スタークにうらみを持つ不穏な影がNYを危機に陥れる。')),
    list(token_generator('高校時代のクラスメイト・山内桜良（浜辺美波）の言葉をきっかけに母校の教師となった【僕】（小栗旬）。彼は、教え子と話すうちに、彼女と過ごした数ヶ月を思い出していくー。膵臓の病を患う彼女が書いていた「共病文庫」（＝闘病日記）を偶然見つけたことから、【僕】（北村匠海）と桜良は次第に一緒に過ごすことに。だが、眩いまでに懸命に生きる彼女の日々はやがて、終わりを告げる。桜良の死から12年。結婚を目前に控えた彼女の親友・恭子（北川景子）もまた、【僕】と同様に、桜良と過ごした日々を思い出していたー。そして、ある事をきっかけに、桜良が12年の時を超えて伝えたかった本当の想いを知る2人ー。')),
    list(token_generator('反悪党同盟をクビになったグルーが、これを機に悪の道に戻ってくれるのではないかと期待するミニオンたちだったが、その世界からは足を洗ったと告げられる。生きがいを求めてグルーと決別し、新たな最強最悪のボス探しの旅を始めるが、ある出来事をきっかけにとんでもないことに！？ 果たして、ミニオンたちの運命は！？')),
]

from gensim import corpora, matutils

dictionary = corpora.Dictionary(doc_list)

corpus = [dictionary.doc2bow(doc) for doc in doc_list]

csc = matutils.corpus2csc(corpus) #(単語、文章) 回数 → 265 * 6

doc_matrix = csc.transpose()

import numpy as np

X = doc_matrix
y = np.array([0, 1, 1, 1, 0, 0]) #アクションものでなければ0、アクションものであれば1

from sklearn.linear_model import LogisticRegression

reg = LogisticRegression()
reg.fit(X, y)

import pandas as pd

result_df = pd.DataFrame([
    (token, reg.coef_[0][token_id]) for token_id, token in dictionary.iteritems()
])
result_df.columns = ['token', 'coef']

@default_reply()
def default_func(message):
    text = message.body['text']
    input_corpus = dictionary.doc2bow(list(token_generator(text)))
    test_x = matutils.corpus2csc([input_corpus], X.shape[1]).transpose()
    pred_y = reg.predict_proba(test_x)
    message.reply("そのストーリーがアクションものかどうか判定します")
    #message.reply("アクションでない VS アクション")
    #message.reply(pred_y[0,1])
    if pred_y[0, 0] > pred_y[0, 1]:
        message.reply("そのストーリーはアクションものじゃないね！")
    else:
        message.reply("そのストーリーはアクションものだね！")
"""
