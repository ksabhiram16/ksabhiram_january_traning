import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_excel("/mnt/data/Spam Email Detection.xlsx")
df.head()

df.columns

df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X = df['message']   # Email text
y = df['label']     # Spam or Not Spam

vectorizer = TfidfVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

y_pred = svm_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))


new_email = ["Congratulations! You won a free prize. Click now!"]

new_email_vectorized = vectorizer.transform(new_email)
prediction = svm_model.predict(new_email_vectorized)

if prediction[0] == 1:
    print("Spam Email ❌")
else:
    print("Not Spam Email ✅")
