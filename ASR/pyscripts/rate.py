from error_rate import *
import sys
from operator import itemgetter

target_f = sys.argv[1]
trans_f = sys.argv[2]
with open(r''+target_f) as f:
    targets2 = f.readlines()
with open(r''+trans_f) as f:
    trans2 = f.readlines()
targets = [i.split(' ') for i in targets2]
trans = [i.split('\t') for i in trans2]
# print(trans)
Cers = []
for tran in trans:
    for tar in targets:
        if tran[0] == tar[0][:-4]:
            Cer = cer(tar[1], tran[1], True, True)
            Cers.append([tar[0], Cer])
# print(Cers)
sum = 0
Cers2 = sorted(Cers, key=itemgetter(1))
for i in Cers2:
    print(i)
    sum += i[1]
aver = round(sum/len(Cers2), 4)
print("The Average Cer(Character Error Rate) is:"+str(aver))
