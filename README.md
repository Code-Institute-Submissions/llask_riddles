# Project Name #
flask_riddles
## Overview ##
This flask web application programme presents a quiz game where you guess the answer to riddles. The rules
and game are very simple. The user is firstly asked to sign in to gain access to the riddle page, which 
can only be viewed by the user during the game. Once signed in, a riddle is presented and the user must 
input a guess in the form field. A correct guess allocates a score of one point and an incorrect guess 
allocates a negative point.  
If the guess is correct, a congratulatory message flashes up along with a positive score and the score is
written to a scores file. The next riddle is presented.  
If the guess is incorrect, a commiserative message flashes up, which also indicates the answer given, along
with the correct answer. A negative score is also indicated and this score is written to a the scores.txt 
file.   
As per the brief, the user and the wrong guess is outputted and stored below the riddle form. From a historical
perspective a date-time stamp is also included. The next riddle is then presented.  
A leaderboard holds all the scores for the different users and ranks them in descending order.  
This application uses the flask framework and incorporates elements of python,  html, css and javascript. 
The python engine template, Jinja (Jinja2), is also used to create html that can be returned to the 
user via an HTTP response. The logic of the game is written in python, while the other elements enhance 
the look and feel of the game.  
## UX ##
### Problem Definition ###
In order to fulfill brief requirements the issues to be sorted were defined as:
* Build a web application game that asks players to guess the answer to a pictorial or text-based riddle. 
* Enter the answer into a textarea and submit the answer using a form. 
* After a player answers a riddle, clear the form and redirect the user to the next riddle. 
* If a player guesses incorrectly, store and print their incorrect guess below the riddle
* Provide unique username sign-in functionality so multiple players can play the game at the same time. 
* Provide a leaderboard to rank top scores for all users

User profiles would typically be gaming enthusiasts who thrive on riddle games. They may be logic driven and like 
to solve problems or lateral thinkers who like to think outside the box. They may be teachers who like to use 
riddles to teach. 
The brief is quite specific in requiring the game to be riddle based and thus it is a simple choice of having a 
word based or picrorial format.

### User Stories ###
User stories include:
* As a riddle solver I want to find a site where I can challege myself against like minded users
* As a riddle enthusiast I want to be entertained while I play the online game
* As a riddle enthusiast I want a selection of riddle types to keep me excited
* As a collector of riddles I want to know the answer to riddles that I cannot solve

For the purposes of this application, it was decided to opt for a word based format being simpler in design, less 
demanding on memory space and potentially being more flexible in the scope of questions that can be introduced.  
It is assumed that this was the conclusion arrived at after analysis of the current market, research on current 
trends and on consultation with the client in a real world situation.
### Wireframing ###
Pencil wireframe was used to sketch out a final representation of what was desired in the browser and the
wireframes (pencil1, pencil2 and pencil3) are included in the additional-info folder.

### Design ###
#### Front-end ####
Bright background colours were chosen with strong bold text for headings to give a feel-good and playful ambience 
to the pages. Bootstrap color codes are thematically used. For example correct answers are associated with 
text-success colour (green). Wrong answers are associated with the text-danger colour (red). The riddle questions 
are associated with the text-warning colour (in this case golden road to give more emphasis on the white 
background textarea.) It is akin to a traffic light system red-amber-green. The text-secondary class is used as
placeholder text. The text-primary class is chosen to state the score for a particular riddle. The guess the riddle 
button is the text-info class with white text. The nav bar and header text are strong bold and white. Strong enough 
to be noticed but light enpugh to be subtle. It is the masthead background image that dominates the header section.
A stone wall with a large question mark leaning against it, presenting the imagery 'you will be challenged here'.  
Template inheritance is used on this project, whereby a parent base html page is set up with the background logo, 
navigation bar and footer common to all pages. The main block is left blank, apart from the {% block tags %}, 
which are over-ridden by the main sections in the other child htmls (ie: forms and tables). Although template 
inheritance on an application of this size is not necessary, it is useful to set up the application this way, to 
enable expansion of the application in the future.

