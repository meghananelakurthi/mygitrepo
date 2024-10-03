# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:54:41 2021

@author: Deepstrats
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:20:13 2021

@author: Deepstrats
"""

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')

def welcome():
    return render_template('form.html')

@app.route('/enter/<int:score>')

def passed(score):
    res = ""
    if score>=35:
        res = "passed"
    else:
        res = "failed"
    return render_template('result.html', result=res)

@app.route('/enter_f/<int:score>')

def failed(score):
    return "You've failed adn your marks is "+ str(score)

@app.route('/results/<int:marks>')

def results(marks):
    result = ""
    if marks<35:
        result = "failed"
    else:
        result = "passed"
    return redirect(url_for(result, score = marks))

@app.route('/submit',methods = ['POST','GET'])
def submit():
  
    total_score = 0
    
    if request.method == 'POST':
        ML = float(request.form['ML'])
        BigData = float(request.form['BigData'])
        WebApp = float(request.form['WebApp'])
        
        total_score = (ML+BigData+WebApp)/3
        
    res = ""
    '''if total_score>=35:
        res = "passed"
    else:
        res = "failed"'''
    return redirect(url_for('passed', score=total_score))
    
if __name__ == '__main__':    
    app.run(debug=True)    