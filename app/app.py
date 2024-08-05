from flask import render_template
from sqlalchemy import text
from . import *

@app.route('/')
def main():
    result = conn.execute(text('select * from sample.test'))
    print(result.all())
    
    return render_template('index.html')
