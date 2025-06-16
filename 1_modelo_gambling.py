from sentence_transformers import SentenceTransformer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import json
import os
import joblib

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

#Leer etiquetas
usuarios_riesgos = {}
with open("task1_train/gold_task1.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 2:
            nick = parts[0]
            risk = parts[1]
            usuarios_riesgos[nick] = float(risk)

usuarios_datos = {}
directorio_datos = "task1_train/subjects"
#Crear el diccionario concatenando para cada usuario todo su texto
for filename in os.listdir(directorio_datos):
    if filename.endswith(".json"):
        nick = filename.replace(".json", "")
        if nick in usuarios_riesgos:
            with open(os.path.join(directorio_datos, filename), "r", encoding="utf-8") as f:
                mensajes = json.load(f)
                mensaje = []
                for msg in mensajes:
                    if "message" in msg:
                        mensaje.append(str(msg["message"]))

                texto = " ".join(mensaje)
                usuarios_datos[nick] = {"text": texto, "risk": usuarios_riesgos[nick]}

#Preparar los datos para el modelo SVC
textos = []
y = []
for data in usuarios_datos.values():
    textos.append(data["text"])
    y.append(data["risk"])

#Evaluacion
X = model.encode(textos)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
svm = SVC(probability=True)
svm.fit(X_train, y_train)
accuracy = svm.score(X_test, y_test)
print(f"Precisión en test: {accuracy}")
#Entrenamiento final
svm_full = SVC(probability=True)
svm_full.fit(X, y)
joblib.dump(svm_full, "svm_gambling_text.pkl")

