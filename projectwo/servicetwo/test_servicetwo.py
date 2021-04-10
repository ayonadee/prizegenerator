from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
from app import app 
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

       
class TestViews(TestBase):
    def test_get_randomnumber(self):
        response = self.client.get(url_for('randomnum'))
        self.assertEqual(response.status_code, 200)

class TestNumber(TestBase):
    def test_len(self):
        response = self.client.get(url_for('randomnum'))
        self.assertEqual(len(response.data), 4)

    def test_number(self):
        with patch('random.randint') as i:
            i.return_value = 1
            response = self.client.get(url_for('randomnum'))
            self.assertIn(b'1111',response.data)
