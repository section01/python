from yaml import load, Loader
from logging.config import dictConfig
from flask import Flask
from sqlalchemy import create_engine
from atexit import register

with open('./app/config.yml', 'r') as yml:
    config = load(yml, Loader=Loader)

dictConfig(config['logging'])

app = Flask(__name__, static_folder='./static', template_folder='./templates')
engine = create_engine(url = 'postgresql://postgres:passw0rd@localhost:5432/python', client_encoding='utf-8', echo=False)

register(lambda: engine.dispose())

if __name__ == '__main__':
    app.run(debug=True)
