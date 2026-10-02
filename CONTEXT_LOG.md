# CONTEXT_LOG.md — E-Commerce Review Intelligence & Sentiment Monitor

> **Purpose:** Persistent session memory for AI tutor–student pair-programming.  
> **Last Updated:** 2026-10-02 | Milestone 0 (Initialization)

---

## 🔒 Tutor Operating Rules (Initializer Prompt)

The AI tutor (Antigravity / any successor agent) MUST follow these rules at all times:

1. **DO NOT WRITE FULL CODE.** Guide the student to write it. Provide architecture, signatures, pseudocode, and targeted hints only. Point out errors and explain mechanisms — never just fix them.
2. **SYLLABUS SPOTLIGHT.** Every time a syllabus concept is implemented, pause and deliver an "Exam Concept Spotlight" covering: (a) what it does under the hood, (b) why it's used here, (c) typical exam/viva questions.
3. **CONTEXT LOG.** Update this file after every significant step. Structure: Current Phase → Syllabus Checklist → Architectural Decisions → Next Milestone.
4. **STEP-BY-STEP CADENCE.** One tiny milestone at a time. Wait for the student's code and test output before advancing.

---

## 📌 Current Phase & Active Module

- **Phase:** 0 — Project Initialization
- **Active Module:** None yet (setting up environment & folder structure)

---

## 📚 Syllabus Checklist

### UNIT I — Foundations
- [ ] Python Environment Setup (virtualenv, project structure)
- [ ] Variables & Data Types
- [ ] Control Structures (if/elif/else, loops)
- [ ] Functions & Scope (def, return, local/global)
- [ ] Basic File I/O (open, read, write)
- [ ] Context Managers (with statement, `__enter__`/`__exit__`)
- [ ] Basic Error Handling (try/except/else)

### UNIT II — Intermediate Python
- [ ] Advanced Functions (*args, **kwargs, lambda, map/filter/reduce)
- [ ] OOP — Classes, Objects, `__init__`
- [ ] OOP — Inheritance
- [ ] OOP — Encapsulation (public/private, properties)
- [ ] Advanced Exception Handling — Custom Exceptions
- [ ] Advanced Exception Handling — finally, raise, exception chaining

### UNIT III — Data & AI Libraries
- [ ] NumPy (arrays, operations, broadcasting)
- [ ] Pandas (Series, DataFrames, filtering, grouping, merging)
- [ ] Matplotlib & Seaborn (line, bar, hist, box plots)
- [ ] scikit-learn (dataset loading, model intro)

### UNIT IV — Web & Data Sources
- [ ] REST APIs with `requests`
- [ ] Web Scraping with `BeautifulSoup`
- [ ] Database — sqlite3 CRUD
- [ ] Data Storage — CSV & JSON

### UNIT V — AI/ML Pipelines
- [ ] Data Preprocessing (scaling, encoding, missing values)
- [ ] Train-Test Split
- [ ] Fitting Classifiers
- [ ] Model Persistence (pickle / joblib)
- [ ] NLP — nltk tokenization, stopwords, stemming
- [ ] Best Practices — logging
- [ ] Best Practices — virtualenv

---

## 🏗️ Key Architectural Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | Single-repo monolith with modular packages | Keeps it simple for a college project; each package maps to a syllabus unit |
| 2 | SQLite as the data store | No external DB server needed; directly covers sqlite3 CRUD syllabus item |
| 3 | NLTK for NLP (not spaCy) | Explicitly required by syllabus (tokenization, stopwords, PorterStemmer) |
| 4 | scikit-learn for ML pipeline | Syllabus requirement; covers train-test split, classifiers, joblib |

---

## 🎯 Project Build Stages (Roadmap)

| Stage | Milestone | Status |
|-------|-----------|--------|
| 1 | Environment setup, folder layout, logging config, custom exceptions | 🔜 Next |
| 2 | OOP-based Review data models & collectors (API + scraper stubs) | ⬜ |
| 3 | SQLite storage layer (CRUD operations) | ⬜ |
| 4 | CSV/JSON import-export utilities | ⬜ |
| 5 | NLTK NLP preprocessing pipeline | ⬜ |
| 6 | NumPy & Pandas data analysis | ⬜ |
| 7 | scikit-learn sentiment classifier | ⬜ |
| 8 | Matplotlib & Seaborn visualizations | ⬜ |
| 9 | Orchestration script (main.py) | ⬜ |

---

## ➡️ Next Immediate Milestone

**Milestone 1 — Environment Setup, Folder Layout, Custom Exceptions**

The student should:
1. Create a virtual environment and `requirements.txt`.
2. Set up the project folder structure (see Milestone 1 guidance in chat).
3. Create a custom exceptions module (`exceptions.py`).
4. Create a basic logging configuration module (`logger.py`).
5. Write a minimal `main.py` entry point that tests logging and exception raising.

---

## 📝 Session Notes

- **2026-10-02:** Project initialized. CONTEXT_LOG.md created. Milestone 1 guidance delivered.
