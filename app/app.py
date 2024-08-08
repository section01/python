from flask import render_template
from sqlalchemy import text
from . import *

@app.route('/')
def main():
    return render_template('index.html')
