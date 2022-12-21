import json
import pika, sys, os
from datetime import datetime


#Função de recebimento dos dados 
def receive():

    #Realizando a conexão
    credentials = pika.PlainCredentials('guest', 'guest')                                    
    connection = pika.BlockingConnection(pika.ConnectionParameters('198.27.114.55',credentials=credentials))
    channel = connection.channel()

    result = channel.queue_declare(queue='',durable=False, exclusive=True) #MUDAR PRA TRUE
    queue_name = result.method.queue
    channel.queue_bind(exchange="ANAQ.STREAM", queue=queue_name, routing_key='ALTO.StreamDataEstadosEquipamento.Json')

    
    def callback(ch, method, properties, body):
        data = json.loads(body)
        print(data['DATA'])
        valorCalculado = data['DATA'][0]['value'] * data['DATA'][1]['value'] 
        date = datetime.today().strftime('%Y-%m-%d:%H:%M')
        dataSaida = {
            "TimeStamp" : date,
            "DATA": {
                "name" : "ValorSaida",
                "value" : valorCalculado
            }
        }
        
        message = json.dumps(dataSaida)
        print(dataSaida)
        channel.exchange_declare(exchange="ANAQ.STREAM.JSON", exchange_type="topic")
        channel.queue_declare(queue="ANAQ.STREAM")
        channel.basic_publish(exchange="ANAQ.STREAM.JSON",
                              routing_key="ALTO.StreamDataEstadosEquipamentoResult.Json",
                              body=message)
        
    channel.basic_consume(queue=queue_name,
                        auto_ack=True,
                        on_message_callback=callback)
    print(' [*] Aguardando por mensagens')
    channel.start_consuming()


#MAIN
if __name__ == '__main__':
    try:
        receive()

    #Realiza o looping de recebimento até ser interrompido
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)