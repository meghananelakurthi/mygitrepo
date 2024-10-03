# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:48:21 2021

@author: Deepstrats
"""

from flask import Flask, redirect, url_for, json, jsonify

app = Flask(__name__)

emp = [{'ID':'0', 'NAME':'Pavan', 'Dept':'IT'},
        {'ID':'1', 'NAME':'Sean', 'Dept':'Sales'},
        {'ID':'2', 'NAME':'John', 'Dept':'HR'},
        {'ID':'3', 'NAME':'Monica', 'Dept':'Marketing'}]


@app.route('/')

def index():
    return "Welcome to ABC Company's portal"


@app.route('/emp', methods=['GET'])

def get():
    return jsonify({'emp':emp})

@app.route('/emp/<int:ID>', methods=['GET'])

def get_ID(ID):
    return jsonify({'emp':emp[ID]})


@app.route('/emp', methods=['POST'])

def create_post():
    
    emp_new = {'ID':'4', 'NAME':'Robert', 'Dept':'UI'}
    emp.append(emp_new)
    return jsonify({'Created':emp_new})


@app.route('/emp/<int:ID>', methods=['PUT'])

def update_emp(ID):
    emp[ID]['JD'] = 'Social media marketing'
    return jsonify({'empupdate':emp[ID]})


@app.route('/emp/<int:ID>', methods = ['DELETE'])

def delete(ID):
    emp.remove(emp[ID])
    return jsonify({'result':True})


if __name__ == '__main__':    
    app.run(debug=True)    
    
    