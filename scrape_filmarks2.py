import requests
from bs4 import BeautifulSoup
import csv

#取得したいwebページのURLの指定
url = 'https://filmarks.com/list/trend'
#リクエストに含める追加の情報、User‐Agentは自分がどんなブラウザを使っているかの指定、人間ですよアピール
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
#RequestsライブラリのGetメソッド、HTTPのGetリクエストを送信する
response = requests.get(url, headers=headers)     #ここで取得した情報はresponseに格納される
soup = BeautifulSoup(response.text, 'html.parser')      #Webスクレイピング用のライブラリ、HTMLを解析しやすくする
#response.textはWebページの中身そのまま、html.parserはBeautifulSoupに解析方法の指定

#取得した情報の中のほしいところをとりあえず変数に格納
title_class = 'p-content-cassette__title'
rating_class = 'c-rating__score'
release_date_title_class = 'p-content-cassette__other-info__title'
director_class = 'p-content-cassette__people-list-desc'
country_title_class = 'p-content-cassette__other-info__title'
duration_title_class = 'p-content-cassette__other-info__title'
genre_title_class = 'p-content-cassette__genre__title'

#title_class,、rating_classと一致するものを探す
titles = soup.find_all(class_=title_class)
ratings = soup.find_all(class_=rating_class)
#class_はPythonのclassと区別するため

#上映日
release_dates = []
for title_tag in soup.find_all('h4', class_=release_date_title_class):
    if '上映日：' in title_tag.text:
        span_tag = title_tag.find_next_sibling('span')
        release_dates.append(span_tag.text.strip() if span_tag else 'データなし')

#監督
directors = []
for li_tag in soup.find_all('li', class_=director_class):
    a_tag = li_tag.find('a')
    directors.append(a_tag.text.strip() if a_tag else 'データなし')

#制作された国
countries = []
for title_tag in soup.find_all('h4', class_=country_title_class):
    if '製作国：' in title_tag.text:
        li_tag = title_tag.find_next('ul').find('li')
        a_tag = li_tag.find('a') if li_tag else None
        countries.append(a_tag.text.strip() if a_tag else 'データなし')

#上映時間
durations = []
for title_tag in soup.find_all('h4', class_=duration_title_class):
    if '上映時間：' in title_tag.text:
        span_tag = title_tag.find_next_sibling('span')
        durations.append(span_tag.text.strip() if span_tag else 'データなし')

#ジャンル
genres = []
for title_tag in soup.find_all('h4', class_=genre_title_class):
    if 'ジャンル：' in title_tag.text:
        ul_tag = title_tag.find_next('ul')
        genre_list = [li.find('a').text.strip() for li in ul_tag.find_all('li')] if ul_tag else []
        genres.append(',' .join(genre_list) if genre_list else 'データなし')

#csvファイルを開いて書き込む作業
#withを使うと自動で閉じてくれる
with open('movies.csv', mode='w', newline='', encoding='utf-8') as file:      #open()が開く関数、mode='w'は書き込みモード、newlineは改行
    writer = csv.writer(file)
    writer.writerow(['順位', 'タイトル', '評価', '上映日', '監督名', '製作国', '上映時間', 'ジャンル'])  
    for i in range(len(titles)):
        writer.writerow([
            i + 1,  # 番号
            titles[i].text.strip(),  # タイトル
            ratings[i].text.strip() if i < len(ratings) else 'データなし',          # 評価
            release_dates[i] if i < len(release_dates) else 'データなし',       # 上映日
            directors[i] if i < len(directors) else 'データなし',       # 監督名
            countries[i] if i < len(countries) else 'データなし',       # 製作国
            durations[i] if i < len(durations) else 'データなし',       # 上映時間
            genres[i] if i < len(genres) else 'データなし'          # ジャンル
        ])

print('映画情報をCSVファイルに保存しました！')