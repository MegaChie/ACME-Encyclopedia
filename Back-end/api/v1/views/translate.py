#!/usr/bin/python3
"""Contains the translation logic"""
from flask import jsonify
from flask_login import login_required
import json
import requests as req
from api.v1.views import app_views
from database import ArticleInfo


def translate_article(translate_this: list, next: str,
                      prev: str):
    """
    Sends the article to the translation server
    and returns the translation from the response.

    Args:
    - translate_this: A list containing the texts to translate.
    - next: The language to translate to.
    - prev: The language to translate from.
    """
    from api.v1.app.app import translate_API


    text = {"q": translate_this,
            "source": prev,
            "target": next}
    head = {"Content-Type": "application/json"}
    with req.post(translate_API, headers=head,
                  data=json.dumps(text)) as marko:
        if marko.status_code == 200:
            print(marko.json().get("translatedText"))
            return marko.json().get("translatedText")
        print(marko.content)


@app_views.route("/translate/<id>/<lan>", methods=["POST"])
@login_required
def translate(id=None, lan=None):
    """Translates the article, displays it, and saves it to the database"""
    if not id:
        no_article = {"Error": "Article not found"}
        return jsonify(no_article), 404
    else:
        print(f'{id}\n')
    # if not lan:
    #     return redirect(url_for(articles.get_article(id)))
    # else:
        print(f'{lan}\n')

    article = ArticleInfo.find_by_id(id)
    if not article:
        no_article = {"Error": "Article not found"}
        return jsonify(no_article), 404

    article_data = article.to_json()
    if article_data.get("source") and article_data.get("language") == lan:
        exists = {"Status": "Translated before",
                  "Traslation ID": article_data.get("db ID")}
        return jsonify(exists), 303
        # Should redirect to article
    tag_list = article_data.get("Tags")
    translatable = [article_data.get("Title"), article_data.get("Content")]
    translatable = translatable + tag_list
    translated = translate_article(translate_this=translatable,
                                    next=lan,
                                    prev=article_data.get("Language"))

    new_article = ArticleInfo(title=translated[0], content=translated[1],
                              tags=translated[2:], language=lan,
                              author=article_data.get("Author"),
                              source=article_data.get("db ID"))
    new_article.add_to_coll()
    return jsonify(new_article.to_json()), 201
