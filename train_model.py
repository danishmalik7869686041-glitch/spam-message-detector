import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pickle

# Sample SMS dataset
data = {
    "label": [
        "ham", "ham", "spam", "ham", "spam",
        "ham", "ham", "spam", "ham", "spam",
        "ham", "ham", "spam", "ham", "spam",
        "ham", "spam", "ham", "ham", "spam"
    ],
    "message": [
        "Hey, are you coming to class today?",
        "Can you call me when you are free?",
        "Congratulations! You won a free prize. Claim now!",
        "Please send me the notes.",
        "URGENT! You have won a cash reward. Click now!",
        "What time is the meeting?",
        "Your account has won a free lottery prize!",
        "I will reach home in 10 minutes.",
        "Don't forget to submit your assignment.",
        "You have been selected for a FREE gift. Reply now!",
        "Can we meet tomorrow?",
        "Thanks for your message.",
        "WINNER! Claim your exclusive cash prize today!",
        "Are you available for a call?",
        "Get free coupons worth $500. Click the link now!",
        "See you at college tomorrow.",
        "You won a guaranteed prize. Call now!",
        "Please bring the project file.",
        "How are you doing?",
        "Congratulations! You are a lucky winner!"
    ]
}

df = pd.DataFrame(data)

# Convert labels into numbers
df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    df["message"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )),
    ("classifier", MultinomialNB())
])

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save trained model
with open("spam_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully as spam_model.pkl")