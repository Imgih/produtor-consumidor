#utilizei o Broker RabbitMQ e a linguagem python para um exemplo de aplicação 

import pika
import time

# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='fila')

# Função para enviar mensagens para a fila
def enviar_mensagem(mensagem):
    channel.basic_publish(exchange='',
                          routing_key='fila',
                          body=mensagem)
    print(" [x] Enviado %r" % mensagem)

# Loop para enviar mensagens
for i in range(5):
    mensagem = f'Mensagem {i}'
    enviar_mensagem(mensagem)
    time.sleep(1)


connection.close()
