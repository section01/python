from flask import Flask, render_template
from dotenv import load_dotenv
from yaml import safe_load
from logging import getLogger
from logging.config import dictConfig
from flask_sqlalchemy import SQLAlchemy

load_dotenv(override=True)

app = Flask(__name__, static_folder='./public', template_folder='./views')

with open('./apps/application.yml') as yml:
    config = safe_load(yml)

dictConfig(config['logging'])
logger = getLogger(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(
    config['database']['user'],
    config['database']['password'],
    config['database']['host'],
    config['database']['port'],
    config['database']['name'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
engine = SQLAlchemy(app)

@app.route('/')
def main():
    return render_template('kintai-input.html')

@app.route('/kintai/input')
def input():
    return render_template('kintai-input.html')

@app.route('/kintai/search')
def search():
    return render_template('kintai-search.html', list=[
        {
            "date": "01",
            "start": "09:00",
            "end": "18:00",
            "break": "1:00",
            "remark": "テスト1"
        },
        {
            "date": "02",
            "start": "09:00",
            "end": "18:00",
            "break": "1:00",
            "remark": "テスト2"
        },
        {
            "date": "03",
            "start": "09:00",
            "end": "18:00",
            "break": "1:00",
            "remark": "テスト3"
        }
    ])

if __name__ == '__main__':
    app.run(debug=True)
