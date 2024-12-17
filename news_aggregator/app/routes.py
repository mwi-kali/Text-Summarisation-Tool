from flask import Blueprint, request, render_template, jsonify
from app.services import ArticleService

routes_blueprint = Blueprint("routes", __name__)
service = ArticleService()

@routes_blueprint.route("/", methods=["GET"])
def index():
    return render_template("home.html")

@routes_blueprint.route("/fetch", methods=["POST"])
def fetch():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        if url.endswith(".xml") or "rss" in url.lower():
            articles = service.process_rss_feed(url)
            return jsonify({
                "message": f"Fetched and summarized {len(articles)} articles.",
                "articles": articles
            })
        else:
            article = service.process_single_article(url)
            return jsonify(article)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
