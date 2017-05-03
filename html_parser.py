#coding=utf-8
'''
Created on Apr 12, 2017

@author: lurker2006
'''
from bs4 import BeautifulSoup
import re
import urllib2
from pip._vendor.requests.packages.urllib3.util import url
import urlparse
from yaoqi.jpg_downloader import jpgDownloader

class HtmlParser(object):


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        ul = soup.find('ul', class_ = 'piclist listcon')
#        for link in links:
#            new_url = link['href']
#            new_full_url = urlparse.urljoin(page_url, new_url)
#            new_urls.add(new_full_url)
        for ele in ul.find_all('li'):
            new_urls.add(ele.find('a')['href'])
        #print new_urls
        return new_urls
    
    def _get_new_pic_src(self, page_url, soup):
         img = soup.find('ul', class_ = 'mnlt').find('img')
         #print img['src']
         return img['src']
    def _get_new_data(self, page_url, soup):
        #        <dd class="lemmaWgt-lemmaTitle-title">
        #        <h1>Python</h1>
        res_data = {}
        res_data['url'] = page_url
        title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        #<div class="lemma-summary" label-module="lemmaSummary">
        #<div class="para" label-module="para">
        summary_node = soup.find('div', class_ = 'lemma-summary').find('div', class_ = 'para')
        res_data['summary'] = summary_node.get_text()
        return res_data
    
    
    def parse_pre(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html5lib', from_encoding = 'utf8')
        return soup
    
    def parse(self, page_url, html_cont):
        soup = self.parse_pre(page_url, html_cont)
        new_urls = self._get_new_urls(page_url, soup)
        return new_urls
    
    def parse_pic(self, page_url, html_cont):
        soup = self.parse_pre(page_url, html_cont)
        pic_src = self._get_new_pic_src(page_url, soup)
        return pic_src
    
        #new_data = self._get_new_data(page_url, soup)
        #print new_data['summary'].encode('gbk', 'ignore')
        #return new_urls, new_data
#new_url = 'http://www.yqimh.com/shaonvmanhua/3750.html'
#parser = HtmlParser()
#html = urllib2.urlopen(new_url).read()
#pic_url = parser.parse_pic(new_url, html)
#
#print pic_url
if __name__ == '__main__':
    exf = open('D:/JavaProject/yulj/yaoqi/extra.txt','w')   

    url = 'http://www.yqimh.com/shaonvmanhua/list_4_%d.html'
    url_root = 'http://www.yqimh.com'
    parser = HtmlParser()
    set_url = set()
    
#if __name__ == '__main__':     
    for i in range(89,91):
        urlnew = url % i
        #print urlnew
        html = urllib2.urlopen(urlnew).read()
        new_urls = parser.parse(urlnew, html)
        set_url = set_url.union(new_urls)
#    print set_url
    
#set_url = set()
#set_url.add('/shaonvmanhua/7582.html')
#url_root = 'http://www.yqimh.com'
#parser = HtmlParser()

#if __name__ == '__main__':
    set_pic_url = set()
    reg = re.compile('''/shaonvmanhua/(\d+).html''')
    reg_del = re.compile('''http://pic.taov5.com/1/''')
    jpg_dl = jpgDownloader('D:/JavaProject/yulj/yaoqi/save')
    url_cnt = 0
    for urlnew in set_url:
        url_cnt = url_cnt + 1
        #/shaonvmanhua/8512.html
        #http://www.yqimh.com/shaonvmanhua/8512.html
        print len(set_url) ,urlnew, url_cnt
        m = reg.match(urlnew)
        if not m:
            exf.write(urlnew)
            continue
        prefix = m.group(1)
        full_url = url_root + urlnew
        count = 2
        while True:
            try:
                html = urllib2.urlopen(full_url).read()
                pic_url = parser.parse_pic(full_url, html)
                #dl if qualify
                m2 = reg_del.match(pic_url)
                full_url = url_root + '/shaonvmanhua/%s_%d.html' % (prefix, count)
                if m2:
                    #print 'hit http://pic.taov5.com/1/', pic_url
                    count = count + 1
                    continue
                else:
                    print 'no hit', pic_url, prefix, count
                    jpg_dl.dl_jpg(pic_url, prefix, count)
                    count = count + 1
                                    
            except Exception, e:
                print e
                print 'exc', urlnew
                break
        
        #set([u'2015', u'1', u'tu', u'uploads'])
        #http://pic.taov5.com/1/648/177.jpg
        #http://pic.taov5.com/2015/6502/001.jpg
        #http://pic.taov5.com/tu/allimg/150320/1-150320202G6.jpg
        #http://pic.taov5.com/uploads/allimg/150121/1-150121125329.jpg
    if __name__ == '1__main__':     
        reg = re.compile('''http://pic.taov5.com/1/''')
        m = reg.match(pic_url)
        if m:
            if  m.group(1) not in set_pic_url:
                set_pic_url.add(m.group(1))
                print 'diff url %s' % pic_url
        else:
            print pic_url
            print 'no match'
        
        print set_pic_url
        
        

        

    
    


