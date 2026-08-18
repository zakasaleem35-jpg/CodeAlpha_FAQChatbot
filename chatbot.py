"""
FAQ Chatbot Core Logic
Handles text preprocessing and question matching using TF-IDF + Cosine Similarity.
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faqs import FAQS

# Download required NLTK data (only runs once, then cached locally)
def _ensure_nltk_data():
    resources = [
        ("corpora/stopwords", "stopwords"),
        ("corpora/wordnet", "wordnet"),
        ("tokenizers/punkt_tab", "punkt_tab"),
    ]
    for path, name in resources:
        try:
            nltk.data.find(path)
        except LookupError:
            nltk.download(name, quiet=True)

_ensure_nltk_data()

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


def preprocess(text: str) -> str:
    """
    Cleans and normalizes text:
    1. Lowercase everything
    2. Remove punctuation/special characters
    3. Remove stopwords (common words like 'is', 'the', 'a')
    4. Lemmatize words (running -> run, universities -> university)
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return " ".join(words)


class FAQChatbot:
    def __init__(self, faqs=None):
        self.faqs = faqs if faqs is not None else FAQS
        self.questions = [faq["question"] for faq in self.faqs]

        # Preprocess all FAQ questions once at startup
        self.processed_questions = [preprocess(q) for q in self.questions]

        # Build TF-IDF vectorizer on the FAQ questions
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.processed_questions)

    def get_response(self, user_input: str, threshold: float = 0.25):
        """
        Takes user's question, finds the most similar FAQ question,
        and returns its answer along with the similarity score.
        """
        cleaned_input = preprocess(user_input)

        if not cleaned_input.strip():
            return {
                "answer": "Please type a question so I can help you.",
                "matched_question": None,
                "score": 0.0,
            }

        # Convert user's question into the same TF-IDF space
        input_vector = self.vectorizer.transform([cleaned_input])

        # Compare against all FAQ question vectors
        similarities = cosine_similarity(input_vector, self.question_vectors)[0]

        best_idx = similarities.argmax()
        best_score = similarities[best_idx]

        if best_score < threshold:
            return {
                "answer": "Sorry, I couldn't find a relevant answer to that. "
                          "Could you rephrase your question or ask something else about admissions?",
                "matched_question": None,
                "score": float(best_score),
            }

        return {
            "answer": self.faqs[best_idx]["answer"],
            "matched_question": self.faqs[best_idx]["question"],
            "score": float(best_score),
        }
