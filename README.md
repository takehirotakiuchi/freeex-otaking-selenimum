# Selenim メルマガ登録 スクリプト

定期購読システム デモサイトのメルマガ登録を自動化するためのスクリプト


## 動作確認環境
MacOS　64bit
Python 3.6.4
Chrome 最新版

### 前提条件
- selenium　ライブラリーがインストールされていること

- Google Chrome Driverの最新版がインストールされていること
[公式サイト](http://docs.seleniumhq.org/download/)

```
pip install selenium
```

### インストール

リポジトリをローカル環境にもってきて、設定ファイルを作成する。
(env.exampleファイルをコピーして、.envファイルを作成する)

```bash
git clone https://github.com/takehirotakiuchi/freeex-otaking-selenimum.git
cd freeex-otaking-selenimum.git
cp -p env.example .env
```

.envの中身
```text
# WebサイトのトップURLを設定する(注意：末尾にスラッシュを入れない)
BASE_URL="http://laravel-saas-boilerplate.dev" 

# ログインメールアドレスを設定する
USER_MAIL="sample@example.com"

# ログインパスワードを設定する
USER_PASS="password"

# jsonファイルが保存されいるディレクトリパスを指定する
JSON_DIRECTORY="json"

# 登録済みのjsonファイルを読み込まない設定(true)にする。falseで無効化
ENABLE_MEMORIZING=true
```

jsonファイルの設定
```json
{
	"date": "2018-07-03 06:00:00",
  "is-saved": false,
	"title": "sample",
	"body": "body"
}
```
is-saveがtrueの時は、読み込まない


## 実行コマンド

```bash
python main.py
```
