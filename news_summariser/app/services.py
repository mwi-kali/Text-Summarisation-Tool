from summarizer.summarizer_service import ExtractiveSummarizer, AbstractiveSummarizer, SentimentAnalyzer
from summarizer.utils import RSSFetcher, ArticleFetcher
from database.models import Article, db

class ArticleService:
    def __init__(self):
        self.rss_fetcher = RSSFetcher()
        self.article_fetcher = ArticleFetcher()
        self.extractive = ExtractiveSummarizer()
        self.abstractive = AbstractiveSummarizer()
        self.sentiment = SentimentAnalyzer()

    def process_single_article(self, url):
        """Fetch, summarize, and analyze a single article."""
        article = self.article_fetcher.fetch_article(url)
        content = article["content"]
        article["summary_extractive"] = self.extractive.summarize(content)
        article["summary_abstractive"] = self.abstractive.summarize(content)
        article["sentiment"] = self.sentiment.analyze(content)
        db.session.add(Article(**article))
        db.session.commit()
        return article

    def process_rss_feed(self, rss_url):
        """Fetch articles from RSS feed and summarize each."""
        articles = self.rss_fetcher.fetch_articles(rss_url)
        results = []
        for article in articles:
            content = article.get("content", "")
            title = article.get("title", "No Title")
            url = article.get("url", "No URL")
            published = article.get("published", "Unknown Date")

            if content:  
                summary_extractive = self.extractive.summarize(content)
                summary_abstractive = self.abstractive.summarize(content)
                sentiment = self.sentiment.analyze(content)
            else:
                summary_extractive = "Content not available"
                summary_abstractive = "Content not available"
                sentiment = "Not Analyzed"

            article_data = {
                "title": title,
                "summary_extractive": summary_extractive,
                "summary_abstractive": summary_abstractive,
                "sentiment": sentiment,
                "published": published,
                "url": url,
            }
            results.append(article_data)

            db.session.add(Article(
                title=title,
                content=content,
                summary_extractive=summary_extractive,
                summary_abstractive=summary_abstractive,
                sentiment=sentiment,
                url=url,
                published=published
            ))
            
        db.session.commit()
        return results
