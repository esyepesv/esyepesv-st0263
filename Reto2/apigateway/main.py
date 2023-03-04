from flask import Flask, request, jsonify
import os

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/', methods=['GET'])
def get_users():
    response = {'message': 'services: /find?file={filename} and /list'}
    return jsonify(response), 200, {'Content-Type': 'application/json'}

@app.route('/list', methods=['GET'])
def list_files():
    # obtener la lista de archivos en la carpeta 'files'
    files = os.listdir('../files')
    # devolver la lista de archivos como una respuesta JSON
    return jsonify(files), 200

@app.route('/find', methods=['GET'])
def find_file():
    # obtener el parámetro de consulta 'file' de la solicitud
    file = request.args.get('file')
    # verificar si el archivo existe en la carpeta 'files'
    if file in os.listdir('../files'):
        # si el archivo existe, devolver una respuesta 200
        return 'El archivo {} existe.'.format(file), 200
    else:
        # si el archivo no existe, devolver una respuesta 404
        return 'El archivo {} no existe.'.format(file), 404

if __name__ == '__main__':
    app.run(debug=True)