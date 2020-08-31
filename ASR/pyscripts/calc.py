import re

with open('res.txt','r') as f:
    txt = f.read()
nums = re.findall('= ([0-9.]+)', txt)
print(nums)
sum = 0
for i in nums:
    sum += float(i)
print(sum/len(nums))