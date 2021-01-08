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

    # パラグラフ
    source = source.replace('<p>', '<p class="">')
  
    # 見出し 
    source = source.replace('<h2>', '<h2 class="">')
    source = source.replace('<h3>', '<h3 class="">')

    # 画像
    source = re.sub('<img src=\"(.*?)\"', '<img src=""', source)

    # リスト
    source =source.replace('<ul>', '<ul class="">')
    source =source.replace('<ol>', '<ol class="">')

    # --------------------- class setting end ---------------------

    html = BeautifulSoup(source, 'lxml')
    html = html.prettify()
    messages = result.messages

    outputfile = file.replace('.docx', '.html')
    outputfile = outputfile.replace('/src/', '/dist/')

  with open(outputfile, mode='w') as f:
    f.write(html)

  print("finished convert (´-ω-`)")