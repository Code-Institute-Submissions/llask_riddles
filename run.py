#import various modules and files that provide functionality to the programme
import os
from datetime import datetime
import json
from flask import Flask, redirect, render_template, request, flash, url_for, session, jsonify

app = Flask(__name__)
#5 append messages
# def add_messages(username, message):
#     messages.append ("{0}: {1}\n".format(username, message))



@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")
    
    
    
@app.route('/leader_board', methods=["GET", "POST"])
def leader_board():
    return render_template("leader_board.html")
    
 
@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    return username
 
@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}\n".format(username, message)
 
   
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get('PORT', 0)), debug=True)

    