import os
import json

# Rutas
ruta_etiquetas = "task1_train/gold_task1.txt"
ruta_jsons = "task1_train/subjects"
salida = "non_gambling.txt"

#Usar los usuarios no adictos
non_gambling_users = []
with open(ruta_etiquetas, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        nick, label = line.split(",")
        if label.strip() == "0":
            non_gambling_users.append(nick.strip())

#Recorrer sus ficheros e ir guardando mensajes
mensajes_usuarios = []
for nick in non_gambling_users:
    json_path = os.path.join(ruta_jsons, f"{nick}.json")
    with open(json_path, "r", encoding="utf-8") as f:
        mensajes = json.load(f)
        for msg in mensajes:
            if "message" in msg:
                texto = msg["message"]
                if texto:
                    mensajes_usuarios.append(texto)

#Escribir mensajes
with open(salida, "w", encoding="utf-8") as f:
    for msg in mensajes_usuarios:
        f.write(msg + "\n")
