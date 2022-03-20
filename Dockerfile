FROM python:3.10.2

RUN mkdir /app
WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv \
  && pipenv install --system # pipenvの仮想環境は作らずにコンテナに直接インストール

COPY . /app
