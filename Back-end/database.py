#!/usr/bin/python3
"""Contains the MongoDB database class"""
from mongoengine import Document, StringField
from flask_bcrypt import Bcrypt
from bson import ObjectId
from flask_login import UserMixin
from api.v1.app import app, load_user


bcrypt = Bcrypt(app)

class UserInfo(Document, UserMixin):
    """Sets the details of the user"""
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True, unique=True)
    authed = False
    meta = {"collection": "Users"}

    def add_to_coll(self):
        """Adds the document to the proper collection"""
        try:
            self.save()
        except Exception as error:
            failed = {
                      "Status": "Unsuccessful",
                      "Error": str(error)
                      }
            return failed

    @classmethod
    def find_by_id(cls, id) -> UserInfo:
        """Find a user using the id created by the database"""
        found = cls.objects(id=ObjectId(id)).first()
        return found

    def user_modfy(self, id, **kwargs):
        """Update the information of a user"""
        user = self.find_by_id(id)
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()

    def delete_by_id(self, id):
        """Delete a user by their ID"""
        UserInfo.objects(id=ObjectId(id)).delete()

    def hash_password(self):
        """Hashes the password"""
        self.password = (bcrypt.generate_password_hash(self.password)
                         .decode('utf-8'))

    def is_password(self, password) -> bool:
        """Matches the hased password with the normal one"""
        return bcrypt.check_password_hash(self.password, password)

    def is_authenticated(self) -> bool:
        """Returns a boolen to indicate whether a user is loged in or not"""
        return self.authed

    def is_active(self):
        """
        Retuens a boolen to indicate is user is still active.
        More logic to deactivate user is to come.
        """
        return True

    def get_id(self):
        return str(self.id)

    def to_json(self):
        """Returns the json version of data inside object"""
        return {
                "username": self.username,
                "email": self.email,
                "db ID": str(self.id)
                }
