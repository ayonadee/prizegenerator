from unittest.mock import patch
from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
from app import app 
import requests

class TestBase(TestCase):
    def create_app(self):
        return app

       
class TestViews(TestBase):
    def test_get_randomnumberandletter(self):
        response = self.client.get(url_for('prizegenerator'))
        self.assertEqual(response.status_code, 500)


    def test_prizegen(self):
        with patch('requests.get') as i:
            i.return_value.text = "abcd1234"
            response = self.client.get(url_for('prizegenerator'))
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.data)

    # def test_account_number(self):
    #     with patch('requests.post') as g:
    #         g.return_value.text = "a"
    #         response = self.client.post(url_for('prizegenerator'), data = 'a')
    #         self.assertEqual(response.status_code, 200)
    #         self.assertIn(b'package', response.data)
    #         response2 = self.client.post(url_for('prizegenerator'), data = '4')
    #         self.assertEqual(response2.status_code, 200)
    #         self.assertIn(b'package', response2.data)

    # def test_letter(self):
    #     with patch('random.choice') as r:
    #         r.return_value = 'a'
    #         response = self.client.get(url_for('prizegenerator'))
    #         self.assertIn(b'aaaa',response.data)

    # def test_number(self):
    #     with patch('random.randint') as i:
    #         i.return_value = 1
    #         response = self.client.get(url_for('prizegenerator'))
    #         self.assertIn(b'1111',response.data)

    # def test_account_number(self):
    #     with patch('account_number') as g:
    #         g.return_value = 'abcd1234'
    #         response = self.client.get(url_for('prizegenerator'))
    #         self.assertIn(b'abcd1234', response.data)

