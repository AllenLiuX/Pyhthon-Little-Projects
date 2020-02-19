#-*- coding: utf-8 -*-
from aip import AipSpeech
import re
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf8')

""" 你的 APPID AK SK """
APP_ID = '17917934'
API_KEY = '8qk4iuWO6md9kOk9oMnKP6yV'
SECRET_KEY = '4XKNqCZF1iArUZEHvbQAWY9D8YmqmmYL'

url = "https://mp.weixin.qq.com/s?__biz=MjM5MTMwMTI3NA==&mid=2652458946&idx=1&sn=b798bb974cdbf62b16eb54ead2ccc1b4&chksm=bd5a44378a2dcd21456b7ddd0be28ddba66102078c3b5bf224478f445dce04f14b1c97b6d865#wechat_redirect"
text0 = urllib2.urlopen(url).read()
text0 = unicode(text0)
# print repr(text0)
re_words = re.compile(u"[\u4e00-\u9fa5]+")
m =  re_words.search(text0,0)
matched = re.findall(re_words,text0)
res = "朗读开始。"
begin = False
print "There are %d parts:\n"% len(matched)
count = 0
for p in matched:
    if begin:
        res = res + str(p) + ", "
        count += 1
    if p == "以第一人称撰写":
        begin = True
    if count>200:
        break
print(res)
# print(matched)
# print m.group()
print(type(res))
# text = "你好，我叫Vincent！"
text = "Our maze game allows people to use keystrokes to walk in a 3D maze, in which the player needs to find keys, open gates, and find the exit."
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result = client.synthesis(res, 'zh', 1, {
    'vol': 5, 'per': 4
})
print(type(result))
# print(result)
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
# print(result)
# if not isinstance(result, dict):
with open('auido.mp3', 'wb') as f:
    f.write(result)


text = """昨天，我在脉脉（一款职场实名社交平台app）上看到一个，哦不，一批蛮让人惊讶的故事。
 
有一个腾讯的程序员，在工作中不争不抢不站队，也没有处理好跟领导的关系。

于是他常被领导说是假清高，处处针对他，大坑小坑都是他的坑，大奖小奖都是别人的奖，于是他一气之下裸辞了。
 
裸辞一时爽，求职苦断肠。

他没想到，三个月后他仍然没找到满意的工作，但没了进项之后压力丛生。
 
有一次，他很偶然的跟一个外卖小哥聊天后，感觉送外卖也是一件很有意思的事情，决定来体验一下。
 
没想到，工作了一段时间之后，他发现送外卖收入还不错，干了一个多月赚了2万多。
 
他觉得现在还算不错，靠送外卖养活自己，至少不用处理让人头疼的人际关系。"""