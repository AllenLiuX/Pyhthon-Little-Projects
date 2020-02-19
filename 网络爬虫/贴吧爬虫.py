# coding:utf-8

import urllib
import re

def get_html(url):
    page = urllib.urlopen(url)
    html_code = page.read()
    return html_code

def get_image(html_code):
    reg = r'src="(.+?\.jpg)" width'
    reg_img = re.compile(reg)
    img_list = reg_img.findall(html_code)
    x=0
    for i in img_list:
        urllib.urlretrieve(img, '%s.jpg' % x)
        x += 1

print ('Please enter url:')
url = input()
if url:
    pass
else:
    url = 'http://tieba.baidu.com/p/1753935195'

html_code = get_html(url)
get_image(html_code)
print ('Download Success')