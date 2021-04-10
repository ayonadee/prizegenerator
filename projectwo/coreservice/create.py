from app import db
from application import models 


db.drop_all()
db.create_all()

# testuser = models.Users(first_name= "Ayona", last_name= "Duncan", account_number= "", message= "")
# db.session.add(testuser)
# db.session.commit()