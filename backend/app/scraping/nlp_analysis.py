from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Predefined topics (admin-defined)
TOPICS = {
    "Derivatives": ["calculus", "differentiation", "tangents", "slope"],
    "World History": ["revolution", "empire", "trade", "war"],
    # Add more topics here
}

def categorize_content(text):
    vectorizer = TfidfVectorizer()
    topic_keywords = [" ".join(keywords) for keywords in TOPICS.values()]
    
    # Vectorize text and topic keywords
    vectors = vectorizer.fit_transform([text] + topic_keywords)
    similarities = cosine_similarity(vectors[0:1], vectors[1:])
    
    # Match to the most similar topic
    best_match = max(enumerate(similarities[0]), key=lambda x: x[1])
    topic_name = list(TOPICS.keys())[best_match[0]]
    relevance_score = best_match[1]
    
    return {"topic": topic_name, "relevance_score": relevance_score}
