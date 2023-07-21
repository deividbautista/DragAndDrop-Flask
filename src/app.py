from flask import Flask, render_template, request, redirect, url_for
from random import sample
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

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
    extensiones_permitidas = {'png', 'jpg', 'jpeg', 'gif'}

    # Obtener la extensión del archivo
    extension = filename.rsplit('.', 1)[1].lower()

    # Verificar si la extensión está permitida
    if '.' in filename and extension in extensiones_permitidas:
        return True
    else:
        return False


@app.route('/upload', methods=['POST'])
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
                print (len(archivos))
                return 'archivo no valido'
        print (len(archivos))
        return redirect(url_for('home'))  


if __name__ == '__main__':
    app.run(debug=True, port=9000)


