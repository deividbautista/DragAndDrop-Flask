#------------------------------------------------------------------------------------
# El presente código posee la finalidad de aprender y practicar conocimientos intermedios 
# del lenguaje de programación python y javascripts, cabe aclarar que estractos de código 
# y sobre todo diseño principal se sustrajeron de un tutorial el cual se reflejara su link a continuación.
#------------------------------------------------------------------------------------

# Código sustraido del canal: Vida MRR - Programacion web "https://www.youtube.com/@vidamrr" 
# link-video: https://youtu.be/qWFwYLUGWrc
# link-repositorios: https://github.com/marcosrivasr/Curso-de-NodeJS  

# En este apartado se realiza la importación de las librerias y modulos a utilizar en este proyecto.
from flask import Flask, render_template, request, redirect, url_for
from random import sample
import os

app = Flask(__name__)

#------------------------------------------------------------------------------------
# En el siguiente apartados se observaran las distintas rutas con las que se trabajara
# en el servidor de flask incluyendo tambien las funciones dentro de estas.
#------------------------------------------------------------------------------------
# Ruta principal que contendra el diseño de drag and drop principal.
@app.route("/")
def home():
    return render_template('index.html')

# Definimos la funcion "stringAleatorio" el cual nos retornara un valor aleatorio con los parametros especificados.
def stringAleatorio():
     #Generando string aleatorio
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio


def extensiones_validas(filename):
    # Lista de extensiones permitidas para los archivos de imagen
    extensiones_permitidas = {'png', 'jpg', 'jpeg', 'gif', 'svga', 'webp'}

    # Obtener la extensión del archivo
    extension = filename.rsplit('.', 1)[1].lower()

    # Verificar si la extensión está permitida
    if '.' in filename and extension in extensiones_permitidas:
        return True
    else:
        return False

@app.route('/upload', methods=['POST', 'GET'])
def upload_files():
    
    # Obtener la lista de archivos enviados en la solicitud
    archivos = request.files.getlist('archivos')

    # Verificar si se enviaron archivos
    if 'archivos' not in request.files or not bool(request.files['archivos']):
        return 'No se han enviado archivos'
    else:
        # Recorrer la lista de archivos y guardarlos en el directorio de destino
        for archivo in archivos:
            # Directorio de destino para guardar los archivos
            directorio_destino = 'src/static/img'

            # Verificar si es un archivo de imagen válido
            if archivo and extensiones_validas(archivo.filename):
                extension = (".jpg")
                archivo.filename = stringAleatorio() + extension
                archivo.save(os.path.join(directorio_destino, archivo.filename))
            else:
                print("Archivo invalido")
                return "Archivo invalido"    

if __name__ == '__main__':
    app.run(debug=True, port=7000)


