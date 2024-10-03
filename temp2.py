# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:37:09 2021

@author: Deepstrats
"""

from flask import Flask, render_template
# Flask constructor takes the __name__ of current module as argument

app = Flask(__name__)

@app.route('/home/<int:score>')

def index(score):
    return render_template('index2.html', marks=score)

if __name__ == '__main__':
    app.run(debug=True)