import pandas as pd
from xml.dom.minidom import Document
# import xml

total_time = 30000

df = pd.read_table('ctm', '\s+', names=['sound', 'channel', 'begin', 'end', 'text'])
# print(df)
#get the names of the sound files
sounds = list(set(df.sound.values))   #第一列所有值存进array并去重
sounds_name = []
for s in sounds:
    sounds_name.append(s[:-2])
sounds_name = list(set(sounds_name))

#process each file
for task in sounds_name:
    task_L = df[df.sound == task+"_L"]
    task_R = df[df.sound == task+"_R"]
    if task_L.shape[0] <= 0:
        task_end = task_R.begin.values[-1]+task_R.end.values[-1]
    elif task_R.shape[0] <= 0:
        task_end = task_L.begin.values[-1]+task_L.end.values[-1]
    else:
        task_end = max(task_L.begin.values[-1]+task_L.end.values[-1], task_R.begin.values[-1]+task_R.end.values[-1])
    task_end = round(task_end, 2)
    ratio = total_time / task_end   #multiply by ratio for begin and end

    #genereate xml
    doc = Document()  # 创建DOM文档对象
    RecognizeResult = doc.createElement('RecognizeResult')  # 创建根元素
    doc.appendChild(RecognizeResult)
    Speech = doc.createElement('Speech')
    RecognizeResult.appendChild(Speech)
    Speech.setAttribute('Uri', '/mydata/qianxun484/data-source/speech/Sub/2020-06-03/file/7400872.mp3.wav')
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
    EndPoint.setAttribute("Count", str(task_L.shape[0]))
    Role0.appendChild(EndPoint)
    for i in range(task_L.shape[0]):
        Item = doc.createElement('Item')
        EndPoint.appendChild(Item)
        begin = int(task_L.iloc[i:i+1, 2]*ratio)
        end = int((task_L.iloc[i:i+1, 2]+task_L.iloc[i:i+1, 3])*ratio)
        Item.setAttribute("Begin", str(begin))
        Item.setAttribute("End", str(end))
        Text = doc.createElement("Text")
        Item.appendChild(Text)
        Text_text = doc.createTextNode(str(task_L.iloc[i:i+1, 4].values[0]))
        Text.appendChild(Text_text)
        Time = doc.createElement("Time")
        EndPoint.appendChild(Time)
        Time_text = doc.createTextNode(str(begin)+','+str(end))
        Time.appendChild(Time_text)

    Role1 = doc.createElement('Role')
    Role1.setAttribute('Name', 'R1')
    Subject0.appendChild(Role1)

    EndPoint = doc.createElement("EndPoint")
    EndPoint.setAttribute("Count", str(task_R.shape[0]))
    Role1.appendChild(EndPoint)
    for i in range(task_R.shape[0]):
        Item = doc.createElement('Item')
        EndPoint.appendChild(Item)
        begin = int(task_R.iloc[i:i + 1, 2] * ratio)
        end = int((task_R.iloc[i:i + 1, 2] + task_R.iloc[i:i + 1, 3]) * ratio)
        Item.setAttribute("Begin", str(begin))
        Item.setAttribute("End", str(end))
        Text = doc.createElement("Text")
        Item.appendChild(Text)
        Text_text = doc.createTextNode(str(task_R.iloc[i:i + 1, 4].values[0]))
        Text.appendChild(Text_text)
        Time = doc.createElement("Time")
        EndPoint.appendChild(Time)
        Time_text = doc.createTextNode(str(begin) + ',' + str(end))
        Time.appendChild(Time_text)

    f = open(task+'.xml', 'w')
    doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
    f.close()

# print(sounds)