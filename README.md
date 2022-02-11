## セットアップ

### 事前に必要なもの

- Python
- pipenv

### 初回起動

```shell
$ pipenv install -r requirements.txt
$ echo 'BEARER_TOKEN="your_bearer_token"' > .env
```

### 使い方

```shell
$ pipenv shell
$ python main.py
```
