# -*- coding:UTF-8 -*-
import requests
import json
from contextlib import closing
import secret as api  # the access key for the unsplash API is saved in secret.py


class get_photos(object):

    def __init__(self):
        self.base_url = "https://api.unsplash.com/search/photos"
        self.headers = {'Accept-Version': 'v1',
                        'Authorization': 'Client-ID ' + api.access_key}
        self.urls = []
        self.titles = []
        self.num = 1  # how many photos to download

    def get_urls(self, term='image'):
        """
        Get the urls for images
        Parameters:
          term: String, search term
        Returns: 
          none  
        """
        payload = {'page': '1', 'query': term}
        req = requests.get(url=self.base_url,
                           headers=self.headers, params=payload)
        data = json.loads(req.text)
        for i in range(self.num):
            self.urls.append(data['results'][i]['links']['download'])
            self.titles.append(data['results'][i]['description'])
            print(self.urls[i])

    def download(self, i):
        """
        Download the i-th photo
        Parameters:
          i: Int, the index of the photo to download. i <= self.num
        Returns: 
          none 
        """
        with closing(requests.get(url=self.urls[i], stream=True)) as r:
            with open(self.titles[i]+'.jpg', 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__ == '__main__':
    gp = get_photos()
    gp.num = 2
    print('Getting the download urls...')
    gp.get_urls(term="office")
    print('Start to download:')
    for i in range(gp.num):
        print(' Downloading the %dth image' % (i+1))
        gp.download(i)
