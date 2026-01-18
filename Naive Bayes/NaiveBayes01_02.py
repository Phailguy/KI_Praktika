import pandas as pd
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# CSV-Datei laden
df = pd.read_csv("spam_ham_dataset.csv")

# Nur relevante Spalten verwenden
texts = df["text"].astype(str)
labels = df["label"].astype(str)

# Textvorverarbeitung
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

texts = texts.apply(clean_text)

# Bag-of-Words erzeugen
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(texts)

# Klassifikator trainieren
model = MultinomialNB()
model.fit(X, labels)

print("Training abgeschlossen.")
print("Anzahl Trainingsbeispiele:", len(df))
print("Spam:", sum(labels == "spam"), "Ham:", sum(labels == "ham"))


