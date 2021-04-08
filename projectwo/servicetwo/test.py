from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
from servicetwo.app import app 

class TestBase(TestCase):
    def create_app(self):
        return app

       
class TestViews(TestBase):
    def test_get_randomnumber(self):
        response = self.client.get(url_for('randomnum'))
        self.assertEqual(response.status_code, 200)

class TestNumber(TestBase):
    with patch('randomnum') as f:
        f.return_value = 1234