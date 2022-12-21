import json
import sys
import os
from datetime import datetime
import random
import pika

# Função de envio do JSON aleatório
def send():

    #Realizando a conexão com servidor
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('198.27.114.55'))
    channel = connection.channel()

    # Enviando a data de hoje formatada
    print(datetime.today())
    date = datetime.today().strftime('%Y-%m-%d:%H:%M')

    #Json com os valores que serão enviados
    dataSaida = {
        "TimeStamp" : date,
        "DATA": [
            {
                "name" : "ValorBase",
                "value" : random.randint(0, 100)
            },
            {
                "name" : "ValorCalculo",
                "value" : random.randint(0, 100)
            }
        ]
    }

    mesage = ''

    print(json.dumps(dataSaida))
    mesage = json.dumps(dataSaida)

    #Setando a rota que será enviada
    channel.queue_declare(queue='')
    channel.basic_publish(
        exchange="ANAQ.STREAM",
        routing_key='ALTO.StreamDataEstadosEquipamento.Json',
        body=mesage)

    print("[x] Enviado")


if __name__ == '__main__':
    try:
        send()

    #Realiza o looping de envio até ser interrompido
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
