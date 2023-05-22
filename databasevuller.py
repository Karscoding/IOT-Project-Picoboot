import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#operating system path
basedir = os.path.abspath(os.path.dirname(__file__))

#flask configureren
app = Flask("Dashboard")
app.config['SECRET_KEY']='shbfijsbdhsbdsdffggdghkjhgfhvj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Gegevens.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#connection to database
db=SQLAlchemy(app)

#tabellen aanmaken
class Afstand(db.Model):
    __tablename__ = 'Afstand'
    id=db.Column(db.Integer,primary_key=True)
    tijd = db.Column(db.Text)
    afstand = db.Column(db.Integer)

    def __init__(self,id,tijd,afstand):
        self.id=id
        self.tijd = tijd
        self.afstand=afstand

class Temperatuur(db.Model):
    __tablename__ = 'Temperatuur'
    id=db.Column(db.Integer,primary_key=True)
    tijd = db.Column(db.Text)
    temperatuur = db.Column(db.Float)

    def __init__(self,id,tijd,temperatuur):
        self.id=id
        self.tijd = tijd
        self.temperatuur = temperatuur


#runnen
if __name__=='__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()