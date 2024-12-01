from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

def add_user(name):
    user = UserModel(name=name)
    db.session.add(user)
    db.session.commit()
