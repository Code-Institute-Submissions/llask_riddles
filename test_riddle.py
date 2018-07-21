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
    def test_for_leader_board_html(self):
        leader_board_html = app.test_client(self)
        response = leader_board_html.get('/leader_board',content_type = 'html/text')
        self.assertIn("Play Again", response.data)
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
   
    # def test_check_tot_scores_file_is_storing_scores(self):
    #     data = run.tot_scores("bob", "1")
    #     self.assertIn("1", str(data))    
        
        
        
        
        
        
        
    # def test_check_message_file_is_storing_wrong_guesses(self):
    #     wrongGuess = run.get_all_messages()
    #     self.assertGreater(len(wrongGuess), 0)
     #alternatively use test below 
    # def test_check_message_file_is_storing_wrong_guesses(self):
    #     with open("data/messages.txt", "r") as file:
    #         wrongGuess = file.read().splitlines()
    #         self.assertGreater(len(wrongGuess), 0)
    #     #alternatively use test below to prevent data being added
    
        
        
        
        
        
        
     # def test_check_tot_scores_file_is_storing_scores(self):
    #     with open("data/tot_scores.txt", "r") as file:
    #         lines = file.read().splitlines()
            #  self.assertIn(str(1), lines )
    #       
            # def test_guess_right(self):
    #     guess = run.user(self)
    #     self.assertEqual(guess(), '56')

if __name__ == '__main__':
    unittest.main(verbosity = 2)       

