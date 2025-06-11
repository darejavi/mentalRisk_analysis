from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
import nltk
from nltk.corpus import stopwords
import joblib

#Generation of AI
def read_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


#Leer los dos archivos creados anteriormente
gambling_texts = read_lines("frases_gambling.txt")
non_gambling_texts = read_lines("non_gambling.txt")
textos = gambling_texts + non_gambling_texts
labels = [1] * len(gambling_texts) + [0] * len(non_gambling_texts)


X_train, X_test, y_train, y_test = train_test_split(textos, labels, test_size=0.2, random_state=42)

nltk.download('stopwords')
spanish_stopwords = stopwords.words('spanish')
vectorizer = TfidfVectorizer(max_features=5000, stop_words=spanish_stopwords)

pipeline = make_pipeline(
    vectorizer,  
    RandomForestClassifier(class_weight='balanced', 
                           n_estimators=100,
                           )  
)
# Evaluacion
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Reporte de clasificación:\n", classification_report(y_test, y_pred))
#Entrenamiento con todos los datos
pipeline.fit(textos, labels)  
joblib.dump(pipeline, "gambling_detector_per_msg.pkl")
