# CodeAlpha - FAQ Chatbot

**CodeAlpha Artificial Intelligence Internship — Task 2**

A university admissions FAQ chatbot that matches natural-language questions against a knowledge base using NLP preprocessing and similarity-based matching, served through a Streamlit chat interface.

> **Note:** Uses sample/demo FAQ data created for this internship task. Not affiliated with or endorsed by any official institution.

---

## Overview

This project fulfills Task 2 of the CodeAlpha AI internship: collect FAQs, preprocess text using NLP techniques, match user questions to the most relevant FAQ using similarity scoring, and return the best-matching answer through a chat interface.

---

## Features

| Feature | Description |
|---|---|
| Chat-style interface | Built with Streamlit's native chat components |
| NLP preprocessing | Lowercasing, punctuation removal, stopword removal, lemmatization (NLTK) |
| Similarity matching | TF-IDF vectorization + Cosine Similarity (scikit-learn) |
| Confidence display | Shows the matched FAQ question and similarity score for transparency |
| Fallback handling | Returns a clear "couldn't find an answer" message below the similarity threshold |
| Knowledge base | 20 sample FAQs covering admissions, fees, scholarships, eligibility, hostel, and more |

---

## Tech Stack

- **Language:** Python
- **UI:** Streamlit
- **NLP preprocessing:** NLTK (stopwords, WordNet lemmatizer)
- **Matching:** scikit-learn (`TfidfVectorizer`, `cosine_similarity`)

---

## How It Works

1. At startup, all FAQ questions are preprocessed (cleaned, lemmatized) and converted into TF-IDF vectors
2. When a user submits a question, it goes through the same preprocessing pipeline
3. Cosine similarity is computed between the user's question vector and every FAQ vector
4. The FAQ with the highest similarity score is returned as the answer
5. If the best score falls below a set threshold (0.25), a fallback "no match found" response is shown instead

**Example results from testing:**

| User Question | Matched FAQ | Similarity Score |
|---|---|---|
| "How much is the fee?" | "How much is the semester fee?" | 0.82 |
| "Do you have scholarships" | "Is there a scholarship available?" | 0.78 |
| "what about scholarships?" | "Is there a scholarship available?" | 0.78 |
| "blah random gibberish xyz" | *(no match)* | 0.00 |

---

## Setup & Run Locally

```bash
git clone https://github.com/zakasaleem35-jpg/CodeAlpha_FAQChatbot.git
cd CodeAlpha_FAQChatbot
pip install -r requirements.txt
streamlit run app.py
```

The app opens automatically in your browser at `http://localhost:8501`.

---

## Project Structure

| File | Description |
|---|---|
| `app.py` | Streamlit UI and chat session logic |
| `chatbot.py` | NLP preprocessing and TF-IDF + Cosine Similarity matching logic |
| `faqs.py` | FAQ knowledge base (20 sample question-answer pairs) |
| `requirements.txt` | Python dependencies |

---

## Task Requirements Checklist

| Requirement | Status |
|---|---|
| Collect FAQs (questions + answers) | ✅ (20 sample FAQs) |
| Preprocess text using NLP libraries | ✅ (NLTK) |
| Match user questions using similarity techniques | ✅ (TF-IDF + Cosine Similarity) |
| Display best-matching answer as chatbot response | ✅ |
| Optional: chat UI | ✅ (Streamlit) |

---

## Author

**Zaka Saleem** — [@zakasaleem35-jpg](https://github.com/zakasaleem35-jpg)

Built as part of the CodeAlpha Artificial Intelligence internship program (Batch: August 2026).
