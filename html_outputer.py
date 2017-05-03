'''
Created on Apr 12, 2017

@author: lurker2006
'''


class HtmlOutputer(object):
    
    def __init__(self):
        self.all_data = []
        
    def collect_data(self, data):
        if data is None:
            return
        
        self.all_data.append(data)

    
    def output_html(self):
        fobject = open('data.html', 'w')
        
        fobject.write('<html>')
        fobject.write('<body>')
        fobject.write('<table>')
        
        for data in self.all_data:
            fobject.write('<tr>')
            
#            fobject.write('<td>')
#            fobject.write(data['url'].encode('utf-8'))
#            fobject.write('</td>')
            
            fobject.write('<td>')
            fobject.write(data['title'].encode('utf-8'))
            fobject.write('</td>')
            
            fobject.write('<td>')
            fobject.write(data['summary'].encode('utf-8'))
            fobject.write('</td>')
            fobject.write('</tr>')
        
        fobject.write('</table>')
        fobject.write('</body>')
        fobject.write('</html>')
        
        return
    
    
    



