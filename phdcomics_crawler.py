import requests
from bs4 import BeautifulSoup
import json


actual_comics = []
def phdcomics_crawler(int_page, max_pages):
    page = int_page
    while page <= max_pages:
        url = 'http://www.phdcomics.com/comics/archive.php?comicid=' + str(page)
        source_code = requests.get(url, allow_redirects=True)
        plain_text = source_code.text.encode('ascii', 'replace')
        soup = BeautifulSoup(plain_text,'html5lib')
        urls = []
        for link in soup.find_all("img", class_="img-responsive"):
            href = link.get('src')
            title = link.string
            urls.append(href)
        page += 1
        actual_comics.append(urls[0])
    #~ print(actual_comics)


    with open ('phdcomics_images ' + str(int_page) + '-' + str(max_pages) + '.json', 'w') as file_object:
        json.dump(actual_comics, file_object)
        print('completed')
 


phdcomics_crawler(401, 405)

