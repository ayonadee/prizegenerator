from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import db, app, models
from app import app
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///',
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            # WTF_CSRF_ENABLED=False
            )
        return app

    def setUp(self):
            """
            Will be called before every test
            """
            # Create table
            
            db.create_all()

            testuser = models.Users(first_name= "Ayona", last_name= "Duncan", account_number= '1234abcd', message= 'hello')
            db.session.add(testuser)
            # save users to database
            db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()

       
class TestViews(TestBase):
    def test_home(self):
        with requests_mock.mock() as m:
            m.get("http://servicefour:5003/prizegenerator", json='package')
            response = self.client.get(url_for('home'))
# hello
