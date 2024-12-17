from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary_extractive = db.Column(db.Text)
    summary_abstractive = db.Column(db.Text)
    sentiment = db.Column(db.String(20))
    category = db.Column(db.String(50), default="Uncategorized")
    url = db.Column(db.String(255), nullable=False)
    published = db.Column(db.String(50), nullable=True)
