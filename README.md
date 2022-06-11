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

検索ワードの部分を分かりやすいように変数 `search_words` として分離させた。クエリ(検索)を作成する当該部分は `main.py` ファイルのこの部分。

```py
search_words = '#bitcoin'
res = client.search_recent_tweets(
        query=search_words,
        max_results = 10,
        expansions = expansions,
        tweet_fields = tweet_fields,
        user_fields = user_fields,
        media_fields = media_fields,
        place_fields = place_fields,
        poll_fields = poll_fields,
)
```

`search_words` に入れる検索ワード自体は Twitter 検索の条件そのままなので、以下の API ドキュメントを参照してクエリを構築する。

- [Search Tweets - How to build a query | Docs | Twitter Developer Platform](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query#list)

```py
# 具体例: イーロン・マスクのアカウントによるツイートで bitcoin というワードを含むツイート
search_words = 'from:elonmusk bitcoin'
```

ただし、`Client.search_recent_tweets()` API は**直近７日間のみのツイートで検索条件に合致するものしか取得できない**ため、上の `'from:elonmusk bitcoin'` でその期間に当該の条件を含むツイートがなければツイートを取得しようとしてもできない。

>The recent search endpoint returns Tweets from the last seven days that match a search query.
>(https://docs.tweepy.org/en/latest/client.html#tweepy.Client.search_recent_tweets より引用)

検索条件に合致するツイートを取得できない場合には、現時点ではエラーを履かずcsvもでないので注意。

`Client.search_all_tweets()` というメソッドもあるが、こちらは「Academic Research」という学術用の用途でAPI承認されたユーザーのみが使うことができる。学術用なので完全な検索が可能。

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

