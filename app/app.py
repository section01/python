from flask import Flask, render_template
from logging import getLogger
from logging.config import dictConfig
from yaml import load, Loader

with open('./app/conf.yml', 'r') as yml:
    config = load(yml, Loader=Loader)

dictConfig(config['logging'])
logger = getLogger()

app = Flask(__name__, static_folder='/')

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)