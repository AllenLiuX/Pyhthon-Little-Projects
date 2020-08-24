import pandas as pd
import re
import os
import sys
import numpy as np

"""
Pass in an argument of a txt or excel table where the first column is the words before changes and the second column is the words after changes.
Or, pass in two arguments, first one is the original words, and second one is the changed words. 
"""
#Modify the path(of words.txt) and changelog if you need to modify other files with similar operations.
# path = '/Users/vincentl/Downloads/words_test.txt'
# changelog = '/Users/vincentl/Downloads/changelog.txt'
path = '/mnt/data/home/gpu/kaldi/egs/aidatatang_asr/exp/chain/tdnn_1a_sp/graph/words.txt'
changelog = '/mnt/data/home/gpu/kaldi/egs/aidatatang_asr/exp/chain/tdnn_1a_sp/graph/changelog'

with open(path, 'r') as f:
    target = f.read()
    # print(target)

if len(sys.argv) == 2:  # process a file with wanted changes.
    ori = []
    sub = []
    file = sys.argv[1]
    if re.search(r'.*\.txt',file):
        with open(file, 'r') as f1:
            for line in f1:
                l = line.split()
                ori.append(l[0])
                sub.append(l[1])
        print(ori, sub)
        # #save it to xlsx
        # df = pd.DataFrame({'Originals':ori, 'Substitutions':sub})
        # df.to_excel('/Users/vincentl/Downloads/changes.xlsx', sheet_name='Worksheet')
    elif re.search(r'.*\.xlsx', file):
        df = pd.read_excel(file,'Sheet1', index_col=0)
        print(df)
        # ori = df.iloc[:,[0]].values
        # sub = df.iloc[:,[1]].values
        ori = df['Originals'].tolist()
        sub = df['Substitutions'].tolist()
        print(ori, sub)
    for i in range(len(ori)):
        target = re.sub(r'\b'+ori[i]+' ', r''+sub[i]+' ', target)
    # print(target)
    with open(path, 'w') as f2:
        f2.write(target)
    with open(changelog,'w') as f3:
        for i in range(len(ori)):
            f3.write(sub[i]+' '+ori[i]+'\n')

elif len(sys.argv) == 3:    #sub one word with a new one
    w1 = sys.argv[1]
    w2 = sys.argv[2]
    target = re.sub(r'\b'+w1+' ', r''+w2+' ', target)
    # print(target)
    with open(path, 'w') as f2:
        f2.write(target)
    with open(changelog, 'w') as f3:
        f3.write(w2+' '+w1+'\n')

