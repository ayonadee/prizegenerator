from application import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    account_number = db.Column(db.String(15), nullable=False)
    message = db.Column(db.String(300), nullable=False)