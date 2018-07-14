import os
import unittest
import run
from run import app
from flask import Flask, url_for, session

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
        
        
        
        
    #run unit tests    
if __name__ == '__main__':
    unittest.main(verbosity = 2)       
