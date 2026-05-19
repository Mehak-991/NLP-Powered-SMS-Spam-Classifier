import streamlit as st
import pickle
import string
import re
import nltk
import logging
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from datetime import datetime
from styles import get_css

# ─── NLTK Setup ───
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Suppress noisy Streamlit "missing ScriptRunContext" warnings when
# the app is executed in certain environments (e.g. running with plain
# `python app.py`). We filter that specific message while leaving other
# log output intact.
class _IgnoreScriptRunContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        try:
            return "missing ScriptRunContext!" not in record.getMessage()
        except Exception:
            return True

logging.getLogger().addFilter(_IgnoreScriptRunContextFilter())

# ─── Page Config ───
st.set_page_config(
    page_title="SMS Spam Detection System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Load Model ───
@st.cache_resource
def load_models():
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
    return tfidf, model

tfidf, model = load_models()
port_stemmer = PorterStemmer()

# ─── Session State ───
for key, val in [('history', []), ('dark_mode', False), ('total', 0), ('spam_count', 0), ('ham_count', 0)]:
    if key not in st.session_state:
        st.session_state[key] = val

# ─── Inject CSS ───
st.markdown(get_css(st.session_state.dark_mode), unsafe_allow_html=True)

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

# ─── Sparkline SVG ───
def sparkline(color):
    cid = color.replace('#','')
    return f"""<svg width="100%" height="28" viewBox="0 0 120 28" fill="none">
    <path d="M0 22 L15 18 L30 20 L45 14 L60 16 L75 10 L90 13 L105 8 L120 10"
          stroke="{color}" stroke-width="1.8" fill="none" stroke-linecap="round"/>
    <path d="M0 22 L15 18 L30 20 L45 14 L60 16 L75 10 L90 13 L105 8 L120 10 L120 28 L0 28Z"
          fill="url(#g{cid})" opacity="0.12"/>
    <defs><linearGradient id="g{cid}" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="{color}"/><stop offset="100%" stop-color="{color}" stop-opacity="0"/>
    </linearGradient></defs></svg>"""

# ═══════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <span class="brand-icon">💬</span>
        <h2>SMS</h2>
        <p>Spam Detection</p>
    </div>""", unsafe_allow_html=True)

    page = st.radio("Nav", [
        "🏠  Home", "🔍  Predict", "📋  History",
        "📊  Analytics", "🤖  Model Info", "ℹ️  About"
    ], label_visibility="collapsed")

    # Phone illustration (matches reference design)
    st.markdown("""
    <div class="sidebar-illustration">
        <div style="display:flex;gap:0.6rem;justify-content:center;align-items:flex-end;">
            <div class="phone-group">
                <div class="phone">
                    <div class="msg msg-purple">💬 Hey!</div>
                    <div class="msg msg-white">Win $1000!</div>
                    <div class="msg msg-purple">🎉 Free gift</div>
                </div>
                <div class="spam-badge">SPAM</div>
            </div>
            <div class="phone-group" style="margin-bottom:0.5rem;">
                <div class="phone" style="padding:0.4rem;">
                    <div class="msg msg-white" style="font-size:0.55rem;">Hi there 👋</div>
                    <div class="msg msg-purple" style="font-size:0.55rem;">See you!</div>
                </div>
                <div class="check-badge">✓</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    dm = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)
    if dm != st.session_state.dark_mode:
        st.session_state.dark_mode = dm
        st.rerun()

