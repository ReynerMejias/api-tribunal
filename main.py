import pandas as pd
from flask import Flask, jsonify

df = pd.read_csv("C:/Users/Reyner/Desktop/test/PADRON_COMPLETO.txt", encoding='latin1', header=None)
app = Flask(__name__)

def quitar_espacios(palabra):
    return " ".join([elemento for elemento in palabra.split(" ") if elemento])

@app.route('/')
def inicio():
    mensaje = {'mensaje': 'Hola, por favor digite su numero de cedula despues del dominio usando una barra inclinada'}
    return jsonify(mensaje)

@app.route('/<cedula>', methods=['GET'])
def obtener_mensaje(cedula):
    cedula = int(cedula)
    busqueda_nombre = df[df[0] == cedula]
    return jsonify(
        {
            "nombre": quitar_espacios(busqueda_nombre.iloc[0, 5]),
            "primer apellido": quitar_espacios(busqueda_nombre.iloc[0, 6]),
            "segundo apellido": quitar_espacios(busqueda_nombre.iloc[0, 7]),
        
        }
    )

if __name__ == '__main__':
    app.run()