import mammoth # docx → html
import os # create file
import glob # read file name

from bs4 import BeautifulSoup # html linter 
from bs4 import Tag

import re # 正規表現

files = glob.glob('./src/*.docx')

for file in files:
  with open(file, 'rb') as docx_file:
    result = mammoth.convert_to_html(docx_file)
    source = result.value

    # --------------------- class setting start ---------------------

    # 見出し 
    source = source.replace('<h1>', '<h1 class="">')
    source = source.replace('<h2>', '<h2 class="">')
    source = source.replace('<h3>', '<h3 class="">')
    source = source.replace('<h4>', '<h4 class="">')
    source = source.replace('<h5>', '<h5 class="">')

    # パラグラフ
    source = source.replace('<p>', '<p class="">')

    # 画像 (画像は未対応の為、ダミー画像を表示)
    source = re.sub('<img src=\"(.*?)\"', '<img src="https://placehold.jp/150x150.png"', source)

    # リスト
    source =source.replace('<ul>', '<ul class="">')
    source =source.replace('<ol>', '<ol class="">')

    # テーブル
    source =source.replace('<table>', '<table class="">')
    source =source.replace('<tr>', '<tr class="">')
    source =source.replace('<td>', '<td class="">')

    # --------------------- class setting end ---------------------

    html = BeautifulSoup(source, 'lxml')
    html = html.prettify()
    
    outputfile = file.replace('.docx', '.html')
    outputfile = outputfile.replace('/src/', '/dist/')

  with open(outputfile, mode='w') as f:
    f.write(html)

  print("finished convert (´-ω-`)")