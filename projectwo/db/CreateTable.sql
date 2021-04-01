from application import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    email_address = db.Column(db.String(50),nullable=True)


db.drop_all()
db.create_all()

testuser = models.Users(first_name= "Ayona", last_name= "Duncan", email_address: "aydunc@yahoo.com")
db.session.add(testuser)
db.session.commit()
