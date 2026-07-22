# 🐦 Tweet Sentiment Analysis System

An end-to-end **Natural Language Processing (NLP)** pipeline built in Python that automatically classifies tweets into **Positive**, **Negative**, or **Neutral** sentiments using NLTK's **VADER** (Valence Aware Dictionary and sEntiment Reasoner) model.

## 📖 Overview

This project analyzes the emotional polarity of tweets and generates rich visual insights through Matplotlib charts. It follows a clean **ETL (Extract → Transform → Load)** architecture, making it scalable and easy to integrate into larger data workflows.

## 🎯 Key Features

- ✅ Automated sentiment classification using VADER lexicon
- ✅ Compound sentiment scoring (range: -1.0 to +1.0)
- ✅ Threshold-based labeling (Positive / Negative / Neutral)
- ✅ 4 data visualizations: Bar Chart, Pie Chart, Histogram, Grouped Bar
- ✅ Enriched output exported to CSV for downstream analysis

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** pandas, NLTK (VADER), Matplotlib
- **Data Format:** CSV

## 🔄 Workflow

1. **Extract** tweets from `tweets.csv`
2. **Transform** using VADER to compute compound scores
3. **Classify** tweets based on score thresholds
4. **Visualize** results with 4 Matplotlib charts
5. **Export** enriched data to `output.csv`

## 📊 Visualizations

- Sentiment Distribution Bar Chart
- Sentiment Share Pie Chart
- Compound Score Histogram
- Average Score per Sentiment

## 🌍 Applications

- Brand reputation monitoring
- Customer feedback analysis
- Social media trend tracking
- Product review analytics

## 🚀 Future Enhancements

- Twitter/X API integration for real-time data
- BERT model for higher accuracy
- Streamlit dashboard for interactive exploration
- Multilingual sentiment support

## 👨‍💻 Author

**Shubham Mishra** | [LinkedIn](https://www.linkedin.com/in/shubham-mishra-97028a26a) | [GitHub](https://github.com/shubham8832)

---

*Built with Python, NLTK, and Matplotlib* ❤️
