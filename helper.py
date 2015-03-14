# coding=utf-8

Dic = '''a   あ  ア
i   い  イ
u   う  ウ
e   え  エ
o   お  オ
ka  か  カ
ki  き  キ
ku  く  ク
ke  け  ケ
ko  こ  コ
sa  さ  サ
shi し  シ
su  す  ス
se  せ  セ
so  そ  ソ
ta  た  タ
chi ち  チ
tsu つ  ツ
te  て  テ
to  と  ト
na  な  ナ
ni  に  ニ
nu  ぬ  ヌ
ne  ね  ネ
no  の  ノ
ha  は  ハ
hi  ひ  ヒ
fu  ふ  フ
he  へ  ヘ
ho  ほ  ホ
ma  ま  マ
mi  み  ミ
mu  む  ム
me  め  メ
mo  も  モ
ra  ら  ラ
ri  り  リ
ru  る  ル
re  れ  レ
ro  ろ  ロ
ya  や  ヤ
yu  ゆ  ユ
yo  よ  ヨ
wa  わ  ワ
wo  を  ヲ
n   ん  ん

ga  が  ガ
gi  ぎ  ギ
gu  ぐ  グ
ge  げ  ゲ
go  ご  ゴ
za  ざ  ザ
ji  じ  ジ
zu  ず  ズ
ze  ぜ  ゼ
zo  ぞ  ゾ
da  だ  ダ
de  で  デ
do  ど  ド
ba  ば  バ
bi  び  ビ
bu  ぶ  ブ
be  べ  ベ
bo  ぼ  ボ
pa  ぱ  パ
pi  ぴ  ピ
pu  ぷ  プ
pe  ぺ  ペ
po  ぽ  ポ

kya きゃ    キャ
kyu きゅ    キュ
kyo きょ    キョ
gya ぎゃ    ギャ
gyu ぎゅ    ギュ
gyo ぎょ    ギョ
sha しゃ    シャ
shu しゅ    シュ
sho しょ    ショ
ja  じゃ    ジャ
ju  じゅ    ジュ
jo  じょ    ジョ
cha ちゃ    チャ
chu ちゅ    チュ
cho ちょ    チョ
nya にゃ    ニャ
nyu にゅ    ニュ
nyo にょ    ニョ
hya ひゃ    ヒャ
hyu ひゅ    ヒュ
hyo ひょ    ヒョ
bya びゃ    ビャ
byu びゅ    ビュ
byo びょ    ビョ
pya ぴゃ    ピャ
pyu ぴゅ    ピュ
pyo ぴょ    ピョ
mya みゃ    ミャ
myu みゅ    ミュ
myo みょ    ミョ
rya りゃ    リャ
ryu りゅ    リュ
ryo りょ    リョ'''

import re

Dic = Dic.split('\n')
Dic = filter(lambda x: x != '', Dic)
Dic = [re.split(' +', item) for item in Dic]

def make_entry(item):
    ret = '''
<d:entry id="__id__" d:title="__id__">
    <d:index d:value="__平假名__" />
    <d:index d:value="__片假名__" />
    <h1>__平假名__ __片假名__ __id__</h1>
</d:entry>'''
    ret = ret.replace("__id__", item[0])
    ret = ret.replace("__平假名__", item[1])
    ret = ret.replace("__片假名__", item[2])
    return ret

print '''
<?xml version="1.0" encoding="UTF-8"?>
<!--
	This is a sample dictionary source file.
	It can be built using Dictionary Development Kit.
-->
<d:dictionary xmlns="http://www.w3.org/1999/xhtml" xmlns:d="http://www.apple.com/DTDs/DictionaryService-1.0.rng">
'''

for item in Dic:
    print make_entry(item)

print '''
</d:dictionary>
'''
