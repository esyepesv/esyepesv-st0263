import os
from flask import Flask, jsonify
import grpc
import sys
sys.path.append('../service1-gRPC')
import file_service_pb2
import file_service_pb2_grpc


app = Flask(__name__)

# crear un canal de comunicación con el servidor de gRPC
channel = grpc.insecure_channel('localhost:50051')

# crear un cliente de gRPC para el servicio de FileService
file_service_client = file_service_pb2_grpc.FileServiceStub(channel)

@app.route('/files', methods=['GET'])
def list_files():
    # crear una solicitud de gRPC para obtener la lista de archivos
    request = file_service_pb2.ListFilesRequest()
    # hacer la llamada al servicio de gRPC
    response = file_service_client.ListFiles(request)
    # convertir el campo "filenames" a una lista
    filenames = list(response.filenames)
    # devolver la lista de archivos como una respuesta HTTP
    return jsonify(filenames)


@app.route('/find/<filename>', methods=['GET'])
def file_exists(filename):
    # crear una solicitud de gRPC para verificar si el archivo existe
    request = file_service_pb2.FileExistsRequest(filename=filename)
    # hacer la llamada al servicio de gRPC
    response = file_service_client.FileExists(request)
    # devolver la respuesta del servicio de gRPC como una respuesta HTTP
    if response.exists:
        return 'El archivo {} existe.'.format(filename), 200
    else:
        return 'El archivo {} no existe.'.format(filename), 404

if __name__ == '__main__':
    app.run(debug=True)
