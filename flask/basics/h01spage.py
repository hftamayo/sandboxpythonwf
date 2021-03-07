"""
h01spage.py
general purpose = return a simple HTML page 
@hftamayo
"""
from flask import Flask

app = Flask(__name__)
@app.route('/', methods = ['GET'])

def home():
    return ('<!DOCTYPE html><html><head><title>What up!</title></head>' +  
    '<body><h1>Hello World!</h1></body></html>')

if __name__=='__main__':
    app.run(port = 7000, debug = True)