#coding=utf-8
import pandas as pd
from xml.dom.minidom import Document
from operator import itemgetter
import sys
import re
# import xml

#total_time = 30000
sounds_info = sys.argv[1]
ctm = sys.argv[2]
df = pd.read_table(ctm, '\s+', names=['sound','channel','begin','end','text'])
# print(df)
#get the names of the sound files
sounds = list(set(df.sound.values))   #第一列所有值存进array并去重
sounds_name = []
for s in sounds:
    sounds_name.append(s[:-2])
sounds_name = list(set(sounds_name))
# print(sounds_info)
info = pd.read_table(sounds_info, '\s+', names=['name','time','uri'])
concat_text = ''

#process each file
for task in sounds_name:
    total_time = int(info[info.name == task].time.values[0] * 1000)
    uri = info[info.name == task].uri.values[0]
    # print(total_time,uri)
    task_L = df[df.sound == task+"_L"]
    task_R = df[df.sound == task+"_R"]

    #get concat text
    task_all = task_L
    task_all = task_all.append(task_R)
    sorted_df = task_all.sort_values(by='begin')
    i = 0
    wds = sorted_df.text.values
    sentence = ' '.join(wds)        #use space in order to seperate words
    sentence = re.sub('[-_0-9]+', '', sentence)
    concat_text += task +'\t' + sentence + '\n'
    # print(concat_text)

    if task_L.shape[0] <= 0:
        task_end = task_R.begin.values[-1] + task_R.end.values[-1]
    elif task_R.shape[0] <= 0:
        task_end = task_L.begin.values[-1] + task_L.end.values[-1]
    else:
        task_end = max(task_L.begin.values[-1] + task_L.end.values[-1], task_R.begin.values[-1] + task_R.end.values[-1])
    task_end = round(task_end, 2)
    ratio = total_time / task_end   #multiply by ratio for begin and end
    time_gaps = [] #保存每个begin与end
    t_words_L = 0 #统计总字数
    time_L = 0 #统计说话时间
    t_words_R = 0
    time_R = 0

    #genereate xml
    doc = Document()  # 创建DOM文档对象
    RecognizeResult = doc.createElement('RecognizeResult')  # 创建根元素
    doc.appendChild(RecognizeResult)
    Speech = doc.createElement('Speech')
    RecognizeResult.appendChild(Speech)
    # Speech.setAttribute('Uri', '/mydata/qianxun484/data-source/speech/Sub/2020-06-03/file/7400872.mp3.wav')
    Speech.setAttribute('Uri', uri)
    Speech.setAttribute('Duration', str(total_time))
    ResultCode = doc.createElement('ResultCode')
    ResultCode_text = doc.createTextNode('0')
    ResultCode.appendChild(ResultCode_text)
    Speech.appendChild(ResultCode)
    Confidence = doc.createElement("Confidence")
    Confidence_text = doc.createTextNode('100')
    Confidence.appendChild(Confidence_text)
    Speech.appendChild(Confidence)
    Subject0 = doc.createElement("Subject")
    Subject0.setAttribute('Name', 'RecognizeText')
    Speech.appendChild(Subject0)

    Role0 = doc.createElement('Role')
    Role0.setAttribute('Name', 'R0')
    Subject0.appendChild(Role0)

    EndPoint = doc.createElement("EndPoint")
    # EndPoint.setAttribute("Count", str(task_L.shape[0]))
    Role0.appendChild(EndPoint)

    tot = 0 # 统计句子数量
    i = 0
    while (i < task_L.shape[0]):
        Item = doc.createElement('Item')
        EndPoint.appendChild(Item)
        begin = int(task_L.iloc[i:i+1, 2]*ratio)
        end = int((task_L.iloc[i:i+1, 2]+task_L.iloc[i:i+1, 3])*ratio)
        time_gaps.append([begin,end])
        text_temp = str(task_L.iloc[i:i + 1, 4].values[0])
        time_temp = str(begin)+','+str(end)
        time_L += end - begin
        while (i + 1 < task_L.shape[0]):
            next_begin = int(task_L.iloc[i + 1:i + 2, 2] * ratio)
            if (next_begin - end < 200):
                i = i + 1
                end =  int((task_L.iloc[i:i + 1, 2] + task_L.iloc[i:i + 1, 3]) * ratio)
                text_temp += ' '+str(task_L.iloc[i:i + 1, 4].values[0])
                time_temp += ' '+str(next_begin)+','+str(end)
                time_L += end - next_begin
                time_gaps.append([next_begin,end])
                #print(text_temp)
                #print(i)
            else: break
        Item.setAttribute("Begin", str(begin))
        Item.setAttribute("End", str(end))
        Text = doc.createElement("Text")
        Item.appendChild(Text)
        #Text_text = doc.createTextNode(str(task_L.iloc[i:i+1, 4].values[0]))
        Text_text = doc.createTextNode(text_temp)
        t_words_L += len(text_temp)
        tot += 1
        Text.appendChild(Text_text)
        Time = doc.createElement("Time")
        Item.appendChild(Time)
        #Time_text = doc.createTextNode(str(begin)+','+str(end))
        Time_text = doc.createTextNode(time_temp)
        Time.appendChild(Time_text)
        i = i + 1
    EndPoint.setAttribute("Count", str(tot))

    Role1 = doc.createElement('Role')
    Role1.setAttribute('Name', 'R1')
    Subject0.appendChild(Role1)

    EndPoint = doc.createElement("EndPoint")
    # EndPoint.setAttribute("Count", str(task_R.shape[0]))
    Role1.appendChild(EndPoint)

    tot = 0 
    i = 0
    while (i < task_R.shape[0]):
        Item = doc.createElement('Item')
        EndPoint.appendChild(Item)
        begin = int(task_R.iloc[i:i + 1, 2] * ratio)
        end = int((task_R.iloc[i:i + 1, 2] + task_R.iloc[i:i + 1, 3]) * ratio)
        time_gaps.append([begin,end])
        text_temp = str(task_R.iloc[i:i + 1, 4].values[0])
        time_temp = str(begin)+','+str(end)
        time_R += end - begin
        while (i + 1 < task_R.shape[0]):
            next_begin = int(task_R.iloc[i + 1:i + 2, 2] * ratio)
            if (next_begin - end < 200):
                i = i + 1
                end =  int((task_R.iloc[i:i + 1, 2] + task_R.iloc[i:i + 1, 3]) * ratio)
                text_temp += ' '+str(task_R.iloc[i:i + 1, 4].values[0])
                time_temp += ' '+str(next_begin)+','+str(end)
                time_R += end - next_begin
                time_gaps.append([next_begin,end])
                #print(text_temp)
                #print(i)
            else: break
        Item.setAttribute("Begin", str(begin))
        Item.setAttribute("End", str(end))
        Text = doc.createElement("Text")
        Item.appendChild(Text)
        #Text_text = doc.createTextNode(str(task_R.iloc[i:i + 1, 4].values[0]))
        Text_text = doc.createTextNode(text_temp)
        t_words_R += len(text_temp)
        tot += 1
        Text.appendChild(Text_text)
        Time = doc.createElement("Time")
        Item.appendChild(Time)
        #Time_text = doc.createTextNode(str(begin) + ',' + str(end))
        Time_text = doc.createTextNode(time_temp)
        Time.appendChild(Time_text)
        i = i + 1
    EndPoint.setAttribute("Count", str(tot))

    # SpeakSpeed
    Subject1 = doc.createElement("Subject")
    Subject1.setAttribute('Name', 'SpeakSpeed')
    Speech.appendChild(Subject1)
    Role = doc.createElement('Role')
    Role.setAttribute('Name', 'mix')
    Subject1.appendChild(Role)
    Speed = doc.createElement('SpeakSpeed')
    Role.appendChild(Speed)
    Speed.setAttribute("value", str(round((t_words_L + t_words_R) * 1000 / (time_L + time_R),2)))
    Role = doc.createElement('Role')
    Role.setAttribute('Name', 'R0')
    Subject1.appendChild(Role)
    Speed = doc.createElement('SpeakSpeed')
    Role.appendChild(Speed)
    if time_L == 0:
        Speed.setAttribute("value", 'NaN')
    else:
        Speed.setAttribute("value", str(round(t_words_L * 1000 / time_L,2)))
    Role = doc.createElement('Role')
    Role.setAttribute('Name', 'R1')
    Subject1.appendChild(Role)
    Speed = doc.createElement('SpeakSpeed')
    Role.appendChild(Speed)
    if time_R == 0:
        Speed.setAttribute("value", 'NaN')
    else:
        Speed.setAttribute("value", str(round(t_words_R * 1000 / time_R,2)))

    # LongSilence
    time_gaps_sorted = sorted(time_gaps, key=itemgetter(0))
    # print(time_gaps_sorted)
    Subject2 = doc.createElement("Subject")
    Subject2.setAttribute('Name', 'LongSilence')
    Speech.appendChild(Subject2)
    Role = doc.createElement('Role')
    Role.setAttribute('Name', 'mix')
    Subject2.appendChild(Role)
    cnt = 0 # LongSilence次数
    EndPoint = doc.createElement("EndPoint")
    Role.appendChild(EndPoint)
    for i in range(1, len(time_gaps_sorted)):
        if (time_gaps_sorted[i][0] > time_gaps_sorted[i-1][1]):
            cnt += 1
            Item = doc.createElement('Item')
            EndPoint.appendChild(Item)
            Item.setAttribute("Begin", str(time_gaps_sorted[i-1][1]))
            Item.setAttribute("End", str(time_gaps_sorted[i][0]))
    EndPoint.setAttribute("Count", str(cnt))

    f = open(sys.argv[3]+task+'.xml', 'w')
    doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
    f.close()

with open(sys.argv[3]+'all_text.txt', 'w') as f:
    f.write(concat_text)
# print(sounds)
