#概要  
Filmarksの映画のトレンド情報をcsv形式で保存します。  
順位とタイトル、評価に加え、上映日、監督名、制作国、上映時間、ジャンルの項目を追加しました。  
RequestsライブラリのGetメソッドでHTTPのGetリクエストを送信し、取得した情報をBeautifulSoupで分析しています。  

#追加機能  
トレンドに入っている映画のジャンル別の数を棒グラフで見れるようにしました。  
pandasでCSVからデータを取り出して操作し、matplotlibでグラフとして表示できるようにしました。  

#このリポジトリについて
scrape_filmarks.pyが処理の内容になっていて、movie.csvに情報が入ります。  
visual_filmarks.pyがジャンル別映画数をグラフとして見れるようにしたものです。  

#使い方
１．このリポジトリをクローンする

git clone https://github.com/cinamocha/scrape-movie-review.git
  
２．下記ライブラリのインストール  
pip install requests beautifulsoup4  
*pip install pandas
*pip install matplotlib
  
３．スクリプト実行  
python scrape_filmarks.py  
*python visual_filmarks.py
  
#オプション
冒頭の
url = 'ここで'
URLの指定ができます。  

Python 3.13.0  
beautifulsoup4 4.12.3  
bs4 0.0.2  
requests 2.32.3  
pandas 2.2.3  
matplotlib 3.9.3
