# Docker-Python-Docx
`Python3`を使用してWordファイル（.docx）を元に  
htmlファイルを生成するモジュール

## 使用方法
> ※ Dockerがインストールされている事が前提です

### 環境の立ち上げ

プロジェクト直下で下記コマンドを実行  
※ こちらは初回のみで可

```
docker-compose build
```

完了したら下記コマンドで`container`が立ち上がる
```
docker-compose up -d
```

http://localhost:8080/  
に`Apache`の画面が表示されたら立ち上げ成功

### `.docx`ファイルの準備
元となるWordファイルを`/data/dist/`ディレクトリに設置

### 各タグのクラス名等の設定
`/data/converter.py`内で各タグの設定を行う

### 変換の実行
プロジェクト直下で下記コマンドを実行しコンテナ内に入る
```
docker exec -it docker-python-docx sh
```

変換処理が書いてあるファイルを実行
```
python3 /var/www/html/converter.py
```

### 確認
`/data/dist/`ディレクトリにHTMLファイルが生成されていたら成功  
