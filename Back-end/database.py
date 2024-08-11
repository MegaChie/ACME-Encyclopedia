#!/usr/bin/python3
"""Contains the MongoDB database class"""
from mongoengine import Document, StringField, IntField


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

    def to_json(self):
        """Returns the json version of data inside object"""
        return {
                "username": self.username,
                "email": self.email
                }