#### Back-end ####
The routes and views were established to allow game related messages to be sent between the urls. The messages 
are stored as strings in a list in text files using the append() method. These are then outputted to the browser 
in the form of a string. In the case of the leader board the data is further analysed to break it down into 
output to a ranked style table. It was decided to have a separate file for users (users.txt), one for messages 
(which stores username, datetime and wrong guess), for output to the user page and a scores.txt file, containing 
a timestamp, usernames and respective scores. Another file (tot_scores.txt), containing only username and score 
is created and analysed to create the leaderboard.    
The riddles are read into the form as a dictionary object from a json data file. They are retrieved using the 
request.form object. The lower() method is used to ensure caps or lowercase can be used as input. A riddle counter 
is also incorporated into the form, which cycles through the riddles and is used to exit the game when the final 
riddle is answered. A simple table below the riddle form, stores the wrong answer(date/timestamp, username and 
wrong answer) in string format, which is retrieved from the messages.txt file. This table is only can only br 
viewed while on the user page.   
This version will ask for only one guess, regardless if the answer is right or wrong. It awards a score of +1 
for a right answer and -1 for a wrong answer. The score awarded for a particular answer, is flashed under the 
guess riddle form.     
Comments are displayed throughout the code to explain or describe functions and methods or in the case of html, 
sections. 
## Features ##
The features are described below.
### Existing Features ###
*Feature 1:* Sign-in form: The main block in the home page contains the instructions for playing the game along 
with a form for username sign in. Once signed in the user is directed to a user page, another child html of the 
base html, called answer_riddles.html. The leaderboard can be viewed from the home page.   
*Feature 2:* Riddle form. This is a user game page and is only accessed through sign in. This page comprises a 
text-area form that presents the riddles and asks for an answer. There are links to the home-page and leaderboard
page from the game page but a user will need to sign back in again (or use the browser go back key) to play the 
game.  
*Feature 3:* The leader board page main body contains a link to replay the game and a link to refresh the 
leaderboard, to view ranks, usernames and scores. The leader board table is a bootstrap responsive table, which 
ranks all users  with their score. As with the home page having a link to the leader board page, there is a link 
from the leader board page back to the home page. The play again button redirects a user back to the sign-in page.    
*Feature 4:* User Feedback: The flashing system with categories is used to provide feedback to the user. For 
example if the user gets one right a success banner with a well done message is flashed. If the user gets one 
wrong a danger banner with a hard luck message, along with the right answer is flashed to the user. Finally when 
the last riddle is guessed  an info-banner with a game is over message is flashed. The leader board html is 
rendered at this stage.     
*Feature 5:* Long-polling: Long-polling was added to ensure changes are viewed by all users in real time. It has 
been set to 10secs to allow time to enter data in the form fields.
### Features left to implement ###
There are some limitations to this application in its current state:   
Gaining access only requires a simple username and not a full validation process with username, email and password. 
The lack of secure sign in means that any user can borrow another person's username and alter their score. A 
proper login form with standard authorisation and authentication would sort this out. This is something that can 
be added in the future.     
During testing it was noticed that while on the user page, hitting the back button takes you to the previous 
riddle, effectively giving you an infinite amount of guesses. However the scores are still stored meaning you 
receive a negative score for each guess (an incentive not to do this!). However a positive score is received for
a correct guess, allowing a high score to be built up for the same riddle). This issue can be sorted with future 
development.    
Currently the tot_scores text file is read for each game, meaning that every time a user plays, their score is 
added to the previous tally. Consequently the username only appears once in the leader board with a cumulative 
score (i.e: if a user plays twice and guesses all correctly s/he will have double the score of someone who played 
once and guesses all correctly). This is not necessarily an issue as some users may wish to continue a session. 
However with future development, code could be added to allow users to begin a new session with the same username.  
New riddles can be added very easily to the riddles.json file. As the list expands there is potential to use a 
database, which would allow the riddles to be grouped into categories. A separate children's riddle group could be
introduced.  

