from api.v1.views import app_views
from flask import jsonify, request, session
from flask_login import (login_required, current_user)
from database import ArticleInfo


@app_views.route("/add_article", methods=["POST"])
@login_required
def add_article():
    """Adds article to the database."""
    if request.is_json:
        data = request.get_json()
        if not data.get("title") or not data.get("content"):
            data_missing = {"Error": "Plese add a tile, content"}
            return jsonify(data_missing), 400

        new_article = ArticleInfo(title=data.get("title"),
                                  content=data.get("content"),
                                  tags=data.get("tags"),
                                  status=data.get("status"), # If selected
                                  author=current_user.username,
                                  language=data.get("language"))

        new_article.add_to_coll()
        return jsonify(new_article), 201
    else:
        not_json = {"Error": "Request must be a JSON"}
        return jsonify(not_json), 400


@app_views.route("/articles/<id>", methods=["GET"], strict_slashes=False)
@login_required
def get_article(id):
    """Fetchs articles from the database."""
    article = ArticleInfo.find_by_id(id)
    if article:
        return jsonify(article), 200
    else:
        return jsonify({"Error": "Article not found"}), 404


@app_views.route("/articles", methods=["GET"], strict_slashes=False)
@login_required
def list_articles():
    """Lists all articles from the database"""
    articles = ArticleInfo.objects.all().order_by("-rank")
    articles_list = [article.to_json() for article in articles
                     if article.status == "published"]
    return jsonify({"articles": articles_list}), 200


@app_views.route("/search_articles", methods=["GET"], strict_slashes=False)
@login_required
def search_articles():
    """Search for articles by title"""
    query = request.args.get("q")
    if query:

        # Perform a case-insensitive search for titles that contain the query string
        articles = ArticleInfo.objects(title__istartswith=query)

        if articles:
            article_list = [article.to_json() for article in articles
                            if article.status == "published"]
            return jsonify({"articles": article_list}), 200
        else:
            return jsonify({"Error": "No articles found"}), 404
    else:
        return jsonify({"Error": "No search query provided"}), 400


@app_views.route("/edit_articles/<id>", methods=["PUT"],
                 strict_slashes=False)
@login_required
def edit_article(id=None):
    """Edits an exsisting article provided that it is the author"""
    article = ArticleInfo.find_by_id(id)
    if not article:
        not_found = {"Error": "Article not found"}
        return jsonify(not_found), 404

    if current_user.username != article.author:
        not_author = {"Error": "You are not the author of this article"}
        return jsonify(not_author), 401

    if request.is_json:
        data = request.get_json()
        article.update_article = "draft"
        article.update_article(id, data)
        done = {"Status": "Success"}
        return jsonify(done), 201

    not_json = {"Error": "Request must be a JSON"}
    return jsonify(not_json), 400


@app_views.route("/article/<id>/rank", methods=["PUT"],
                 strict_slashes=False)
@login_required
def increase_rank(id=None):
    """Increases the rank of an article when viewed"""
    if not id:
        not_found = {"Error": "Article not found"}
        return jsonify(not_found), 404

    if 'viewed_articles' not in session:
        session['viewed_articles'] = []
    if id not in session['viewed_articles']:
        article = ArticleInfo.find_by_id(id)
        if not article:
            not_found = {"Error": "Article not found"}
            return jsonify(not_found), 404

        article.update(inc__rank=1)
        session['viewed_articles'].append(id)
        rank_up = {"Status": "Article  ranked up by one"}
        return jsonify(rank_up), 201

    ranked = {"Status": "This article is already ranked by logged in user"}
    return jsonify(ranked), 403
