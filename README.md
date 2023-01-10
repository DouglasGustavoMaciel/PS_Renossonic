# Rennosonic Tecnologia - Case do Processo Seletivo

### Objteivos

* A aplicação realiza o envio de um JSON, com valores aleatórios, como explicado no ANEXO I, para o RabbitMQ, utilizando o Exchange: ‘ANAQ.STREAM’, e Routing Key: ‘ALTO.StreamDataEstadosEquipamento.Json’;
* A aplicação ealiza o recebimento dos dados, enviados pelo primeiro ponto, realizar a multiplicação desses valores (ValorBase * ValorCalculo) e
realizar o envio de um novo JSON para RabbitMQ, utilizando o Exchange: ‘ANAQ.STREAM.JSON’, e Routing Key: ‘ALTO.StreamDataEstadosEquipamentoResult.Json’;
* A aplicação que receba o JSON enviado pelo segundo ponto, e deverá exibe o mesmo na tela;

## Antes da Instalação

Antes de começar, verifique se você atendeu aos seguintes requisitos:
* Você tem uma máquina `<Windows / Linux / Mac>`.
* Você instalou a versão mais recente de `python`
* Você instalou as bibliotecas `pika` e `json`.

## Instalando a Aplicação

Para instalar a Aplicação, siga estas etapas:

Git:
```
git clone ![GitHub repo https]
```

## Como utilizar a aplicação

Siga estas etapas:

> Entre na pasta do projeto
```
cd ![GitHub repo name]
```

> Execute o script de envio do JSON com dados aleatórios
```
python send.py
```

> Execute o script de recebimento do primeiro script, cálculo dos dados e posteriormente envio dos dados
```
python main.py
```

> Execute o script de recebimento do segundo script e impressão na tela
```
python receiver.py
```


