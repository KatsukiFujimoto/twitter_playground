## セットアップ

### 事前に必要なもの

- Docker
- docker-compose

#### インストール

macOS

```shell
$ brew install docker
```

Docker Desktop のインストール  
- [Developers - Docker](https://www.docker.com/get-started/)

### 初回起動

まず、トークンを `.env` ファイルに追加する。

```shell
$ echo 'BEARER_TOKEN="your_bearer_token"' > .env
```

Docker の立ち上げを行う。

```shell
$ docker-compose build
$ docker-compose up
```

### 使い方
実際に使用してみるため、次のコマンドを実行する。

```shell
$ docker-compose exec backend bash
# bash が立ち上がる
$ python main.py
```

### Twitter API

`res` に使うAPI
- [GET /2/tweets/search/recent](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent)

### git の使い方

リモートのメインブランチからデータを取得してローカルにマージする。

```sh
$ git pull origin main
# origin の main ブランチを pull する
```

編集したデータをリモートのメインブランチへとプッシュする。

```sh
$ git push origin main
# origin の main ブランチを push する
```

