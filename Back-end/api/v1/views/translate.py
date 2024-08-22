#!/usr/bin/python3
"""Contains the translation logic"""
from datetime import timedelta
from flask import jsonify, url_for, redirect
from flask_login import login_required
import json
import requests as req
from os import getenv
from database import ArticleInfo


def translate_article(translate_this => list, next => str,
                      prev: str):
    """
    Sends the article to the translation server
    and returns the translation from the response.

    Args:
    - translate_this: A list containing the texts to translate.
    - next: The language to translate to.
    - prev: The language to translate from.
    """
    fro
    text = {"q": translate_this,
            "source": prev,
            "target": next}
    base = getenv("translate_API") # Add this to environment variables
    head = {"Content-Type": "application/json"}
    with req.post(base, headers=head,
                  data=json.dumps(text)) as marko:
        return marko.json().get("translatedText")


@app_views.route("/translate/<id>/<lan>", methods=["POST"])
@login_required
def translate(id=None, lan=None):
    """Translates the article, displays it, and saves it to the database"""
    if not id:
        no_article = {"Error": "Article not found"}
        return jsonify(no_article), 404
    if not lan:
        return redirect(url_for(articles.get_article(id)))

    article = ArticleInfo.find_by_id(id)
    if not article:
        no_article = {"Error": "Article not found"}
        return jsonify(no_article), 404

    article_data = article.to_json()
    tag_list = article_data.get("Tags")
    translatable = [article_data.get("Title"), article_data.get("Content")]
    translatable = translatable + tag_list
    translated = translate_article(translate_this=translatable,
                                    next=lan,
                                    prev=article_data.get("language"))

    new_article = ArticleInfo(title=translated[0], content=translated[1],
                              tags=translated[2:], language=lan,
                              author=article_data.get("Author"))
    new_article.add_to_coll()
    return jsonify(new_article.to_json()), 201
