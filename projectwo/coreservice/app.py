from flask import Flask, render_template,request, url_for, jsonify, Response
from application import app, models, db
import random as rand
import string
import requests
from sqlalchemy import desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from os import getenv


class UserForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Submit New User')
    

@app.route('/home', methods = ['GET', 'POST'])
@app.route('/',methods = ['GET', 'POST'])
def home():
    form = UserForm()
    acc_num = requests.get("http://servicefour:5003/prizegenerator").json()
    if(request.method=='POST'):
        first_name = form.first_name.data
        last_name = form.last_name.data
        new_user = models.Users(first_name = form.first_name.data, last_name =form.last_name.data, account_number = acc_num['Account_Number'] , message = acc_num['Message'] )
        db.session.add(new_user)
        db.session.commit()
    users = models.Users.query.order_by(desc("id")).limit(4).all()
    return render_template('home.html',form = form, users=users)
    
   

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)