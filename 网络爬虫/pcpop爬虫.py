import urllib2
import urllib
import os
from BeautifulSoup import BeautifulSoup
def getAllImageLink():

    html = urllib2.urlopen('http://www.pcpop.com/doc/1/1279/1279531.shtml').read()
    soup = BeautifulSoup(html)
    liResult = soup.findAll('img',attrs={"width":"175"})
    #print liResult 方便调试

    count = 0
    for image in liResult:
        count += 1
        link = image.get('src')
        imageName = count
        filesavepath = '/Users/justinjing/Desktop/testpython/%s.jpg' % imageName
        urllib.urlretrieve(link,filesavepath)
        print(filesavepath)
if __name__ == '__main__':
    getAllImageLink()