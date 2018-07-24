# -*- coding: utf-8 -*
import os
import unittest
import json
import run
from run import app
from flask import Flask, url_for, request

class test_run(unittest.TestCase):
    """
    Test suite for riddle quiz
    """
    #return a flask instance
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app
        
    #can establish routes
    def test_index(self):
        index = app.test_client(self)
        response = index.get('/',content_type = 'html/text')
        self.assertEqual(response.status_code, 200)
    def test_leader_board(self):
        leader_board = app.test_client(self)
        response = leader_board.get('/leader_board',content_type = 'html/text')
        self.assertEqual(response.status_code, 200)  
    def test_user_page(self):
        user = app.test_client(self)
        response = user.get('/<username>', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)
        """THIS TEST ADDS BLANK MESSAGE(S) TO THE LAST LINE OF THE MESSAGES
        TEXT FILE WHICH NEED(S) TO BE REMOVED AFTER THE TEST(S) ARE COMPLETED"""
    def test_message_can_be_sent(self):
        message = app.test_client(self)
        response = message.get('/<username>/<message>', content_type = 'html/text')
        self.assertEqual(response.status_code, 302)  
    #test that html pages are rendered
    def test_for_base_html(self):
        base = app.test_client(self)
        response = base.get('/',content_type = 'html/text')
        self.assertIn("Home", response.data)
    def test_for_index_html(self):
        index = app.test_client(self)
        response = index.get('/',content_type = 'html/text')
        self.assertIn("Riddle Me This", response.data)
        #test that riddle page loads
    def test_riddle_page(self):
        riddle_page = app.test_client(self)
        response = riddle_page.get('/<username>', content_type = 'html/text')
        self.assertIn('Welcome', response.data)
        #test users text file takes data this fails if the file is empty
    def test_check_user_file_is_storing_username(self):
        with open("data/users.txt", "r") as file:
            lines = file.read().splitlines()
            self.assertGreater(len(lines), 0)
    def test_data_file_loads(self):
        with open("data/riddles.json", "r") as json_data:
            data = json.load(json_data)
        self.assertGreater(len(data), 0)
     #test that riddle form loads
    def test_riddle_form(self):
        riddle_form = app.test_client(self)
        response = riddle_form.get('/<username>', content_type = 'html/text')
        self.assertIn("Write guess here", response.data)
        #test that counter works
    def test_riddle_counter(self):
        riddle_counter = app.test_client(self)
        self.assertGreaterEqual(riddle_counter, 0)
        # test that text files are functioning
    def test_check_data_is_in_scores_file(self):
        with open("data/scores.txt", "r") as file:
            score = file.read().splitlines()
            self.assertIn("1", (str(score)))
    def test_check_data_is_in_tot_scores_file(self):
        with open("data/tot_scores.txt", "r") as file:
            score = file.read().splitlines()
            self.assertIn("1", (str(score)))
        #check that data is loaded to leader board. this also verifys that
        #the leaderboard html page loads
    def test_check_data_is_in_leaderBoard(self):
        score = run.get_scores()
        self.assertIn(("a"),(str(score)))
        #test that riddles and answers are correct
    def test_riddle_has_correct_answer(self):
        data = []
        riddle_counter = 0
        with open("data/riddles.json", "r") as json_data:
            data = json.load(json_data)
        riddle1 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('Fill in the missing number: Give the answer as a number (for example 24): 46  65  84  ??  28 ', '56'), riddle1)
        riddle_counter +=1
        riddle2 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('What number does not fit: Give the answer as a number (for example 24): 16  25   4   32   81', '32'), riddle2)
        riddle_counter +=1
        riddle3 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('12 kids at a party. 6 have shoes on and 4 have socks. 3 have both shoes and socks. How many are barefoot: Give the answer as a number (for example 24)', '5'), riddle3)
        riddle_counter +=1
        riddle4 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('I have 12 pairs of gloves in a drawer. 6 are black and  6 are brown. In the dark how many gloves must I take out  to ensure I have a matching pair?: Give the answer as a number (for example 24)', '13'), riddle4)
        riddle_counter +=1
        riddle5 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('What number when trebled remains the same when doubled?: Give the answer as a number (for example 24)', '0'), riddle5)
        riddle_counter +=1
        riddle6 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('I am 4 times older than my daughter now and in 20 years will be twice her age. How old am I?: Give the answer as a number (for example 24)', '40'), riddle6)
        riddle_counter +=1
        riddle7 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('I can be smooth as silk when you touch me. Yet hard as rock when you hit me. I can be crystal clear or dark as pitch. I can be still and silent, or I can rumble and roar. What am I ? (The answer to this one is a single word)', 'water'), riddle7)
        riddle_counter +=1
        riddle8 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('What is black when bought, red when used and grey when thrown away?: (The answer to this one is a single word)', 'charcoal'), riddle8)
        riddle_counter +=1
        riddle9 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('Name the most recent year that was the same upside down?(Write this answer in date format (for example 1984))', '1961'), riddle9)
        riddle_counter +=1
        riddle10 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('Mr. Smith has 4 daughters. Each of his daughters has a brother. How many children does Mr. Smith have?: Give the answer as a number (for example 24)', '5'), riddle10)
        riddle_counter +=1
        riddle11 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('I am 90cm + half my height. How tall am I? Write this answer in number format (for example 120cm))', '180cm'), riddle11)
        riddle_counter +=1
        riddle12 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('When Tom asked Mary how old she was. She replied that in two years she would be twice as old as she was five years ago. How old is Mary?: Give the answer as a number (for example 24)', '14'), riddle12)
        riddle_counter +=1
        riddle13 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('What number gives 240 when added to its own square (choose between fifteen. Sixteen. Eighteen and twenty)?: Give the answer as a number (for example 24)', '15'), riddle13)
        riddle_counter +=1
        riddle14 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('I am an odd number. If you take away one of the letters in my name, I become even. What number am I?: Give the answer as a number (for example 24)', '7'), riddle14)
        riddle_counter +=1
        riddle15 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('How many cats can one get into an empty box? : Give the answer as a number (for example 24)', '1'), riddle15)
        riddle_counter +=1
        riddle16 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('How far can a fox run into a forest? : (The answer to this one is a single word)', 'halfway'), riddle16)
        riddle_counter +=1
        riddle17 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('What kind of cheese is made backwards? : (The answer to this one is a single word)', 'edam'), riddle17)
        riddle_counter +=1
        riddle18 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('What five-letter word becomes shorter when you add two letters to it? : (The answer to this one is a single word)', 'short'), riddle18)
        riddle_counter +=1
        riddle19 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('Poor people have it. Rich people need it. If you eat it, you will die. What is it?: (The answer to this one is a single word)', 'nothing'), riddle19)
        riddle_counter +=1
        riddle20 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('2 fathers and two sons had sausages for breakfast. The cook made a total of nine sausages for the party. Each ate the same amount. How many did each have?: Give the answer as a number (for example 24)', '3'), riddle20)
        riddle_counter +=1
        riddle21 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('I have selected a number between 1 and 10. I double it and multiply the answer by 5. I then divide this number by my original number and subtract 7 from the answer. What is my final number?: Give the answer as a number (for example 24)', '3'), riddle21)
        riddle_counter +=1
        riddle22 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('Name an 11 letter word that is always spelled incorrectly?: (The answer to this one is a single word)', 'incorrectly'), riddle22)
        riddle_counter +=1
        riddle23 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('What word when pronounced right is wrong and when pronounced wrong is right?: (The answer to this one is a single word)', 'wrong'), riddle23)
        riddle_counter +=1
        riddle24 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('What is so fragile that when you say its name, it breaks?: (The answer to this one is a single word)', 'silence'), riddle24)
        riddle_counter +=1
        riddle25 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('What is full of holes, but still holds water?: (The answer to this one is a single word)', 'sponge'), riddle25)
        riddle_counter +=1
        riddle26 = (data[riddle_counter]["riddle"], data[riddle_counter]["answer"])
        self.assertEqual(('What is the next number in this sequence: 1, 3, 5, ?, Give the answer as a number (for example 24)', '4'), riddle26)

if __name__ == '__main__':
    unittest.main(verbosity = 2)       

