"""Custom CSS styles matching the reference dashboard design."""

def get_css(dark_mode=False):
    bg = "#111127" if dark_mode else "#f0f2f8"
    card_bg = "rgba(25,25,50,0.92)" if dark_mode else "#ffffff"
    text_color = "#e2e2f0" if dark_mode else "#1a1a2e"
    text_muted = "#9a9ab0" if dark_mode else "#6b7280"
    border_color = "rgba(255,255,255,0.07)" if dark_mode else "rgba(0,0,0,0.07)"
    input_bg = "#1e1e3a" if dark_mode else "#f8f9fc"
    input_border = "rgba(255,255,255,0.1)" if dark_mode else "#e2e5f1"

    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    .stApp {{
        background: {bg} !important;
        font-family: 'Inter', sans-serif !important;
        color: {text_color};
    }}
    header[data-testid="stHeader"] {{ background: transparent !important; }}
    #MainMenu, footer, .stDeployButton {{ display: none !important; }}
    .block-container {{
        padding: 1.2rem 2rem 2rem 2rem !important;
        max-width: 1150px;
    }}

    /* ===== SIDEBAR ===== */
    section[data-testid="stSidebar"] {{ width: 220px !important; min-width: 220px !important; }}
    section[data-testid="stSidebar"] > div:first-child {{
        background: linear-gradient(180deg, #1a1650 0%, #252363 35%, #3730a3 70%, #4f46e5 100%) !important;
        padding: 1.2rem 0.8rem !important;
        width: 220px !important;
    }}
    /* Hide radio label header */
    section[data-testid="stSidebar"] [data-testid="stRadio"] > label {{ display: none !important; }}
    /* Hide radio circle/dot */
    section[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label > div:first-child {{ display: none !important; }}
    section[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] {{ gap: 3px !important; }}
    /* Nav items — bright white text */
    section[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label {{
        color: rgba(255,255,255,0.85) !important;
        font-size: 0.93rem !important;
        font-weight: 500 !important;
        padding: 0.6rem 1rem !important;
        border-radius: 10px !important;
        cursor: pointer !important;
        transition: all 0.25s ease !important;
        background: transparent !important;
    }}
    /* Hover */
    section[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label:hover {{
        background: rgba(255,255,255,0.12) !important;
        color: #ffffff !important;
    }}
    /* Active nav item — multiple selectors for compatibility */
    section[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"],
    section[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label[aria-checked="true"],
    section[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked),
    section[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] div[data-checked="true"] label,
    section[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] div[role="radio"][aria-checked="true"] {{
        background: rgba(99,102,241,0.5) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 8px rgba(99,102,241,0.3);
    }}
    /* Dark mode toggle */
    section[data-testid="stSidebar"] .stToggle label {{
        color: rgba(255,255,255,0.8) !important;
        font-size: 0.85rem !important;
    }}
    /* Sidebar illustration */
    .sidebar-illustration {{
        text-align: center;
        padding: 1rem 0.5rem;
        margin-top: 1rem;
        position: relative;
    }}
    .sidebar-illustration .phone-group {{
        position: relative;
        display: inline-block;
    }}
    .sidebar-illustration .phone {{
        background: rgba(255,255,255,0.12);
        border-radius: 14px;
        padding: 0.6rem;
        display: inline-flex;
        flex-direction: column;
        gap: 0.3rem;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255,255,255,0.1);
    }}
    .sidebar-illustration .msg {{
        padding: 0.25rem 0.5rem;
        border-radius: 8px;
        font-size: 0.6rem;
        max-width: 90px;
        line-height: 1.3;
    }}
    .sidebar-illustration .msg-purple {{
        background: #7c3aed;
        color: white;
        align-self: flex-start;
    }}
    .sidebar-illustration .msg-white {{
        background: rgba(255,255,255,0.9);
        color: #1a1a2e;
        align-self: flex-end;
    }}
    .sidebar-illustration .spam-badge {{
        position: absolute;
        top: -8px;
        right: -12px;
        background: #ef4444;
        color: white;
        padding: 0.15rem 0.5rem;
        border-radius: 6px;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        box-shadow: 0 2px 8px rgba(239,68,68,0.4);
    }}
    .sidebar-illustration .check-badge {{
        position: absolute;
        bottom: -5px;
        right: -10px;
        background: #22c55e;
        color: white;
        width: 22px;
        height: 22px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.7rem;
        box-shadow: 0 2px 6px rgba(34,197,94,0.4);
    }}

    /* ===== WRAPPER CARD ===== */
    .wrapper-card {{
        background: {card_bg}; border: 1px solid {border_color};
        border-radius: 18px; padding: 1.5rem 1.8rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        margin-bottom: 1rem;
    }}

    /* ===== TEXTAREA ===== */
    .stTextArea textarea {{
        background: {input_bg} !important; border: 1.5px solid {input_border} !important;
        border-radius: 12px !important; font-family: 'Inter', sans-serif !important;
        font-size: 0.92rem !important; color: {text_color} !important;
        padding: 0.9rem 1rem !important; resize: none !important;
    }}
    .stTextArea textarea:focus {{
        border-color: #6366f1 !important; box-shadow: 0 0 0 3px rgba(99,102,241,0.12) !important;
    }}
    .stTextArea label {{ display: none !important; }}

    /* ===== BUTTONS ===== */
    .stButton > button {{
        border-radius: 10px !important; font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important; padding: 0.55rem 1.8rem !important;
        font-size: 0.85rem !important; transition: all 0.3s ease !important;
    }}
    /* Predict */
    .predict-btn .stButton > button {{
        background: linear-gradient(135deg, #5b5bd6, #7c3aed) !important;
        color: white !important; border: none !important;
        box-shadow: 0 4px 14px rgba(99,102,241,0.3) !important;
    }}
    .predict-btn .stButton > button:hover {{
        box-shadow: 0 6px 20px rgba(99,102,241,0.45) !important; transform: translateY(-1px);
    }}
    /* Clear */
    .clear-btn .stButton > button {{
        background: {card_bg} !important; color: {text_muted} !important;
        border: 1.5px solid {border_color} !important;
    }}
    .clear-btn .stButton > button:hover {{
        border-color: #6366f1 !important; color: #6366f1 !important;
    }}

    /* ===== STAT CARDS ===== */
    .stat-card {{
        background: {card_bg}; border: 1px solid {border_color};
        border-radius: 16px; padding: 1rem 1.1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    .stat-card:hover {{
        transform: translateY(-3px); box-shadow: 0 8px 25px rgba(99,102,241,0.1);
    }}
    .stat-top {{ display: flex; align-items: center; gap: 0.7rem; margin-bottom: 0.1rem; }}
    .stat-icon {{
        width: 40px; height: 40px; border-radius: 12px;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.1rem; flex-shrink: 0;
    }}
    .stat-label {{ font-size: 0.78rem; color: {text_muted}; font-weight: 500; }}
    .stat-value {{ font-size: 1.55rem; font-weight: 700; margin: 0.15rem 0 0; line-height: 1.2; }}

    /* ===== SECTION TITLES ===== */
    .section-title {{
        font-size: 1rem; font-weight: 700; color: #6366f1; margin-bottom: 0.8rem;
    }}

    /* ===== BOTTOM CARD ===== */
    .bottom-card {{
        background: {card_bg}; border: 1px solid {border_color};
        border-radius: 16px; padding: 1.3rem 1.4rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}

    /* ===== TABLE ===== */
    .pred-table {{ width: 100%; border-collapse: separate; border-spacing: 0; font-size: 0.85rem; }}
    .pred-table th {{
        text-align: left; padding: 0.5rem 0.7rem; color: {text_muted};
        font-weight: 600; font-size: 0.78rem; border-bottom: 1.5px solid {border_color};
    }}
    .pred-table td {{
        padding: 0.55rem 0.7rem; border-bottom: 1px solid {border_color};
        color: {text_color}; font-size: 0.84rem;
    }}
    .pred-table tr:last-child td {{ border-bottom: none; }}
    .pred-table tr:hover td {{ background: rgba(99,102,241,0.04); }}
    .badge-spam {{
        background: rgba(239,68,68,0.13); color: #ef4444;
        padding: 0.15rem 0.6rem; border-radius: 20px; font-size: 0.76rem; font-weight: 600;
    }}
    .badge-ham {{
        background: rgba(34,197,94,0.13); color: #22c55e;
        padding: 0.15rem 0.6rem; border-radius: 20px; font-size: 0.76rem; font-weight: 600;
    }}
    .view-all-btn {{
        display: inline-flex; align-items: center; gap: 0.3rem;
        margin-top: 0.8rem; padding: 0.4rem 1rem;
        border: 1.5px solid {border_color}; border-radius: 20px;
        font-size: 0.8rem; font-weight: 500; color: {text_muted};
        background: transparent; cursor: pointer;
    }}

    /* ===== MODEL INFO ===== */
    .model-row {{
        display: flex; align-items: center; gap: 0.65rem;
        padding: 0.55rem 0; border-bottom: 1px solid {border_color}; font-size: 0.88rem;
    }}
    .model-row:last-child {{ border-bottom: none; }}
    .model-icon {{
        width: 30px; height: 30px; border-radius: 8px;
        background: rgba(99,102,241,0.1);
        display: flex; align-items: center; justify-content: center; font-size: 0.82rem;
    }}
    .model-label {{ color: {text_muted}; font-weight: 600; min-width: 95px; font-size: 0.84rem; }}
    .model-value {{ color: {text_color}; font-weight: 500; font-size: 0.84rem; }}

    /* ===== RESULT DISPLAY ===== */
    .result-box {{
        text-align: center; padding: 0.5rem 0;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        min-height: 200px;
    }}
    .result-circle {{
        width: 80px; height: 80px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 2.2rem; margin-bottom: 0.6rem;
    }}

    /* ===== SIDEBAR BRAND ===== */
    .sidebar-brand {{
        text-align: center; padding: 0.5rem 0 1.2rem;
        border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 0.8rem;
    }}
    .sidebar-brand .brand-icon {{ font-size: 2rem; margin-bottom: 0.15rem; display: block; }}
    .sidebar-brand h2 {{ color: #fff; font-size: 1rem; font-weight: 700; margin: 0; }}
    .sidebar-brand p {{ color: rgba(255,255,255,0.45); font-size: 0.72rem; margin: 0.15rem 0 0; }}

    /* ===== HEADER ===== */
    .main-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.2rem; }}
    .main-header h1 {{ font-size: 1.55rem; font-weight: 800; color: {text_color}; margin: 0 0 0.15rem; }}
    .main-header .subtitle {{ color: {text_muted}; font-size: 0.88rem; margin: 0; }}
    .about-btn {{
        background: #1e1b4b; color: #fff; padding: 0.45rem 1rem;
        border-radius: 20px; font-size: 0.82rem; font-weight: 600;
        display: flex; align-items: center; gap: 0.4rem;
    }}

    /* ===== DIVIDER LINE (vertical) ===== */
    .v-divider {{
        width: 1.5px; background: {border_color}; min-height: 100%;
        margin: 0 auto;
    }}

    /* ===== FOOTER ===== */
    .app-footer {{
        text-align: center; padding: 1.2rem 0 0.5rem; color: {text_muted};
        font-size: 0.8rem; border-top: 1px solid {border_color}; margin-top: 1.5rem;
    }}

    @media (max-width: 768px) {{
        .block-container {{ padding: 0.8rem !important; }}
        .stat-value {{ font-size: 1.2rem; }}
    }}
    </style>
    """
