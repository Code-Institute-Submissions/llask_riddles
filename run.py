#import various modules and files that provide functionality to the programme
import os
from datetime import datetime
import json
from flask import Flask, redirect, render_template, request, flash, url_for, session, jsonify

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    
    return"<h1>Hello World!</h1>"
    
    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get('PORT', 0)), debug=True)

    