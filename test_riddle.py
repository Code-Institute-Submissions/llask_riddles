import os
import unittest
import run
from run import app
from flask import Flask, url_for, session

class test_run(unittest.TestCase):
    """
    Test suite for riddle quiz
    """
    #can establish routes
    def test_index(self):
        index = app.test_client(self)
        response = index.get('/',content_type = 'html/text')
        self.assertEqual(response.status_code, 200)
        
        
        
        
        
    #run unit tests    
if __name__ == '__main__':
    unittest.main(verbosity = 2)       
