from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return "welcome admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello %s as guest" %guest

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest = name))
    
if __name__ == '__main__':    
    app.run(debug=True)    