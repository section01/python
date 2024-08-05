import yaml
import dotenv
import os
import logging
import logging.config
import sqlalchemy
from flask import Flask

with open('./app/config.yml', 'r') as yml:
    config = yaml.load(yml, Loader=yaml.Loader)
dotenv.load_dotenv(override=True)

app = Flask(__name__, static_folder='/static')

logging.config.dictConfig(config['logging'])
logger = logging.getLogger()

url = '{}://{}:{}@{}:{}/{}'.format(os.getenv('DIALECT'), os.getenv('USER'), os.getenv('PASSWD'),
    os.getenv('HOST'), os.getenv('PORT'), os.getenv('DATABASE'))
engine = sqlalchemy.create_engine(url, client_encoding='utf-8', echo=False)
connect = engine.connect()


__all__ = ['app', 'logger', 'connect']
