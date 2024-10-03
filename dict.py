# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:46:41 2021

@author: Deepstrats
"""

from flask import Flask, render_template
# Flask constructor takes the __name__ of current module as argument

app = Flask(__name__)

@app.route('/result')

def result():
    dict = {'Python':80,"Spark":65,"ML":88}
    return render_template('result.html', result=dict)

if __name__ == '__main__':
    app.run(debug=True)