import os
from flask import Flask, jsonify
import grpc
import sys
import pika
import uuid
from concurrent import futures
sys.path.append('../service1-gRPC')
import file_service_pb2
import file_service_pb2_grpc

app = Flask(__name__)

# crear un canal de comunicación con el servidor de gRPC
grpc_channel = grpc.insecure_channel('localhost:50051')
# crear un cliente de gRPC para el servicio de FileService
file_service_client = file_service_pb2_grpc.FileServiceStub(grpc_channel)

# crear una conexión con RabbitMQ
mom_connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password'))
)
mom_channel = mom_connection.channel()

# crear una cola temporal y enlazarla con la clave 'response'
result = mom_channel.queue_declare(queue='', exclusive=True)
response_queue = result.method.queue
mom_channel.queue_bind(exchange='my_exchange', queue=response_queue, routing_key='response')

@app.route('/files', methods=['GET'])
def list_files():
    try:
        filenames = list_files_grpc()
        if not filenames:
            filenames = list_files_mom()
        return jsonify(filenames)
    except:
        return "Error al obtener los archivos"

def list_files_grpc():
    # crear una solicitud de gRPC para obtener la lista de archivos
    request = file_service_pb2.ListFilesRequest()
    # hacer la llamada al servicio de gRPC
    response = file_service_client.ListFiles(request)
    # convertir el campo "filenames" a una lista
    return list(response.filenames)

def list_files_mom():
    # definir un identificador único para la solicitud
    correlation_id = str(uuid.uuid4())

    # publicar un mensaje en el exchange 'my_exchange' con la clave 'request'
    mom_channel.basic_publish(
        exchange='my_exchange',
        routing_key='request',
        body='files'.encode(),
        properties=pika.BasicProperties(
            reply_to=response_queue,
            correlation_id=correlation_id
        )
    )

    # crear una variable para almacenar la respuesta
    response = None

    # definir una función para procesar los mensajes de respuesta
    def callback(ch, method, props, body):
        nonlocal response
        if props.correlation_id == correlation_id:
            response = body.decode()

    # consumir mensajes de la cola temporal y esperar a que se reciba la respuesta
    mom_channel.basic_consume(queue=response_queue, on_message_callback=callback, auto_ack=True)
    while response is None:
        mom_connection.process_data_events()

    # devolver la respuesta
    return response.split(',')

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
