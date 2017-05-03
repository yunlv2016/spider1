'''
Created on Apr 12, 2017

@author: lurker2006
'''
import urllib2


class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        
        response = urllib2.urlopen(new_url)
        
        if response.getcode() == 200:
            return response.read()
        else:
            return None

if __name__ == '__main__':
    downloader = HtmlDownloader()
    print downloader.download('http://www.yqimh.com/shaonvmanhua/')
        
    
    



