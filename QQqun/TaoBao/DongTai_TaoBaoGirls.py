"""
A web crawler for tao nv lang. Grabing all MM's images with hierarchical structure:
MM's name(folder) --> MM's albums(folder) --> MM's images(files)

Run the code with three steps:
1.Create a instance of web crawler class
2.Select a range of pages with start index and end index.
3.Run a class function named save_all(start, end)

All images are going to save in your current path.

Please notice there are including chinese character. It may cause unreadable folder names,
If your computer do not support chinese language.

Author:	Alien_gmx
Date:	10/20/2015
version: 1.0
"""
import urllib
import urllib2
import re
import os
import spynner
class web_crawler:
    def __init__(self):
        self.mainurl = 'http://mm.taobao.com/json/request_top_list.htm'
        
    #get page information by page index 
    def get_page(self, index):
        url = self.mainurl + '?page=' + str(index)
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)
        # GBK is the encode method of chinese character 
        return resp.read().decode('gbk')
    
    #get page information by single url
    def get_details(self, url):
        resp = urllib2.urlopen(url)
        return resp.read().decode('gbk')

    #get main page contents including [0]:url of mm's page [1]:user id [2]:name [3]:age [4]:city 
    def get_contents(self, index):
        page = self.get_page(index)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<a class="lady-name.*?user_id=(\d*).*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
                             re.S)
        items = re.findall(pattern, page)
        content = []
        for i in items:
            content.append([i[0],i[1],i[2],i[3],i[4]])
        return content

    #return a dic with key of album_ids and value of album_names
    def get_album_contents(self, user_id):
        main_url = 'https://mm.taobao.com/self/album/open_album_list.htm?&user_id=' + user_id + '&page='
        page_index = 1
        album_ids = []
        album_names = []
        album_contents = {}
        
        while(True):
            url = main_url + str(page_index)
            page = self.get_details(url)
            pattern_ids = re.compile('<a class="mm-first" href=".*?album_id=(\d*).*?"')
            pattern_names = re.compile('\s*(.*?)</a></h4>')    #mutiple space 
            items_ids = re.findall(pattern_ids, page)
            items_names = re.findall(pattern_names, page)
            
            if len(items_ids) == 0:
                break
            else:
                page_index += 1
                for i in items_ids:
                    if i not in album_ids:
                         album_ids.append(i)
            
            album_names += items_names
        for n in range(len(album_names)):
            album_contents[album_ids[n]] = album_names[n]
        return album_contents
    

    #return all image urls in a album
    def get_images_urls(self, user_id, album_id):
        main_url = 'https://mm.taobao.com/album/json/get_photo_list_tile_data.htm?user_id=' + user_id + '&album_id=' + album_id + '&page='
        page_index = 1
        images_url = []
        while(True):
            url = main_url + str(page_index)
            page = self.get_details(url)
            pattern = re.compile('<img src="(.*?)"')
            items = re.findall(pattern, page)
            if len(items) == 0:
                break
            else:
                page_index += 1
            images_url += items
        return images_url

 
    def new_folder(self, path, name):
        os.chdir(path)  
        name = name.strip()
        name = name.strip('.') #. cannot including in a name of folder
        is_exists = os.path.exists(name)
        if not is_exists:
            print 'Creating a new folder:', name
            os.makedirs(name)    
        else:
            print 'The folder named', name, 'exists'
        
        return_path = path + '/' + name
        return return_path


    def save_images(self, user_id, user_name, album_contents):
        path_user = self.new_folder(path = os.getcwd(), name = user_name)
        #print path_user
        for album_id in album_contents:
            path_album = self.new_folder(path_user, album_contents[album_id])
            urls = spider.get_images_urls(user_id, album_id)  
            for n in range(len(urls)):
                self.save_image('https:' + urls[n],
                                path_album + '/' + str(n + 1)+'.'+'jpg')  
    
    def save_image(self, url, f_name):
        resp = urllib.urlopen(url)
        page = resp.read()
        f = open(f_name,'wb')
        f.write(page)
        print 'You are saving images......'
        f.close()

                     
    def save_all(self, start, end):
        for page_index in range(start, end + 1):
            contents = self.get_contents(page_index)
            for i in contents:
                album_contents = self.get_album_contents(i[1])
                self.save_images(i[1],i[2],album_contents)

                
if __name__ == '__main__':           
    spider = web_crawler()
    spider.save_all(1,1)

     
