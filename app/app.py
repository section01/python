from flask import Flask, render_template
from logging.config import dictConfig
import yaml

# コンフィグ読込
with open('./app/config.yml', 'r') as yml:
    config = yaml.load(yml, Loader=yaml.Loader)

# ロギング設定
dictConfig(config['logging'])

# FLASKインスタンス生成
app = Flask(__name__, static_folder='/')

"""
Function:
    初期画面を表示する
Returns:
    初期画面を返す
"""
@app.route('/')
def main():
    return render_template('index.html')