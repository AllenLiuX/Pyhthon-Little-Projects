import urllib.request
from urllib.parse import quote
import string
import pdfkit
from PyPDF2 import PdfFileReader
from datetime import datetime, timedelta
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import re
import os
import sys
import getopt
# from html2pdf import HTMLToPDF
# import dryscrape
# import requests


# def get_url_dynamic(url):
#     session_req=dryscrape.Session()
#     session_req.visit(url) #请求页面
#     response=session_req.body() #网页的文本
#     #print(response)
#     return response


def get_pagenum(path):
    reader = PdfFileReader(path)
    if reader.isEncrypted:
        reader.decrypt('')
    page_num = reader.getNumPages()
    return page_num


def get_url_dynamic(url):
    driver=webdriver.Chrome()   # 调用本地的火狐浏览器，Chrom 甚至 Ie 也可以的
    driver.get(url)     # 请求页面，会打开一个浏览器窗口
    html_text=driver.page_source
    # driver.quit()
    return html_text


def get_urls(searchword, begin_time, art_num):
    url = "http://api.woshipm.com/search/list.html?tab=0&key="+searchword+"&sortType=1"
    url = quote(url, safe=string.printable)  # to transcribe Chinese searchword in url
    res = []
    page = 1
    while len(res) < art_num:
        cur_url = url+"&page="+str(page)
        page += 1
        print("Searching by: " + cur_url)
        # ==== Try to get the html after js-rendering
        # # 1 urllib method
        # try:
        #     header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
        #     request = urllib.request.Request(cur_url, headers=header)
        #     response = urllib.request.urlopen(request, timeout=10.0).read()
        #     response = response.decode('utf-8', 'ignore').replace(u'\xa9', u'')
        # except:
        #     print('error')
        # # 2 requests method
        # response = requests.get(url).content
        # # 3 Selenium method
        response = get_url_dynamic(cur_url)
        # print(response)
        with open('page.html', 'w') as f:
            f.write(response)
        # soup = BeautifulSoup(response, features="html.parser")

        break   # temporarily go through the loop only once
    res = ['4071301', '3858983', '3134984']
    return res


def form_json(id, soup, content, searchword):
    info = {}
    # 获取id, type, source, author
    info['id'] = id
    info['type'] = 'report'
    info['source'] = '人人都是产品经理'
    info['url'] = 'http://www.woshipm.com/pd/'+id+'.html'
    info['content'] = content
    author = soup.find(class_='author u-flex').find('a').text
    print('author:', author)
    info['author'] = author
    # 获取页数
    path = searchword+"/"+id+'.pdf'
    page_num = get_pagenum(path)
    print("Number of pages:", page_num)
    info['page_num'] = page_num
    # 获取时间
    date = soup.find_all('time')[0].text
    print('date:', date)
    info['date'] = date
    # 获取title
    title = soup.find_all(class_='article--title')[0].text
    print('title:', title)
    info['title'] = title
    # print(info)
    with open(searchword+'/'+id+'.json', 'w') as f:
        f.write(json.dumps(info, ensure_ascii=False, indent=4, separators=(',', ':')))


def calc_keywords(content, keywords):
    keys = keywords.split(',')
    stats = {}
    for i in keys:
        count = len(re.findall(i, content))
        stats[i] = count
    print(stats)


def process_article(id, words_min, searchword, keywords):
    url = "http://www.woshipm.com/pd/"+id+".html"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request).read()
    result = response.decode('utf-8', 'ignore').replace(u'\xa9', u'')
    soup = BeautifulSoup(result, features="html.parser")
    # 获取纯文本信息raw_txt
    # content = str(soup.find_all(class_="article--content grap"))
    # re_words = re.compile(u"[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\u4e00-\u9fa5]+")
    # txt = re.findall(re_words, content)
    # raw_txt = "".join(txt)
    txt = soup.find(class_="article--content grap").find_all('p')
    raw_txt = ""
    for t in txt:
        raw_txt += t.text

    if len(raw_txt) >= words_min: # 判断文本长度
        # 转换pdf
        print("Downloading article #" + id + ' ' + url)
        print("content:", raw_txt)
        print("Word count: ", len(raw_txt))
        path = searchword + "/" + id + '.pdf'
        config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
        pdfkit.from_url(url, path, configuration=config)
        # 获取json信息
        form_json(id, soup, raw_txt, searchword)
        calc_keywords(raw_txt, keywords)
    # print(result)


def main():
    """
    Two modes: directed run without options / called with 4 optional options: searchword, words_min, begin_time, and art_num.
    """
    searchword, words_min, begin_time, art_num, keywords = '', '', '', '', ''
    if len(sys.argv) == 1:
        searchword = input("Searchword: ")
        words_min = input("Min words count: ")
        begin_time = input("End time(yyy-mm-dd): ")
        art_num = input("Max number of articles: ")
        keywords = input("keywords: ")
    else:
        opts, args = getopt.getopt(sys.argv[1:], '-s:-w:-e:-a:-k:', ['searchword=', 'words_min=', 'begin_time=', 'art_num=', 'keywords='])
        for opt_name, opt_value in opts:
            if opt_name in ('-s', 'searchword'):
                searchword = opt_value
            if opt_name in ('-w', 'words_min'):
                words_min = opt_value
            if opt_name in ('-e', 'begin_time'):
                begin_time = opt_value
            if opt_name in ('-a', 'art_num'):
                art_num = opt_value
            if opt_name in ('-k', 'keywords'):
                keywords = opt_value
    # set default values
    if searchword == '':
        searchword = '中芯国际'
    if words_min == '':
        words_min = str(3000)
    if begin_time == '':
        cur = datetime.now()
        before = cur - timedelta(days=1095)
        begin_time = before.strftime("%Y-%m-%d")
        print(begin_time)
    if art_num == '':
        art_num = 30
    if keywords == '':
        keywords = '战略,进步,成功,失败,生长,增长'
    if searchword not in os.listdir():
        os.mkdir(searchword)
    ids = get_urls(searchword, begin_time, int(art_num))
    print("Found articles count: " + str(len(ids)))
    for id in ids:
        print("Processing article #"+str(id))
        process_article(id, int(words_min), searchword, keywords)


if __name__=="__main__":
    main()