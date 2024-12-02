import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
#pandasはデータを扱うためのライブラリ、CSVやSQLからデータを取り込んで操作できる。
#matplotlibはデータをグラフや表にできる、Pandasと連携するといい感じ

#matplotlibのフォントの設定
plt.rcParams['font.family'] = 'MS Gothic'

#CSVを読み込む、読み込んだデータをdfに格納、DataFrameの略で使う人多いらしい
df = pd.read_csv('movies.csv')

#色の設定
colors = ['skyblue']

#dfのジャンルの列から映画数をカウント
all_genres = []     #空のリストをとりあえず作成
for genres in df['ジャンル']:     #dfでジャンル列のすべての値を取り出す、そしてgenresに格納
  if genres != 'データなし':      #データなしを除外
    all_genres.extend(genres.split(','))      #all_genresに追加、ジャンルがアクション、SFの場合→アクション,SFになる

#all_genresの中身の要素をカウントして辞書のようにする
genre_counts = Counter(all_genres)

genres = list(genre_counts.keys())      #辞書のジャンル名を別の変数に格納して使いやすくする
counts = list(genre_counts.values())      #数を別の変数に

#棒グラフとして可視化していく
plt.figure(figsize=(10, 6))     #全体のサイズ
plt.bar(genres, counts, color=colors)     #棒グラフを書く関数、ｘ軸、ｙ軸、色
plt.title('ジャンル別映画数', fontsize=18, fontweight='bold')     #タイトル
plt.xlabel('ジャンル', fontsize=14)     #ｘ軸のラベル
plt.ylabel('映画数', fontsize=14)     #ｙ軸のラベル
plt.xticks(fontsize=12, rotation=45)      #ｘ軸目盛
plt.yticks(fontsize=12)     #ｙ軸目盛
plt.grid(axis='y', linestyle='--', color='gray', alpha=0.7)     #グリッド線

#棒グラフに数値ラベルを追加
#enumerate関数でcountsの中身を取り出して繰り返し処理
for i, count in enumerate(counts):
  plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12, color='black')

plt.tight_layout()      #グラフのレイアウトを自動的に調整
plt.show()      #画面に表示