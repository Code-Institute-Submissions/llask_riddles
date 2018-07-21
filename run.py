#import various modules and files that provide functionality to the programme
import os
from datetime import datetime
import json
from flask import Flask, redirect, render_template, request, flash, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'some_secret'
data = []

def write_to_file(filename, data):
    """Handle the process of writing data to a file using writelines method"""
    with open(filename, "a") as file:
            file.writelines(data)
        
def add_messages(username, message):
    """Add messages to the messages text file"""
    #add a date/timestamp and separate them with a line break
    write_to_file("data/messages.txt", "({0}) {1} - {2}\n".format(
            datetime.now().strftime("(%Y-%m-%d)(%H:%M:%S)"),
            username.title(),
            message))
            
def get_all_messages():
    """Get all of the messages"""
    messages = []
    with open("data/messages.txt", "r") as game_messages:
        messages = game_messages.readlines()
    return messages
    
def add_scores(score):
    """  Add scores to the `scores` text file"""
    write_to_file("data/scores.txt", " - {0} - {1}\n".format(
        datetime.now().strftime("(%Y-%m-%d)(%H:%M:%S)"),
            score))
    
def tot_scores(username, score):
        with open("data/tot_scores.txt", "a") as file:
            file.writelines(str(username) + "\n")
            file.writelines(str(score) + "\n")


@app.route('/', methods=["GET", "POST"])
def index():
    """7 Main page with instructions"""
    # Handle POST request
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        #redirect user to their homepage
        return redirect(request.form["username"])
    return render_template("index.html")

@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    """Display chat messages for the user"""
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    riddle_counter = 0
    total_riddles = len(data)
    numRight = 0
    numWrong = 0
    score = 0
    if request.method == "POST":
        write_to_file("data/users.txt", username + "\n")
        # use a counter to pass in the riddles into the text-area
        riddle_counter = int(request.form["riddle_counter"])
        # get the input from the user. Use lower method to format strings with capitals to lowercase
        guess = request.form["message"].lower()
        # Compare the guess with actual answer
        if data[riddle_counter]["answer"] == guess:
            numRight += 1 
            # with correct answer flash a message and continue to next riddle
            if request.method == "POST":
                flash("Well Done! You got that one correct", 'alert alert-success')
            #riddle_counter += 1
        else:
            # with incorrect answer log the wrong guess and flash a message
            add_messages(username, guess + "\n")
            numWrong -= 1 
            if request.method == "POST":
                flash("Oh Dear! You got that one wrong.You guessed {}, the answer is {}".format(
                    request.form["message"], data[riddle_counter]["answer"]), 'alert alert-danger')
        riddle_counter += 1
        score = (numRight + numWrong)
        write_to_file("data/scores.txt", username)
        add_scores(score)
        tot_scores(username, score)
        #exit from the game on completion
        if request.method == "POST":
            if riddle_counter == total_riddles:
                flash("Game Over! That brings us to the end of this session of riddles. Thank you for playing.", "alert alert-info")
                return render_template("leader_board.html")
    messages = get_all_messages()
    return render_template("answer_riddles.html",
                            username=username, game_messages=messages, riddles_data=data, riddle_counter=riddle_counter, score=score) 

@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the game page"""
    add_messages(username, message)
    return redirect(username)
    
@app.route('/leader_board', methods=["GET", "POST"])
def leader_board():
    return render_template("leader_board.html")
# def widget(length,width):
#     length =50
#     width = 50
   
if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get('PORT', 0)), debug=True)

    