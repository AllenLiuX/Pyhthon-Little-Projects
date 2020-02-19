from bs4 import BeautifulSoup
import urllib.request as ure
import os
url = 'https://zhuanlan.zhihu.com/p/35336704'
response = ure.urlopen(url, timeout=30)
circle = response.read().decode('utf-8')

# 将获取的图片地址依次放入count中
count = []
# 将获取的网页内容放入BeautifulSoup
soup = BeautifulSoup(circle, 'lxml')
# 根据谷歌SelectGadGet这个插件，获取html标签，比如获取：#gallery-list
for item in soup.select('#gallery-list'):
    # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签,limit:限制爬取的数量。
    for img in item.find_all('img', limit=5):
        print('img', img)
        # m 是 img标签中存在的属性
        img_path = img.get('m')
        count.append(img_path)
if not os.path.exists('photo'):
    os.makedirs('photo')
# 用enumerate依次取出count中的图片地址 放入v中
for i,v in enumerate(count):
    # 存取图片过程中，出现不能存储 int 类型，故而，我们对他进行类型转换 str()。w:读写方式打开，b：二进制进行读写。图片一般用到的都是二进制。
    path = 'photo\\img'+str(i)+'.jpg'
    with open(path, 'w') as file:
        ure.urlretrieve(v, path)
    print(i)