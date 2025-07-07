import pika

credentials = pika.PlainCredentials('root', 'root')
parameters = pika.ConnectionParameters(host='localhost', port=5672, virtual_host='myvhost', credentials=credentials)

try:
    connection = pika.BlockingConnection(parameters)
    print("Connected successfully to RabbitMQ!")
    connection.close()
except pika.exceptions.AMQPConnectionError as e:
    print(f"Connection failed: {e}")