## Technologies used ##
[Clean blog theme:](https://startbootstrap.com/)    
A free bootstrap startup theme is used enabling a responsive design approach. Extra styles were added during the 
development phase, to give the pages a game feel. Bright contrasting colors are used and the question mark logo 
image stamps the game theme on each page. Bootstrap classes such as text-center, table-responsive, table-striped 
and so on are used throughout the html pages minimising the need to create css.    
Added css styles deal mainly with background colour, font colour  and size.  
[jQuery:](https://jquery.com/)   
jQuery is included as part of the bootstrap library.    
Some javascript is used to trigger long-polling and to scroll to the riddle answer section in the riddle form.  
[Unittest](https://docs.python.org/3/library/unittest.html)  
The Unit Testing Framework module was used to derive automated tests for the python based functions.  
## Testing ##
A TDD approach was used to set up the views and routes and establish that the text files were reading and writing 
data. A test logic notes file is included in the additional_info folder illustrating the approach used. The 
unittest module was used in the test methods. It is noted that if there is no data in the text files, then 
certain tests will fail. During testing it was also noted that each time the unit tests were run, message data 
is added to the scores and messages text files. Tests for the scores files were re-done using another method so 
now there is only blank data added to the message text file. There is a message in the test file stating that 
it should be removed after testing. These messages will be visible in the wrong guesses table on the user riddle 
page, if not removed.  
It was also noticed during testing that any character entered that did not equate to the answer, was rendered as 
an incorrect answer. However the character “£”  was throwing up a unicode error when entered as an answer, 
effectively ending the game. A solution to this was eventually found while searching for syntax to prevent 
unwanted characters in the input. The solution found on stack overflow, based on the pattern attribute in forms, 
is referenced in the otherCode file the in additional-info folder. The pattern attribute is also used in the 
sign in form, to  ensure a range of name characters are entered.  
The application renders well on chrome, firefox and microsoft edge and all the varying screen sizes.  
Due to the html page set up it was noticed that the riddle form was out of view when another riddle was presented 
and it was becoming increasingly annoying to scroll down to the riddle question. This was overcome by applying 
some script that would auto scroll to the riddle form, when another riddle was presented.

## Deployment ##
The repository for this site is located at https://github.com/vmcggh18/llask_riddles  
The repo can be downloaded as a zip file for installation into a local ide. When installed locally, check 
for any dependencies that need to be installed to run it, by checking the requirements.txt file. Then just 
select the run.py file and click run to view in the browser.      
Alternatively the working application can be viewed at https://flask-riddles.herokuapp.com/  
## Credits ##
### Content ###
The riddles used in this application were adapted from:  
[Do Riddles](http://www.doriddles.com/riddle-175#show)  
[Riddles Brain Teasers](https://riddlesbrainteasers.com/less-see)   
Both sites display riddles submitted by the general public. No terms are dictated for the use of riddles.

### Media ###
The image used in this application is sourced from:  
[Logo Banner](https://pixabay.com/en/question-mark-problem-question-2546106/)    
[Creative Commons License](https://creativecommons.org/publicdomain/zero/1.0/deed.en)  
### Acknowledgments ###
The sources below provided inspiration for this application:
#### Code Institute ####
Code Institute Module 7 Practical Python 
#### Other Documentation Consulted ####
[flask:](http://flask.pocoo.org/)  
[Accept only requested input from user on a form:](https://stackoverflow.com/questions/16434174/only-allow-certain-characters-to-be-entered-in-html-textinput)  
[Sorting tuples in a list:](https://stackoverflow.com/questions/39734549/sum-numbers-by-letter-in-list-of-tuples)  
[Script for scrolling:](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_scrollto2)    
[Unittest Framework](https://docs.python.org/3/library/unittest.html)  
[Flask Message Flashing](http://flask.pocoo.org/docs/0.12/patterns/flashing/)  
[Jinja Template Engine](http://jinja.pocoo.org/)  

