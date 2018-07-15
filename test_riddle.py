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
    def test_user_page(self):
        user = app.test_client(self)
        response = user.get('/<username>', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)
    def test_message_can_be_sent(self):
        message = app.test_client(self)
        response = message.get('/<username>/<message>', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)  
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
   
if __name__ == '__main__':
    unittest.main(verbosity = 2)       

# @app.route('/post/')
# def new_post(self):
#   if storage.create_post(request.form['post']):
#     flash(u'Post added')
#     return redirect(url_for('home'))
#   return render_template('new-post.html')
#   def should_flash_a_success_message(self):
#   response = self.client.post('/post/', data=self.valid_post_data,
#                               follow_redirects=True)

#   assert 'Post added' in response.data