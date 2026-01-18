import pandas as pd
import string
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

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

# Trainings- und Testdaten aufteilen (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=12, stratify=labels
)

# Bag-of-Words erzeugen
vectorizer = CountVectorizer(stop_words="english")

X_train_bow = vectorizer.fit_transform(X_train)
X_test_bow = vectorizer.transform(X_test)

# Naive-Bayes-Modell trainieren
model = MultinomialNB()
model.fit(X_train_bow, y_train)

# Vorhersage auf Testdaten
y_pred = model.predict(X_test_bow)

# Evaluation
print("Training abgeschlossen.")
print("Trainingsbeispiele:", len(X_train))
print("Testbeispiele:", len(X_test))

print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nKlassifikationsbericht:")
print(classification_report(y_test, y_pred))



feature_names = vectorizer.get_feature_names_out()

# Top-Werte der Wörter für Spam und Ham
log_probs = model.feature_log_prob_

classes = model.classes_

for i, cls in enumerate(classes):
    top10 = np.argsort(log_probs[i])[-10:]
    print(f"\nTop Wörter für Klasse '{cls}':")
    for k in reversed(top10):
        print(f"{feature_names[k]} ({log_probs[i][k]:.3f})")

# Index der Klassen finden
spam_index = list(model.classes_).index("spam")
ham_index = list(model.classes_).index("ham")

# Differenz der log-Wahrscheinlichkeiten
diff = model.feature_log_prob_[spam_index] - model.feature_log_prob_[ham_index]

# Top-Wörter für Ham (Aussagekraft)
top_ham = np.argsort(diff)[:10]

print("\nWörter, die am stärksten für HAM sprechen:")
for i in top_ham:
    print(f"{feature_names[i]} ({diff[i]:.3f})")

# Top-Wörter für Spam (Aussagekraft)
top_spam = np.argsort(diff)[-10:]

print("\nWörter, die am stärksten für SPAM sprechen:")
for i in reversed(top_spam):
    print(f"{feature_names[i]} ({diff[i]:.3f})")