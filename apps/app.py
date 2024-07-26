from flask import Flask, render_template
from logging.config import dictConfig
import yaml

with open('./apps/config.yml', 'r') as yml:
    dictConfig(yaml.load(yml, Loader=yaml.Loader))

app = Flask(__name__, static_folder='/')

@app.route('/')
def main():
    return render_template('index.html')