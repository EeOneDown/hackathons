from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    captains_teams = db.relationship('Team', backref='captain', lazy='dynamic')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__set_password(password)

    def __repr__(self):
        return '<User {0} {1}>'.format(self.id, self.email)

    def __set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Hack(db.Model):
    __tablename__ = 'hacks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    place = db.Column(db.String(128), index=True)
    date = db.Column(db.Date, index=True)
    description = db.Column(db.Text)
    link = db.Column(db.String(128))

    def __repr__(self):
        return "<Hackacthon \"{0}\">".format(self.name)


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    captain_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Team {0}>'.format(self.name)
