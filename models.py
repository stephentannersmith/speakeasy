
from flask import flash
from sqlalchemy.sql import func
from config import db, bcrypt
from sqlalchemy import text
from flask_migrate import Migrate
import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# - Users Table:
#     - OAuth UserID

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.BOOLEAN, default = False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    passwordHash = db.Column(db.String(255))    #only for non-facebook users
    creator_name = db.Column(db.String(255))
    # oauth_link = db.Column(db.String(255))    #link to OAuth UserID
    earnings_tips = db.Column(db.Float, default = 0.00)
    earnings_donations = db.Column(db.Float, default = 0.00)
    earnings_watcher_seconds = db.Column(db.Float, default = 0.00)
    description = db.Column(db.Text, default = "About Me...")
    user_image = db.Column(db.String(255), default = "blank_profile.png")  #retrieve from OAuth Facebook Picture, default will be path to default avatar
    stream = db.relationship("Streams", uselist = False, backref = "creator")
    videos = db.relationship("Videos", backref = "creator")
    fb_user_id = db.relationship("FBUsers", uselist = False, backref = "user")
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return "UserID: " + str(self.id) + " Name: " + self.first_name + " " + self.last_name

    @classmethod
    def add_new_user(cls, user_data):
        hashed_password = bcrypt.generate_password_hash(user_data['password'])
        new_user = cls(first_name=user_data['first_name'], last_name=user_data['last_name'], email=user_data['email'], passwordHash=hashed_password)
        db.session.add(new_user)
        print("adding new user...")
        print(new_user)
        db.session.commit()
        return new_user
    
    @classmethod
    def validate_user(cls, user_data):
        is_valid = True
        if len(user_data["first_name"]) < 1:
            is_valid = False
            flash("Please provide a first name", "reg_error")
        if len(user_data["last_name"]) < 1:
            is_valid = False
            flash("Please provide a last name", "reg_error")
        if not EMAIL_REGEX.match(user_data["email"]):
            is_valid = False
            flash("Please provide a valid email", "reg_error" )
        if len(user_data["password"]) < 8:
            is_valid = False
            flash("Password should be at least 8 characters", "reg_error")
        if user_data["password"] != user_data["cpassword"]:
            is_valid = False
            flash("Passwords do not match", "reg_error")
        return is_valid

class FBUsers(db.Model):
    __tablename__ = "FBUsers"
    id = db.Column(db.Integer, primary_key=True)
    oauth_user_id = db.Column(db.Integer) #this will be populated by Oauth userID
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete="cascade"))



class Videos(db.Model):
    __tablename__ = "Videos"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), default = "My Video")
    video_link = db.Column(db.String(255)) #url of video from whatever platform used
    num_times_watched = db.Column(db.Integer, default = 0)
    earnings_tips = db.Column(db.Float, default = 0.00)
    earnings_donations = db.Column(db.Float, default = 0.00)
    description = db.Column(db.Text)
    video_author_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete="cascade"))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


    def __repr__(self):
        return "VideoID: " + self.id + " video_author_id: " + self.video_author_id

class Streams(db.Model):
    __tablename__ = "Streams"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), default = "My Stream")
    stream_link = db.Column(db.String(255)) #the link to the stream from whatever platform we use
    num_current_watchers = db.Column(db.Integer, default = 0)
    num_total_watchers = db.Column(db.Integer, default = 0)
    earnings_tips = db.Column(db.Float, default = 0.00)
    earnings_donations = db.Column(db.Float, default = 0.00)
    earnings_watcher_seconds = db.Column(db.Float, default = 0.00) #how much money earned from the seconds of all watchers combined
    amount_watcher_seconds = db.Column(db.Time, default = 0) #number of seconds that all watchers combined have spent on this stream
    description = db.Column(db.Text)
    time_running = db.Column(db.Time)
    stream_author_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete="cascade"))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return "StreamID: " + self.id + " stream_author_id: " + self.stream_author_id


































