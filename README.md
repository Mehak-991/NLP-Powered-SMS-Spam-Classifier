# SMS Spam Detection

Interactive Streamlit app for classifying SMS messages as spam or ham using a trained NLP pipeline.

## Overview

This project packages a lightweight SMS spam classifier with a clean UI, saved model artifacts, and the same preprocessing flow used during training. The app loads the trained vectorizer and model directly, so you can run predictions without retraining.

## Project Contents

- `app.py` - Streamlit application and prediction flow
- `styles.py` - Custom UI styling for the dashboard
- `model.pkl` - Trained classification model
- `vectorizer.pkl` - Saved TF-IDF vectorizer
- `requirements.txt` - Python dependencies
- `UCI SMS Spam.ipynb` - Training and experimentation notebook

## Dataset

The project is based on the UCI SMS Spam Collection dataset. It contains SMS messages labeled as spam or ham and is commonly used for binary text classification tasks. See the notebook for the exact download and attribution details.

## Requirements

- Python 3.8–3.11 (recommended)
- See `requirements.txt` for pinned runtime dependencies

Install the project dependencies with:

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows PowerShell
pip install -r requirements.txt
```

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

On Windows PowerShell the full sequence is:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Results

The saved model in this repository was trained to detect spam messages with strong precision on the test split.

| Metric | Score |
|---|---:|
| Accuracy | 97.10% |
| Precision | 100% |
| Recall | 76.19% |
| F1-score | 86.49% |

These metrics were computed on the test split recorded in `UCI SMS Spam.ipynb`.

## What’s Included

- `app.py` — Streamlit application and prediction flow. Loads `vectorizer.pkl` and `model.pkl` at runtime.
- `styles.py` — Custom CSS used by the Streamlit UI.
- `model.pkl` / `vectorizer.pkl` — Trained classifier and TF-IDF vectorizer used by the app.
- `UCI SMS Spam.ipynb` — Notebook used for data exploration, preprocessing, training and evaluation.

## Model & Artifacts

The repository ships the trained model and TF-IDF vectorizer so you can run the app without retraining. Key details:

- Algorithm: scikit-learn classifier (see notebook for exact model and hyperparameters)
- Artifacts: `model.pkl`, `vectorizer.pkl`
- To retrain: open and run `UCI SMS Spam.ipynb`; replace the artifacts with newly exported files.

## Data & Preprocessing

Preprocessing steps applied during training include:

- Lowercasing, punctuation removal, and tokenization
- Stopword removal and optional stemming
- TF-IDF vectorization (saved as `vectorizer.pkl`)

See `UCI SMS Spam.ipynb` for the exact preprocessing pipeline and reproducible training/evaluation code.

## Examples

Try these sample messages in the app to see typical outputs:

- "Free entry in 2 a weekly competition to win FA Cup tickets. Text WIN to 12345" → **spam**
- "Hey, are we still meeting for dinner tonight?" → **ham**
- "Congratulations! You have won a $1000 gift card. Reply STOP to opt-out." → **spam**

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repo and create a feature branch.
2. Add tests and update `requirements.txt` if new runtime deps are required.
3. Open a pull request describing your changes.

## License

This project is provided under the MIT License — add a `LICENSE` file to publish the project publicly.

## Contact

Questions, issues or feature requests: missmehak755@gmail.com

---

If you want, I can also add a `LICENSE` file (MIT) and a minimal `Dockerfile` for containerized runs. Would you like me to add those now?