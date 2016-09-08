import urllib
import urllib.request
import urllib.parse
import bs4
import os
import datetime

url = "http://www.demonoid.pw/files/?category=9&subcategory=0&language=0&quality=0&seeded=2&external=2&query=naruto&uid=0&sort="

# This is basically for later use. I want to get the domain.
baseurl = urllib.parse.urlparse(url)
DOMAIN = '{uri.scheme}://{uri.netloc}/'.format(uri=baseurl)

req = urllib.request.Request(url)
soup = bs4.BeautifulSoup(urllib.request.urlopen(req), 'html.parser')
# soup = soup.prettify('utf-8')

myfile = 'myfile.txt'
link = soup.find_all('a')

with open(myfile, 'w', encoding='utf-8') as myfile:
    for link in soup.find_all('a', href=True):
        if '/files/details/' in link['href']:
            myfile.write(str(link['href'])+'\n')

# I'll let go of my laziness and make a directory!


for link in open('myfile.txt', 'r').readlines():
    # Now I've to append the link to the DOMAIN
    tmp_url = DOMAIN + link[:-1]
    # The [:-1] is basically because there's a '\n' in the file
    # I know there should be a better way to do this, there is a method
    # in str that does this, anyway.
    # I should make a folder to contain the results.
    req = urllib.request.Request(tmp_url)
    soup = bs4.BeautifulSoup(urllib.request.urlopen(req), 'html.parser')
    # magnets_file = 'myfile_%s_%s' %(datetime.datetime().now(), DOMAIN)
    magnets_file = 'magnets_file.txt'

    with open(magnets_file, 'w', encoding='utf-8') as myfile:
        for link in soup.find_all('a', href=True):
            if 'magnet' in link:
                magnets_file.write(str(link)+'\n')




