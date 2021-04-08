from unittest.mock import patch
from flask_testing import TestCase
from servicethree.app import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):
    def test_get_randomnumber(self):
        response = self.client.get(url_for('randomnum'))
        self.assertEqual(response.status_code, 200)

class TestLetter(TestBase):
    with patch('randomletter') as a:
        a.return_value = abcd