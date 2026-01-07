import pandas as pd
import string
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("train.csv")  # Make sure this file is in your project folder

# Combine title, author, and text into one field
df['content'] = df['author'].fillna('') + ' ' + df['title'].fillna('') + ' ' + df['text'].fillna('')

# Drop rows with missing content or label
df = df[['content', 'label']].dropna()

# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Apply preprocessing
df['content'] = df['content'].apply(clean_text)

# Features and labels
X = df['content']
y = df['label']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_tfidf = vectorizer.fit_transform(X_train)

# Train the model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved successfully!")
