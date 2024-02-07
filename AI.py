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
        preprocessed_text.append(' '.join(preprocessed_words))
    return preprocessed_text

# Function to answer questions
def answer_question(question, text):
    preprocessed_text = preprocess_text(text)
    preprocessed_question = preprocess_text(question)
    
    # Join preprocessed text and question into one list
    preprocessed_data = preprocessed_text + preprocessed_question
    
    # Calculate TF-IDF vectors for the text and question
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_data)
    
    # Calculate cosine similarity between question and each sentence in the text
    similarity_scores = cosine_similarity(tfidf_matrix[:-len(preprocessed_question)], tfidf_matrix[-len(preprocessed_question):])
    
    # Find the index of the most similar sentence
    max_score_index = similarity_scores.argmax()
    
    # Return the corresponding sentence from the text
    return preprocessed_text[max_score_index]

# Example text
text = ""

# Interactive question-answering loop
while True:
    question = input("Ask a question (or type 'exit' to quit): ")
    if question.lower() == 'exit':
        print("Goodbye!")
        break
    else:
        answer = answer_question(question, text)
        if answer:
            print("Answer:", answer)
        else:
            print("Sorry, I couldn't find an answer to that question.")