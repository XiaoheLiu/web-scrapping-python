# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup 
import requests, sys

class downloader(object):
  """
  Download articles in Academie Duello blog
  """

  def __init__(self):
    self.target = 'https://www.academieduello.com/news-blog/'
    self.names = []     # Names for the articles
    self.urls = []      # urls of the articles
    self.nums = 0       # Total number of articles

  def get_download_url(self):
    """
    Get urls of the articles
    """
    target = 'https://www.academieduello.com/news-blog/'
    html = requests.get(url = target).text
    div_bf = BeautifulSoup(html, features="html.parser")
    main_div = div_bf.find(id = 'main')
    main_div_bf = BeautifulSoup(str(main_div), features="html.parser")
    a = main_div_bf.find_all('a')
    
    for each in a:
      if each.parent.name == 'h2':
        self.names.append(each.string)
        self.urls.append(each.get('href'))
        self.nums += 1;
  
  def get_contents(self, target):
    """
    Get contents of an article given the url
    Parameters:
      target - download url(string)
    Returns:
      md - contents of the article in markdown format(string)
    """
    md = ''
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html, features="html.parser")
    title = bf.find('h1', class_ = 'entry-title')
    md += '# '+title.text+'\n\n'
    content = bf.find('div', class_ = 'entry-content')
    paragraphs = content.findAll(['p', 'h2'])
    for p in paragraphs:
      if p.name == 'h2':
        md += "## "+p.text+'\n\n'
      else:
        md += p.text+'\n\n'
    return md
  
  def writer(self, name, path, text):
    """
    Write all articles into one markdown file
    """
    with open(path, 'a', encoding='utf-8') as f:
      f.write(name + '\n')
      f.writelines(text)
      f.write('\n\n')
  
  def writeOne(self, i, path):
    """
    Write one article into a markdown file
    Parameters:
      i - index of the article
      path - path to the file, eg. ./folder/
    Returns:
      none
    """
    name = self.names[i]
    url = self.urls[i]
    text = self.get_contents(url)
    with open(path+name+'.md', 'a', encoding='utf-8') as f:
      f.writelines(text)  


if __name__ == '__main__':
  dl = downloader()
  dl.get_download_url()
  print('Start downloading articles...')
  for i in range(dl.nums):
    dl.writer(dl.names[i], './Duello/All-Articles.md', dl.get_contents(dl.urls[i]))
    dl.writeOne(i, './Duello/')
    sys.stdout.write(" %.0f%% Downloaded..." %  float(i/dl.nums*100) + '\r')
    sys.stdout.flush()
  print('Download complete!')
