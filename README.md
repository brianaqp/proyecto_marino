# proyecto_marino
Proyecto de Topicos Avanzados de Inteligencia Artificial

Adjunto Reporte en formato IEEE, llamado pdf.pdf

Los siguientes archivos de python sirven para lo siguiente

- entrenar.py: Es el archivo que crea, entrena y guarda el modelo secuencial.
- predict.py: Se podria decir que es el archivo main, al correrlo toma un video y aplica las predicciones en tiempo real.
- predict_1img.py: Codigo para predecir imagenes estaticas.
- remove_water.py: Fue el archivo que utilice para tratar al coral - Branching-, removiendo el agua para que solo extrajera las caracteristicas importantes.
- resize.py: Archivo que al darle una carpeta, escala todas las imagenes a 128x128 pixeles.
- train_data.py: Un script que utilice para sacar imagenes de un video de 11 horas. Cada tanto tiempo guardaba una imagen. Sirvio como fuente de informacion.

IMPORTANTE
Puede que el video no le corra correctamente debido a que algunas direcciones estan en windows, lo unico que habria que cambiar seria el formato, pero en general esta funcional.
Solo pude entrenar al modelo per clase con: 
- 70 imagenes para entrenamiento
- 40 para validacion.

Con mas datos, se podrian obtener mejores resultados.

En github no me deja subir los videos que utilice para testear porque duran 11 horas, asi que en el video tratare de mostrar como se ve.

Adjunto drive con algunos *videos de prueba* y con el *modelo entrenado*:
https://drive.google.com/drive/folders/1Kzo9fSFaN8x0ii_QoQj1erKYSWaMG9U_?usp=sharing
