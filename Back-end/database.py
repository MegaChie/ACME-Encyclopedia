#!/usr/bin/python3
"""Contains the MongoDB database class"""
from mongoengine import Document, StringField, IntField
from bson import ObjectId


class UserInfo(Document):
    """Sets the details of the user"""
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
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

    def find_by_id(self, id):
        """Find a user using the id created by the database"""
        found = UserInfo.objects(id=ObjectId(id)).first()
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

    def to_json(self):
        """Returns the json version of data inside object"""
        return {
                "username": self.username,
                "email": self.email,
                "db ID": str(self.id)
                }
