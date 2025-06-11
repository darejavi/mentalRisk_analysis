
def contar_0s_y_1s(ruta_archivo):
    contador_0 = 0
    contador_1 = 0

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                etiqueta = partes[1]
                if etiqueta == "0":
                    contador_0 += 1
                elif etiqueta == "1":
                    contador_1 += 1

    print(f"Numero de 0s: {contador_0}")
    print(f"Numero de 1s: {contador_1}")


ruta = "task1_train/gold_task1.txt"
contar_0s_y_1s(ruta)
