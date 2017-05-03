'''
Created on Apr 12, 2017

@author: lurker2006
'''


class UrlManger(object):
    def __init__(self):
        object.__init__(self)
        self.new_urls = set()
        self.old_urls = set()
        
    def add_new_url(self, new_url):
        if new_url and new_url not in self.new_urls and new_url not in self.old_urls:
            self.new_urls.add(new_url)

    def add_new_urls(self, new_urls):
        if new_urls:
            for new_url in new_urls:
                self.add_new_url(new_url)
    
    def has_new_url(self):
        return len(self.new_urls)

    
    def get_new_url(self):
        return self.new_urls.pop()

    
    
    
    
    
    
    
    
    



