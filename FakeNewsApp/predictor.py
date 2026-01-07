import pickle
import os

# Load model and vectorizer
model_path = os.path.join(os.getcwd(), "model.pkl")
vectorizer_path = os.path.join(os.getcwd(), "vectorizer.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

def predict_news(title, author, text):
    if not text.strip():
        return "Invalid input"
    
    combined = f"{title} {author} {text}"
    transformed_text = vectorizer.transform([combined])
    prediction = model.predict(transformed_text)[0]
    
    return "FAKE" if prediction == 1 else "REAL"
