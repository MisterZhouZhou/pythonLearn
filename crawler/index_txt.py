# coding:utf-8
import json
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    headers = {'User-Agent': user_agent}
    r = requests.get('http://seputu.com/', headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    content = []
    for mulu in soup.find_all(class_='mulu'):
        h2 = mulu.find('h2')
        if h2 != None:
            h2_title = h2.string
            lisit = []
            for a in mulu.find(class_='box').find_all('a'):
                href = a.get('href')
                box_title = a.string
                lisit.append({'href': href, 'box_title': box_title})
            content.append({'title': h2_title, 'content': lisit})
    with open('qiye.txt', 'w') as fp:
        for row in content:
            fp.write('\n'+str(row))
