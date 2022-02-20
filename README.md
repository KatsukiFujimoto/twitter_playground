## セットアップ

### 事前に必要なもの

- Docker
- docker-compose

### 初回起動

```shell
$ docker-compose build
$ docker-compose up
$ echo 'BEARER_TOKEN="your_bearer_token"' > .env
```

### 使い方

```shell
$ docker-compose exec backend bash
$ python main.py
```
