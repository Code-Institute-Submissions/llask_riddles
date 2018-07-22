#import various modules that provide functionality to the programme
import os
from datetime import datetime
import json
from flask import Flask, redirect, render_template, request, flash, url_for, session, jsonify
from operator import itemgetter, attrgetter

app = Flask(__name__)
app.secret_key = 'some_secret'
data = []

def write_to_file(filename, data):
    """Handle the process of writing data to a file using writelines method"""
    with open(filename, "a") as file:
            file.writelines(data)
        
def add_messages(username, message):
    """Add wrong guesses to the messages text file"""
    #add a date/timestamp to maintain an historical record
    write_to_file("data/messages.txt", "({0}) {1} - {2}".format(
            datetime.now().strftime("(%Y-%m-%d)(%H:%M:%S)"),
            username.title(),
            message))
            
def get_all_messages():
    """Get all of the messages for routing to the answer riddle page"""
    messages = []
    with open("data/messages.txt", "r") as game_messages:
        messages = game_messages.readlines()
    return messages
    
def add_scores(score):
    """ Add scores with timestamp to the scores.text file to maintain an overall user score record"""
    write_to_file("data/scores.txt", " - {0} - {1}\n".format(
        datetime.now().strftime("(%Y-%m-%d)(%H:%M:%S)"),
            score))
    """  Add usernames and scores to the tot_scores.text file for routing to the leaderboard"""
def tot_scores(username, score):
    with open("data/tot_scores.txt", "a") as file:
        file.writelines(str(username) + "\n")
        file.writelines(str(score) + "\n")
            
def get_scores():
    usernames = []
    scores = []
    """ Open the tot_scores.txt file and split each line"""
    with open("data/tot_scores.txt", "r") as file:
        lines = file.read().splitlines()
    for i, text in enumerate(lines):
        # Add the usernames (on even lines) to the empty score list
        if i % 2 ==0:
            usernames.append(text)
        else:
            # Add the scores (on odd lines) to the empty username list
            scores.append(text)
    """ Zip the two lists into a tuple, convert into a dictionary for grouping by key,
    sum the values by username and sort into highset first"""
    userScores = zip(usernames, scores)
    dict = {x:0 for x,_ in userScores}
    for username, score in userScores: 
        dict[username] += int(score)
        result = map(tuple, dict.items())
    sorted_by_value = sorted(result,key=itemgetter(1), reverse=True)
    return sorted_by_value

@app.route('/', methods=["GET", "POST"])
def index():
    """Home page with sign in and game instructions"""
    # Handle POST request
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        #redirect user to their homepage
        return redirect(request.form["username"])
    return render_template("index.html")

@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    """Display riddles for the user and post data to text files"""
    data = []
    with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
    #set up variables used
    riddle_counter = 0
    #the total riddles variable will also be used to end the game
    total_riddles = len(data)
    numRight = 0
    numWrong = 0
    score = 0
    if request.method == "POST":
        write_to_file("data/users.txt", username + "\n")
        # use a counter to pass in the riddles into the text-area; the counter will also be used to end the game
        riddle_counter = int(request.form["riddle_counter"])
        # get the input from the user. Use lower method to format strings with capitals to lowercase
        guess = request.form["message"].lower()
        # Compare the guess with actual answer
        if data[riddle_counter]["answer"] == guess:
            numRight += 1 
            score = numRight
            # with correct answer flash a message and continue to next riddle
            if request.method == "POST":
                flash("Well Done! You got that one correct", 'alert alert-success')
        else:
            # with incorrect answer log the wrong guess and flash a message
            add_messages(username, guess + "\n")
            numWrong -= 1 
            score = numWrong
            if request.method == "POST":
                flash("Oh Dear! You got that one wrong.You guessed {}: the answer is {}".format(
                    request.form["message"], data[riddle_counter]["answer"]), 'alert alert-danger')
        riddle_counter += 1
        score = score
        write_to_file("data/scores.txt", username)
        add_scores(score)
        tot_scores(username, score)
        #exit from the game on completion
        if request.method == "POST":
            if riddle_counter == total_riddles:
                flash("Game Over! That brings us to the end of this session of riddles. Thank you for playing.", "alert alert-info")
                return render_template("leader_board.html")
    messages = get_all_messages()
    return render_template("answer_riddles.html", scroll = "return_here",
                            username=username, game_messages=messages, riddles_data=data, riddle_counter=riddle_counter, score=score) 

@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the game page"""
    add_messages(username, message)
    return redirect(username)
    
@app.route('/leaderboard')
def leader_board():
    sorted_by_value = get_scores()
    return render_template("leader_board.html", sorted_by_value=sorted_by_value)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get('PORT', 0)), debug=True)

    