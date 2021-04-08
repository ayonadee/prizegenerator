from unittest.mock import patch
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
from servicefour.app import app 
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

       
class TestViews(TestBase):
    def test_get_randomnumber(self):
        response = self.client.get(url_for('prizegenerator'))
        self.assertEqual(response.status_code, 200)

    def test_number(self):
        with patch('requests.get') as g:
            g.return_value.text = 1234
            response = self.client.get(url_for('prizegenerator'))
            self.assertIn(b'4', response.data)

    def test_letter(self):
        with patch('requests.get') as l:
            g.return_value.text = abcd
            response = self.client.get(url_for('prizegenerator'))
            self.assertIn(b'a', response.data)

    def test_account_number(self):
        with patch('requests.get') as l:
            g.return_value.text = abcd1234
            response = self.client.get(url_for('prizegenerator'))
            self.assertIn(b'a', response.data)

