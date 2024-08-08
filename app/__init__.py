import yaml
import logging
import logging.config
import sqlalchemy
import atexit
from flask import Flask

# YAMLファイルを読込
with open('./app/config.yml', 'r') as yml:
    config = yaml.load(yml, Loader=yaml.Loader)

# アプリケーションインスタンスを作成
app = Flask(__name__, static_folder='/static')

# ロガーを読込
logging.config.dictConfig(config['logging'])
logger = logging.getLogger()

# DBエンジンを作成
# TODO ENVファイルから読み込んでも良いが面倒なので直接設定（ENVファイルからの読み込みはos.getenvを利用）
engine = sqlalchemy.create_engine(url = 'postgresql://postgres:passw0rd@localhost:5432/python', client_encoding='utf-8', echo=False)

# アプリケーション終了時にDBエンジンを破棄
atexit.register(lambda: engine.dispose())

# 公開するインスタンス、メソッドなどを設定
__all__ = ['app', 'logger', 'engine']

# おまじない
if __name__ == '__main__':
    app.run(debug=True)
