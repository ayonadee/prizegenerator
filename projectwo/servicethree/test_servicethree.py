from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app 
import requests


class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):
    def test_get_randomletter(self):
        response = self.client.get(url_for('randomletter'))
        self.assertEqual(response.status_code, 200)

class TestLetter(TestBase):
    def test_len(self):
        response = self.client.get(url_for('randomletter'))
        self.assertEqual(len(response.data), 2)
    

    def test_letter(self):
        with patch('random.choice') as r:
            r.return_value = 'A'
            response = self.client.get(url_for('randomletter'))
            self.assertIn(b'AA',response.data)