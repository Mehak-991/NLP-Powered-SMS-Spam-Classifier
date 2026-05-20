import pandas as pd
import zipfile
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score
import pickle

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

# 1. Load Data
with zipfile.ZipFile('sms+spam+collection.zip') as z:
    with z.open('SMSSpamCollection') as f:
        data = pd.read_csv(f, sep='\t', header=None, encoding='utf-8')
data.rename(columns={0: 'Category', 1: 'Email Text'}, inplace=True)
data = data.drop_duplicates(keep='first').reset_index(drop=True)

# 2. Text Preprocessing
port_stemmer = PorterStemmer()
sw = set(stopwords.words('english'))

def clean_text(text):
    text = word_tokenize(text)
    text= " ".join(text)
    text = [char for char in text if char not in string.punctuation]
    text = ''.join(text)
    text = [char for char in text if char not in re.findall(r"[0-9]", text)]
    text = ''.join(text)
    text = [word.lower() for word in text.split() if word.lower() not in sw]
    text = list(map(lambda x: port_stemmer.stem(x), text))
    return " ".join(text)

print("Cleaning text data... this may take a moment.")
data['Clean Email'] = data['Email Text'].apply(clean_text)

# 3. Encoding Labels (ham=0, spam=1)
encoder = LabelEncoder()
data['target'] = encoder.fit_transform(data['Category'])

# 4. Feature Extraction
print("Vectorizing data...")
tf = TfidfVectorizer(max_features=3000)
X = tf.fit_transform(data['Clean Email']).toarray()
y = data['target'].values

# 5. Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
mnb = MultinomialNB()
print("Training model...")
mnb.fit(X_train, y_train)
y_pred = mnb.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Precision: {precision_score(y_test, y_pred)}")

# 6. Save Model
pickle.dump(tf, open('vectorizer.pkl', 'wb'))
pickle.dump(mnb, open('model.pkl', 'wb'))
print("Model and Vectorizer saved successfully.")
