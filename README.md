ESPAÑOL  
Este github contiene la participación del grupo HULAT_UC3M en la tarea de MentalRiskES. Los datos están disponibles en https://sites.google.com/view/mentalriskes2025. La funcionalidad de cada uno de los programas es la siguiente:  
  0_preprocesado sirve para contar las etiquetas de las anotaciones  
  1_modelo_gambling entrena el modelo SVM además de hacer una evaluación interna. Finaliza con la serialización del mismo  
  2_generar_frases es un programa generado por ChatGPT con la finalidad de crear frases anotadas a nivel de mensaje  
  3_crear_no_gambling_txt utiliza usuarios no catalogados como adicctos y crea un archivo de texto con sus mensajes  
  4_random_forest crea el modelo de RF utilizando los archivos generados en los programas 2 y 3 finalizando con una serialización  
  5_prueba_rf es el programa que prueba los TP, FP y FN con diferentes umbrales  
  6_clientserver se encarga de realizar la comunicación con el servidor  
  prueba_rf_mensajes es un programa creado para detectar FP aunque se ha usado también versiones similares para TP y FN  

ENGLISH  
This GitHub repository contains the participation of the HULAT_UC3M group in the MentalRiskES task. The data is at https://sites.google.com/view/mentalriskes2025. The functionality of each program is as follows:  
  0_preprocesado: used to count the labels in the annotations.  
  1_modelo_gambling: trains the SVM model and performs internal evaluation. It ends with model serialization.  
  2_generar_frases: a program generated by ChatGPT aimed at creating annotated message-level phrases.  
  3_crear_no_gambling_txt: uses users not labeled as addicts and creates a text file with their messages.  
  4_random_forest: builds the RF model using the files generated by programs 2 and 3, ending with serialization.  
  5_prueba_rf: tests TP, FP, and FN with different thresholds.  
  6_clientserver: handles communication with the server.  
  prueba_rf_mensajes: a program created to detect FP, though similar versions have also been used for TP and FN.  
