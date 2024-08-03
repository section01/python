import yaml
import dotenv
import os
import logging
import logging.config
import sqlalchemy
import atexit
from flask import Flask

'''
TODO 2024/08/03 課題点
    importされた際に同じ処理が実行されている可能性があります。
    __main__とかで.py呼出のみ実行する様に修正が必要です。
'''

print('アプリケーションの初期化を行います')

with open('./app/config.yml', 'r') as yml:
    config = yaml.load(yml, Loader=yaml.Loader)

dotenv.load_dotenv(override=True)

app = Flask(__name__, static_folder='/static')

logging.config.dictConfig(config['logging'])
log = logging.getLogger()

url = '{}://{}:{}@{}:{}/{}'.format(os.getenv('DIALECT'), os.getenv('USER'), os.getenv('PASSWD'),
    os.getenv('HOST'), os.getenv('PORT'), os.getenv('DATABASE'))
engine = sqlalchemy.create_engine(url, client_encoding='utf-8', echo=False)
con = engine.connect()

@atexit.register
def finalize():
    con.close()

__all__ = ['app', 'log', 'con']