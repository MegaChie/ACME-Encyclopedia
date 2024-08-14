#!/usr/bin/python3
"""Contains the MongoDB database class"""
from datetime import datetime

from mongoengine import Document, StringField, BooleanField, ListField, DateTimeField
from flask_bcrypt import Bcrypt
from bson import ObjectId
from flask_login import UserMixin

bcrypt = Bcrypt()


class UserInfo(Document, UserMixin):
    """Sets the details of the user"""
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=False, unique=True)
    authed = BooleanField(default=False)
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
    def find_by_id(cls, id):
        """Find a user using the id created by the database"""
        found = cls.objects(id=ObjectId(id)).first()
        return found

    @classmethod
    def find_by_email(cls, email):
        found = cls.objects(email=email).first()
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


class ArticleInfo(Document):
    """Represents an article in the database"""
    title = StringField(required=True, unique=True)
    content = StringField(required=True)
    tags = ListField(StringField(), required=False)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    meta = {"collection": "Articles"}

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
    def find_by_id(cls, id):
        """Find an article using the id created by the database"""
        found = ArticleInfo.objects(id=ObjectId(id)).first()
        return found

    def find_by_title(cls, title):
        found = ArticleInfo.objects(tile=title).first()
        return found

    def update_article(self, id, **kwargs):
        """Update the content of an article"""
        article = self.find_by_id(id)
        for key, value in kwargs.items():
            setattr(article, key, value)
        article.updated_at = datetime.utcnow()
        article.save()

    def delete_by_id(self, id):
        """Delete an article by its ID"""
        ArticleInfo.objects(id=ObjectId(id)).delete()

    def to_json(self):
        """Returns the JSON version of the article data"""
        return {
            "title": self.title,
            "content": self.content,
            "tags": self.tags,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "db ID": str(self.id)
        }

    @classmethod
    def find_all(cls):
        """Returns all articles in the database"""
        articles = ArticleInfo.objects().all()
        return articles
