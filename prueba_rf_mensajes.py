import json
import joblib
from nltk.corpus import stopwords
import nltk

modelo_path = 'gambling_detector_per_msg.pkl'
modelo = joblib.load(modelo_path)
nltk.download('stopwords')
spanish_stopwords = stopwords.words('spanish')

#Usuarios no gambling
usuarios = [
    "user174",
    "user179",
    "user210",
    "user246",
    "user301",
    "user420",
    "user435",
    "user466",
    "user580",
    "user658",
    "user689",
    "user712",
    "user771",
    "user1149",
    "user1178",
    "user1181",
    "user1211",
    "user1259",
    "user1399",
    "user1441"
]


data = []  
#Leer todos los mensajes y guardarlos en una lista de mensajes
for user in usuarios:
    with open(f'task1_train/subjects/{user}.json', 'r', encoding='utf-8') as f:
        contenido = json.load(f)
        if isinstance(contenido, list):
            data += contenido
        else:
            data.append(contenido)
mensajes = [
    str(item['message']) for item in data
    if isinstance(item, dict) and 'message' in item and isinstance(item['message'], str)
]

#Predecir para todos los mensajes
probs = modelo.predict_proba(mensajes)

#Los que sean positivos, se escriben
with open('prueba_modelo_random_forest.txt', 'w', encoding='utf-8') as out_file:
    for mensaje, prob in zip(mensajes, probs):
        if prob[1]>0.4:
            out_file.write(f"{mensaje}\t{prob[1]:.4f}\n")
