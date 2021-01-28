import csv
from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
search = input('검색어를 입력하세요: ')
plusUrl = urllib.parse.quote_plus(search)
i = input('몇 페이지를 크롤링 할까요?: ')
minusKeyword = urllib.parse.quote_plus('-한국인공지능협회')
lastPage = int(i)*10 - 9
pageNum = 1
PageNo = 1
NumberofSearch = 0
searchlist = []
while pageNum < lastPage + 1:
url = f'https://search.naver.com/search.naver?&where=news&query={plusUrl}+{minusKeyword}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=68&start={pageNum}&refresh_start=0'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
title = soup.find_all(class_='news_tit')
searchlist.append(f"★{PageNo}페이지 결과입니다.")
index = 1
for i in title:
temp = []
temp.append(i.attrs['title'])
temp.append(i.attrs['href'])
temp.append("\n")
searchlist.append(temp)
index += 1
pageNum += 10
PageNo += 1
NumberofSearch += len(title)
temp2 = []
temp2.append("총 검색결과:")
temp2.append(str(NumberofSearch))
searchlist.append(temp2)
f = open('./csvfile/' + f'네이버_{search}.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for j in searchlist:
csvWriter.writerow(j)
f.close()
print('완료 되었습니다.')