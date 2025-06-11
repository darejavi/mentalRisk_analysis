import json
import joblib
from nltk.corpus import stopwords
import nltk

modelo_path = 'gambling_detector_per_msg.pkl'
modelo = joblib.load(modelo_path)
nltk.download('stopwords')
spanish_stopwords = stopwords.words('spanish')

usuarios_no_gambling = [
    "user174", "user179", "user210", "user246", "user301", "user420",
    "user435", "user466", "user580", "user658","user689", "user712",
    "user771", "user1149", "user1178", "user1181", "user1211", "user1259",
    "user1399", "user1441"
]

usuarios_gambling = [
    "user253", "user2536", "user283", "user2865", "user292", "user295",
    "user2952", "user300", "user325", "user3546", "user3650", "user3690",
    "user3784", "user3946", "user3959", "user4058", "user4060", "user4128",
    "user4130", "user4180"
]
#Se tiene que cambiar este valor para probar
confianza= 0.4
data = []
Fp = []  

#Falsos positivos
with open('mensajes_falsos_positivos.txt', 'w', encoding='utf-8') as out_file:
    for user in usuarios_no_gambling:
        with open(f'task1_train/subjects/{user}.json', 'r', encoding='utf-8') as f:
            mensajes = json.load(f)
            for msg in mensajes:
                if "message" in msg:
                    prob = modelo.predict_proba([msg["message"]])
                    if prob[0][1]>confianza:
                        out_file.write(f"{msg['message']}\t{prob[0][1]:.4f}\n")
                        if user not in Fp:
                            Fp.append(user)




Tp = []
Fn = []
#Verdaderos positivos (los no detectados son falsos negativos)
for user in usuarios_gambling:
    with open(f'task1_train/subjects/{user}.json', 'r', encoding='utf-8') as f:
        mensajes = json.load(f)
        for msg in mensajes:
            if "message" in msg:
                probs = modelo.predict_proba([msg["message"]])
                if probs[0][1]>confianza:
                    if user not in Tp:
                        Tp.append(user)

with open('true_positives_y_false_negatives.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(f"Hay {len(Tp)} true positives, {len(usuarios_gambling)-len(Tp)} false negatives\n y {len(Fp)} false positives en un total de {len(usuarios_gambling)+len(usuarios_no_gambling)} usuarios")
    for user in usuarios_gambling:
        if user not in Tp:
             out_file.write(f"{user} se ha detectado como Fn \n")
        else:
             out_file.write(f"{user} se ha detectado como Tp\n")
    for user in Fp:
         out_file.write(f"{user} se ha detectado como Fp\n")
         
             
             
          

        
                     
                     