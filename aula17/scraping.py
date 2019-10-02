import urllib3
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://www.youtube.com/'
http = urllib3.PoolManager()
page = http.request('GET', quote_page)
soup = BeautifulSoup(page.data, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find_all('img')

for source in name_box:
    try:
        print(source['src'])
    except KeyError:
        pass

# print(name_box)

# https://lxml.de/tutorial.html
