def get_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

    /* Global settings */
    .stApp {
        background: #f8fafc !important;
        font-family: 'Outfit', sans-serif !important;
        color: #1e293b;
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
        background: linear-gradient(135deg, #1e3a8a 0%, #4338ca 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 4px 12px rgba(67, 56, 202, 0.15);
    }
    .header-container p {
        font-size: 1.1rem;
        color: #475569;
        margin-top: 0.5rem;
        font-weight: 400;
    }

    /* Main Card Layout */
    .main-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(0, 0, 0, 0.05);
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.08);
        animation: fadeInUp 0.8s ease-out;
    }

    /* Text Area */
    .stTextArea textarea {
        background: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 12px !important;
        color: #334155 !important;
        font-size: 1.05rem !important;
        padding: 1.2rem !important;
        transition: all 0.3s ease !important;
        font-family: 'Outfit', sans-serif !important;
        box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.02);
    }
    .stTextArea textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2) !important;
        outline: none !important;
    }
    .stTextArea textarea::placeholder {
        color: #94a3b8 !important;
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
        box-shadow: 0 10px 25px -5px rgba(124, 58, 237, 0.3) !important;
    }
    [data-testid="stFormSubmitButton"] button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 35px -5px rgba(124, 58, 237, 0.45) !important;
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
        background: rgba(254, 226, 226, 0.7);
        border: 1px solid rgba(248, 113, 113, 0.4);
    }
    .result-box.spam-box h3 {
        color: #991b1b;
        margin: 0.5rem 0;
        font-size: 1.5rem;
    }
    .result-box.spam-box p { color: #dc2626; margin: 0; }
    
    .result-box.ham-box {
        background: rgba(220, 252, 231, 0.7);
        border: 1px solid rgba(74, 222, 128, 0.4);
    }
    .result-box.ham-box h3 {
        color: #166534;
        margin: 0.5rem 0;
        font-size: 1.5rem;
    }
    .result-box.ham-box p { color: #15803d; margin: 0; }

    .result-box.warning-box {
        background: rgba(254, 249, 195, 0.7);
        border: 1px solid rgba(250, 204, 21, 0.4);
    }
    .result-box.warning-box h3 {
        color: #854d0e;
        margin: 0.5rem 0;
        font-size: 1.5rem;
    }
    .result-box.warning-box p { color: #a16207; margin: 0; }

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
        font-weight: 400;
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
