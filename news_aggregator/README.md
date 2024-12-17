# 📰 Extractive & Abstractive News Summarisation with Sentiment Analysis

This repository includes a **News Summarisation Tool** that can handle both individual news articles and RSS feeds. It combines extractive and abstractive summarisation techniques to produce succinct summaries, as well as sentiment analysis to provide deeper insights into the text.

The project employs modern NLP models and technologies, making it an effective solution for rapidly digesting enormous amounts of news.

---

## 📌 Key Features

### 1. Data retrieval and preprocessing

**Single Article Summarisation** retrieves and processes individual news articles with 'newspaper3k'.

**RSS Feed Summarisation** use 'feedparser' to get bulk articles from RSS feeds.

**Preprocessing** removes superfluous characters and noise from inputs to prepare them for summarisation.

### 2. Summarisation Techniques

**Extractive Summarization** uses the TextRank algorithm with 'Sumy' to extract key sentences from the source text.

**Abstractive Summary** creates human-like summaries with the pre-trained 'facebook/bart-large-cnn' model and Hugging Face's 'transformers' library. It divides large texts into digestible bits to efficiently deal with input size limits.

### 3. Sentiment Analysis 

It uses 'TextBlob' library to analyse sentiment in news articles. Sentiment polarity is returned as **positive**, **negative**, or **neutral**.

### 4. Front-End Interface 

It utilises HTML, CSS (Bootstrap 5) and JavaScript to provide a modern and responsive user interface. Users can enter a single article URL or RSS feed link, view the extracted and abstract summaries and evaluate sentiment for individual articles and bulk RSS feeds.

### 5. Database Storage

Articles and summaries are saved to a SQLite database via 'SQLAlchemy' for future retrieval or analysis.


---

## 💻 How to Run the Project

### 1. Prerequisites
Ensure you have:
- Python 3.8+
- pip (Python package manager)

### 2. Installation
Clone the repository:
```bash
git clone https://github.com/your-username/news-summariser.git
cd news-summariser
```

#### Installation Steps

##### Install the required packages:
```bash
pip install -r requirements.txt
```

##### Download NLTK's punkt tokenizer

```python
import nltk
nltk.download('punkt')
```

##### Start the Flask Server

```bash
python3 app.py
```

##### Open the application in your browser:

```
http://127.0.0.1:5000
```

---

## 🛠️ How to Use

### Summarise a Single Article:
1. Paste a valid article URL into the input box.
2. Click **Fetch and Summarise**.
3. View:
   - **Extractive Summary**
   - **Abstractive Summary**
   - **Sentiment Analysis Result**

### Summarise an RSS Feed:
1. Paste an RSS feed URL (e.g., `https://feeds.bbci.co.uk/news/rss.xml`).
2. Click **Fetch and Summarise**.
3. The application will:
   - Fetch multiple articles.
   - Summarise each article.
   - Perform sentiment analysis.

---

## 🧪 API Endpoints

### 1. Fetch Single Article
- **Endpoint**: `/fetch`
- **Method**: `POST`
- **Request Body**:

```json
{
   "url": "https://edition.cnn.com/2024/12/14/europe/italy-giorgia-meloni-trump-relationship-intl/index.html"
}
```

- **Response**:

```json
{
   "title": "Italy's PM Giorgia Meloni's political journey",
   "summary_extractive": "...",
   "summary_abstractive": "...",
   "sentiment": "POSITIVE"
}
```

### 2. Fetch RSS Feed
- **Endpoint**: `/fetch`
- **Request Body**:

```json
{
   "url": "https://feeds.bbci.co.uk/news/rss.xml"
}
```

- **Response**:

```json
{
   "message": "Fetched and summarised 10 articles.",
   "articles": [
      {
         "title": "Article 1 Title",
         "summary_extractive": "...",
         "summary_abstractive": "...",
         "sentiment": "NEGATIVE"
      },
      ...
   ]
}
```

---

## 📊 Future Enhancements

### Advanced Summarisation Models
- Use models like T5 or PEGASUS to create better abstract summaries.

### Create an interactive dashboard using Dash or Plotly to visualise sentiment trends and summaries.

### User Accounts
- Enable authentication to save and access summarised articles.

### Cloud Deployment
- Publish the application on platforms such as Heroku, AWS, or Azure.

### Multi-Language Support
- Summarise non-English articles with multilingual NLP models.
---

## 🤝 Contributing

Contributions are welcome! 

To contribute:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature-branch
```

3. Commit changes:

```bash
git commit -m "Add new feature"
```

4. Push the branch:

```bash
git push origin feature-branch
```

5. Open a pull request.

---
