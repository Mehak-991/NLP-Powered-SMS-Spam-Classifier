import streamlit as st
import pickle
import string
import re
import nltk
import logging
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from styles import get_css

# ─── NLTK Setup ───
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

class _IgnoreScriptRunContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        try:
            return "missing ScriptRunContext!" not in record.getMessage()
        except Exception:
            return True

logging.getLogger().addFilter(_IgnoreScriptRunContextFilter())

# ─── Page Config ───
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─── Inject CSS ───
st.markdown(get_css(), unsafe_allow_html=True)

# ─── Load Model ───
@st.cache_resource
def load_models():
    try:
        tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
        model = pickle.load(open('model.pkl', 'rb'))
        return tfidf, model
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None

tfidf, model = load_models()
port_stemmer = PorterStemmer()

# ─── Text Cleaning ───
def clean_text(text):
    text = word_tokenize(text)
    text = " ".join(text)
    text = [c for c in text if c not in string.punctuation]
    text = ''.join(text)
    text = [c for c in text if c not in re.findall(r"[0-9]", text)]
    text = ''.join(text)
    sw = set(stopwords.words('english'))
    text = [w.lower() for w in text.split() if w.lower() not in sw]
    text = list(map(lambda x: port_stemmer.stem(x), text))
    return " ".join(text)

# ─── Main UI ───
st.markdown("""
<div class="header-container">
    <h1>💬 SMS Spam Detector</h1>
    <p>Analyze any SMS message instantly to determine if it's spam or safe.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

with st.form("spam_detector_form", clear_on_submit=False):
    sms_input = st.text_area(
        "Message to analyze:", 
        placeholder="Type or paste the SMS message here...",
        height=150,
        label_visibility="collapsed"
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submit_button = st.form_submit_button("Let's Predict", use_container_width=True)

if submit_button:
    if not sms_input.strip():
        st.markdown("""
        <div class="result-box warning-box">
            <h3>⚠️ Please enter a message</h3>
            <p>The text area cannot be empty.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        if tfidf and model:
            try:
                cleaned = clean_text(sms_input)
                # Transform using the loaded vectorizer and convert to dense array
                vector = tfidf.transform([cleaned]).toarray()
                res = model.predict(vector)[0]
                
                if res == 1:
                    st.markdown("""
                    <div class="result-box spam-box">
                        <div class="icon">🚫</div>
                        <h3>Spam</h3>
                        <p>This message looks like a spam or promotional message.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="result-box ham-box">
                        <div class="icon">✅</div>
                        <h3>Not Spam</h3>
                        <p>This message appears to be legitimate.</p>
                    </div>
                    """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Prediction Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    Powered by Machine Learning & Natural Language Processing
</div>
""", unsafe_allow_html=True)
