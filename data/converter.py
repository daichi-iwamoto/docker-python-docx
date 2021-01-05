import mammoth # docx → html
import os # create file

from bs4 import BeautifulSoup # html linter 
from bs4 import Tag

import re # 正規表現

with open('./src/input.docx', 'rb') as docx_file:
  result = mammoth.convert_to_html(docx_file)
  source = result.value


  # --------------------- class setting start ---------------------

  # パラグラフ
  source = source.replace('<p>', '<p class="">')
 
  # 見出し 
  source = source.replace('<h2>', '<h2 class="">')
  source = source.replace('<h3>', '<h3 class="">')
  source = source.replace('<h4>', '<h4 class="">')

  # 画像
  source = re.sub('<img src=\"(.*?)\"', '<img src=""', source)

  # リスト
  source =source.replace('<ul>', '<ul class="list">')

  # --------------------- class setting end ---------------------
  


  html = BeautifulSoup(source, 'lxml')
  html = html.prettify()
  messages = result.messages

with open('./dist/index.html', mode='w') as f:
  f.write(html)

print("finished convert (´-ω-`)")