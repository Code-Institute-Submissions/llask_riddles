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
re-done using another method so now there is only blank data added to the message text file. There is a 
message in the test file stating that it should be removed after testing. These messages will be visible
in the wrong guesses table on the user riddle page, if not removed.
The routes and views were established to allow game related messages to be sent between the urls. The 
messages are stored as strings in a list in text files using append. These are then outputted to the 
browser in the form of a string. In the case of the leader board the data is further analysed to break 
it down into output to a ranked style table. It was decided to have a separate file for users (users.txt), 
one for messages (which stores username, datetime and wrong guess), for output to the user page and a 
scores.txt file, containing a timestamp, usernames and respective scores. Another file (tot_scores.txt), 
containing only username and score is created and analysed to create the leaderboard.
Comments are displayed throughout the code to explain or describe functions and methods or in the case of html, sections. 
Template inheritance is used on this project, whereby a parent base html page is set up with 
the background logo, navigation bar and footer common to all pages. The main block is  left 
blank, apart from the {% block tags %}, which are over-ridden by the main sections in the 
other child htmls (ie: forms and tables). Although template inheritance on an application of 
this size is not necessary, it is useful to set up the application this way, to enable 
expansion of the application in the future.
The main block in the home page contains the instructions for playing the game along with a 
form for username sign in. Once signed in the user is directed to a user page, another child 
html of the base html, called answer_riddles.html.  This is a user page and is only accessed 
through sign in. This page comprises a text-area form that presents the riddles and asks for 
an answer. The riddles are read into the form as a dictionary object from a json data file. 
They are retrieved using the request.form object. A riddle counter is also incorporated into 
the form, which cycles through the riddles and is used to exit the game when the final riddle 
is answered. A simple table below the riddle form, stores the wrong answer(date/timestamp, 
username and wrong answer) in string format, which is retrieved from the messages.txt file. 
Again this table is unique to users and is only viewed while on the user page.
This version will ask for only one guess, regardless if the answer is right or wrong. 
It awards a score of +1 for a right answer and -1 for a wrong answer. The score awarded for 
a particular answer, is flashed under the guess riddle form. The flashing system with 
categories is used to provide feedback to the user. For example if the user gets one right 
a success banner with a well done message is flashed. If the user gets one wrong a danger 
banner with a hard luck message, along with the right answer is flashed to the user. Finally 
when the last riddle is guessed  an info-banner with a game is over message is flashed. The 
leader board html is rendered at this stage.
Due to the html page set up it was noticed that the riddle form was out of view when another 
riddle was presented and it was becoming increasingly annoying to scroll down to the riddle 
question. This was overcome by applying some script that would auto scroll to the riddle form, 
when another riddle was presented.(script for this adopted from w3schools.com; see otherCode 
file in the additional_info folder.).
The leader board page main body contains a link to replay the game and a link to display the 
leaderboard, to view ranks and scores. The leader board table is a bootstrap responsive table, 
which ranks all users  with their score. As with the home page having a link to the leader 
board page, there is a link from the leader board page back to the home page. Code was 
adopted from stack overflow to sort a list of tuples by rank and is included in the otherCode 
file in the additional_info folder. 
A free bootstrap startup theme is used enabling a responsive design approach. The browser 
renders well on chrome, firefox and microsoft edge and all the varying screen sizes.  Extra 
styles were added during the development phase, to give the pages a game feel. Bright 
contrasting colors are used and the question mark logo image (borrowed from  pixabay; 
https://pixabay.com/en/service /terms/#usage;  https://creativecommons.org/publicdomain/zero/1.0/deed.en), 
stamps the game theme on each page. The riddles are presented with an amber text colour
(GoldenRod) with the bootstrap themes of success, warning and info then used to convey right, 
wrong and game over. Bootstrap classes such as text-center, table-responsive, table-striped 
and so on are used throughout the html pages minimising the need to create css.  Added css 
styles deal mainly with background colour, font colour  and size.
Long-polling was added to ensure changes are viewed by all in real time. It has been set to 
10secs to allow time to enter data in the form fields. It may irritate some users, particularly 
at the point of inputting data and other ways to address this could be considered with future 
development.
There are some limitations to this application in its current state. Gaining access only 
requires a simple username and not a full validation process with username, email and 
password. The lack of secure sign in,  means that any user can borrow another person's 
username and alter their score. A proper login form with password would sort this out. This 
is something that can be added in the future. During testing it was noticed that while on 
the user page, hitting the back button takes you to the previous riddle, effectively giving 
you an infinite amount of guesses. However the scores are still stored meaning you receive a 
negative score for each guess (an incentive not to do this!). However a positive score is 
received for a correct guess, allowing a high score to be built up for the same riddle). This 
issue can be sorted with future development. Currently the tot_scores text file is read for 
each game, meaning that every time a user plays, their score is added to the previous tally. 
Consequently the username only appears once in the leader board with a cumulative score (i.e: 
if a user plays twice and guesses all correctly s/he will have double the score of someone 
who played once and guesses all correctly). For the purposes of this brief this is not an 
issue. However this could be sorted in the future by calculating an average score based on 
number of games played,  or by changing the code to ensure each game played is unique regardless 
of user, if this is required.
It was also noticed during testing that any character entered that did not equate to the 
answer, was rendered as an incorrect answer. However the character “£”  was throwing up a 
unicode error when entered as an answer, effectively ending the game. A solution to this was 
eventually found while searching for syntax to prevent unwanted characters in the input. The 
solution found on stack overflow, based on the pattern attribute in forms, is referenced in 
the otherCode file the in additional-info folder. The pattern attribute is also used in the 
sign in form, to  ensure a range of name characters are entered.
The riddles used in this application were adapted from http://www.doriddles.com/riddle-175#show  
Do Riddles site and https://riddlesbrainteasers.com/less-see/ Riddles Brain Teasers site, 
both of which display riddles submitted by the general public. No terms were dictated for 
the use of riddles.