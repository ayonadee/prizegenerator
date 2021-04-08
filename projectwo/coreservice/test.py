from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from coreservice.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

       

class TestViews(TestBase):
    def test_get_homepage(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)