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

#------------------------------------------------------------------------------------
# Definimos la funcion "stringAleatorio" el cual nos retornara un valor aleatorio con los parametros especificados.
def stringAleatorio():
    # Caracteres que puede poseer el string aleatorio.
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    # Logintud determinada para el estring aleatorio.
    longitud         = 20
    # Utilizamos la función upper para combertir los caracteres en mayuscula.
    secuencia        = string_aleatorio.upper()
    # Definimos la variable "resultado_aleatorio", que con la función sample 
    # y los parametros de secuencia y longitud, generamos el string aleatorio.
    resultado_aleatorio  = sample(secuencia, longitud)
    # Volvemos a definir a la varibale "string_aleatorio", pero esta vez le 
    # concatenamos el valor optenido de "resultado_aleatorio". 
    string_aleatorio     = "".join(resultado_aleatorio)
    # Finalmente retornamos de nuestra función el resultado con el string aleatorio.
    return string_aleatorio
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
# Definimos la función "extensiones_validas" para corroborar que nuestro archivo sea de tipo img y evitar el envio 
# de scritps maliciosos en el servidor.
def extensiones_validas(filename):
    # Definimos la lista de extensiones permitidas para los archivos de imagen.
    extensiones_permitidas = {'png', 'jpg', 'jpeg', 'gif', 'svga', 'webp'}

    # Definimos la varibale "extenciones" que almacenara la extensión del archivo por medio del metodo de cadena 
    # "rsplit" utilizado para dividir cadenas de texto de derecha a izquierda por medio de un separador y con el 
    # metodo de cadena "lower", devolvermos el resultado obtenido por "rsplit" en minusculas.
    extension = filename.rsplit('.', 1)[1].lower()

    # Utilizamos la condicional if para determinar si se cumple con el caso de que el parametro filename posea un 
    # ".", es su valor y que su extension contenga alguno de los valores permitidas para esta.
    if '.' in filename and extension in extensiones_permitidas:
        # Si la condicional se cumple se retornara verdadero.
        return True
    else:
        # Si la condicional no se cumple se retornara falso.
        return False
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
# Definimos la ruta upload en la que se realizara todo el proceso de subida de archivos, 
# gracias a la función "upload_files".
@app.route('/upload', methods=['POST', 'GET'])

# Funcion upload_files la cual se encarga de realizar proceso de almacenamiento de archivos.
def upload_files():
    # Obtener la lista de archivos enviados en la solicitud
    archivos = request.files.getlist('archivos')

    # Verificar si se enviaron archivos
    if 'archivos' not in request.files or not bool(request.files['archivos']):
        return 'No se han enviado archivos'
    else:
        # Recorrer la lista de archivos y guardarlos en el directorio destino
        for archivo in archivos:
            # Directorio de destino para guardar los archivos
            #------------------------------------------------------------------
            # Nota del autor: no es necesario utilizar una ruta absoluta para el 
            # directorio, pero si posees algún error con este parametro, podrias probar hacerlo.
            #------------------------------------------------------------------
            directorio_destino = 'src/static/img'

            # Verificar si es un archivo de imagen válido
            if archivo and extensiones_validas(archivo.filename):
                # Definir extensión predeterminada para almacenar los archivos
                extension = (".jpg")
                # Definimos el nombre e+del archivo con los parametros del string 
                # aleatorio y la extensión predeterminada deseada.
                archivo.filename = stringAleatorio() + extension
                # Finalmente guardamos los archivos con la funcion save relacionada normalmente al 
                # objeto "LocalStorage" y la funcion "os.path.join" la cual nos fabrica una ruta 
                # con el directorio y el nombre del archivo para proceder a almacenarlo.
                archivo.save(os.path.join(directorio_destino, archivo.filename))
            else:
                # En caso de que alguno de los archivos no este permitido se retornara "Archivo invalido".
                print("Archivo invalido")
                return "Archivo invalido"    
#------------------------------------------------------------------------------------

# Sentencia para correr el app en el puerto "7000" y con la propiedad "debug=True" que nos permite 
# mantener el servidor activo mientras realizamos cambios.
if __name__ == '__main__':
    app.run(debug=True, port=7000)


