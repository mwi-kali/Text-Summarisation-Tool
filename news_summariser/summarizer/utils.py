import feedparser
from newspaper import Article

class RSSFetcher:
    def fetch_articles(self, rss_url: str) -> list[dict]:
        feed = feedparser.parse(rss_url)
        articles = []
        for entry in feed.entries:
            try:
                article = Article(entry.link)
                article.download()
                article.parse()
                articles.append({
                    "title": article.title,
                    "content": article.text,
                    "url": entry.link,
                    "published": entry.published,
                })
            except:
                pass
        return articles

class ArticleFetcher:
    def fetch_article(self, url: str) -> dict:
        article = Article(url)
        article.download()
        article.parse()
        return {"title": article.title, "content": article.text, "url": url, "published": article.publish_date}
