import os
import pika

# Crear cola para almacenar las respuestas
responses_queue = []

# Función de callback para procesar los mensajes
def callback(ch, method, properties, body):
    print(f'{body} is received')
    if body == b"files":
        filenames = os.listdir('../files')
        responses_queue.append(filenames)

# Conectarse al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "password")))
channel = connection.channel()

# Consumir mensajes de la cola "request"
channel.basic_consume(queue="my_request", on_message_callback=callback, auto_ack=True)
channel.start_consuming()

# Publicar respuestas en la cola "response"
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))
channel = connection.channel()

# Obtener respuestas de la cola y publicarlas en la cola "response"
while responses_queue:
    response = responses_queue.pop(0)
    channel.basic_publish(exchange='response', routing_key='request', body=str(response))

# Cerrar la conexión
connection.close()