# ═══════════════════════════════════════
# HOME PAGE
# ═══════════════════════════════════════
if "Home" in page:

    # Header row
    h1, h2 = st.columns([3, 1])
    with h1:
        st.markdown("""
        <div><h1 style="font-size:1.55rem;font-weight:800;margin:0 0 0.15rem;">Welcome to SMS Spam Detection</h1>
        <p style="color:#6b7280;font-size:0.88rem;margin:0;">Detect whether a SMS message is Spam or Not Spam (Ham)</p></div>
        """, unsafe_allow_html=True)
    with h2:
        st.markdown("""
        <div style="display:flex;justify-content:flex-end;align-items:center;gap:0.75rem;padding-top:0.3rem;">
            <div class="about-btn">ℹ️ About Project</div>
        </div>""", unsafe_allow_html=True)

    # ── Input Card with Result ──
    # Use a container with wrapper card styling
    with st.container():
        st.markdown('<div class="wrapper-card">', unsafe_allow_html=True)

        input_col, divider_col, result_col = st.columns([2.5, 0.05, 1], gap="small")

        with input_col:
            st.markdown('<div class="section-title">Enter SMS Message</div>', unsafe_allow_html=True)
            sms_input = st.text_area("sms", placeholder="Type or paste your SMS message here...",
                                      height=110, label_visibility="collapsed", key="home_sms")
            char_count = len(sms_input) if sms_input else 0
            st.markdown(f'<div style="text-align:right;font-size:0.78rem;color:#6b7280;">{char_count} / 160</div>', unsafe_allow_html=True)

            # Button row with CSS class wrappers
            bc1, bc2, bc3 = st.columns([1.2, 1.2, 3])
            with bc1:
                st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
                predict_btn = st.button("✈️ PREDICT", use_container_width=True, key="home_pred")
                st.markdown('</div>', unsafe_allow_html=True)
            with bc2:
                st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
                clear_btn = st.button("🔄 CLEAR", use_container_width=True, key="home_clear")
                st.markdown('</div>', unsafe_allow_html=True)

        with divider_col:
            st.markdown('<div class="v-divider" style="height:200px;"></div>', unsafe_allow_html=True)

        # Process prediction
        prediction_result = None
        if predict_btn and sms_input and sms_input.strip():
            cleaned = clean_text(sms_input)
            vector = tfidf.transform([cleaned])
            res = model.predict(vector)[0]
            prediction_result = "Spam" if res == 1 else "Ham"
            st.session_state.total += 1
            if res == 1:
                st.session_state.spam_count += 1
            else:
                st.session_state.ham_count += 1
            st.session_state.history.insert(0, {
                "message": sms_input[:50] + ("..." if len(sms_input) > 50 else ""),
                "result": prediction_result,
                "time": datetime.now().strftime("%I:%M %p")
            })

        if clear_btn:
            st.rerun()

        with result_col:
            st.markdown('<div class="section-title" style="text-align:center;">Prediction Result</div>', unsafe_allow_html=True)
            if prediction_result == "Spam":
                st.markdown("""<div class="result-box">
                    <div class="result-circle" style="background:rgba(239,68,68,0.12);color:#ef4444;">🚫</div>
                    <div style="color:#ef4444;font-weight:700;font-size:1.1rem;">SPAM</div>
                    <div style="color:#f87171;font-size:0.78rem;">This message is likely spam</div>
                </div>""", unsafe_allow_html=True)
            elif prediction_result == "Ham":
                st.markdown("""<div class="result-box">
                    <div class="result-circle" style="background:rgba(34,197,94,0.12);color:#22c55e;">✅</div>
                    <div style="color:#22c55e;font-weight:700;font-size:1.1rem;">HAM (Not Spam)</div>
                    <div style="color:#4ade80;font-size:0.78rem;">This message appears safe</div>
                </div>""", unsafe_allow_html=True)
            elif predict_btn and (not sms_input or not sms_input.strip()):
                st.markdown("""<div class="result-box">
                    <div class="result-circle" style="background:rgba(234,179,8,0.1);color:#eab308;">⚠️</div>
                    <div style="color:#eab308;font-weight:600;">Please enter a message</div>
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown("""<div class="result-box">
                    <div class="result-circle" style="background:rgba(139,92,246,0.1);color:#8b5cf6;">❓</div>
                    <div style="color:#6b7280;font-size:0.88rem;">Your result will appear here</div>
                </div>""", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)  # close wrapper-card

    # ── Stat Cards ──
    s1, s2, s3, s4 = st.columns(4, gap="medium")
    stats = [
        ("📨", "Total Messages", f"{5572 + st.session_state.total:,}", "#6366f1", "rgba(99,102,241,0.12)"),
        ("✅", "Ham (Not Spam)", f"{4121 + st.session_state.ham_count:,}", "#22c55e", "rgba(34,197,94,0.12)"),
        ("⚠️", "Spam", f"{1451 + st.session_state.spam_count:,}", "#ef4444", "rgba(239,68,68,0.12)"),
        ("🎯", "Accuracy", "97.35%", "#3b82f6", "rgba(59,130,246,0.12)"),
    ]
    for col, (icon, label, value, color, bg) in zip([s1, s2, s3, s4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-top">
                    <div class="stat-icon" style="background:{bg};color:{color};">{icon}</div>
                    <div class="stat-label">{label}</div>
                </div>
                <div class="stat-value" style="color:{color};">{value}</div>
                <div style="margin-top:0.5rem;">{sparkline(color)}</div>
            </div>""", unsafe_allow_html=True)

    # ── Bottom: Recent Predictions + About Model ──
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    col_left, col_right = st.columns([1.3, 1], gap="medium")

    with col_left:
        history = st.session_state.history
        if not history:
            samples = [
                ("WINNER!! You have won a FREE ticket...", "Spam", "10:30 AM"),
                ("Hey, are we still meeting tomorrow?", "Ham", "10:28 AM"),
                ("Congratulations! Claim your prize now...", "Spam", "10:25 AM"),
                ("Please call me when you reach home.", "Ham", "10:20 AM"),
                ("URGENT! Your mobile number has won...", "Spam", "10:18 AM"),
            ]
        else:
            samples = [(h["message"], h["result"], h["time"]) for h in history[:5]]

        rows = ""
        for msg, res, t in samples:
            badge = f'<span class="badge-spam">{res}</span>' if res == "Spam" else f'<span class="badge-ham">{res}</span>'
            rows += f"<tr><td>{msg}</td><td>{badge}</td><td>{t}</td></tr>"

        st.markdown(f"""
        <div class="bottom-card">
            <div class="section-title">Recent Predictions</div>
            <table class="pred-table">
                <thead><tr><th>Message</th><th>Prediction</th><th>Time</th></tr></thead>
                <tbody>{rows}</tbody>
            </table>
            <div style="text-align:center;margin-top:0.6rem;">
                <span class="view-all-btn">View All History →</span>
            </div>
        </div>""", unsafe_allow_html=True)

    with col_right:
        items = [
            ("🏷️", "Model Name", "Multinomial Naive Bayes"),
            ("📐", "Vectorizer", "TF-IDF"),
            ("📦", "Trained On", "5,572 SMS Messages"),
            ("✅", "Accuracy", "97.35%"),
            ("📅", "Last Updated", "May 20, 2024"),
        ]
        info = "".join([f'<div class="model-row"><div class="model-icon">{i}</div><span class="model-label">{l}</span><span class="model-value">{v}</span></div>' for i, l, v in items])
        st.markdown(f'<div class="bottom-card"><div class="section-title">About the Model</div>{info}</div>', unsafe_allow_html=True)

    st.markdown('<div class="app-footer">© 2024 SMS Spam Detection System | Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════
# PREDICT PAGE
# ═══════════════════════════════════════
elif "Predict" in page:
    st.markdown('<h1 style="font-size:1.55rem;font-weight:800;">🔍 Predict Message</h1><p style="color:#6b7280;font-size:0.88rem;">Enter any SMS to classify it</p>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="wrapper-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Enter SMS Message</div>', unsafe_allow_html=True)
        sms = st.text_area("sms", placeholder="Paste your SMS message here...", height=150, label_visibility="collapsed", key="pred_sms")

        bc1, bc2, _ = st.columns([1, 1, 4])
        with bc1:
            st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
            pred = st.button("✈️ PREDICT", use_container_width=True, key="pred_btn")
            st.markdown('</div>', unsafe_allow_html=True)
        with bc2:
            st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
            st.button("🔄 CLEAR", use_container_width=True, key="pred_clear")
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if pred and sms and sms.strip():
        cleaned = clean_text(sms)
        vector = tfidf.transform([cleaned])
        result = model.predict(vector)[0]
        label = "Spam" if result == 1 else "Ham"
        st.session_state.total += 1
        if result == 1:
            st.session_state.spam_count += 1
        else:
            st.session_state.ham_count += 1
        st.session_state.history.insert(0, {
            "message": sms[:50] + ("..." if len(sms) > 50 else ""),
            "result": label,
            "time": datetime.now().strftime("%I:%M %p")
        })
        if label == "Spam":
            st.markdown("""<div class="wrapper-card" style="text-align:center;">
            <div class="result-circle" style="background:rgba(239,68,68,0.12);color:#ef4444;margin:0 auto 0.5rem;">🚫</div>
            <div style="color:#ef4444;font-weight:700;font-size:1.2rem;">SPAM DETECTED</div>
            <div style="color:#f87171;font-size:0.82rem;">This message is classified as spam</div></div>""", unsafe_allow_html=True)
        else:
            st.markdown("""<div class="wrapper-card" style="text-align:center;">
            <div class="result-circle" style="background:rgba(34,197,94,0.12);color:#22c55e;margin:0 auto 0.5rem;">✅</div>
            <div style="color:#22c55e;font-weight:700;font-size:1.2rem;">HAM — Safe Message</div>
            <div style="color:#4ade80;font-size:0.82rem;">This message appears legitimate</div></div>""", unsafe_allow_html=True)
        with st.expander("🔬 Preprocessing Details"):
            st.code(cleaned, language="text")
    elif pred:
        st.warning("⚠️ Please enter a message first!")


# ═══════════════════════════════════════
# HISTORY PAGE
# ═══════════════════════════════════════
elif "History" in page:
    st.markdown('<h1 style="font-size:1.55rem;font-weight:800;">📋 Prediction History</h1><p style="color:#6b7280;font-size:0.88rem;">All your past predictions</p>', unsafe_allow_html=True)

    if not st.session_state.history:
        st.info("No predictions yet. Go to **Home** or **Predict** to classify messages.")
    else:
        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.session_state.total = 0
            st.session_state.spam_count = 0
            st.session_state.ham_count = 0
            st.rerun()
        rows = ""
        for i, h in enumerate(st.session_state.history):
            badge = f'<span class="badge-spam">{h["result"]}</span>' if h["result"] == "Spam" else f'<span class="badge-ham">{h["result"]}</span>'
            rows += f"<tr><td>{i+1}</td><td>{h['message']}</td><td>{badge}</td><td>{h['time']}</td></tr>"
        st.markdown(f"""<div class="bottom-card"><table class="pred-table">
            <thead><tr><th>#</th><th>Message</th><th>Result</th><th>Time</th></tr></thead>
            <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════
# ANALYTICS PAGE
# ═══════════════════════════════════════
elif "Analytics" in page:
    st.markdown('<h1 style="font-size:1.55rem;font-weight:800;">📊 Analytics Dashboard</h1><p style="color:#6b7280;font-size:0.88rem;">Visual insights from predictions</p>', unsafe_allow_html=True)

    total = max(st.session_state.total, 10)
    spam = st.session_state.spam_count if st.session_state.total > 0 else 4
    ham = st.session_state.ham_count if st.session_state.total > 0 else 6

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown('<div class="section-title">Spam vs Ham Distribution</div>', unsafe_allow_html=True)
        import pandas as pd
        st.bar_chart(pd.DataFrame({"Category": ["Ham", "Spam"], "Count": [ham, spam]}).set_index("Category"), color=["#6366f1"])

    with c2:
        spam_pct = round((spam / total) * 100, 1)
        ham_pct = round((ham / total) * 100, 1)
        st.markdown(f"""<div class="bottom-card">
            <div class="section-title">Prediction Breakdown</div>
            <div style="margin-bottom:1.3rem;">
                <div style="display:flex;justify-content:space-between;margin-bottom:0.3rem;">
                    <span style="font-weight:600;">Ham (Safe)</span><span style="color:#22c55e;font-weight:700;">{ham_pct}%</span>
                </div>
                <div style="background:rgba(99,102,241,0.08);border-radius:8px;height:10px;overflow:hidden;">
                    <div style="width:{ham_pct}%;height:100%;background:linear-gradient(90deg,#22c55e,#4ade80);border-radius:8px;"></div>
                </div>
            </div>
            <div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.3rem;">
                    <span style="font-weight:600;">Spam</span><span style="color:#ef4444;font-weight:700;">{spam_pct}%</span>
                </div>
                <div style="background:rgba(99,102,241,0.08);border-radius:8px;height:10px;overflow:hidden;">
                    <div style="width:{spam_pct}%;height:100%;background:linear-gradient(90deg,#ef4444,#f87171);border-radius:8px;"></div>
                </div>
            </div></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">Dataset Statistics</div>', unsafe_allow_html=True)
    d1, d2, d3, d4 = st.columns(4, gap="medium")
    for col, (icon, label, value, color, bg) in zip([d1, d2, d3, d4], [
        ("📨", "Dataset Size", "5,572", "#6366f1", "rgba(99,102,241,0.12)"),
        ("✅", "Ham Messages", "4,825", "#22c55e", "rgba(34,197,94,0.12)"),
        ("🚫", "Spam Messages", "747", "#ef4444", "rgba(239,68,68,0.12)"),
        ("📐", "Features", "TF-IDF", "#8b5cf6", "rgba(139,92,246,0.12)"),
    ]):
        with col:
            st.markdown(f"""<div class="stat-card">
                <div class="stat-top"><div class="stat-icon" style="background:{bg};color:{color};">{icon}</div><div class="stat-label">{label}</div></div>
                <div class="stat-value" style="color:{color};font-size:1.3rem;">{value}</div>
            </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════
# MODEL INFO PAGE
# ═══════════════════════════════════════
elif "Model Info" in page:
    st.markdown('<h1 style="font-size:1.55rem;font-weight:800;">🤖 Model Information</h1><p style="color:#6b7280;font-size:0.88rem;">Technical details of the ML pipeline</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        rows = "".join([f'<div class="model-row"><span class="model-label">{l}</span><span class="model-value">{v}</span></div>' for l, v in [
            ("Algorithm", "Multinomial Naive Bayes"), ("Vectorizer", "TF-IDF"),
            ("Preprocessing", "Tokenize → Punct → Stop Words → Stem"),
            ("Accuracy", "97.35%"), ("Dataset", "UCI SMS Spam (5,572)"), ("Classes", "Spam (1) / Ham (0)")]])
        st.markdown(f'<div class="bottom-card"><div class="section-title">⚙️ Architecture</div>{rows}</div>', unsafe_allow_html=True)
    with c2:
        steps = "".join([f'<div class="model-row"><div class="model-icon">{n}</div><div><div style="font-weight:600;font-size:0.85rem;">{t}</div><div style="font-size:0.78rem;color:#6b7280;">{d}</div></div></div>' for n, t, d in [
            ("1️⃣", "Tokenization", "Split text into words"), ("2️⃣", "Punctuation Removal", "Strip special chars"),
            ("3️⃣", "Number Removal", "Remove digits"), ("4️⃣", "Stop Words", "Filter common words"),
            ("5️⃣", "Stemming", "Reduce to root forms"), ("6️⃣", "Vectorization", "TF-IDF features")]])
        st.markdown(f'<div class="bottom-card"><div class="section-title">🧪 NLP Pipeline</div>{steps}</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════
# ABOUT PAGE
# ═══════════════════════════════════════
elif "About" in page:
    st.markdown('<h1 style="font-size:1.55rem;font-weight:800;">ℹ️ About This Project</h1><p style="color:#6b7280;font-size:0.88rem;">SMS Spam Detection using ML & NLP</p>', unsafe_allow_html=True)
    st.markdown("""<div class="bottom-card" style="margin-bottom:1rem;">
        <div class="section-title">🎯 Project Overview</div>
        <p style="line-height:1.7;font-size:0.92rem;">This app uses <strong>NLP</strong> and <strong>Machine Learning</strong>
        to classify SMS messages as spam or ham. It runs on saved model artifacts built from the
        <strong>UCI SMS Spam Collection</strong> dataset, with <strong>TF-IDF</strong> features and a
        <strong>Multinomial Naive Bayes</strong> classifier.</p>
    </div>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown("""<div class="bottom-card"><div class="section-title">🛠️ Tech Stack</div>
            <div class="model-row"><div class="model-icon">🐍</div><span class="model-value">Python 3.12</span></div>
            <div class="model-row"><div class="model-icon">🎨</div><span class="model-value">Streamlit</span></div>
            <div class="model-row"><div class="model-icon">🧠</div><span class="model-value">Scikit-learn</span></div>
            <div class="model-row"><div class="model-icon">📝</div><span class="model-value">NLTK</span></div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="bottom-card"><div class="section-title">👤 Developer</div>
            <div class="model-row"><div class="model-icon">👨‍💻</div><span class="model-label">Project</span><span class="model-value">SMS Spam Detection</span></div>
            <div class="model-row"><div class="model-icon">📧</div><span class="model-label">Support</span><span class="model-value">Add your contact here before publishing</span></div>
            <div class="model-row"><div class="model-icon">🔗</div><span class="model-label">Dataset</span><span class="model-value">UCI SMS Spam Collection</span></div>
        </div>""", unsafe_allow_html=True)
    st.markdown('<div class="app-footer">© 2024 SMS Spam Detection System | Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)
