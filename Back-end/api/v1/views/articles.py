from api.v1.views import app_views
from flask import jsonify, request
from flask_login import (login_required , login_user,
                         logout_user, login_required,
                         current_user)
from database import ArticleInfo


@app_views.route("/add_article", methods=["POST"])
@login_required
def add_article():
    """add article to the database."""
    if request.is_json:
        data = request.get_json()
        if not data.get("title") or not data.get("content"):
            missing = {"Error": "Missing \"title\" and \"content\" fields"}
            return jsonify(missing), 400

        new_article = ArticleInfo(title=data.get("title"),
                                  content=data.get("content"),
                                  tags=data.get("tags"),
                                  status=data.get("status"),
                                  author=current_user.username)


        new_article.add_to_coll()
        return jsonify(new_article), 201
    else:
        not_json = {"Error": "Request must be JSON"}
        return jsonify(not_json), 400


@app_views.route("/articles/<id>", methods=["GET"], strict_slashes=False)
@login_required
def get_article(id):
    """fetch articles from the database."""
    article = ArticleInfo.find_by_id(id)
    if article and current_user.username == article.author:
        return jsonify(article), 200
    else:
        return jsonify({"Error": "Article not found"}), 404


@app_views.route("/articles", methods=["GET"], strict_slashes=False)
@login_required
def list_articles():
    """list all articles from the database"""
    articles = ArticleInfo.objects.all()
    articles_list = [article.to_json() for article in articles
                     if article.status == "published"]
    return jsonify({"articles": articles_list}), 200


@app_views.route("/search_articles", methods=["GET"], strict_slashes=False)
@login_required
def search_articles():
    """Search for articles by title"""
    query = request.args.get("q")
    if query:
        # Perform a case-insensitive search for
        # the titles that contain the query string
        articles = ArticleInfo.objects(title__icontains=query)
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
        wrong_user = {"Error": "You are not the author of this article"}
        return jsonify(wrong_user), 403

    if request.is_json:
        data = request.get_json()
        article.update_article = "draft"
        article.update_article(id, data)
        done = {"Status": "Success"}
        return jsonify(done), 201
