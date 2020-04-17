import os
import sys
import re
import urllib.request
import pandas as pd
import sqlite3

"""
Pass in a directory path(where we have the audios) or an url to an audio file, and the database's name, and the table's name.
It automatically calls run2.sh to translate the audio(s) to texts, and extract the texts into dataframe, and then save them to the destinated database.
"""

file = sys.argv[1]
database = sys.argv[2]
table = sys.argv[3]
if file[:4]=="http":
    url = file
    if not os.path.exists('audio'):
        os.makedirs('audio')
    file = 'audio/' + url.split('/')[-1]
    if not os.path.exists(file):
        try:
            urllib.request.urlretrieve(url, filename = file)
        except Exception as e:
            print("Error occurred when downloading file, error message:")
            print(e)

myCmd = 'sudo /mnt/data/home/gpu/kaldi/egs/aidatatang_asr/run2.sh %s' % file
result = os.popen(myCmd).read()
des = re.search(r'recognition result in ([\w/.]+)', result).group(1)
# print(des)

files = []
content = []
with open(des, 'r') as f:
    for line in f:
        match = re.search(r'([\w_.]+)(.+)', line)
        if match:
            files.append(match.group(1))
            content.append(match.group(2))
        else:
            content[-1] += line
    # print(files)
    # print(content)
#To Pandas Dataframe
df = pd.DataFrame({'File':files, 'Content':content})
# print(df)
# df.to_excel('res1.xlsx', sheet_name='Worksheet')

#To Database
conn = sqlite3.connect(database)
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS %s (File text, Content text)'%table)
conn.commit()
# df.to_sql('Res1', conn, if_exists='replace', index=False)
for row in range(df.shape[0]):
    cmd = "INSERT INTO {} (File,Content) VALUES ('{}','{}')".format(table, df["File"][row], df["Content"][row])
    c.execute(cmd)
    # print(df["File"][row], df["Content"][row])
conn.commit()
c.execute("SELECT * FROM %s"%table)
for row in c.fetchall():
    print(row)