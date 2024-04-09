#utilizei o Broker RabbitMQ e a linguagem python para um exemplo de aplicação 
import pika

# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='fila')

# Função callback para tratar as mensagens recebidas
def callback(ch, method, properties, body):
    print(" [x] Recebido %r" % body)

# Configuração do consumo da fila
channel.basic_consume(queue='fila',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Aguardando mensagens. Pressione CTRL+C para sair.')
channel.start_consuming()
