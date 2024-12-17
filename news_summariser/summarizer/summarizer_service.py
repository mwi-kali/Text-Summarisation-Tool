from transformers import pipeline
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from textblob import TextBlob

class ExtractiveSummarizer:
    def summarize(self, content: str, num_sentences: int = 3) -> str:
        parser = PlaintextParser.from_string(content, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        sentences = summarizer(parser.document, num_sentences)
        return " ".join(str(sentence) for sentence in sentences)

class AbstractiveSummarizer:
    def __init__(self, min_length: int = 30, max_length: int = 400):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)
        self.min_length = min_length
        self.max_length = max_length

    def summarize(self, text: str) -> str:
        words = text.split()
        if len(words) < 10:
            return "Text too short to summarize effectively."

        if len(words) > self.max_length:
            chunks = [' '.join(words[i:i + self.max_length]) for i in range(0, len(words), self.max_length)]
            summaries = []
            for chunk in chunks:
                input_length = len(chunk.split())
                current_max_length = min(self.max_length, input_length)
                try:
                    chunk_summary = self.summarizer(
                        chunk,
                        min_length=self.min_length if self.min_length<=current_max_length else current_max_length,
                        max_length=current_max_length,
                        do_sample=False
                    )[0]['summary_text']
                    summaries.append(chunk_summary)
                except Exception as e:
                    summaries.append("Error summarizing chunk: " + str(e))
            return " ".join(summaries)

        else:
            input_length = len(words)
            current_max_length = min(self.max_length, input_length)
            try:
                result = self.summarizer(
                    text,
                    min_length=self.min_length if self.min_length<=current_max_length else current_max_length,
                    max_length=current_max_length,
                    do_sample=False
                )
                return result[0]['summary_text']
            except Exception as e:
                return f"Error summarizing text: {e}"

class SentimentAnalyzer:
    def analyze(self, content: str) -> str:
        sentiment = TextBlob(content).sentiment.polarity
        if sentiment > 0:
            return "POSITIVE"
        elif sentiment < 0:
            return "NEGATIVE"
        return "NEUTRAL"
