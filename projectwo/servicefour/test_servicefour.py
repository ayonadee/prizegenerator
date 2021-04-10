from unittest.mock import patch
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
from app import app 
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

       
class TestViews(TestBase):

    def test_prizegen(self):
        with patch('requests.get') as i:
            i.return_value.text = "abcd1234"
            response = self.client.get(url_for('prizegenerator'))
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.data)


    def test_prizegenerator(self):
        with requests_mock.mock() as m:
            m.get('http://servicethree:5002/randomletter', text='a')
            m.get('http://servicetwo:5001/randomnum', text= '4')
            response = self.client.get(url_for('prizegenerator'))


