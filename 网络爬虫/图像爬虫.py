import requests
from bs4 import BeautifulSoup
circle = requests.get('https://baike.baidu.com/item/Python/407313?fr=aladdin')

#http://travel.quanjing.com/tag/12975/%E9%A9%AC%E5%B0%94%E4%BB%A3%E5%A4%AB

# 将获取的图片地址依次放入count中
count = []
# 将获取的网页内容放入BeautifulSoup
soup = BeautifulSoup(circle.text, 'lxml')
# 根据谷歌SelectGadGet这个插件，获取html标签，比如获取：#gallery-list
for item in soup.select('#gallery-list'):
    # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签
    for img in item.find_all('img'):
        print('img', img)
        # m 是 img标签中存在的属性
        img_path = img.get('m')
        count.append(img_path)
# 用enumerate依次取出count中的图片地址 放入v中
for i,v in enumerate(count):
    # 将获取的v值再次放入request中进行与网站相应
    image = requests.get(v)
    # 存取图片过程中，出现不能存储 int 类型，故而，我们对他进行类型转换 str()。w:读写方式打开，b：二进制进行读写。图片一般用到的都是二进制。
    with open('D:\\img'+str(i)+'.jpg', 'wb') as file:
        # content：图片转换成二进制，进行保存。
        file.write(image.content)
    print(i)