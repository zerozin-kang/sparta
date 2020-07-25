import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
# regularTeamRecordList_table > tr// > td > div > span id="team_NC"
# regularTeamRecordList_table > tr > th > div > span id="team_NC"
# select를 이용해서, tr들을 불러오기
movies = soup.select('#regularTeamRecordList_table > tr')

for movie in movies:
    # movie 안에 a 가 있으면,
    value=''
    span_team = movie.select_one('td.tm > div > span').text
    th_rank = movie.select_one('th > strong').text
    win_rate = movie.select_one('td:nth-child(7) > strong').text
    if float(win_rate) > 0.5:
       value = th_rank + " " + span_team + " " + win_rate

    print(value)
