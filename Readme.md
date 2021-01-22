# Docker-Python-Docx

`Python3`を使用して Word ファイル（.docx）を元に  
html ファイルを生成するモジュール

## 使用方法

> ※ Docker がインストールされている事が前提です

### 作業環境の設定

`.env.example`をコピーして`.env`ファイルを作成し  
自身の環境に合わせて`PATH`を指定してください

`PORT`については、既に`8080`を他のアプリ等で使用していなければ  
そのままで問題ありません

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

元となる Word ファイルを`/data/dist/`ディレクトリに設置

### 各タグのクラス名等の設定

`/data/converter.py`内で各タグの設定を行う

### 変換の実行

プロジェクト直下で下記コマンドを実行しコンテナ内に入る

```
docker exec -it docker-python-docx sh
```

変換処理が書いてあるファイルを実行

```
cd /var/www/html
python3 converter.py
```

### 確認

`/data/dist/`ディレクトリに HTML ファイルが生成されていたら成功

### Docker 停止コマンド

`docker-compose down`