import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbweek3_homework# 'dbsparta'라는 이름의 db를 만듭니다.

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# 아래 빈 칸('')을 채워보세요
for tr in trs:
    rank = tr.select_one('td.number').text[0:2].strip()
    title = tr.select_one('td.info > a.albumtitle').text.strip()
    artist = tr.select_one('td.info > a.artist').text.strip()
    print(rank+'------'+title+'------'+artist)
    doc = {
        'rank': rank,
        'title': title,
        'artist': artist
    }
    db.song_chart.insert_one(doc)