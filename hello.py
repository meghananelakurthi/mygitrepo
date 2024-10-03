# pip install flask
from flask import Flask
# Flask constructor takes "hello", the __name__ of current module as argument

app = Flask(__name__)

@app.route('/home')
def welcome():
    return "Welcome to the class folks!"

@app.route('/mycity')
def blr():
    return "Welcome to your city, Bengaluru"

@app.route('/myorg')
def org():
    return "Welcome Harman"

if __name__ == '__main__':
    app.run(debug=True)
    '''print(" I am imported from the same module")
else:
    print("I am being imported from another module")'''