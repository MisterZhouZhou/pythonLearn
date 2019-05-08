# coding:utf-8
import csv
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    headers = {'User-Agent': user_agent}
    r = requests.get('http://seputu.com/', headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    lisit = []
    for mulu in soup.find_all(class_='mulu'):
        h2 = mulu.find('h2')
        if h2 != None:
            h2_title = h2.string

            for a in mulu.find(class_='box').find_all('a'):
                href = a.get('href')
                box_title = a.string
                lisit.append((h2_title, box_title, href))
    headers_ = {'标题', '章节名', '链接'}
    with open('qiye.csv', 'w', newline='') as fp:
        # csv需要指定newline，否则每行数据之间都有空行
        f_csv = csv.writer(fp)
        f_csv.writerow(headers_)
        f_csv.writerows(lisit)
