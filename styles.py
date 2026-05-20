def get_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

    /* Global settings */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(14, 26, 64) 0%, rgb(4, 11, 23) 90%) !important;
        font-family: 'Outfit', sans-serif !important;
        color: #e2e8f0;
    }
    
    /* Hide top bar and footer elements of Streamlit */
    header[data-testid="stHeader"] { background: transparent !important; }
    #MainMenu, footer, .stDeployButton { display: none !important; }

    /* Adjust main padding */
    .block-container {
        padding: 3rem 1.5rem !important;
        max-width: 800px; 
        margin: 0 auto;
    }

    /* Header styling */
    .header-container {
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeInDown 0.8s ease-out;
    }
    .header-container h1 {
        font-size: 2.8rem;
        font-weight: 700;
        margin: 0;
        background: linear-gradient(135deg, #a8c0ff 0%, #3f2b96 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 4px 12px rgba(63, 43, 150, 0.4);
    }
    .header-container p {
        font-size: 1.1rem;
        color: #94a3b8;
        margin-top: 0.5rem;
        font-weight: 300;
    }

    /* Main Card Layout */
    .main-card {
        background: rgba(15, 23, 42, 0.4);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        animation: fadeInUp 0.8s ease-out;
    }

    /* Text Area */
    .stTextArea textarea {
        background: rgba(0, 0, 0, 0.25) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: #f8fafc !important;
        font-size: 1.05rem !important;
        padding: 1.2rem !important;
        transition: all 0.3s ease !important;
        font-family: 'Outfit', sans-serif !important;
        box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.1);
    }
    .stTextArea textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2) !important;
        outline: none !important;
    }
    .stTextArea textarea::placeholder {
        color: #64748b !important;
    }

    /* Form Submit Button */
    [data-testid="stFormSubmitButton"] button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        padding: 0.7rem 1.5rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 25px -5px rgba(124, 58, 237, 0.4) !important;
    }
    [data-testid="stFormSubmitButton"] button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 35px -5px rgba(124, 58, 237, 0.6) !important;
    }
    [data-testid="stFormSubmitButton"] button:active {
        transform: translateY(1px);
    }

    /* Result Boxes */
    .result-box {
        margin-top: 2rem;
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        animation: scaleIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .result-box.spam-box {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    .result-box.spam-box h3 {
        color: #fca5a5;
        margin: 0.5rem 0;
        font-size: 1.5rem;
    }
    .result-box.spam-box p { color: #f87171; margin: 0; }
    
    .result-box.ham-box {
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid rgba(34, 197, 94, 0.3);
    }
    .result-box.ham-box h3 {
        color: #bbf7d0;
        margin: 0.5rem 0;
        font-size: 1.5rem;
    }
    .result-box.ham-box p { color: #86efac; margin: 0; }

    .result-box.warning-box {
        background: rgba(234, 179, 8, 0.1);
        border: 1px solid rgba(234, 179, 8, 0.3);
    }
    .result-box.warning-box h3 {
        color: #fef08a;
        margin: 0.5rem 0;
        font-size: 1.5rem;
    }
    .result-box.warning-box p { color: #fde047; margin: 0; }

    .icon {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.85rem;
        color: #64748b;
        font-weight: 300;
    }

    /* Animations */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
    }
    </style>
    """
