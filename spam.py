from pyexpat import model

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib

df = pd.read_csv("spam.csv", encoding="latin-1")
X = df["v2"]
y = df["v1"]


x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()), 
    ('model', MultinomialNB(alpha=0.1))
])

pipeline.fit(x_train, y_train)
score = pipeline.score(x_test, y_test)
print(f"Score: {score}")
pred = pipeline.predict(x_test)

print(x_test.iloc[0])
print(pred[0])

joblib.dump(pipeline, "spam_model.pkl")
