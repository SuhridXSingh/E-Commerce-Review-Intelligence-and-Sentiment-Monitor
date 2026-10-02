# 🛒 E-Commerce Review Intelligence & Sentiment Monitor

> An end-to-end Python project that collects, stores, analyzes, and classifies e-commerce product reviews using NLP and Machine Learning — built as a comprehensive demonstration of core Python, data science, and AI concepts.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

---

## 📌 About

This project builds a complete pipeline that:

1. **Collects** product reviews from REST APIs and web scraping
2. **Stores** them in SQLite with CSV/JSON import-export support
3. **Preprocesses** text using NLP (tokenization, stopword removal, stemming)
4. **Analyzes** data with NumPy and Pandas (statistics, grouping, trends)
5. **Classifies** sentiment using scikit-learn ML models
6. **Visualizes** insights with Matplotlib and Seaborn

Every module is designed to systematically demonstrate Python programming concepts from fundamentals through advanced AI/ML applications.

---

## 🏗️ Project Structure

```
Ecom_rev_intelligence/
├── main.py                  # Orchestration entry point
├── requirements.txt         # Project dependencies
├── CONTEXT_LOG.md           # Development progress tracker
│
├── config/                  # Configuration & logging
│   ├── __init__.py
│   └── logger.py            # Logging setup (console + file)
│
├── core/                    # Core utilities
│   ├── __init__.py
│   └── exceptions.py        # Custom exception hierarchy
│
├── collectors/              # Data collection layer
│   ├── __init__.py
│   ├── api_collector.py     # REST API client (requests)
│   └── scraper.py           # Web scraper (BeautifulSoup)
│
├── storage/                 # Persistence layer
│   ├── __init__.py
│   ├── db_manager.py        # SQLite CRUD operations
│   └── file_manager.py      # CSV & JSON utilities
│
├── nlp/                     # NLP preprocessing
│   ├── __init__.py
│   └── preprocessor.py      # NLTK tokenization, stemming, stopwords
│
├── ml/                      # Machine Learning
│   ├── __init__.py
│   └── classifier.py        # scikit-learn sentiment classifier
│
├── viz/                     # Visualization
│   ├── __init__.py
│   └── plotter.py           # Matplotlib & Seaborn charts
│
├── data/                    # Runtime data (DB, logs, CSVs)
└── models/                  # Saved ML models (pickle/joblib)
```

---

## 🛠️ Tech Stack

| Category | Libraries |
|----------|-----------|
| **Data Collection** | `requests`, `beautifulsoup4` |
| **Storage** | `sqlite3` (built-in), `csv`, `json` |
| **Data Analysis** | `numpy`, `pandas` |
| **NLP** | `nltk` (tokenizer, stopwords, PorterStemmer) |
| **Machine Learning** | `scikit-learn` (classifiers, train-test split, joblib) |
| **Visualization** | `matplotlib`, `seaborn` |
| **Best Practices** | `logging`, `virtualenv`, custom exceptions |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher

### Installation

```bash
# Clone the repository
git clone https://github.com/SuhridXSingh/E-Commerce-Review-Intelligence-and-Sentiment-Monitor.git
cd E-Commerce-Review-Intelligence-and-Sentiment-Monitor

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

---

## 📚 Concepts Covered

This project is structured to cover the following topics across five units:

### Unit I — Python Foundations
- [x] Environment setup & virtual environments
- [x] Variables, data types, control structures
- [x] Functions & scope
- [ ] File I/O & context managers
- [x] Error handling & custom exceptions

### Unit II — Intermediate Python
- [ ] Advanced functions (`*args`, `**kwargs`, `lambda`, `map`/`filter`/`reduce`)
- [ ] OOP (classes, inheritance, encapsulation)
- [x] Custom exception hierarchies with `raise` and `finally`

### Unit III — Data & AI Libraries
- [ ] NumPy arrays, operations, broadcasting
- [ ] Pandas DataFrames, filtering, grouping, merging
- [ ] Matplotlib & Seaborn visualizations
- [ ] scikit-learn model introduction

### Unit IV — Web & Data Sources
- [ ] REST APIs with `requests`
- [ ] Web scraping with `BeautifulSoup`
- [ ] SQLite3 CRUD operations
- [ ] CSV & JSON data storage

### Unit V — AI/ML Pipelines
- [ ] Data preprocessing & train-test split
- [ ] Fitting classifiers & model persistence
- [ ] NLP with NLTK (tokenization, stopwords, stemming)
- [ ] Logging & best practices

---

## 📈 Build Progress

| Stage | Description | Status |
|-------|-------------|--------|
| 1 | Environment, folder layout, logging, custom exceptions | ✅ Complete |
| 2 | OOP data models & collectors (API + scraper) | 🔜 In Progress |
| 3 | SQLite storage layer | ⬜ Planned |
| 4 | CSV/JSON import-export | ⬜ Planned |
| 5 | NLTK NLP pipeline | ⬜ Planned |
| 6 | NumPy & Pandas analysis | ⬜ Planned |
| 7 | scikit-learn sentiment classifier | ⬜ Planned |
| 8 | Matplotlib & Seaborn visualizations | ⬜ Planned |
| 9 | Full orchestration | ⬜ Planned |

---

## 🤝 Contributing

This is a learning/portfolio project. Suggestions and feedback are welcome — open an issue or submit a PR!

---

## 📄 License

This project is licensed under the MIT License.

---

<p align="center">
  Built with 🧠 by <a href="https://github.com/SuhridXSingh">Suhrid Singh</a>
</p>
