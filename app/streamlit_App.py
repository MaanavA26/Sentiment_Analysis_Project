import streamlit as st
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score
import re

nltk.download('punkt')


st.title("E-commerce Sentiment Analysis")

# Load the trained model
model_filename = '/Users/maanavaryan/Documents/Project/sentiment_analysis_project/data/sentiment_model.pkl' 
model = joblib.load(model_filename)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words("english")]
    words = [PorterStemmer().stem(word) for word in words]
    return " ".join(words)


comment = st.text_area("Enter your comment:")
if st.button("Analyze"):
    preprocessed_comment = preprocess_text(comment)
    sentiment = model.predict([preprocessed_comment])[0]
    st.write("Predicted Sentiment:", sentiment)

st.subheader("Context:")
st.write("1 means negative")
st.write("2 means positive")
