# python-template

Python プロジェクトを始めるためのテンプレートです。

## 主な内容

* Poetry を使用
* pre-commit を設定
    * pre-commit のサンプル設定にある基本的なもの
    * black によるフォーマットチェック
    * Pylint による静的解析

# 使い方

1. [sdispater/poetry](https://github.com/sdispater/poetry/) のインストール
2. [pre\-commit/pre\-commit](https://github.com/pre-commit/pre-commit) のインストール
3. このプロジェクトから新規プロジェクトを clone
4. pyproject.toml のテンプレート用の設定を書き換える
    * プロジェクト名
    * バージョン番号
    * 作者 etc...
5. `poetry install`
6. 開発開始

# ライセンス

* MIT

# その他

* black と isort を併用すると結果が変わってしまうので、仕方なく black のみ利用することを前提にしている
