from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


X_train = [
    "check room availability", "what rooms are free", "show available rooms",
    "book a room", "I want to book a room", "reserve a room",
    "I want to order food", "order pizza", "I want burger",
    "hello", "hi", "hey",
    "bye", "goodbye", "see you"
]
y_train = [
    "check_availability", "check_availability", "check_availability",
    "book_room", "book_room", "book_room",
    "order_food", "order_food", "order_food",
    "greeting", "greeting", "greeting",
    "goodbye", "goodbye", "goodbye"
]


vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)

clf = MultinomialNB()
clf.fit(X_train_counts, y_train)


def predict_intent(text):
    text = text.lower()
    X_test_counts = vectorizer.transform([text])
    pred = clf.predict(X_test_counts)[0]
    print(f"[DEBUG] User Input: {text} -> Predicted Intent: {pred}")
    return pred
