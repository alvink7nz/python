import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Function to preprocess the text
def preprocess_text(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    # Remove stopwords and punctuation, and lemmatize the words
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    preprocessed_text = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        preprocessed_words = [lemmatizer.lemmatize(word.lower()) for word in words if word.isalnum() and word.lower() not in stop_words]
        if preprocessed_words:
            preprocessed_text.append(' '.join(preprocessed_words))
    return preprocessed_text

# Function to answer questions
def answer_question(question, text):
    preprocessed_text = preprocess_text(text)
    preprocessed_question = preprocess_text(question)
    
    # If either the text or question is empty after preprocessing, return None
    if not preprocessed_text or not preprocessed_question:
        return None
    
    # Join preprocessed text and question into one list
    preprocessed_data = preprocessed_text + preprocessed_question
    
    # Calculate TF-IDF vectors for the text and question
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_data)
    
    # Calculate cosine similarity between question and each sentence in the text
    similarity_scores = cosine_similarity(tfidf_matrix[:-len(preprocessed_question)], tfidf_matrix[-len(preprocessed_question):])
    
    # Set a threshold for cosine similarity scores
    similarity_threshold = 0.1
    
    # Find the index of the most similar sentence above the threshold
    max_score_index = -1
    for i, score in enumerate(similarity_scores):
        if score > similarity_threshold:
            max_score_index = i
            break
    
    # If no sentence above the threshold is found, return a default response
    if max_score_index == -1:
        return "I'm sorry, I don't have an answer to that question."
    
    # Return the corresponding sentence from the text
    return preprocessed_text[max_score_index]

# Example text
text = """
Natural Language Processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. The goal is a computer capable of 'understanding' the contents of documents, including the contextual nuances of the language within them.

NLP can be applied to various tasks, such as machine translation, sentiment analysis, speech recognition, named entity recognition, and question answering.
"""

# Interactive question-answering loop
while True:
    question = input("Ask a question (or type 'exit' to quit): ")
    if question.lower() == 'exit':
        print("Goodbye!")
        break
    else:
        answer = answer_question(question, text)
        print("Answer:", answer)