# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:20:13 2021

@author: Deepstrats
"""

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('ex1.html')

@app.route('/enter/<int:score>')
def passed(score):
    return "Congrats! you've passed!"

@app.route('/enter_f/<int:score>')
def failed(score):
    return "You've failed and your marks is "+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks<35:
        result = "failed"
    else:
        result = "passed"
    return redirect(url_for(result, score = marks))
'''
@app.route('/Submit',methods = ['POST','GET'])
def submit():
  
    total_score = 0
    
    if request.method == 'POST':
        ML = float(request.form['ML'])
        BigData = float(request.form['BigData'])
        WebApp = float(request.form['WebApp'])
        
        total_score = (ML+BigData+WebApp)/3
        
    res = ""
    if total_score>=35:
        res = "passed"
    else:
        res = "failed"
    return redirect(url_for(res, score=total_score))''' 
    
if __name__ == '__main__':    
    app.run(debug=True)    