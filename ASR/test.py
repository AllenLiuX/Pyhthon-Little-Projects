import re
import pandas as pd
import sqlite3

files = []
content = []
with open('res.txt', 'r') as f:
    for line in f:
        match = re.search(r'([\w_.]+)(.+)', line)
        if match:
            files.append(match.group(1))
            content.append(match.group(2))
        else:
            content[-1] += line
    print(files)
    print(content)
df = pd.DataFrame({'File':files, 'Content':content})
# print(df)
# df.to_excel('res1.xlsx', sheet_name='Worksheet')
conn = sqlite3.connect('ResDB2.db')
c = conn.cursor()
c.execute('CREATE TABLE RES1 (File text, Content text)')
conn.commit()
# df.to_sql('Res1', conn, if_exists='replace', index=False)

# cmd = "INSERT INTO Res1 (File,Content) VALUES ('{}','{}')".format('yuan', '你好 欢迎 致电 圆通速递 请问 ')
# print(cmd)
# c.execute(cmd)
# conn.commit()
for row in range(df.shape[0]):
    cmd = "INSERT INTO Res1 (File,Content) VALUES ('{}','{}')".format(df["File"][row], df["Content"][row])
    c.execute(cmd)
    # print(df["File"][row], df["Content"][row])
conn.commit()
c.execute("SELECT * FROM Res1")
for row in c.fetchall():
    print(row)