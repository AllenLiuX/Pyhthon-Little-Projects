import pypinyin as py
import sys
import getopt
import re
import pandas as pd

path = 'words2.txt'
changelog = 'changelog.txt'

def to_pinyin(word):
    return py.pinyin(word, style=py.NORMAL)

'''
Two modes:
1. Forceful translation of certain pinyin to certain words. Use -p or --pinyin=wordbank, where wordbank is the file storing target words.
2. Substitute certain words into other words. Use -s or --sub=change, where change stores the paired two words '[ori] [sub]'
'''
def main():
    pinyin_mode = False
    sub_mode = False
    pos = ''
    opts, args = getopt.getopt(sys.argv[1:], '-a-p-s-f:', ['all', 'pinyin', 'sub', 'file='])
    for opt_name, opt_value in opts:
        if opt_name in ('-a', '--all'):
            pinyin_mode = True
            sub_mode = True
        if opt_name in ('-p', '--pinyin'):
            pinyin_mode = True
        if opt_name in ('-s', '--sub'):
            sub_mode = True
        if opt_name in ('f', 'file'):
            pos = opt_value

    if pinyin_mode:
        if pos != '':
            wordbank = pos
        else:
            wordbank = 'wordbank'
        with open(wordbank, 'r') as f:
            file = f.read()
            words = file.split('\n')
        pinyin = [to_pinyin(i) for i in words]
        print(pinyin)

        f = open(r''+path)
        lines = f.readlines()
        f.close()
        altered = 0
        i = 0
        for line in lines:
            w = line.split(' ')
            wp = to_pinyin(w[0])
            if wp in pinyin:
                ind = pinyin.index(wp)
                new_line = words[ind]+'-'+str(altered)+line[len(wp):]   #add index so that the words in dictionary have unique ids
                print(new_line)
                lines[i] = new_line
                altered += 1
            i += 1
        print("Number of altered words:", altered)
        f = open('words2.txt', 'w')
        f.writelines(lines)
        f.close()
    elif sub_mode:
        if pos != '':
            changes = pos
        else:
            changes = 'change.csv'
        ori = []
        sub = []
        if re.search(r'.*\.csv', changes):
            with open(r''+changes, 'r') as f1:
                ind = 0
                for line in f1.readlines():
                    line = line.strip('\n')
                    l = line.split(',')
                    print(l)
                    ori.append(l[0])
                    sub.append(l[1]+'_'+str(ind))   #add index so that the words in dictionary have unique ids
                    ind+=1
            print(ori, sub)
            # #save it to xlsx
            # df = pd.DataFrame({'Originals':ori, 'Substitutions':sub})
            # df.to_excel('/Users/vincentl/Downloads/changes.xlsx', sheet_name='Worksheet')
        elif re.search(r'.*\.xlsx', changes):
            df = pd.read_excel(changes, 'Sheet1', index_col=0)
            print(df)
            ori = df['Originals'].tolist()
            sub = df['Substitutions'].tolist()
            print(ori, sub)
        with open(path, 'r') as f2:
            target = f2.read()
        for i in range(len(ori)):
            target = re.sub(r'\b' + ori[i] + ' ', r'' + sub[i] + ' ', target)
        # print(target)
        with open('words2.txt', 'w') as f2:
            f2.write(target)
        with open(changelog, 'w') as f3:
            for i in range(len(ori)):
                f3.write(sub[i] + ' ' + ori[i] + '\n')

if __name__=='__main__':
    main()