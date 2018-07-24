This flask web application programme presents a quiz game where you guess the answer to riddles. The rules
and game are very simple. The user is firstly asked to sign in to gain access to the riddle page, which 
can only be viewed by the user during the game. Once signed in, a riddle is presented and the user must 
input a guess in the form field. A correct guess allocates a score of one point and an incorrect guess 
allocates a negative point.
If the guess is correct, a congratulatory message flashes up along with a positive score and the score is
written to a scores file. The next riddle is presented.
If the guess is incorrect, a commiserative message flashes up, which also indicates the answer given, along
with the correct answer. A negative score is also indicated and this score is written to a the scores.txt 
file. As per the brief, the user and the wrong guess is outputted and stored below the riddle form. From 
a historical perspective a date-time stamp is also included. The next riddle is then presented.
A leaderboard holds all the scores for the different users and ranks them in descending order.
This application uses the flask framework and incorporates elements of python,  html, css and javascript. 
The python engine template, Jinja (Jinja2), is also used to create html that can be returned to the 
user via an HTTp response. The logic of the game is written in python, while the other elements enhance 
the look and feel of the game.
Pencil wireframe was used to sketch out a final representation of what was desired in the browser and the
wireframes (pencil1, pencil2 and pencil3) are included in the additional-info folder.
A TDD approach was used to set up the views and routes and establish that the text files were reading and
writing data. A test logic notes file is included in the additional_info folder illustrating the approach
used. The unittest module was used in the test methods. It is noted that if there is no data in the 
text files, then certain tests will fail. During testing it was also noted that each time the unit tests 
were run, message data is added to the scores and messages text files. Tests for the scores files were
re-done using another metod so now there is only blank data added to the message text file. There is a 
message in the test file stating that it should be removed after testing. These messages will be visible
in the wrong guesses table on the user riddle page.
The routes and views were established to allow game related messages to be sent between the urls. The 
messages are stored as strings in a list in text files using append. These are then outputted to the 
browser in the form of a string. In the case of the leader board the data is further analysed to break 
it down into output to a ranked style table. It was decided to have a separate file for users (users.txt), 
one for messages (which stores username, datetime and wrong guess), for output to the user page and a 
scores.txt file to score the users timestamp, and respective scores. This file is further analysed to produce 
another tot_scores.txt file, of users and scores, which is used to create the leaderboard.
