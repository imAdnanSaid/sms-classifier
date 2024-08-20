import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize PorterStemmer
ps = PorterStemmer()

# Text transformation function
def transform_text(text):
    text = text.lower()  # Convert to lowercase
    text = nltk.word_tokenize(text)  # Tokenize

    # Remove special characters and stopwords
    y = [i for i in text if i.isalnum()]
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]

    # Stemming
    y = [ps.stem(i) for i in y]

    return " ".join(y)

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
tfdif = pickle.load(open('vectorizer.pkl', 'rb'))

# Streamlit App Layout
st.set_page_config(page_title="Spam Classifier", page_icon="📧", layout="wide")

# Custom CSS for enhanced styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            color: #333;
        }
        .main-title {
            font-size: 36px;
            font-weight: bold;
            color: #0066cc;
            text-align: center;
            margin-bottom: 20px;
        }
        .sub-title {
            font-size: 18px;
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .stTextArea [data-baseweb="textarea"] {
            background-color: #f8f9fc;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton button {
            background-color: #0066cc;
            color: white;
            padding: 10px 30px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 16px;
        }
        .stButton button:hover {
            background-color: #004c99;
            transform: scale(1.05);
            transition: all 0.3s ease;
        }
        .result-box {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
        }
        .spam {
            background-color: #ffcccc;
            color: #cc0000;
        }
        .not-spam {
            background-color: #ccffcc;
            color: #006600;
        }
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<div class="main-title">📧 SMS/Email Spam Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Classify messages as Spam or Not Spam with a single click</div>', unsafe_allow_html=True)

# Input text box
input_sms = st.text_area('Type your message here:', height=150)

# Predict button with custom style
if st.button('Predict', help="Click to classify the message"):
    with st.spinner('Analyzing...'):
        # 1. Preprocess
        transformed_sms = transform_text(input_sms)

        # 2. Vectorize
        vector_input = tfdif.transform([transformed_sms])

        # 3. Predict
        result = model.predict(vector_input)[0]

        # 4. Display
        if result == 1:
            st.markdown('<div class="result-box spam">🚨 This message is Spam!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-box not-spam">✅ This message is Not Spam!</div>', unsafe_allow_html=True)

# Hide default Streamlit footer
st.markdown("""
    <style>
    .reportview-container .main footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
